---
title: "MCMC"
status: draft
tags: [scrapbox, probability-statistics]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/MCMC"
source_created: "2024-01-14T02:26:33Z"
source_updated: "2024-01-14T02:27:05Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# MCMC

ベイズ・MCMC・統計モデルの関係を確かめるための短いリンクメモ。

原ページ作成：2024-01-14 ／ 最終更新：2024-01-14（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/mcmc.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/MCMC)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### MCMC

<a id="source-L2"></a>[統計的機械学習](statistical-machine-learning.md)  

> <a id="source-L4"></a>ベイズとMCMCと統計モデルの関係  

<a id="source-L5"></a><https://logics-of-blue.com/ベイズとmcmcと統計モデルの関係/#:~:text=MCMCを使う目的は,を推定することです%E3%80%82>  


<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

MCMCは事後分布そのものではなく、目標分布からの期待値などを近似するための計算方法の一つ。標本は通常、互いに独立ではない。モデルの妥当性と、連鎖が十分に混合したかは別の確認事項になる。短い原メモを広げるなら、有限状態の遷移行列で定常分布を求め、実際の頻度と比較する例から始められる。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [統計的機械学習](statistical-machine-learning.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
