---
title: "圏論"
status: draft
tags: [scrapbox, algebra]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E5%9C%8F%E8%AB%96"
source_created: "2023-01-18T11:25:24Z"
source_updated: "2024-10-24T13:10:50Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 圏論

「自然な」とは何か、矢印の合成とは何か、という問いを含む記録。

原ページ作成：2023-01-18 ／ 最終更新：2024-10-24（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/category-theory.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E5%9C%8F%E8%AB%96)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

## 思考の手がかり

> 「自然な」とは？

[本文の該当箇所へ](#source-L48)

> 矢印の合成が本質

[本文の該当箇所へ](#source-L49)

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 圏論


<a id="source-L3"></a>[数学の分野を復習しながらお気持ち確認](../learning-paths/revisiting-mathematics.md)  
<a id="source-L4"></a>[数学・物理・情報科学・機械工学の分野マップ(独断と偏見)](../learning-paths/original-field-map.md)  
<a id="source-L5"></a>[圏論的量子力学入門](categorical-quantum-mechanics.md)  
<a id="source-L6"></a>[線形代数](../linear-algebra/linear-algebra.md)  
<a id="source-L7"></a>[代数の基礎](algebra-foundations.md)  
<a id="source-L8"></a>[微分幾何学とトポロジー](../geometry/differential-geometry-and-topology.md)  
<a id="source-L9"></a>[多様体](../geometry/manifolds.md)  
<a id="source-L10"></a>[圏論的機械学習](categorical-machine-learning.md)  


> <a id="source-L13"></a>圏論勉強会  

> > <a id="source-L14"></a><http://nineties.github.io/category-seminar>  
> > <a id="source-L15"></a><https://www.youtube.com/watch?v=uWST7UivqeM>  
> > <a id="source-L16"></a>圏論勉強会のYoutubeいいぞ〜  



> <a id="source-L20"></a>トポロジーと圏論の夜明け  

> > <a id="source-L21"></a>[https://www.youtube.com/watch?v=h_YJDTdHhU4](<https://www.youtube.com/watch?v=h_YJDTdHhU4>)  



> <a id="source-L25"></a>圏論の地平線  

> > <a id="source-L26"></a><https://gihyo.jp/book/2022/978-4-297-13150-0>  
> > <a id="source-L27"></a>良いらしい  



> <a id="source-L31"></a>圏論でゲーム攻略  

> > <a id="source-L32"></a><https://twitter.com/0xtkgshn/status/1617747220320735237?s=20&t=rhwOTLPoK4tj-ONOUtNWdw>  
> > <a id="source-L33"></a><https://gihyo.jp/science/serial/01/category_theory_talk/0001>  



> <a id="source-L37"></a>[/tkgshn/2023/1/24 神話構造から圏論完全理解](https://scrapbox.io/tkgshn/2023/1/24%20%E7%A5%9E%E8%A9%B1%E6%A7%8B%E9%80%A0%E3%81%8B%E3%82%89%E5%9C%8F%E8%AB%96%E5%AE%8C%E5%85%A8%E7%90%86%E8%A7%A3)  

> > <a id="source-L38"></a>面白い！！  



> <a id="source-L42"></a>圏論  

<a id="source-L43"></a><http://alg-d.com/math/kan_extension/>  



> <a id="source-L47"></a>メモ  

<a id="source-L48"></a>「自然な」とは？  
<a id="source-L49"></a>矢印の合成が本質  
<a id="source-L50"></a>全てはKAN拡張  
<a id="source-L51"></a>矢印が主体らしい、矢印を解析  
<a id="source-L52"></a>米田の補題「矢印見れば元が同値みたいな」  
<a id="source-L53"></a>自然変換：ガッチリ定義が決まっている？ボンボン  


> <a id="source-L56"></a>関連するらしいリンク  

> > <a id="source-L57"></a>[微分幾何学とトポロジー](../geometry/differential-geometry-and-topology.md)  
> > <a id="source-L58"></a>[代数の基礎](algebra-foundations.md)  
> > <a id="source-L59"></a>[線形代数](../linear-algebra/linear-algebra.md)  


> <a id="source-L62"></a>ニューラルネットワークの圏論的分析  

<a id="source-L63"></a><https://ibisml.org/ibis2021/files/2021/11/katsumata_ibis2021.pdf>  



> <a id="source-L67"></a>Category Theory in Machine Learning  



> <a id="source-L71"></a>数理科学11月号〜拡がりゆく圏論〜  

<a id="source-L73"></a>集合にはない特徴を備えた集まりとして圏という新概念が打ち立てられた  

<a id="source-L75"></a>集合論では、元・集合が先で、写像が後であるが、圏論では射が先で、集合が後である  

<a id="source-L77"></a>モノイダル圏としての量子論  
<a id="source-L78"></a>量子論の数学的構造をモノイダル圏とよばれる圏として捉えると、量子論の構造をある程度視覚的にわかりやすい形で表せる  

<a id="source-L80"></a>圏論的機械学習  





<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

「矢印が本質」という直感を保ちつつ、対象・射・合成・恒等射・結合法則を一組で定義する。自然変換の「自然」は日常語の印象ではなく、関手の間の射の族が可換図式を満たす条件。米田の補題も「元が同じ」という一句には置き換えない。次は集合と写像の圏で、合成と可換図式を一つ書くところから始める。[Riehl, Category Theory in Context](https://emilyriehl.github.io/files/context.pdf)を定義の参照先にできる。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [数学の分野を復習しながらお気持ち確認](../learning-paths/revisiting-mathematics.md)
- [数学・物理・情報科学・機械工学の分野マップ(独断と偏見)](../learning-paths/original-field-map.md)
- [圏論的量子力学入門](categorical-quantum-mechanics.md)
- [線形代数](../linear-algebra/linear-algebra.md)
- [代数の基礎](algebra-foundations.md)
- [微分幾何学とトポロジー](../geometry/differential-geometry-and-topology.md)
- [多様体](../geometry/manifolds.md)
- [圏論的機械学習](categorical-machine-learning.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
