---
title: "最適輸送"
status: draft
tags: [scrapbox, optimization-computation]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E6%9C%80%E9%81%A9%E8%BC%B8%E9%80%81"
source_created: "2023-01-23T06:21:50Z"
source_updated: "2024-09-23T08:46:52Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 最適輸送

確率分布を比較する道具として、最適輸送を学ぶ読書項目。

原ページ作成：2023-01-23 ／ 最終更新：2024-09-23（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/optimal-transport.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E6%9C%80%E9%81%A9%E8%BC%B8%E9%80%81)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 最適輸送

<a id="source-L2"></a>[数理最適化](mathematical-optimization.md)  
<a id="source-L3"></a>[統計的機械学習](../probability-statistics/statistical-machine-learning.md)  
<a id="source-L4"></a>[生成モデル](https://scrapbox.io/MistMavGamer/%E7%94%9F%E6%88%90%E3%83%A2%E3%83%87%E3%83%AB)  
<a id="source-L5"></a>[微分積分学](../analysis/calculus.md)  
<a id="source-L6"></a>[線形代数](../linear-algebra/linear-algebra.md)  


> <a id="source-L9"></a>最適輸送の理論とアルゴリズム  

<a id="source-L11"></a>1章 確率分布を比較するツールとしての最適輸送  
<a id="source-L12"></a>2章 最適問題としての最適化  
<a id="source-L13"></a>3章 エントロピー正則化とシンクホーンアルゴリズム  
<a id="source-L14"></a>4章 敵対的ネットワーク  
<a id="source-L15"></a>5章 スライス法  
<a id="source-L16"></a>6章 他のダイバージェンスとの比較  
<a id="source-L17"></a>7章 不均衡最適輸送  
<a id="source-L18"></a>8章 ワッサースタイン重心  
<a id="source-L19"></a>9章 グロモフ・ワッサースタイン距離  
<a id="source-L20"></a>10章 おわりに  




> <a id="source-L25"></a>Workshop OT  

<a id="source-L26"></a><http://webpark2072.sakura.ne.jp/otworkshop/index.php/program/>  



> <a id="source-L30"></a>最適輸送の基礎から最近の動向まで  

<a id="source-L31"></a><https://speakerdeck.com/ssii/ssii2024-ss2-ryomasato>  


<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

離散的な二つの確率分布なら、輸送量 $\pi_{ij}\ge0$ を変数にし、行和・列和をそれぞれの確率質量に一致させ、$\sum_{ij}c_{ij}\pi_{ij}$ を最小化するところから始められる。確率分布の重なりだけでなく、どこからどこへ動かすかの費用を使うのが見通しになる。正則化した目的値と、元のWasserstein距離は区別する。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [数理最適化](mathematical-optimization.md)
- [統計的機械学習](../probability-statistics/statistical-machine-learning.md)
- [微分積分学](../analysis/calculus.md)
- [線形代数](../linear-algebra/linear-algebra.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
