---
title: "ケモインフォマティクス"
status: draft
tags: [scrapbox, materials-informatics]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E3%82%B1%E3%83%A2%E3%82%A4%E3%83%B3%E3%83%95%E3%82%A9%E3%83%9E%E3%83%86%E3%82%A3%E3%82%AF%E3%82%B9"
source_created: "2025-11-17T01:59:10Z"
source_updated: "2025-11-17T14:06:39Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# ケモインフォマティクス

分子の記述子、SMILES、機械学習、構造式画像認識の資料。

原ページ作成：2025-11-17 ／ 最終更新：2025-11-17（UTC、取得時点）

[化学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/cheminformatics.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E3%82%B1%E3%83%A2%E3%82%A4%E3%83%B3%E3%83%95%E3%82%A9%E3%83%9E%E3%83%86%E3%82%A3%E3%82%AF%E3%82%B9)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### ケモインフォマティクス

<a id="source-L2"></a>[物性化学](../../physics/electromagnetism-matter/physical-chemistry.md)  
<a id="source-L3"></a>[生命科学](../life-sciences/life-sciences.md)  
<a id="source-L4"></a>[高校化学](../foundations/high-school-chemistry.md)  
<a id="source-L5"></a>[量子論](../../physics/quantum/quantum-theory.md)  
<a id="source-L6"></a>[物性化学](../../physics/electromagnetism-matter/physical-chemistry.md)  
<a id="source-L7"></a>[バイオインフォマティクス](../life-sciences/bioinformatics.md)  
<a id="source-L8"></a>[マテリアルズインフォマティクス](materials-informatics.md)  
<a id="source-L9"></a>[AIロボット駆動科学](automated-experimental-science.md)  




> <a id="source-L14"></a>ケモインフォマティクス入門書  

<a id="source-L15"></a><https://zenn.dev/poclabweb/books/chemoinfomatics_beginner/viewer/lesson04_00_rdkit2>  



> <a id="source-L19"></a>ケモインフォマティクス理論(化学記述子)  

<a id="source-L20"></a><https://zenn.dev/poclabweb/books/chemoinfomatics_theory_descriptor>  



> <a id="source-L24"></a>ケモインフォマティクス理論(機械学習編)  

<a id="source-L25"></a><https://zenn.dev/poclabweb/books/chemoinfomatics_theory_machinelearning>  




> <a id="source-L30"></a>SMILES記法  

<a id="source-L31"></a><https://ja.wikipedia.org/wiki/SMILES記法>  



> <a id="source-L35"></a>化学のためのマルチモーダル大規模言語モデル（LLM）  

<a id="source-L36"></a><https://www.ecomottblog.com/?p=15283)この辺りの論文を1>  



> <a id="source-L40"></a>MolNexTR: A Generalized Deep Learning Model for Molecular Image Recognition  

<a id="source-L41"></a><https://arxiv.org/pdf/2403.03691>  



> <a id="source-L45"></a>Comparing software tools for optical chemical structure recognition  

<a id="source-L46"></a><https://pubs.rsc.org/en/content/articlehtml/2024/dd/d3dd00228d>  


<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

### 分子をデータとして表現する

元の本文は、入門書・記述子・機械学習・構造式画像認識の資料を集めたものです。すべてを実装済み・読了とは扱いません。

分子式が同じでも結合のつながりが異なることがあります。例えばエタノールとジメチルエーテルはともに $\mathrm{C_2H_6O}$ ですが、SMILESではそれぞれ CCO と COC と書けます。原子と結合をグラフとして扱うと、この違いを保持できます。SMILESの読み込み、記述子、フィンガープリントの基本操作は[RDKit公式 Getting Started](https://www.rdkit.org/docs/GettingStartedInPython.html)で確認できます。

構造を読む処理、特徴量へ変換する処理、物性を予測する処理を分けて考えます。文字列が異なっても同一分子を表す場合があるため、文字列の完全一致だけで同一性を判断しません。立体化学や電荷もデータに残す必要があります。

原文の[L36](#source-L36)にはURLと未完の文が連結しています。正しいリンク先や意図を推測して本文を書き換えていません。次に整理するなら、[高校化学の異性体](../foundations/high-school-chemistry.md#source-L477)から、グラフによる表現で何が残り、何が省かれるかを確かめる経路が考えられます。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [物性化学](../../physics/electromagnetism-matter/physical-chemistry.md)
- [生命科学](../life-sciences/life-sciences.md)
- [高校化学](../foundations/high-school-chemistry.md)
- [量子論](../../physics/quantum/quantum-theory.md)
- [バイオインフォマティクス](../life-sciences/bioinformatics.md)
- [マテリアルズインフォマティクス](materials-informatics.md)
- [AIロボット駆動科学](automated-experimental-science.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
