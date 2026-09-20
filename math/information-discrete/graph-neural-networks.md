---
title: "Graph Neural Network"
status: draft
tags: [scrapbox, information-discrete]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/Graph%20Neural%20Network"
source_created: "2023-01-22T12:25:31Z"
source_updated: "2026-01-16T07:07:39Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# Graph Neural Network

グラフ設計への論点と、物理や知識の表現への応用例を集めた記録。

原ページ作成：2023-01-22 ／ 最終更新：2026-01-16（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/graph-neural-networks.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/Graph%20Neural%20Network)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### Graph Neural Network

<a id="source-L2"></a>[表現学習](https://scrapbox.io/MistMavGamer/%E8%A1%A8%E7%8F%BE%E5%AD%A6%E7%BF%92)  
<a id="source-L3"></a>[グラフ表現](graph-representations.md)  
<a id="source-L4"></a>[ナレッジグラフ](https://scrapbox.io/MistMavGamer/%E3%83%8A%E3%83%AC%E3%83%83%E3%82%B8%E3%82%B0%E3%83%A9%E3%83%95)  
<a id="source-L5"></a>[グラフ理論/離散数学](graph-theory.md)  
<a id="source-L6"></a>\[競技プログラミングでよくあるアルゴリズム集\]  
<a id="source-L7"></a>[Graph Foundation Model](https://scrapbox.io/MistMavGamer/Graph%20Foundation%20Model)  


> <a id="source-L10"></a>グラフ深層学習のすすめ  

<a id="source-L11"></a>[https://www.youtube.com/watch?v=7rgXi3Xp6NI](<https://www.youtube.com/watch?v=7rgXi3Xp6NI>)  


<a id="source-L14"></a>タスクごとに特徴量設計を行う必要がある」を GNN を使う動機にしてるけど，わたしの経験上これはあんまり現実的じゃない．というのは GNN の性能はグラフに大きく依存するので「グラフ設計」が GNN 版の特徴量設計として強く残ってる．  



> <a id="source-L18"></a>PhysGraph: Physics-Based Integration Using Graph Neural Networks  

> > <a id="source-L19"></a><https://arxiv.org/abs/2301.11841v1>  
> > <a id="source-L20"></a>こんな応用ができるんや・・  



> <a id="source-L24"></a>Kaggleの2nd solutionでGraph Attentionが応用されている  

<a id="source-L25"></a><https://www.kaggle.com/competitions/shopee-product-matching/discussion/238022>  




> <a id="source-L30"></a>LangChainを使って自然文の入力を構造化データに変換する実験  

<a id="source-L31"></a><https://note.com/fukufuku_wanko/n/n698e4fdce300>  



> <a id="source-L35"></a>SOLVING NP-HARD PROBLEMS ON GRAPHS WITH EXTENDED ALPHAGO ZERO  

<a id="source-L36"></a><https://arxiv.org/pdf/1905.11623.pdf>  



> <a id="source-L40"></a>グラフニューラルネットワーク(GNN)徹底解説！用途と仕組みからPyGでの実装まで  

<a id="source-L41"></a><https://zenn.dev/kami/articles/83c2daff760f5d>  



> <a id="source-L45"></a>SymbolicRegression.jl  

<a id="source-L46"></a><https://github.com/MilesCranmer/SymbolicRegression.jl>  


<a id="source-L49"></a>[/k1ito/Deep Symbolic Regression RNNと強化学習でシンボリック回帰](https://scrapbox.io/k1ito/Deep%20Symbolic%20Regression%20RNN%E3%81%A8%E5%BC%B7%E5%8C%96%E5%AD%A6%E7%BF%92%E3%81%A7%E3%82%B7%E3%83%B3%E3%83%9C%E3%83%AA%E3%83%83%E3%82%AF%E5%9B%9E%E5%B8%B0)  




> <a id="source-L54"></a>ZEP: A TEMPORAL KNOWLEDGE GRAPH ARCHITECTURE FOR AGENT MEMORY  

<a id="source-L55"></a><https://arxiv.org/pdf/2501.13956>  




> <a id="source-L60"></a>Temporal Knowledge Graphで作る！時間変化するナレッジを扱うAI Agentの世界  

<a id="source-L61"></a><https://tech.layerx.co.jp/entry/tkg-agent>  




> <a id="source-L66"></a>Heterogeneous Graph Neural Network  

<a id="source-L67"></a><https://dl.acm.org/doi/abs/10.1145/3292500.3330961>  




> <a id="source-L72"></a>Auto-GNN: Neural Architecture Search of Graph Neural Networks  

<a id="source-L73"></a><https://arxiv.org/abs/1909.03184>  

<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

原文に残る「グラフ設計が特徴量設計として残る」という論点を消さない。モデル以前に、節点・辺・属性・時間をどう定めたかを記録する。小さな検証として節点の番号を付け替えたとき、節点の出力が対応して並び替わるか、グラフ全体の出力が変わらないかを調べると、設計した対称性を確かめられる。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [グラフ表現](graph-representations.md)
- [グラフ理論/離散数学](graph-theory.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
