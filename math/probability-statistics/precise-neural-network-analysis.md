---
title: "精密解析"
status: draft
tags: [scrapbox, probability-statistics]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E7%B2%BE%E5%AF%86%E8%A7%A3%E6%9E%90"
source_created: "2025-09-02T10:31:34Z"
source_updated: "2025-09-04T03:36:33Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 精密解析

NTK・平均場・テンソル計画など、学習の動力学を分析する理論へのメモ。

原ページ作成：2025-09-02 ／ 最終更新：2025-09-04（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/precise-neural-network-analysis.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E7%B2%BE%E5%AF%86%E8%A7%A3%E6%9E%90)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 精密解析

<a id="source-L2"></a>[深層学習の原理](https://scrapbox.io/MistMavGamer/%E6%B7%B1%E5%B1%A4%E5%AD%A6%E7%BF%92%E3%81%AE%E5%8E%9F%E7%90%86)  
<a id="source-L3"></a>[統計的機械学習](statistical-machine-learning.md)  
<a id="source-L4"></a>[モデルの内部構造解析](https://scrapbox.io/MistMavGamer/%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%86%85%E9%83%A8%E6%A7%8B%E9%80%A0%E8%A7%A3%E6%9E%90)  
<a id="source-L5"></a>[計算量理論](../information-discrete/computational-complexity.md)  
<a id="source-L6"></a>[確率](probability.md)  
<a id="source-L7"></a>[統計力学](https://scrapbox.io/MistMavGamer/%E7%B5%B1%E8%A8%88%E5%8A%9B%E5%AD%A6)  


> <a id="source-L10"></a>NTK理論  

<a id="source-L11"></a>線形近似可能なNNの動力学理論  


> <a id="source-L14"></a>動的平均場理論  

<a id="source-L15"></a>多層NNで有効だが、数学証明は2層まで  


> <a id="source-L18"></a>平均場理論  

<a id="source-L19"></a>2層NNなら  


> <a id="source-L22"></a>テンソル計画法  

<a id="source-L23"></a>多層NNで有効だが、指数計算時間  
<a id="source-L24"></a>ワンチャンTransformerに適用  
<a id="source-L25"></a>言語モデルと、数値的なnnはデータ構造が違うのでそのまま適用は難しいかも  



> <a id="source-L29"></a>Precise gradient descent training dynamics for finite-width multi-layer neural networks  

<a id="source-L30"></a><https://arxiv.org/abs/2505.04898>  




> <a id="source-L35"></a>Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer  

<a id="source-L36"></a><https://arxiv.org/pdf/2203.03466>  



<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

本文の「数学証明は2層まで」「多層で有効」といった記述は、対象・時点・論文を特定しないと一般的な結論にはできない。当時の記録として保持する。[Jacot・Gabriel・HonglerのNTK論文](https://arxiv.org/abs/1806.07572)は、無限幅の極限など特定の設定で学習をカーネルから捉える。有限幅・特徴学習・異なるスケーリングの結果と区別して読む。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [統計的機械学習](statistical-machine-learning.md)
- [計算量理論](../information-discrete/computational-complexity.md)
- [確率](probability.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
