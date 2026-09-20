"""Regression checks for preserving hand edits before any regeneration writes."""
import contextlib
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import scrapbox_import as importer


class RegenerationProtectionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root_patch = patch.object(importer, 'ROOT', Path(self.temp.name))
        root_patch.start()
        self.addCleanup(root_patch.stop)
        self.supplements = {'Sample': 'Initial explanation.'}
        importer.configure(
            'subject', '科目', {'topic': 'Topic'},
            {'Sample': {'group': 'topic', 'slug': 'sample', 'description': 'A sample.'}},
            {}, self.supplements, 'Test snapshot',
        )
        source = {
            'title': 'Sample', 'created': 1, 'updated': 2, 'links': [],
            'lines': [{'text': 'Sample', 'id': 'one'}, {'text': 'Historical text.', 'id': 'two'}],
        }
        loader = patch.object(importer, 'load', return_value=({'Sample': source}, {'Sample'}, {}))
        loader.start()
        self.addCleanup(loader.stop)
        self.build()

    def build(self):
        with contextlib.redirect_stdout(io.StringIO()):
            importer.build()

    def snapshot(self):
        return {p.relative_to(importer.ROOT): p.read_bytes()
                for p in importer.ROOT.rglob('*') if p.is_file()}

    def test_edited_index_prevents_any_refresh(self):
        index = importer.ROOT / 'subject/topic/README.md'
        index.write_text(index.read_text() + '\nPersonal reading path.\n')
        before = self.snapshot()
        # Would update the note before reaching the index in the old implementation.
        self.supplements['Sample'] = 'New explanation.'
        with self.assertRaisesRegex(RuntimeError, 'Edited file protected'):
            self.build()
        self.assertEqual(before, self.snapshot())

    def test_edited_note_prevents_any_refresh(self):
        note = importer.ROOT / 'subject/topic/sample.md'
        note.write_text(note.read_text() + '\nPersonal question.\n')
        before = self.snapshot()
        self.supplements['Sample'] = 'New explanation.'
        with self.assertRaisesRegex(RuntimeError, 'Edited file protected'):
            self.build()
        self.assertEqual(before, self.snapshot())

    def test_edited_source_prevents_any_refresh(self):
        source = importer.ROOT / 'subject/sources/sample.txt'
        source.write_text(source.read_text() + '\nUnexpected edit.')
        before = self.snapshot()
        self.supplements['Sample'] = 'New explanation.'
        with self.assertRaisesRegex(RuntimeError, 'Edited file protected'):
            self.build()
        self.assertEqual(before, self.snapshot())

    def test_unchanged_generation_is_identical(self):
        before = self.snapshot()
        self.build()
        self.assertEqual(before, self.snapshot())


if __name__ == '__main__':
    unittest.main()
