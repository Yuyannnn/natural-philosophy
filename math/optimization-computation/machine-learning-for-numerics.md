---
title: "機械学習で数値解析"
status: draft
tags: [scrapbox, optimization-computation]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%81%A7%E6%95%B0%E5%80%A4%E8%A7%A3%E6%9E%90"
source_created: "2023-02-14T07:06:06Z"
source_updated: "2023-02-14T07:06:28Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 機械学習で数値解析

偏微分方程式とニューラルネットワークをつなぐ論文への入口。

原ページ作成：2023-02-14 ／ 最終更新：2023-02-14（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/machine-learning-for-numerics.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%81%A7%E6%95%B0%E5%80%A4%E8%A7%A3%E6%9E%90)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 機械学習で数値解析


> <a id="source-L3"></a>[数値解析](numerical-analysis.md)  

> <a id="source-L5"></a>Partial Differential Equations Meet Deep Neural Networks: A Survey  

> > <a id="source-L6"></a><https://arxiv.org/abs/2211.05567v2>  

<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

論文を読む際は、何を学習するのかを分ける。解そのもの、時間発展、作用素、従来ソルバの一部では評価が異なる。学習に使わなかった初期条件や境界条件での誤差、保存則、計算時間を確認する案がある。原文が論文への短い入口であることは維持し、結果を検証済みと扱わない。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [数値解析](numerical-analysis.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
