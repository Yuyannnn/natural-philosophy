---
title: "創薬AI"
status: draft
tags: [scrapbox, life-sciences]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E5%89%B5%E8%96%ACAI"
source_created: "2023-03-10T23:21:36Z"
source_updated: "2025-09-07T10:38:34Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 創薬AI

分子生成、タンパク質構造予測、高分子や創薬研究の資料。

原ページ作成：2023-03-10 ／ 最終更新：2025-09-07（UTC、取得時点）

[化学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/ai-drug-discovery.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E5%89%B5%E8%96%ACAI)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 創薬AI

<a id="source-L2"></a>[バイオインフォマティクス](bioinformatics.md)  
<a id="source-L3"></a>[バイオサイバネティクス](biocybernetics.md)  
<a id="source-L4"></a>[生物学](biology.md)  
<a id="source-L5"></a>[生物学的安全保障](https://scrapbox.io/MistMavGamer/%E7%94%9F%E7%89%A9%E5%AD%A6%E7%9A%84%E5%AE%89%E5%85%A8%E4%BF%9D%E9%9A%9C)  
<a id="source-L6"></a>[分子工学](../../physics/electromagnetism-matter/molecular-engineering.md)  
<a id="source-L7"></a>\[分子動力学シミュレーション\]  


> <a id="source-L10"></a>Alpha fold  



> <a id="source-L14"></a><https://twitter.com/yoko_materialDX/status/1633422323750412288?s=20>  

<a id="source-L15"></a>分子生成の論文。  

<a id="source-L17"></a>従来はルールに基づいて生成するため、それから逸脱した構造は生成できませんでした。  

<a id="source-L19"></a>Microsoftさんが、データベースから頻度の高い部分構造を抽出しその接続情報に基づき分子生成することで最高の予測性能を実現したそうです。  



> <a id="source-L23"></a><https://twitter.com/fladdict/status/1632778542630174720?s=20>  

<a id="source-L24"></a>高分子生成の論文。  

<a id="source-L26"></a>ダイセルさんから、候補となる低分子を与えると重合反応の可能性を調べ、合成可能な高分子を網羅的に生成できるPythonライブラリが公開されました。反応データ追加で拡張でき便利そう。  

<a id="source-L28"></a>大規模データベースの実現ももうすぐ？高分子MIが進展に期待。  



> <a id="source-L32"></a>東大と理研、狙った物性を示す物質を自動設計する理論手法を開発  

<a id="source-L33"></a><https://twitter.com/tjmlab/status/1631138266375409664?s=20>  




> <a id="source-L38"></a>ALpha fold3  

<a id="source-L40"></a><https://alphafoldserver.com/about>  




> <a id="source-L45"></a>AIを活用した新薬創出  

<a id="source-L46"></a><https://www.chugai-pharm.co.jp/profile/digital/ai_technology.html>  




> <a id="source-L51"></a>AIによるタンパク質構造予測が飛躍的に進化  

<a id="source-L52"></a><https://www.natureasia.com/ja-jp/ndigest/v18/n3/AIによるタンパク質構造予測が飛躍的に進化/106641>  




> <a id="source-L57"></a>Massive Foundation Model for Biomolecular Sciences Now Available via NVIDIA BioNeMo  

<a id="source-L58"></a><https://blogs.nvidia.com/blog/evo-2-biomolecular-ai/>  




> <a id="source-L63"></a>Dual use of artificial-intelligence-powered drug discovery  

<a id="source-L64"></a><https://www.nature.com/articles/s42256-022-00465-9?utm_source=chatgpt.com>  





> <a id="source-L70"></a>xFOREST Therapeutics  

<a id="source-L71"></a><https://www.xforestx.com/jp>  

<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

### 構造予測から何がわかるか

原文は分子生成やタンパク質構造予測に関する資料の集積です。[L14–28](#source-L14)にはSNSリンクに続く紹介文があり、その期待や評価を本人自身の研究成果とは扱いません。

AlphaFold 3は複合体を含む構造を予測しますが、分子の時間変化をそのまま計算するモデルではありません。構造上の衝突や立体化学の誤りも起こり得ることが[EMBL-EBIの公式教材](https://www.ebi.ac.uk/training/online/courses/alphafold/alphafold-3-and-alphafold-server/introducing-alphafold-3/what-alphafold-3-struggles-with/)で説明されています。構造予測の信頼度と、結合の強さや細胞での働きの測定結果は分けて読みます。

[L7](#source-L7)の「分子動力学シミュレーション」は取得時カタログでページを確認できなかったため、未解決のラベルとして保持しました。[分子工学](../../physics/electromagnetism-matter/molecular-engineering.md)への経路は既存ノートで補います。今回、個別候補の有効性や臨床的な評価は検証していません。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [バイオインフォマティクス](bioinformatics.md)
- [バイオサイバネティクス](biocybernetics.md)
- [生物学](biology.md)
- [分子工学](../../physics/electromagnetism-matter/molecular-engineering.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
