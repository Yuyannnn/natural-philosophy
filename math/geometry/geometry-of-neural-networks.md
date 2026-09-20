---
title: "ニューラルネットワークの幾何学的見方"
status: draft
tags: [scrapbox, geometry]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%A9%E3%83%AB%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%81%AE%E5%B9%BE%E4%BD%95%E5%AD%A6%E7%9A%84%E8%A6%8B%E6%96%B9"
source_created: "2023-02-14T05:23:58Z"
source_updated: "2023-02-14T05:29:00Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# ニューラルネットワークの幾何学的見方

ニューラルネットワークを幾何・トポロジー・力学から捉える資料の入口。

原ページ作成：2023-02-14 ／ 最終更新：2023-02-14（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/geometry-of-neural-networks.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%A9%E3%83%AB%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF%E3%81%AE%E5%B9%BE%E4%BD%95%E5%AD%A6%E7%9A%84%E8%A6%8B%E6%96%B9)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### ニューラルネットワークの幾何学的見方


> <a id="source-L3"></a>ニューラルネットワーク、幾何学、トポロジー  

> > <a id="source-L4"></a><https://qiita.com/KojiOhki/items/af2241027b00f892d2bd>  

> <a id="source-L6"></a>DNNの力学的・幾何学的解釈  

> > <a id="source-L7"></a><https://www.ai-gakkai.or.jp/jsai2016/webprogram/2016/pdf/773.pdf>  

> <a id="source-L9"></a>多様体間のトポロジー的に豊富な写像の深い可逆近似  

> > <a id="source-L10"></a><https://jglobal.jst.go.jp/detail?JGLOBAL_ID=202202203128251645>  

> <a id="source-L12"></a>深層学習の数理  

> > <a id="source-L13"></a><https://www.slideshare.net/trinmu/ss-161240890>  



<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

幾何学的な図を使うときは、入力空間、隠れ表現の空間、パラメータ空間のどれを描いているかを指定する。ネットワークの写像が可逆とは限らず、次元削減や活性化関数によって情報が失われる場合もある。原文にある可逆近似の資料については、その論文が置く条件を読むことが次の作業になる。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [同じ分野のノート](README.md)：幾何・テンソル。

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
