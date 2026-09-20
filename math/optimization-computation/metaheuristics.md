---
title: "メタヒューリスティクス"
status: draft
tags: [scrapbox, optimization-computation]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E3%83%A1%E3%82%BF%E3%83%92%E3%83%A5%E3%83%BC%E3%83%AA%E3%82%B9%E3%83%86%E3%82%A3%E3%82%AF%E3%82%B9"
source_created: "2023-02-21T21:30:28Z"
source_updated: "2024-07-06T06:15:15Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# メタヒューリスティクス

貪欲法・山登り法・焼きなまし法などの関係を整理する資料メモ。

原ページ作成：2023-02-21 ／ 最終更新：2024-07-06（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/metaheuristics.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E3%83%A1%E3%82%BF%E3%83%92%E3%83%A5%E3%83%BC%E3%83%AA%E3%82%B9%E3%83%86%E3%82%A3%E3%82%AF%E3%82%B9)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### メタヒューリスティクス

<a id="source-L2"></a>[ヒューリスティックコンテスト](https://scrapbox.io/MistMavGamer/%E3%83%92%E3%83%A5%E3%83%BC%E3%83%AA%E3%82%B9%E3%83%86%E3%82%A3%E3%83%83%E3%82%AF%E3%82%B3%E3%83%B3%E3%83%86%E3%82%B9%E3%83%88)  
<a id="source-L3"></a>[数理最適化](mathematical-optimization.md)  

> <a id="source-L5"></a>ヒューリスティック最適化資料集  

<a id="source-L6"></a><https://heuristic-ja.growi.cloud/リンク集>  



> <a id="source-L10"></a>貪欲法、山登り法、焼きなまし、ビームサーチ、これらの間の関係について  

<a id="source-L11"></a><https://kmyk.github.io/blog/blog/2019/03/07/local-search-and-greedy/>  




> <a id="source-L16"></a>焼きなまし法  


> <a id="source-L19"></a>ビームサーチ  


> <a id="source-L22"></a>GA  


> <a id="source-L25"></a>ACO  


> <a id="source-L28"></a>タブーサーチ  


> <a id="source-L31"></a>粒子群最適化  



> <a id="source-L35"></a>Introduction to Design and Implementation of Metaheuristics  

<a id="source-L36"></a><https://speakerdeck.com/umepon/introduction-to-design-and-implementation-of-metaheuristics>  


<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

良い解が得られたことと、最適性が証明されたことを区別する。乱数を使う手法では、種、計算予算、複数回のばらつき、比較する基準を残す。同じ問題でも、表現や近傍の選び方で結果が変わるため、手法名だけで性能を判断しない。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [数理最適化](mathematical-optimization.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
