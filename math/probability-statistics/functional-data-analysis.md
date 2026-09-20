---
title: "関数データ解析"
status: draft
tags: [scrapbox, probability-statistics]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E9%96%A2%E6%95%B0%E3%83%87%E3%83%BC%E3%82%BF%E8%A7%A3%E6%9E%90"
source_created: "2025-09-09T00:53:24Z"
source_updated: "2025-10-09T04:43:12Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 関数データ解析

関数としての観測データと、異常検知をつなぐ資料の入口。

原ページ作成：2025-09-09 ／ 最終更新：2025-10-09（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/functional-data-analysis.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E9%96%A2%E6%95%B0%E3%83%87%E3%83%BC%E3%82%BF%E8%A7%A3%E6%9E%90)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 関数データ解析

<a id="source-L2"></a>[異常検知](https://scrapbox.io/MistMavGamer/%E7%95%B0%E5%B8%B8%E6%A4%9C%E7%9F%A5)  
<a id="source-L3"></a>[時系列解析](time-series-analysis.md)  
<a id="source-L4"></a>[ベイズ統計](bayesian-statistics.md)  
<a id="source-L5"></a>[異常検知](https://scrapbox.io/MistMavGamer/%E7%95%B0%E5%B8%B8%E6%A4%9C%E7%9F%A5)  



> <a id="source-L9"></a>関数データ解析  

<a id="source-L10"></a><https://speakerdeck.com/hidetoshimatsui/guan-shu-detajie-xi-henozhao-dai?slide=20>  



> <a id="source-L14"></a>関数データ解析への招待  

<a id="source-L15"></a><https://speakerdeck.com/hidetoshimatsui/guan-shu-detajie-xi-henozhao-dai?slide=20>  



> <a id="source-L19"></a>functionaly anomaly detection  

<a id="source-L20"></a><https://arxiv.org/pdf/2201.05115>  



> <a id="source-L24"></a>functional outlier detection  

<a id="source-L25"></a><https://arxiv.org/abs/2109.06849>  



> <a id="source-L29"></a>Multivariate Functional Outlier Detection using the FastMUOD Indices  

<a id="source-L30"></a><https://arxiv.org/abs/2207.12803>  



> <a id="source-L34"></a>fdaoutlier: Outlier Detection Tools for Functional Data Analysis  

<a id="source-L35"></a><https://cran.r-project.org/web/packages/fdaoutlier/index.html>  
<a id="source-L36"></a><https://cran.r-project.org/web/packages/fdaoutlier/vignettes/simulation_models.html>  






<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

一つの観測を曲線として扱うなら、時間点の数だけでなく、曲線同士の距離や滑らかさをどう定めるかが重要になる。測定間隔、欠測、時間のずれをそろえる処理が結果に与える影響も記録する。原ページの異常検知への関心は、振幅の異常と形の異常を別々に考える小さな例で具体化できる。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [時系列解析](time-series-analysis.md)
- [ベイズ統計](bayesian-statistics.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
