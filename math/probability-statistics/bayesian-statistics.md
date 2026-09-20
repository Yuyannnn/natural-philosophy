---
title: "ベイズ統計"
status: draft
tags: [scrapbox, probability-statistics]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E3%83%99%E3%82%A4%E3%82%BA%E7%B5%B1%E8%A8%88"
source_created: "2025-08-14T14:23:00Z"
source_updated: "2025-10-27T16:53:36Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# ベイズ統計

ベイズ深層学習と、Stanによる統計モデリングの資料・読書項目。

原ページ作成：2025-08-14 ／ 最終更新：2025-10-27（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/bayesian-statistics.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E3%83%99%E3%82%A4%E3%82%BA%E7%B5%B1%E8%A8%88)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### ベイズ統計

<a id="source-L2"></a>[統計的機械学習](statistical-machine-learning.md)  
<a id="source-L3"></a>[因果推論](causal-inference.md)  
<a id="source-L4"></a>[生成モデル](https://scrapbox.io/MistMavGamer/%E7%94%9F%E6%88%90%E3%83%A2%E3%83%87%E3%83%AB)  
<a id="source-L5"></a>[確率](probability.md)  
<a id="source-L6"></a>[確率過程](stochastic-processes.md)  
<a id="source-L7"></a>[PRML](https://scrapbox.io/MistMavGamer/PRML)  
<a id="source-L8"></a>[統計学](statistics.md)  
<a id="source-L9"></a>[線形代数](../linear-algebra/linear-algebra.md)  
<a id="source-L10"></a>[微分積分学](../analysis/calculus.md)  
<a id="source-L11"></a>[深層学習の原理](https://scrapbox.io/MistMavGamer/%E6%B7%B1%E5%B1%A4%E5%AD%A6%E7%BF%92%E3%81%AE%E5%8E%9F%E7%90%86)  
<a id="source-L12"></a>[時系列解析](time-series-analysis.md)  


> <a id="source-L15"></a>ベイズ深層学習  

<a id="source-L16"></a>1章 はじめに  
<a id="source-L17"></a>2章 ニューラルネットワークの基礎  
<a id="source-L18"></a>3章 ベイズ推論の基礎  
<a id="source-L19"></a>4章 近所ベイズ推論  
<a id="source-L20"></a>5章 ニューラルネットワークのベイズ推論  
<a id="source-L21"></a>6章 深層生成モデル  
<a id="source-L22"></a>7章 深層学習とガウス過程  





> <a id="source-L28"></a>cmd-stan  

<a id="source-L29"></a><https://mc-stan.org/cmdstanpy/>  




> <a id="source-L34"></a>stanとRでベイズ統計モデリング  

<a id="source-L36"></a>Chapter1 統計モデリングとStanの概要  
<a id="source-L37"></a>Chapter2 ベイズ推定の復習  
<a id="source-L38"></a>Chapter3 統計モデリングをはじめる前に  
<a id="source-L39"></a>Chapter4 StanとRStanをはじめよう  
<a id="source-L40"></a>Chapter5 基本的な回帰とモデルのチェック  
<a id="source-L41"></a>Chpater6 統計モデリングの視点から確率分布の紹介  
<a id="source-L42"></a>Chapter7 回帰分析の悩みどころ  
<a id="source-L43"></a>Chapter8 階層モデル  
<a id="source-L44"></a>Chapter9 一歩進んだ文法  
<a id="source-L45"></a>Chapter10 収束しない場合の対処法  
<a id="source-L46"></a>Chapter11 離散値をとるパラメータを使う  
<a id="source-L47"></a>Chpater12 時間や空間を扱うモデル  





> <a id="source-L53"></a>【ノンパラメトリックベイズ】ディリクレ過程を用いたクラスタ数推定  

<a id="source-L54"></a><https://qiita.com/kwashi/items/ad3e02bdc25253638776>  




> <a id="source-L59"></a>入門 ベイズ統計学 (ファイナンス・ライブラリー 10)  

<a id="source-L60"></a>ファイナンス分野で特に有効なデータ分析手法の初歩を懇切丁寧に解説。〔内容〕ベイズ分析を学ぼう/ベイズ的視点から世界を見る/成功と失敗のベイズ分析/ベイズ的アプローチによる資産運用/マルコフ連鎖モンテカルロ法/練習問題/他。  





<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

事後分布は、事前分布と尤度を組み合わせ、全体が確率分布になるよう正規化したもの。$p(\theta\mid D)\propto p(D\mid\theta)p(\theta)$ と書いたら、比例定数の存在も含めて適切な事後分布になっているか確認する。データを見た後のモデル評価には、推定したパラメータだけでなく予測の振る舞いも使う。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [統計的機械学習](statistical-machine-learning.md)
- [因果推論](causal-inference.md)
- [確率](probability.md)
- [確率過程](stochastic-processes.md)
- [統計学](statistics.md)
- [線形代数](../linear-algebra/linear-algebra.md)
- [微分積分学](../analysis/calculus.md)
- [時系列解析](time-series-analysis.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
