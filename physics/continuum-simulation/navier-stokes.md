---
title: "Navier-Stokes方程式"
status: draft
tags: [scrapbox, continuum-simulation]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/Navier-Stokes%E6%96%B9%E7%A8%8B%E5%BC%8F"
source_created: "2023-01-21T09:04:05Z"
source_updated: "2024-12-01T14:19:20Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# Navier-Stokes方程式

物質微分と応力から流体の運動方程式を追うメモ。

原ページ作成：2023-01-21 ／ 最終更新：2024-12-01（UTC、取得時点）

[物理学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/navier-stokes.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/Navier-Stokes%E6%96%B9%E7%A8%8B%E5%BC%8F)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<details>
<summary>本文の見出しから探す</summary>

- [0. Navier-Stokes方程式とは](#source-L15)
- [1.流体](#source-L25)
- [2.物理法則](#source-L38)
- [3.Stokes方程式](#source-L58)
- [1.応力](#source-L66)
- [2.平衡方程式](#source-L79)
- [3.体積モーメント](#source-L86)
- [4.主応力](#source-L94)
- [5.等方応力・偏差応力](#source-L102)
- [6.変形速度テンソル](#source-L108)
- [7.ナビエ・ストークス方程式の導出](#source-L115)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### Navier-Stokes方程式 

<a id="source-L2"></a>[流体力学](fluid-mechanics.md)  
<a id="source-L3"></a>[生体流体工学](biofluid-mechanics.md)  
<a id="source-L4"></a>[簡易版流体力学シミュレーション](fluid-simulation.md)  
<a id="source-L5"></a>[材料力学](mechanics-of-materials.md)  
<a id="source-L6"></a>[非線形波動論](../mechanics-waves/nonlinear-waves.md)  
<a id="source-L7"></a>[振動波動論](../mechanics-waves/oscillations-and-waves.md)  
<a id="source-L8"></a>[偏微分方程式](../../math/analysis/partial-differential-equations.md)  
<a id="source-L9"></a>[常微分方程式](../../math/analysis/ordinary-differential-equations.md)  
<a id="source-L10"></a>[有限要素法](finite-element-method.md)  


> <a id="source-L13"></a>よくわかるNavier-Stokes方程式      <http://watanabeckeiich.hatenablog.com/entry/2018/06/02/171540>  


<a id="source-L15"></a>

### 0. Navier-Stokes方程式とは

<a id="source-L16"></a>Navier-Stokes方程式は非圧縮性流体の運動を記述する方程式である  
<a id="source-L17"></a>第一式は流体の運動量保存  
<a id="source-L18"></a>第二式は流体の質量保存を表す  
<a id="source-L19"></a>粘性係数を0とした時はEuler方程式と呼ばれる  
<a id="source-L20"></a>Navier-Stokes方程式は二階非線型偏微分方程式である  
<a id="source-L21"></a>難しさは、非線型項と圧力項があることと、uの時間発展方程式だが圧力pに関してはそうでない故にu,pを同様に扱うことができない点にある  
<a id="source-L22"></a>3次元空間におけるNavier-Stokes方程式の解の存在とその滑らかさはいまだによくわかっていない  



<a id="source-L25"></a>

### 1.流体

<a id="source-L26"></a>1-1 圧縮性流体  
<a id="source-L27"></a>流体とは、気体と液体のことであり、これらの動きについて数式を用いて考えていこうというのが流体力学である  
<a id="source-L28"></a>この流体は主に２種類ある  
<a id="source-L29"></a>空気のように圧縮できる流体を圧縮性流体という  
<a id="source-L30"></a>ここでいう圧縮とは流体の密度が圧力の変化に応じて変化することをいう  

<a id="source-L32"></a>1-2 非圧縮性流体  
<a id="source-L33"></a>水のように圧縮できない流体を非圧縮性流体という  
<a id="source-L34"></a>この場合流体の密度が一定となる  
<a id="source-L35"></a>よって質量保存の式より、非圧縮性条件が出てくる  



<a id="source-L38"></a>

### 2.物理法則

<a id="source-L39"></a>2-1 Lagrange微分  
<a id="source-L40"></a>非線型項が出てくる原因はLagrange微分である  
<a id="source-L41"></a>Navier-Stokes方程式の第一式の左辺に現れる項はuのLagrange微分を表す  
<a id="source-L42"></a>Lagrange微分とは物質微分とも呼ばれ、ざっくり言えば、流体中の粒子を追いかけて微分しようというものである  
<a id="source-L43"></a>流体の測度ベクトルを微分するということは、物体の変化を捉えようとしているわけだが、知りたいのは流体がどんな形に変形されるかではなく、流体中の分子がどこからどこに移動したかを知りたいので速度ベクトルを時間で微分するだけでは不十分なので空間微分もする必要がある  
<a id="source-L44"></a>そこで時間と空間の微分を組み合わせた微分がLagrange微分である  

<a id="source-L46"></a>2-2 Cauchyの応力原理  
<a id="source-L47"></a>流体に対してCauchyの応力原理が成り立つ  
<a id="source-L48"></a>Cauchyの応力原理が成立する場合、運動量保存、すなわち運動方程式が成り立つ  

<a id="source-L50"></a>2-3 Stokesの連続公理  
<a id="source-L51"></a>変形速度テンソルDを次のように定義する  
<a id="source-L52"></a>応力テンソルTと変形速度テンソルDの間にStokesの流体公理を仮定した場合  
<a id="source-L53"></a>T = αI + βD + γD^2  
<a id="source-L54"></a>が成り立つ  
<a id="source-L55"></a>Stokesの流体公理を満たす連続体を流体と呼ぶので、この公理は成り立つと仮定して良い  



<a id="source-L58"></a>

### 3.Stokes方程式

<a id="source-L59"></a>流体の測度が遅い場合、すなわちレイノルズ数が小さい場合は非線型項は無視する  
<a id="source-L60"></a>ことができ、Navier-Stokes方程式で非線型項を無視したものをStokes方程式と呼ぶ  



<a id="source-L64"></a>よくわかるNavier-Stokes方程式 2  


<a id="source-L66"></a>

### 1.応力

<a id="source-L67"></a>固体に外力が作用すると固体は変形し、その内部に内力が発生する  
<a id="source-L68"></a>今、内力について考察したいので、固体内部の面積・方向などの変化は小さいとして無視する  
<a id="source-L69"></a>すなわち物体の点は移動しないとしてない力を考察する  
<a id="source-L70"></a>個体への外力の作用は  
<a id="source-L71"></a>１、表面力（圧力、支持力など）  
<a id="source-L72"></a>２、体積力（重力など）  
<a id="source-L73"></a>表面力をT(n)dSとした時、T(n)は応力テンソルという  
<a id="source-L74"></a>単位法線ベクトルをn,単位面積をdSとした  
<a id="source-L75"></a>応力テンソルは、境界面上の点Pと単位法線ベクトルnを指定すると決定される  




<a id="source-L79"></a>

### 2.平衡方程式

<a id="source-L80"></a>領域Vが受ける力は、表面力と堆積力であり、これらは積分で表せる  
<a id="source-L81"></a>また、領域Vの慣性力も考える  
<a id="source-L82"></a>したがって領域Vにおける運動方程式（質量保存則）がかける  
<a id="source-L83"></a>ガウスの発散定理と、テンソルの計算より、方程式が導かれ、これを平衡方程式という  



<a id="source-L86"></a>

### 3.体積モーメント

<a id="source-L87"></a>電場内で誘電体が影響を受ける場合あるいは磁場内で磁性体が影響を受ける場合などでは固体の各部分がモーメントを受けることがある  
<a id="source-L88"></a>この時、単位体積あたりに働くモーメントはベクトル量である  
<a id="source-L89"></a>このベクトル量を体積モーメントといい、Mで表す  
<a id="source-L90"></a>平衡方程式と角運動方程式を用いると、方程式が得られる  
<a id="source-L91"></a>体積モーメントが0であれば応力テンソルは対称テンソルである  



<a id="source-L94"></a>

### 4.主応力

<a id="source-L95"></a>固体内の点を通る微小面をとり、nを微小面分の単位法線ベクトルとする  
<a id="source-L96"></a>この微小面分を通じて作用する応力ベクトルのn方向への成分をn方向の垂直応力という  
<a id="source-L97"></a>単位ベクトルを変化させた時のT(n)の極値を点Pでの主応力という  
<a id="source-L98"></a>T(n)が主応力となるようなnの向きを点pにおける主方向という  
<a id="source-L99"></a>主応力は応力テンソルの固有値である  



<a id="source-L102"></a>

### 5.等方応力・偏差応力

<a id="source-L103"></a>応力テンソルのトレースは不変量である  
<a id="source-L104"></a>そこで、主応力の平均を等方テンソルという  
<a id="source-L105"></a>また、偏差応力が定義できる  



<a id="source-L108"></a>

### 6.変形速度テンソル

<a id="source-L109"></a>一般に流体の応力は流体の速度の空間的な変化によって引き起こされると考えられている  
<a id="source-L110"></a>ここで、ベクトル値関数の微分を定義し、その反対称部分・対称部分をそれぞれ、  
<a id="source-L111"></a>G(u)、D(u)とおくと、∇uが分解できる  
<a id="source-L112"></a>ここで、D(u)を変形速度テンソルといい、応力は変形速度テンソルからのみ引き起こされることが知られている  



<a id="source-L115"></a>

### 7.ナビエ・ストークス方程式の導出

<a id="source-L116"></a>流体はニュートン流体であると仮定すると、応力テンソルがある式で書けることが知られている  
<a id="source-L117"></a>これは、応力が体積保存の変形運動に起因する成分と体積変化に起因する等方成分の線形結合で表せることを示している  
<a id="source-L118"></a>ここで、Dは変形速度テンソルである  
<a id="source-L119"></a>これより、運動量流束テンソルを定義すると  
<a id="source-L120"></a>運動量保存則を得る  
<a id="source-L121"></a>連続を式を使って整理すると、式が得られる  



> <a id="source-L125"></a>流体力学に必要な数学  

> > <a id="source-L126"></a><https://takun-physics.net/?p=4263>  




<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

名称は非圧縮性に限らず、圧縮性の方程式にも使う。一定密度・一定粘度の非圧縮Newton流体なら、$\nabla\cdot u=0$ と $\rho(\partial_tu+(u\cdot\nabla)u)=-\nabla p+\mu\nabla^2u+\rho b$ を組にする。$\mu$ は粘度（Pa s）、$b$ は単位質量あたりの体積力（m/s²）。各項はN/m³になる。

[原文73行目](#source-L73)の $T(n)$ は応力ベクトルで、応力テンソル $\sigma$ とは $t(n)=\sigma n$ で結ぶ。[82行目](#source-L82)の運動方程式は質量保存ではなく運動量収支。[112行目](#source-L112)も圧力を含む全応力と粘性応力を区別する。確認資料：[Feynman II-31](https://www.feynmanlectures.caltech.edu/II_31.html)、[II-40](https://www.feynmanlectures.caltech.edu/II_40.html)。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [流体力学](fluid-mechanics.md)
- [生体流体工学](biofluid-mechanics.md)
- [簡易版流体力学シミュレーション](fluid-simulation.md)
- [材料力学](mechanics-of-materials.md)
- [非線形波動論](../mechanics-waves/nonlinear-waves.md)
- [振動波動論](../mechanics-waves/oscillations-and-waves.md)
- [偏微分方程式](../../math/analysis/partial-differential-equations.md)
- [常微分方程式](../../math/analysis/ordinary-differential-equations.md)
- [有限要素法](finite-element-method.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
