---
title: "数論"
status: draft
tags: [scrapbox, algebra]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E6%95%B0%E8%AB%96"
source_created: "2023-02-01T04:27:15Z"
source_updated: "2023-02-01T04:27:26Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 数論

整数・合同式・剰余類など、数論の基礎をたどる項目。

原ページ作成：2023-02-01 ／ 最終更新：2023-02-01（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/number-theory.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E6%95%B0%E8%AB%96)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<details>
<summary>本文の見出しから探す</summary>

- [「数論初歩」](#source-L4)
- [「代数的整数論」](#source-L59)
- [0 有理整数環のイデアルと剰余環](#source-L61)
- [1 ピタゴラス数とガウスの整数環](#source-L63)
- [2 代数的整数](#source-L65)
- [3 代数体](#source-L67)
- [4 代数体のイデアル](#source-L69)
- [5 類数の有限性](#source-L71)
- [6 イデアル論の基本定理](#source-L73)
- [7 イデアルのノルム](#source-L75)
- [8 単数](#source-L77)
- [9 素数の分解](#source-L79)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 数論

<a id="source-L2"></a>Number Theory  


<a id="source-L4"></a>

### 「数論初歩」

<a id="source-L5"></a>PDF  

<a id="source-L7"></a>1章 数論の基礎  
<a id="source-L8"></a>自然数  
<a id="source-L9"></a>整数  
<a id="source-L10"></a>約数と倍数  
<a id="source-L11"></a>１次不定方程式  
<a id="source-L12"></a>素数  

<a id="source-L14"></a>2章 剰余類  
<a id="source-L15"></a>合同式  
<a id="source-L16"></a>オイラーの関数  
<a id="source-L17"></a>1のn乗根  
<a id="source-L18"></a>フェルマの小定理  
<a id="source-L19"></a>原始根と指数  


<a id="source-L22"></a>3章 相互法則  
<a id="source-L23"></a>平方剰余  
<a id="source-L24"></a>平方剰余の相互法則  
<a id="source-L25"></a>いくつかの別証明  

<a id="source-L27"></a>4章 除去のできる環  
<a id="source-L28"></a>ユークリッド整域  
<a id="source-L29"></a>多項式環  
<a id="source-L30"></a>ガウス整数環  

<a id="source-L32"></a>5章 連分数  
<a id="source-L33"></a>一次不定方程式と連分数  
<a id="source-L34"></a>２次行列と実数の連分数展開  
<a id="source-L35"></a>連分数と格子点  

<a id="source-L37"></a>6章 ペル方程式  
<a id="source-L38"></a>解集合の構造と解の存在  
<a id="source-L39"></a>連分数による解の構成  

<a id="source-L41"></a>7章 素数分布  
<a id="source-L42"></a>素数の分布とは  
<a id="source-L43"></a>素数が無数にあることの別証明  
<a id="source-L44"></a>素数ぶんぷの探究  
<a id="source-L45"></a>素数定理  

<a id="source-L47"></a>8章 存在と構成  
<a id="source-L48"></a>自然数の構成  
<a id="source-L49"></a>整数と有理数の構成  

<a id="source-L51"></a>9章 解答  
<a id="source-L52"></a>演習問題解答  
<a id="source-L53"></a>入試問題解答  



<a id="source-L57"></a>—————————————————————————————————  


<a id="source-L59"></a>

### 「代数的整数論」



<a id="source-L61"></a>

### 0 有理整数環のイデアルと剰余環



<a id="source-L63"></a>

### 1 ピタゴラス数とガウスの整数環



<a id="source-L65"></a>

### 2 代数的整数



<a id="source-L67"></a>

### 3 代数体



<a id="source-L69"></a>

### 4 代数体のイデアル



<a id="source-L71"></a>

### 5 類数の有限性



<a id="source-L73"></a>

### 6 イデアル論の基本定理



<a id="source-L75"></a>

### 7 イデアルのノルム



<a id="source-L77"></a>

### 8 単数



<a id="source-L79"></a>

### 9 素数の分解


<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

合同式を計算するときは、法を固定する。整数の合同類で割り算をしたいなら、割る元に逆元が存在するかを確かめる。たとえば法6で2は逆元を持たないが、5は $5\cdot5\equiv1\pmod6$ なので逆元を持つ。整数と体では同じ操作ができるとは限らない、という区別が代数への接点になる。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [同じ分野のノート](README.md)：代数・圏論・数論。

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
