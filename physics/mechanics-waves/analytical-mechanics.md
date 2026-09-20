---
title: "解析力学"
status: draft
tags: [scrapbox, mechanics-waves]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E8%A7%A3%E6%9E%90%E5%8A%9B%E5%AD%A6"
source_created: "2023-01-18T10:55:27Z"
source_updated: "2024-12-26T11:10:32Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 解析力学

力学を体系化し、状態空間・ラグランジアン・ハミルトニアンで眺めるメモ。

原ページ作成：2023-01-18 ／ 最終更新：2024-12-26（UTC、取得時点）

[物理学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/analytical-mechanics.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E8%A7%A3%E6%9E%90%E5%8A%9B%E5%AD%A6)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

## 思考の手がかり

> 力学を体系化

[本文の該当箇所へ](#source-L48)

<details>
<summary>本文の見出しから探す</summary>

- [1.プロローグ](#source-L90)
- [2.ラグランジュの運動方程式](#source-L93)
- [3.ハミルトンの正準方程式](#source-L96)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 解析力学

<a id="source-L2"></a>[熱力学](../thermal-statistical/thermodynamics.md)  
<a id="source-L3"></a>[特殊相対性理論](../relativity-cosmology/special-relativity.md)  
<a id="source-L4"></a>[力学・機械力学](classical-mechanics.md)  
<a id="source-L5"></a>[電磁気学](../electromagnetism-matter/electromagnetism.md)  
<a id="source-L6"></a>[量子論](../quantum/quantum-theory.md)  
<a id="source-L7"></a>[量子力学](../quantum/quantum-mechanics.md)  
<a id="source-L8"></a>[グリーン関数と摂動問題](green-functions-and-perturbation.md)  
<a id="source-L9"></a>[微分積分学](../../math/analysis/calculus.md)  
<a id="source-L10"></a>[線形代数](../../math/linear-algebra/linear-algebra.md)  
<a id="source-L11"></a>[微分形式](../../math/geometry/differential-forms.md)  



> <a id="source-L15"></a>基礎講座物理学 --解析力学--  

<a id="source-L17"></a>1章 Lagrangianと最小作用の原理  
<a id="source-L18"></a>2章 対称性に基づいたLagrangianの決定  
<a id="source-L19"></a>3章 対称性と保存則  
<a id="source-L20"></a>4章 拘束のある系の扱い  
<a id="source-L21"></a>5章 連成振動  
<a id="source-L22"></a>6章 Hamilton形式  
<a id="source-L23"></a>7章 正準変換  
<a id="source-L24"></a>8章 Hamilton-Jacobi理論  
<a id="source-L25"></a>9章 微分形式を用いた記述  






> <a id="source-L32"></a><https://qiita.com/kaityo256/items/e9adf792210e8c022010>  

<a id="source-L34"></a>時間に依存する変数の組みについて時間微分がその変数で記述できている時それを力学形という  
<a id="source-L35"></a>つまり運動方程式とは系を記述する変数で張られた空間の点それぞれにその時間微分を表すベクトルを対応づける写像であると考えられる  
<a id="source-L36"></a>この写像は複数の関数から構成されますが、その関数は自由度の数だけ必要になる  
<a id="source-L37"></a>しかし、解析力学で学んだように、世の中の運動は単一のスカラー関数で支配されている  
<a id="source-L38"></a>さらにそのラグラジアンよりもハミルトニアンで考えた方が色々見通しが良くなる  
<a id="source-L39"></a>以下ではルジャンドル変換により、(r,v)を(q,p)に取り替えて、考えてみる  
<a id="source-L40"></a>ハミルトニアンを自分に共役な変数で偏微分すれば自分の時間微分が出てくる  





> <a id="source-L46"></a>解析力学  

<a id="source-L48"></a>力学を体系化  

<a id="source-L50"></a>1	ラグランジアン（Lagrangian）力学  
<a id="source-L51"></a>1.1	仮想仕事とダランベール（d’Alembert）の定理  
<a id="source-L52"></a>1.2	一般化速度と一般化力  
<a id="source-L53"></a>1.3	一般化座標と一般化速度の関数としての運動エネルギー  
<a id="source-L54"></a>1.4	ラグランジアン  
<a id="source-L55"></a>1.5	ハミルトニアン（Hamiltonian）  
<a id="source-L56"></a>1.6	正準共役運動量  
<a id="source-L57"></a>1.7	例題  
<a id="source-L58"></a>1.8	物理的に等価なラグランジアン  
<a id="source-L59"></a>1.9	ポテンシャルが速度に依存する場合（ローレンツ力）  
<a id="source-L60"></a>1.10	連続体のラグランジアン  
<a id="source-L61"></a>1.11	場のラグランジアン  
<a id="source-L62"></a>2	変分原理とラグランジアン力学  
<a id="source-L63"></a>2.1	オイラー（Euler）方程式  
<a id="source-L64"></a>2.2	ハミルトンの原理  
<a id="source-L65"></a>2.3	連続体のオイラー・ラグランジュ方程式  
<a id="source-L66"></a>2.4	場のオイラー・ラグランジュ方程式  
<a id="source-L67"></a>2.5	ラグランジュの未定係数法（Lagrange Multipliers）  
<a id="source-L68"></a>2.6	ホロノミック（Holonomic）な束縛条件を未定係数法で解く  
<a id="source-L69"></a>2.7	非ホロノミックな束縛条件への応用  
<a id="source-L70"></a>3	ネーター（Noether）の定理とハミルトニアン力学  
<a id="source-L71"></a>3.1	角運動量と回転対称性  
<a id="source-L72"></a>3.2	ネーターの定理  
<a id="source-L73"></a>3.3	場の理論のネーターの定理  
<a id="source-L74"></a>3.4	ハミルトン力学とルジャンドル（Legendre）変換  
<a id="source-L75"></a>3.5	位相空間とリュービル（Liouville）の定理  
<a id="source-L76"></a>4	正準変換  
<a id="source-L77"></a>4.1	正準変換  
<a id="source-L78"></a>4.2	ポアソン（Poisson）括弧  
<a id="source-L79"></a>5	ハミルトン・ヤコビ（Jacobi）方程式  
<a id="source-L80"></a>5.1	ハミルトン・ヤコビ方程式  
<a id="source-L81"></a>5.2	作用変数と角変数  
<a id="source-L82"></a>5.3	断熱不変量  
<a id="source-L83"></a>5.4	量子仮説  

<a id="source-L85"></a>解析力学とは何かと問われれば、「ニュートン力学を、一般化座標や一般化運動量を用いて、数学的により洗練された運動方程式で表現する力学」と答えられる。  
<a id="source-L86"></a>具体的には、ニュートンの運動方程式の代わりにラグランジュの運動方程式やハミルトンの正準方程式が使われる。  
<a id="source-L87"></a>解析力学で用いられる、汎関数、変分原理、最速高架線問題、仮想仕事の原理、位相空間とトラジェクトリー、正順変換、ポアソン括弧などは統計力学や量子力学まで関係する。  



<a id="source-L90"></a>

### 1.プロローグ

<a id="source-L91"></a>ラグランジュの運動方程式、ハミルトンの正準方程式、xyz座標の回転を表す行列  


<a id="source-L93"></a>

### 2.ラグランジュの運動方程式

<a id="source-L94"></a>ラグランジュの運動方程式、一般化運動量、一般化力、循環座標が存在するとき、一般化座標は保存される、ラグラジアンの不定性、極座標における一般化力の外力の成分の関係、面積要素、球座標における一般化力と外力の成分の関係、デカルト座標から球座標への変換行列、体積要素、汎関数、変分原理、オイラーの方程式、最小作用の原理、仮想仕事の原理、ダランベールの原理による仮想仕事の原理  


<a id="source-L96"></a>

### 3.ハミルトンの正準方程式

<a id="source-L97"></a>ハミルトンの正準方程式、H=T+U、Hが時刻tを陽に含まない時、リウビルの定理、母関数による清純変換、ポアソン括弧の公式、正準方程式のポアソン括弧による表現、ポアソン括弧による正準変換の判定、ポアソン括弧の清純変換に対する普遍性、無限小変換  



<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

[原文94行目](#source-L94)の循環座標で保存されるのは、一般化座標そのものではなく共役運動量 $p_i=\partial L/\partial\dot q_i$。Euler–Lagrange方程式より、$\partial L/\partial q_i=0$ なら $\dot p_i=0$ となる。

正準方程式は $\dot q_i=\partial H/\partial p_i$、$\dot p_i=-\partial H/\partial q_i$ で、二つ目の符号にも注意する。「最小作用」は常に最小という意味ではなく停留条件として扱う。一般の散逸系を単純な $L=T-V$ だけで記述できるとは限らない。以上は定義からの補足で、本文全体を校閲したものではない。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [熱力学](../thermal-statistical/thermodynamics.md)
- [特殊相対性理論](../relativity-cosmology/special-relativity.md)
- [力学・機械力学](classical-mechanics.md)
- [電磁気学](../electromagnetism-matter/electromagnetism.md)
- [量子論](../quantum/quantum-theory.md)
- [量子力学](../quantum/quantum-mechanics.md)
- [グリーン関数と摂動問題](green-functions-and-perturbation.md)
- [微分積分学](../../math/analysis/calculus.md)
- [線形代数](../../math/linear-algebra/linear-algebra.md)
- [微分形式](../../math/geometry/differential-forms.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
