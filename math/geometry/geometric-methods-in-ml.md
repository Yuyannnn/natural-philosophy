---
title: "MLにおける幾何学的手法"
status: draft
tags: [scrapbox, geometry]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/ML%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E5%B9%BE%E4%BD%95%E5%AD%A6%E7%9A%84%E6%89%8B%E6%B3%95"
source_created: "2023-01-18T11:14:52Z"
source_updated: "2025-09-27T08:19:10Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# MLにおける幾何学的手法

空間をEuclid空間と決めつけず、双曲空間での表現学習を考えたいという記録。

原ページ作成：2023-01-18 ／ 最終更新：2025-09-27（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/geometric-methods-in-ml.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/ML%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E5%B9%BE%E4%BD%95%E5%AD%A6%E7%9A%84%E6%89%8B%E6%B3%95)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

## 思考の手がかり

> 数学わからなすぎる、、幾何学勉強せねば

[本文の該当箇所へ](#source-L13)

> 今度から、MLの数式見たときに距離空間の暗黙の仮定を忘れて、一般的に考える癖をつけよう

[本文の該当箇所へ](#source-L29)

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### MLにおける幾何学的手法

<a id="source-L2"></a>[多様体](manifolds.md)  
<a id="source-L3"></a>[幾何学の基礎of基礎](geometry-foundations.md)  
<a id="source-L4"></a>[微分幾何学とトポロジー](differential-geometry-and-topology.md)  
<a id="source-L5"></a>[座標変換](coordinate-transformations.md)  
<a id="source-L6"></a>[微分形式](differential-forms.md)  
<a id="source-L7"></a>[テンソルと奮闘](tensors.md)  
<a id="source-L8"></a>[一般相対論](https://scrapbox.io/MistMavGamer/%E4%B8%80%E8%88%AC%E7%9B%B8%E5%AF%BE%E8%AB%96)  
<a id="source-L9"></a>[圏論](../algebra/category-theory.md)  
<a id="source-L10"></a>[モデルの内部構造解析](https://scrapbox.io/MistMavGamer/%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%86%85%E9%83%A8%E6%A7%8B%E9%80%A0%E8%A7%A3%E6%9E%90)  


<a id="source-L13"></a>数学わからなすぎる、、幾何学勉強せねば  


> <a id="source-L16"></a>異空間への埋め込み！Poincare Embeddingsが拓く表現学習の新展開  

<a id="source-L17"></a><https://tech-blog.abeja.asia/entry/poincare-embeddings>  
<a id="source-L18"></a><https://github.com/TatsuyaShirakawa>  

<a id="source-L20"></a>めっっっっっっっっっちゃ面白い  
<a id="source-L21"></a>思考停止で空間 = Euclid空間だと考えてたけど、冷静に考えて双曲空間に拡張したらもっとよいEmbeddingがあるかもしれないのはそれはそうすぎる  

<a id="source-L23"></a>双極空間には木構造を自然な形で埋め込める(?)  

<a id="source-L25"></a>ポアンカレ球で表現  

<a id="source-L27"></a>Graph Convolutionがうまくいくのはグラフに局所性や再帰性、フラクタル性、階層構造があるから  

<a id="source-L29"></a>今度から、MLの数式見たときに距離空間の暗黙の仮定を忘れて、一般的に考える癖をつけよう  




> <a id="source-L34"></a>双曲空間でのMachine Learningの最近の進展  

<a id="source-L35"></a><https://tech-blog.abeja.asia/entry/hyperbolic_ml_2019>  

<a id="source-L37"></a>まとめ  
<a id="source-L38"></a>木なら2次元で十分  
<a id="source-L39"></a>双曲空間では指数写像/対数写像が明示的に計算され空間全体に拡張されるので取扱が容易  
<a id="source-L40"></a>Gyrovector space: 双曲空間における線形代数のような代数構造  
<a id="source-L41"></a>Riemann幾何とGyrovector spaceの整合  
<a id="source-L42"></a>双曲空間とガウス分布のFisher情報幾何の対応  





> <a id="source-L48"></a>リーマン多様体上での機械学習  




> <a id="source-L53"></a>Hyperbolic Neural Network  




> <a id="source-L58"></a>坪井さんの幾何の講義、大体YouTubeにある  

<a id="source-L59"></a><https://twitter.com/totomityann/status/1648343550697029632?s=20>  





> <a id="source-L65"></a>データの幾何学と機械学習  

<a id="source-L66"></a>データが持つ幾何学的性質と深層学習  
<a id="source-L67"></a>幾何学的深層学習の分子・結晶解析への応用  
<a id="source-L68"></a>幾何学的な表現学習  
<a id="source-L69"></a>言語の表現空間の形  
<a id="source-L70"></a>双曲埋め込みと潜在空間最適構成  
<a id="source-L71"></a>群上の調和解析と深層ニューラルネットワーク  
<a id="source-L72"></a>幾何学的力学と深層学習  

<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

「Euclid空間だと決めつけない」という原文の気づきを、このページの軸として残す。「双極空間」は文脈上「双曲空間」と読むのが自然だが、本文は原表記を保持した。階層構造の表現を狙う [Nickel・KielaのPoincaré Embeddings](https://arxiv.org/abs/1705.08039)が出発点になる。ただし、任意の木やデータを2次元に歪みなく埋め込める、という一般的保証ではない。距離、歪み、目的関数、評価対象を分けて比べる。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [多様体](manifolds.md)
- [幾何学の基礎of基礎](geometry-foundations.md)
- [微分幾何学とトポロジー](differential-geometry-and-topology.md)
- [座標変換](coordinate-transformations.md)
- [微分形式](differential-forms.md)
- [テンソルと奮闘](tensors.md)
- [圏論](../algebra/category-theory.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
