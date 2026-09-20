#!/usr/bin/env python3
"""Build a lossless source archive and readable Markdown from cached public pages.

Network-free. Inputs stay in inbox; public output contains page text, never user
profiles or API bookkeeping. Edited output is protected unless --overwrite is
explicitly supplied. Run with --check to verify source coverage and local links.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, unquote


ROOT = Path(__file__).resolve().parents[1]
DATE = '2026-09-20'


def configure(section, section_label, groups, pages, signals, supplements, scope, cross_links=None):
    """Configure one archive per CLI process; the renderer is shared across subjects."""
    global SECTION, SECTION_LABEL, GROUPS, PAGES, SIGNALS, SUPPLEMENTS, SCOPE
    global CACHE, MANIFEST, CROSS_LINKS
    SECTION, SECTION_LABEL = section, section_label
    GROUPS, PAGES, SIGNALS, SUPPLEMENTS = groups, pages, signals, supplements
    SCOPE, CROSS_LINKS = scope, cross_links or {}
    CACHE = ROOT / 'inbox/scrapbox' / DATE / (section + '-full')
    MANIFEST = ROOT / section / 'sources/manifest.json'


BASE = 'https://scrapbox.io/MistMavGamer/'
BODY_START = '<!-- BEGIN IMPORTED BODY: preserve historical wording -->'
BODY_END = '<!-- END IMPORTED BODY -->'


def imported_body(text):
    if text.count(BODY_START) != 1 or text.count(BODY_END) != 1:
        raise ValueError('Expected exactly one imported body')
    start = text.index(BODY_START) + len(BODY_START)
    end = text.index(BODY_END)
    if end < start:
        raise ValueError('Imported body markers are reversed')
    return text[start:end]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def quoted(value):
    return json.dumps(value, ensure_ascii=False)


def source_url(title):
    return BASE + quote(title, safe='')


def relative(target, current):
    return Path(os.path.relpath(target, current.parent)).as_posix()


def timestamp(value):
    return datetime.fromtimestamp(value, timezone.utc).isoformat().replace('+00:00', 'Z')


def label(text):
    return html.escape(text, quote=False).replace('[', r'\[').replace(']', r'\]').replace('~', r'\~')


class Renderer:
    def __init__(self, current, titles, assets):
        self.current = current
        self.titles = titles
        self.assets = assets
        self.internal = set()
        self.external = set()
        self.unresolved = set()

    def link(self, title):
        if title in PAGES:
            p = PAGES[title]
            path = ROOT / SECTION / p['group'] / (p['slug'] + '.md')
            self.internal.add(title)
            return f'[{label(title)}]({relative(path, self.current)})'
        if title in CROSS_LINKS:
            self.internal.add(title)
            return f'[{label(title)}]({relative(ROOT / CROSS_LINKS[title], self.current)})'
        if title in self.titles:
            self.external.add(title)
            return f'[{label(title)}]({source_url(title)})'
        # Scrapbox also interprets mathematical intervals/commutators as links.
        # Leave those literal. Missing textual page names are recorded separately.
        if not re.search(r'[,，∀∃<>=]|^[0-9θ]', title):
            self.unresolved.add(title)
        return r'\[' + label(title) + r'\]'

    def bracket(self, inside):
        if inside.startswith('$ '):
            return '$' + inside[2:].strip() + '$'
        style = re.match(r'^(\*+|/|-|_)\s+([\s\S]*)$', inside)
        if style:
            marker, body = style.groups()
            wrapper = '**' if marker.startswith('*') else ('~~' if marker == '-' else '*')
            return wrapper + self.inline(body) + wrapper
        if inside.startswith('[') and inside.endswith(']'):
            return '**' + self.inline(inside[1:-1]) + '**'
        parts = inside.split()
        urls = [p for p in parts if p.startswith(('https://', 'http://'))]
        if urls:
            url = urls[0]
            name = inside.replace(url, '', 1).strip() or url
            if url in self.assets:
                path = ROOT / self.assets[url]['path']
                return f'![元メモの画像]({relative(path, self.current)}) ([画像の出典](<{url}>))'
            return f'[{label(name)}](<{url}>)'
        if inside.startswith('/'):
            return f'[{label(inside)}](https://scrapbox.io{quote(inside, safe="/")})'
        if inside.endswith('.icon'):
            return self.link(inside[:-5]) + '（原文ではアイコン表示）'
        return self.link(inside)

    def inline(self, text):
        out = []
        i = 0
        while i < len(text):
            ch = text[i]
            if ch == '`':
                end = text.find('`', i + 1)
                if end >= 0:
                    out.append(text[i:end + 1]); i = end + 1; continue
            if ch == '[':
                depth, j = 1, i + 1
                while j < len(text) and depth:
                    if text[j] == '[': depth += 1
                    if text[j] == ']': depth -= 1
                    j += 1
                if depth == 0:
                    out.append(self.bracket(text[i + 1:j - 1])); i = j; continue
            if text.startswith(('https://', 'http://'), i):
                match = re.match(r'https?://[^\s<>]+', text[i:])
                if match:
                    url = match.group(0)
                    out.append(f'<{url}>'); i += len(url); continue
            if ch == '\ufffc':
                out.append('**〔原文の埋め込み欠落記号 U+FFFC〕**')
            elif ch in '<>&': out.append(html.escape(ch, quote=False))
            elif ch == '\x0b': out.append('<br>')
            elif ch in '*_~\\': out.append('\\' + ch)
            else: out.append(ch)
            i += 1
        return ''.join(out)


def load():
    inputs = json.loads((CACHE / 'manifest.json').read_text())
    failed = [p for p in inputs if p['status'] != 'fetched']
    if failed: raise ValueError(f'Failed inputs: {failed}')
    pages = {p['title']: json.loads((CACHE / p['path']).read_text()) for p in inputs}
    assert set(pages) == set(PAGES) == set(SUPPLEMENTS), 'Unmapped or unannotated pages'
    catalog = json.loads((CACHE.parent / 'page-catalog.json').read_text())
    assets = json.loads((CACHE / 'assets.json').read_text())
    return pages, {p['title'] for p in catalog}, {a['url']: a for a in assets if a['status'] == 'downloaded'}


def build_page(data, spec, catalog, assets):
    path = ROOT / SECTION / spec['group'] / (spec['slug'] + '.md')
    raw_path = ROOT / SECTION / 'sources' / (spec['slug'] + '.txt')
    title = data['title']
    texts = [line['text'] for line in data['lines']]
    original = '\n'.join(texts).encode('utf-8')
    renderer = Renderer(path, catalog, assets)
    missing = [i + 1 for i, text in enumerate(texts) if '\ufffc' in text]
    heads = []
    body = []
    mapping = []
    previous_indent = 0
    for i, text in enumerate(texts, 1):
        stripped = text.lstrip(' \t\u3000')
        indent = len(text) - len(stripped)
        start = len(body) + 1
        if not text.strip():
            body.append('')
            previous_indent = 0
        else:
            explicit = re.fullmatch(r'\[\*+\s+(.+)\]', stripped)
            heading = explicit.group(1) if explicit else None
            if not heading and len(stripped) < 75 and re.match(r'^(第[0-9０-９一二三四五六七八九十]+[回講章]|[0-9]+(?:\.[0-9]+)*[.． ]\s*[^0-9=])', stripped):
                heading = stripped
            anchor = f'<a id="source-L{i}"></a>'
            if i == 1:
                body += [anchor, '', '### ' + label(text), '']
            elif heading:
                heads.append((i, re.sub(r'\[|\]', '', heading)))
                body += ['', anchor, '', '### ' + renderer.inline(heading), '']
            else:
                # Preserve hierarchy without turning 4-space indentation into code.
                if indent != previous_indent and body and body[-1] != '':
                    body.append('')
                depth = indent
                prefix = '> ' * depth if indent else ''
                rendered = renderer.inline(stripped)
                # Native Markdown tables already present in the source remain tables.
                if stripped.startswith('|'):
                    body.append(rendered)
                else:
                    body.append(prefix + anchor + rendered + '  ')
            previous_indent = indent if not heading and i != 1 else 0
        original_line = data['lines'][i - 1]
        mapping.append({'source_line': i, 'source_line_id': original_line.get('id'),
                        'source_created': original_line.get('created'), 'source_updated': original_line.get('updated'),
                        'body_start': start, 'body_end': len(body)})
    note = [
        '---', f'title: {quoted(title)}', 'status: draft',
        f'tags: [scrapbox, {spec["group"]}]', f'created: {DATE}', f'updated: {DATE}',
        f'source: {quoted(source_url(title))}', f'source_created: {quoted(timestamp(data["created"]))}',
        f'source_updated: {quoted(timestamp(data["updated"]))}', f'imported: {DATE}',
        'provenance: imported-with-separate-ai-notes', '---', '', '# ' + label(title), '',
        spec['description'], '',
        f'原ページ作成：{timestamp(data["created"])[:10]} ／ 最終更新：{timestamp(data["updated"])[:10]}（UTC、取得時点）', '',
        f'[{SECTION_LABEL}の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト]({relative(raw_path, path)}) · [Scrapbox]({source_url(title)})', '',
        '本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。', '',
    ]
    signals = []
    for pattern in SIGNALS.get(title, []):
        for n, text in enumerate(texts, 1):
            if pattern in text:
                signals.append((n, text.strip())); break
    if signals:
        note += ['## 思考の手がかり', '']
        for n, text in signals:
            note += ['> ' + renderer.inline(text), '', f'[本文の該当箇所へ](#source-L{n})', '']
    if missing:
        note += [f'**原文に埋め込み欠落記号が{sum(t.count(chr(0xfffc)) for t in texts)}か所あります。** 取得時点で内容を特定できないため、本文中で位置を示しています。推測した図や式に置き換えていません。', '']
    if heads:
        note += ['<details>', '<summary>本文の見出しから探す</summary>', '']
        for n, heading in heads:
            note.append(f'- [{label(heading)}](#source-L{n})')
        note += ['', '</details>', '']
    note += ['<a id="original"></a>', '', '## 当時の本文', '',
             '原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。', '',
             '<!-- BEGIN IMPORTED BODY: preserve historical wording -->']
    offset = len(note)
    note += body
    note += ['<!-- END IMPORTED BODY -->', '', '<a id="ai-notes"></a>', '', f'## AIによる補足・訂正（{DATE}）', '',
             SUPPLEMENTS[title], '',
             'この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。', '',
             '## つながる移植ノート', '']
    related = [t for t in data.get('links', []) if (t in PAGES or t in CROSS_LINKS) and t != title]
    if related:
        note += ['- ' + renderer.link(t) for t in dict.fromkeys(related)]
    else:
        note.append(f'- [同じ分野のノート](README.md)：{GROUPS[spec["group"]]}。')
    note += ['', '原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。', '']
    content = '\n'.join(note).encode('utf-8')
    return path, content, raw_path, original, {
        'title': title, 'path': str(path.relative_to(ROOT)), 'source_path': str(raw_path.relative_to(ROOT)),
        'source_url': source_url(title), 'source_created': timestamp(data['created']),
        'source_updated': timestamp(data['updated']), 'source_line_count': len(texts),
        'source_sha256': sha(original), 'markdown_sha256': sha(content),
        'body_sha256': sha(imported_body(content.decode('utf-8')).encode('utf-8')),
        'missing_embed_count': sum(t.count('\ufffc') for t in texts), 'missing_embed_lines': missing,
        'body_line_offset': offset, 'line_mapping': mapping,
        'local_links': sorted(renderer.internal), 'external_project_links': sorted(renderer.external),
        'unresolved_link_labels': sorted(renderer.unresolved),
    }


def write(path, data, expected, overwrite):
    if isinstance(data, str): data = data.encode('utf-8')
    if path.exists() and path.read_bytes() != data and not overwrite:
        if expected is None or sha(path.read_bytes()) != expected:
            raise RuntimeError(f'Edited file protected: {path.relative_to(ROOT)}')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def build(overwrite=False):
    pages, catalog, assets = load()
    outputs = []
    records = []
    previous = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {'pages': []}
    old = {p['path']: p['markdown_sha256'] for p in previous['pages']}
    for title, spec in PAGES.items():
        path, content, raw_path, original, record = build_page(pages[title], spec, catalog, assets)
        outputs += [(path, content, old.get(record['path'])), (raw_path, original, record['source_sha256'])]
        records.append(record)
    indexes = {}
    for group, name in GROUPS.items():
        path = ROOT / SECTION / group / 'README.md'
        text = f'# {name}\n\nScrapboxから本文全体を移し、当時の記録と今回のAI補足を分けたノートです。\n\n'
        for title, spec in PAGES.items():
            if spec['group'] == group:
                text += f'- [{label(title)}]({spec["slug"]}.md)：{spec["description"]}\n'
        text += f'\n[{SECTION_LABEL}の入口へ](../README.md) · [移植記録](../import-report.md)\n'
        # Indexes are generated, but protect edits between generations as well.
        expected = previous.get('indexes', {}).get(str(path.relative_to(ROOT)))
        data = text.encode('utf-8')
        outputs.append((path, data, expected))
        indexes[str(path.relative_to(ROOT))] = sha(data)
    manifest = {
        'imported': DATE, 'scope': SCOPE,
        'page_count': len(records), 'source_line_count': sum(p['source_line_count'] for p in records),
        'missing_embed_count': sum(p['missing_embed_count'] for p in records),
        'pages': records, 'assets': list(assets.values()),
        'indexes': indexes,
    }
    manifest_data = (json.dumps(manifest, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    outputs.append((MANIFEST, manifest_data, sha(MANIFEST.read_bytes()) if MANIFEST.exists() else None))
    # Include indexes in the preflight: an edited index must block all writes,
    # including refreshed notes and source files earlier in the output list.
    for path, data, expected in outputs:
        if path.exists() and path.read_bytes() != data and not overwrite:
            if expected is None or sha(path.read_bytes()) != expected:
                raise RuntimeError(f'Edited file protected: {path}')
    for path, data, expected in outputs:
        write(path, data, expected, overwrite)
    print(json.dumps({k: manifest[k] for k in ['page_count', 'source_line_count', 'missing_embed_count']}, ensure_ascii=False))


def check():
    manifest = json.loads(MANIFEST.read_text())
    cached = load() if (CACHE / 'manifest.json').exists() else None
    failures = []
    records = manifest['pages']
    if len(records) != manifest['page_count'] or {p['title'] for p in records} != set(PAGES):
        failures.append('Page coverage mismatch')
    for field in ('title', 'path', 'source_path'):
        if len({p[field] for p in records}) != len(records):
            failures.append(f'Duplicate page {field}')
    for field in ('source_line_count', 'missing_embed_count'):
        if sum(p[field] for p in records) != manifest[field]:
            failures.append(f'Total mismatch: {field}')
    for p in manifest['pages']:
        original = (ROOT/p['source_path']).read_bytes()
        if sha(original) != p['source_sha256']: failures.append(f'Source checksum mismatch: {p["title"]}')
        lines = original.decode('utf-8').split('\n')
        if len(lines) != p['source_line_count']:
            failures.append(f'Source line count mismatch: {p["title"]}')
        if sum(line.count('\ufffc') for line in lines) != p['missing_embed_count']:
            failures.append(f'Missing embed count mismatch: {p["title"]}')
        mappings = p['line_mapping']
        if [r['source_line'] for r in mappings] != list(range(1, p['source_line_count'] + 1)):
            failures.append(f'Incomplete mapping: {p["title"]}')
        saved = (ROOT/p['path']).read_text()
        body = imported_body(saved)
        if sha(body.encode('utf-8')) != p['body_sha256']:
            failures.append(f'Imported body changed: {p["title"]}')
        body_lines = body[1:-1].split('\n')
        next_line = 1
        for mapping in mappings:
            if mapping['body_start'] != next_line or mapping['body_end'] < next_line:
                failures.append(f'Invalid body mapping: {p["title"]}')
                break
            next_line = mapping['body_end'] + 1
        if next_line != len(body_lines) + 1:
            failures.append(f'Incomplete body coverage: {p["title"]}')
        if cached:
            pages, catalog, assets = cached
            _, rendered, _, source, _ = build_page(pages[p['title']], PAGES[p['title']], catalog, assets)
            if original != source: failures.append(f'Cached source mismatch: {p["title"]}')
            if body != imported_body(rendered.decode('utf-8')):
                failures.append(f'Cached rendering mismatch: {p["title"]}')
    # Check local links, including .txt, images, and explicit source anchors.
    link_count = 0
    for path in ROOT.rglob('*.md'):
        if any(part in {'inbox', '.git', 'node_modules'} for part in path.relative_to(ROOT).parts): continue
        for match in re.finditer(r'\[[^\n]*?\]\((<[^>]+>|[^\s)]+)\)', path.read_text()):
            target = match.group(1).strip('<>')
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target): continue
            link_count += 1
            name, _, fragment = target.partition('#')
            dest = path.parent / unquote(name) if name else path
            if not dest.exists(): failures.append(f'Broken link: {path.relative_to(ROOT)} -> {target}'); continue
            if fragment.startswith(('source-L', 'original', 'ai-notes')) and dest.suffix == '.md':
                if f'id="{fragment}"' not in dest.read_text(): failures.append(f'Broken anchor: {target}')
    for a in manifest['assets']:
        if sha((ROOT/a['path']).read_bytes()) != a['sha256']: failures.append(f'Asset mismatch: {a["path"]}')
    if failures: raise SystemExit('\n'.join(failures))
    print(f'PASS: {len(records)} source and body checksums; {manifest["source_line_count"]} lines mapped; {link_count} local links; {len(manifest["assets"])} asset checksums.')
    if cached:
        print('PASS: sources and rendered bodies also match the local API snapshots.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--overwrite', action='store_true')
    args = parser.parse_args()
    check() if args.check else build(args.overwrite)
