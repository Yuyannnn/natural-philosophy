---
title: "因果推論"
status: draft
tags: [scrapbox, probability-statistics]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E5%9B%A0%E6%9E%9C%E6%8E%A8%E8%AB%96"
source_created: "2023-01-13T00:38:14Z"
source_updated: "2026-01-20T16:25:40Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 因果推論

相関と因果を区別し、効果検証と機械学習をつなぐ資料の入口。

原ページ作成：2023-01-13 ／ 最終更新：2026-01-20（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/causal-inference.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E5%9B%A0%E6%9E%9C%E6%8E%A8%E8%AB%96)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<details>
<summary>本文の見出しから探す</summary>

- [1 相関と因果の違いを理解しよう](#source-L32)
- [2 因果効果の種類を把握しよう](#source-L33)
- [3 グラフ表現とバックドア基準を理解しよう](#source-L34)
- [4 因果推論を実装しよう](#source-L35)
- [5 機械学習を用いた因果推論](#source-L36)
- [6 LiNGAMの実装](#source-L37)
- [7 ベイジアンネットワークの実装](#source-L38)
- [8 ディープラーニングを用いた因果探索](#source-L39)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 因果推論

<a id="source-L2"></a>[統計学](statistics.md)  
<a id="source-L3"></a>[確率](probability.md)  
<a id="source-L4"></a>[統計的機械学習](statistical-machine-learning.md)  
<a id="source-L5"></a>[時系列解析](time-series-analysis.md)  
<a id="source-L6"></a>[効果検証](https://scrapbox.io/MistMavGamer/%E5%8A%B9%E6%9E%9C%E6%A4%9C%E8%A8%BC)  


> <a id="source-L9"></a>統計的因果推論スライド  

> > <a id="source-L10"></a><https://speakerdeck.com/arumakan/tong-ji-de-yin-guo-tui-lun-falsemian-qiang-hui-at-2022>  


> <a id="source-L13"></a>DoWhyとEcon MLによる因果推論の実装  

> > <a id="source-L14"></a><https://speakerdeck.com/s1ok69oo/dowhytoeconmlniyoruyin-guo-tui-lun-noshi-zhuang>  


> <a id="source-L17"></a>リッジ回帰やラッソ回帰で因果推論できるのか？  

<a id="source-L18"></a><https://qiita.com/s1ok69oo/items/328781fc18bb75dca102>  



> <a id="source-L22"></a>因果探索アプリケーション「Causalas」  

<a id="source-L23"></a><https://twitter.com/sshimizu2006/status/1633019411937505280?s=20>  



> <a id="source-L27"></a>因果推論の科学  



> <a id="source-L31"></a>Pythonによる因果分析  

<a id="source-L32"></a>

### 1 相関と因果の違いを理解しよう


<a id="source-L33"></a>

### 2 因果効果の種類を把握しよう


<a id="source-L34"></a>

### 3 グラフ表現とバックドア基準を理解しよう


<a id="source-L35"></a>

### 4 因果推論を実装しよう


<a id="source-L36"></a>

### 5 機械学習を用いた因果推論


<a id="source-L37"></a>

### 6 LiNGAMの実装


<a id="source-L38"></a>

### 7 ベイジアンネットワークの実装


<a id="source-L39"></a>

### 8 ディープラーニングを用いた因果探索






> <a id="source-L45"></a>【新卒研修資料】効果検証\_因果推論 / Impact evaluation Causal in...  

<a id="source-L46"></a><https://speakerdeck.com/brainpadpr/effect-verification-causal-inference>  




> <a id="source-L51"></a>plus-d\_ omi MMM（マーケティング・ミックス・モデリング）とは？  

<a id="source-L52"></a><https://xica.net/capabilities/marketing-mix-modeling/?source=WebAd&sf_media=gaw&sf_media_d=gs_general_m_mmm&sf_content=site_magellan-top&creative=000-SR026.m03mmm&kwd=mmm&utm_source=google&utm_medium=gaw&utm_campaign=gs_general_m_mmm&utm_content=000-SR026.m03&utm_term=mmm&gad_source=1&gad_campaignid=12653822840&gbraid=0AAAAABxhiMgv4jd1jm8WNFXXRac-yyTYP&gclid=CjwKCAjwq9rFBhAIEiwAGVAZP7ddikLiVk9NlLxHwIOVjvWFoeIFifaoph4-VmoANnNJizARz9XjDhoC96EQAvD_BwE>  




> <a id="source-L57"></a>CausalImpact  

<a id="source-L58"></a><https://google.github.io/CausalImpact/CausalImpact.html>  






> <a id="source-L65"></a>Inferring causal impact using Bayesian structural time-series models  

<a id="source-L66"></a><https://projecteuclid.org/journals/annals-of-applied-statistics/volume-9/issue-1/Inferring-causal-impact-using-Bayesian-structural-time-series-models/10.1214/14-AOAS788.full?tab=ArticleLinkReference>  





> <a id="source-L72"></a>状態空間モデルを用いた因果効果の推定: CausalImpact  

<a id="source-L73"></a><https://qiita.com/ssugasawa/items/d42fac583a15d8cd6c7d>  





> <a id="source-L79"></a>インベンス・ルービン 統計的因果推論 (上)   

<a id="source-L80"></a><https://www.amazon.co.jp/インベンス・ルービン-統計的因果推論-上-G-W-インベンス/dp/4254122918>  





<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

予測がよく当たることだけでは、介入の効果を識別できない。何を介入とし、どの集団のどの効果を求めるかを先に定める。未観測交絡や選択の仕組みにどんな仮定を置くかを、実装する手法名とは別に記す。回帰の正則化は過学習への対処になっても、それだけで交絡を解消するものではない。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [統計学](statistics.md)
- [確率](probability.md)
- [統計的機械学習](statistical-machine-learning.md)
- [時系列解析](time-series-analysis.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
