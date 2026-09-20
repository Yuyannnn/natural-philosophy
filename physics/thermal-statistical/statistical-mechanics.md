---
title: "統計力学"
status: draft
tags: [scrapbox, thermal-statistical]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E7%B5%B1%E8%A8%88%E5%8A%9B%E5%AD%A6"
source_created: "2023-01-18T11:04:48Z"
source_updated: "2024-12-01T14:01:07Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 統計力学

学部1年で苦戦した記憶と、ミクロからマクロを説明する講義項目。

原ページ作成：2023-01-18 ／ 最終更新：2024-12-01（UTC、取得時点）

[物理学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/statistical-mechanics.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E7%B5%B1%E8%A8%88%E5%8A%9B%E5%AD%A6)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

## 思考の手がかり

> 学部1年のとき受けた授業で一番苦戦した気がする・・

[本文の該当箇所へ](#source-L11)

<details>
<summary>本文の見出しから探す</summary>

- [1．統計力学の基礎 ](#source-L20)
- [2．ミクロカノニカル分布 ](#source-L21)
- [3．カノニカル分布 ](#source-L22)
- [4. グランドカノニカル分布 ](#source-L23)
- [5. 身近な問題にみる統計力学](#source-L24)
- [1.プロローグ](#source-L32)
- [2.統計力学の基礎](#source-L35)
- [3.古典統計力学](#source-L38)
- [4.量子統計力学の基礎](#source-L41)
- [5.量子統計力学](#source-L44)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 統計力学

<a id="source-L2"></a>[微分積分学](../../math/analysis/calculus.md)  
<a id="source-L3"></a>[線形代数](../../math/linear-algebra/linear-algebra.md)  
<a id="source-L4"></a>[統計学](../../math/probability-statistics/statistics.md)  
<a id="source-L5"></a>[量子統計力学](quantum-statistical-mechanics.md)  
<a id="source-L6"></a>[分子工学](../electromagnetism-matter/molecular-engineering.md)  
<a id="source-L7"></a>[統計的機械学習](../../math/probability-statistics/statistical-machine-learning.md)  
<a id="source-L8"></a>[物性化学](../electromagnetism-matter/physical-chemistry.md)  


> <a id="source-L11"></a>学部1年のとき受けた授業で一番苦戦した気がする・・  

<a id="source-L13"></a>統計物理は, 自然界の身近なマクロな現象をミクロなレベルから解き明かす，現代物理学の基礎的な学問である.   
<a id="source-L14"></a>鉄は何で磁石に引かれるのだろう？ゴムは良く伸びるけど，手を離せばもとに戻ってしまう，   
<a id="source-L15"></a>そんな身近な疑問も, 分子, 原子, 電子といったミクロな構成要素が 無数に集まって統計的にどう振る舞うかを定式化すれば 簡単明瞭に理解することができる.   
<a id="source-L16"></a>熱力学では抽象的なマクロ変数をもとに熱平衡という概念を扱った. その際にエントロピーという一見正体不明の物理量が出てきただろう.   
<a id="source-L17"></a>ところが統計物理の言葉では, そのエントロピーの正体も少数の原理を仮定するだけで, 実に明快に定義することができるのである.   
<a id="source-L18"></a>本講義では, 統計物理の枠組みを初歩から理解し, そのうえでゴムや磁石などの問題を具体的に取り上げ, 物理学の面白さを知ってもらい, また物理的なものの見方を理解してもらうことを目標にする.　  


<a id="source-L20"></a>

### 1．統計力学の基礎 


<a id="source-L21"></a>

### 2．ミクロカノニカル分布 


<a id="source-L22"></a>

### 3．カノニカル分布 


<a id="source-L23"></a>

### 4. グランドカノニカル分布 


<a id="source-L24"></a>

### 5. 身近な問題にみる統計力学


<a id="source-L26"></a>以上の各テーマに２－３週程度分をあてる。講義の進行状況に応じて内容を変更することもある.  
<a id="source-L27"></a>特に、５に関しては昨年度までは相転移やイジングモデルを取り上げたが、  
<a id="source-L28"></a>今年度は量子力学との関連と, 黒体輻射の問題を取り上げる可能性もある。  
<a id="source-L29"></a>そのあたりは受講者の希望に応じて柔軟に対応したい。  



<a id="source-L32"></a>

### 1.プロローグ

<a id="source-L33"></a>ハミルトンの正準方程式、ガウス積分、ガンマ関数、n次元の球の体積、スターリングの公式、リーマンのゼータ関数、  


<a id="source-L35"></a>

### 2.統計力学の基礎

<a id="source-L36"></a>リウビルの定理、等確率の原理、エルゴード仮説、熱力学的重率、単原子分子理想気体の状態数、ボルツマンの原理、ギブズの原理  


<a id="source-L38"></a>

### 3.古典統計力学

<a id="source-L39"></a>かのにかるアンサンブルから導かれる公式、エネルギーの平均と分配関数、連続型の公式、デュロン・プティの法則、理想気体のエントロピー、グランドかのにかるアンサンブルの公式  


<a id="source-L41"></a>

### 4.量子統計力学の基礎

<a id="source-L42"></a>1次元調和振動子の全力学的エネルギー、一次元運動する粒子が持つエネルギー固有値、W個の量子調和振動子の全エネルギーEとエントロピーS、デバイの比熱式、プランクの放射法則、シュテファンボルツマンの法則、ウィーンの変位則  


<a id="source-L44"></a>

### 5.量子統計力学

<a id="source-L45"></a>フェルミ分布、ボース分布、  


<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

「一番苦戦した」という記録を、理解済みの要約で置き換えない。再開の足場として、熱浴と接する系のエネルギー準位 $E_i$ に対し $p_i=e^{-\beta E_i}/Z$、$Z=\sum_i e^{-\beta E_i}$、$\beta=1/(k_BT)$ を一組で考える。指数は無次元で、$Z$ が確率の規格化を担う。二準位系なら占有確率から微視的な状態と平均エネルギーの関係を追える。確認資料：[Feynman I-40](https://www.feynmanlectures.caltech.edu/I_40.html)。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [微分積分学](../../math/analysis/calculus.md)
- [線形代数](../../math/linear-algebra/linear-algebra.md)
- [統計学](../../math/probability-statistics/statistics.md)
- [量子統計力学](quantum-statistical-mechanics.md)
- [分子工学](../electromagnetism-matter/molecular-engineering.md)
- [統計的機械学習](../../math/probability-statistics/statistical-machine-learning.md)
- [物性化学](../electromagnetism-matter/physical-chemistry.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
