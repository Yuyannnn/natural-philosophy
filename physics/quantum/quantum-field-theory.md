---
title: "場の量子論"
status: draft
tags: [scrapbox, quantum]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E5%A0%B4%E3%81%AE%E9%87%8F%E5%AD%90%E8%AB%96"
source_created: "2023-01-18T10:58:31Z"
source_updated: "2025-09-04T03:35:25Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 場の量子論

経路積分、場の量子化、相互作用、くりこみをたどる読書・講義メモ。

原ページ作成：2023-01-18 ／ 最終更新：2025-09-04（UTC、取得時点）

[物理学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/quantum-field-theory.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E5%A0%B4%E3%81%AE%E9%87%8F%E5%AD%90%E8%AB%96)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<details>
<summary>本文の見出しから探す</summary>

- [第1章 量子力学の復習と経路積分](#source-L14)
- [第2章 相対論的な波動方程式からその理論へ](#source-L61)
- [第3章 第2量子化](#source-L90)
- [第4章 場の相互作用](#source-L137)
- [第5章 電磁場と物質場の相互作用](#source-L156)
- [第6章 くりこみ](#source-L171)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 場の量子論

<a id="source-L2"></a>[量子論](quantum-theory.md)  
<a id="source-L3"></a>[量子情報](quantum-information.md)  
<a id="source-L4"></a>[量子統計力学](../thermal-statistical/quantum-statistical-mechanics.md)  
<a id="source-L5"></a>[量子力学](quantum-mechanics.md)  
<a id="source-L6"></a>[量子アニーリング](quantum-annealing.md)  
<a id="source-L7"></a>[一般相対論](../relativity-cosmology/general-relativity.md)  



> <a id="source-L11"></a>「量子場の理論入門」   
> <a id="source-L12"></a>どっかのPDFだった気がします  


<a id="source-L14"></a>

### 第1章 量子力学の復習と経路積分


<a id="source-L16"></a>シュレディンガー方程式の復習  
<a id="source-L17"></a>粒子的描像と波動的描像をつなげる式  
<a id="source-L18"></a>ハミルトニアンのエルミート性とシュレディンガー方程式が時間に関して一階の方程式であることが重要  

<a id="source-L20"></a>解析力学では作用が停留値をとる軌道が実現される  
<a id="source-L21"></a>古典力学ではそれが解である  
<a id="source-L22"></a>量子力学では運動方程式の解であるような経路以外も意味をもってくる  
<a id="source-L23"></a>どんな経路も同等になるが、停留値をとるような経路が特別なものになる仕掛けがある  

<a id="source-L25"></a>シュレディンガー方程式と古典的解析力学は関係がある  
<a id="source-L26"></a>波の位相が極値をとるべし！  
<a id="source-L27"></a>変化が小さいところの足算は位相が消し合うことなく残る  

<a id="source-L29"></a>量子力学的状態の表し方  
<a id="source-L30"></a>状態 = ベクトル空間  
<a id="source-L31"></a>波動関数はベクトルとして考えられる  
<a id="source-L32"></a>この世界は無限次元のベクトルで表現されている  
<a id="source-L33"></a>量子力学で観測結果と比べられるものは波動関数ではなく、物理量を表す演算子の固有値や期待値  
<a id="source-L34"></a>演算子の固有値や期待値を求める計算は量子力学的状態から物理量に対応する数を取り出す操作  

<a id="source-L36"></a>無限次元のベクトルをブラケットベクトルとして象徴的に表す  
<a id="source-L37"></a>ブラケットベクトルを用いると基底ベクトルの変換がわかりやすくなる  

<a id="source-L39"></a>物理量を演算子で考えることを量子化という  

<a id="source-L41"></a>量子力学の演算子解法  
<a id="source-L42"></a>1次元の調和振動子を演算子的手法を使って解くことを考える  
<a id="source-L43"></a>いろいろな演算子の固有状態を使って状態を表せるので、演算子の固有状態を求めていく応報を考える  
<a id="source-L44"></a>固有値を変える演算子は何か？を考える  

<a id="source-L46"></a>シュレディンガー表示とハイゼンベルグ表示  
<a id="source-L47"></a>シュレディンガー表示  
<a id="source-L48"></a>ハイゼンベルグ表示  
<a id="source-L49"></a>ハイゼンベルグ表示とシュレディンガー表示の中間にあたる相互作用表示というものもある  

<a id="source-L51"></a>Green関数：ある微分演算子があって、その微分演算子をかけると答えがδ関数となるものを演算子に対するGreen関数という  

<a id="source-L53"></a>経路積分による量子力学  
<a id="source-L54"></a>Green関数を求めることで量子力学的状態を系統的に求めていくことができる  
<a id="source-L55"></a>ここではGreen関数を求めるもう１つの方法を説明する  

<a id="source-L57"></a>関数の計算が複雑な理論では面倒になるので、経路積分を利用してうまく計算できる  
<a id="source-L58"></a>量子力学の特徴として、２つの古典的経路がありえるとき、あたかもその両方の経路をとおてきた波が干渉するかのごとき現象が起こったが、それは経路積分の立場では両方の経路を対等に積分する必要があるということから理解できる  



<a id="source-L61"></a>

### 第2章 相対論的な波動方程式からその理論へ


<a id="source-L63"></a>Klein-Gordon方程式  
<a id="source-L64"></a>古典的なエネルギー・運動量の関係を翻訳したものがシュレディンガ方程式  
<a id="source-L65"></a>同様に相対論的な方程式を作ることを考える  
<a id="source-L66"></a>相対論ではアインシュタインのエネルギーの関係式が成り立つ  
<a id="source-L67"></a>Klein-Gordon方程式は時間に関して2階の微分を含んでいるのでシュレディンガー方程式と大きく性質が違う  

<a id="source-L69"></a>Dirac方程式とその解  
<a id="source-L70"></a>一階の微分方程式であらわせて規格化されたものが保存料になるような相対論的な方程式を作ることは難しい  
<a id="source-L71"></a>Diracは変数を列ベクトルにすることでこれを成功させた  
<a id="source-L72"></a>DiracはKein-Gordon方程式から出発し、一階の方程式が作れないかという議論からDirac方程式を作った  
<a id="source-L73"></a>Dirac方程式でも負エネルギーの問題が出てくる  

<a id="source-L75"></a>負エネルギーの状態にはすでに粒子が入っていて、これ以上入ることはできないと考えれば観測される粒子が負エネルギーに落ち込まないことの説明がつく  
<a id="source-L76"></a>Dirac方程式およびこの方程式のψに対する解釈として電子の集団として記述することを考えた  
<a id="source-L77"></a>これが場の理論である  

<a id="source-L79"></a>Klein-Gordon方程式の解  
<a id="source-L80"></a>フーリエ変換して求める  
<a id="source-L81"></a>負エネルギー解を許さないと相対論的因果律を満たすような形で解を作ることはできない  

<a id="source-L83"></a>Green関数  
<a id="source-L84"></a>Green関数を求めておくと後の計算で便利  
<a id="source-L85"></a>実際の計算には注意が必要となる  





<a id="source-L90"></a>

### 第3章 第2量子化

<a id="source-L91"></a>場とは？  
<a id="source-L92"></a>場の概念が物理にはよく現れる  
<a id="source-L93"></a>単純には、空間の各点各点に定義された力学変数の集まりである  
<a id="source-L94"></a>場の理論とは空間の各点各点にあり互いに関係しあっている無限個の力学的自由度について考える理論  
<a id="source-L95"></a>これを量子力学的に考えるものを量子場の理論という  

<a id="source-L97"></a>光に限らず、空間に分布した物質場を調和振動子の集まりとして考えて量子化することができる  
<a id="source-L98"></a>これを量子場の理論といい、現代の素粒子論、物性理論の基礎となる  

<a id="source-L100"></a>第1量子化から第2量子化へ  
<a id="source-L101"></a>場の量子化を第2量子化と呼ぶことがある  
<a id="source-L102"></a>量子力学ではハミルトニアンを作るまでが同じで、その続きは正準交換関係を仮定する  
<a id="source-L103"></a>シュレディンガー方程式を立てるというところが違う  
<a id="source-L104"></a>場の理論では空間の各点に場という力学変数を考えるので自由度が無限大となる  
<a id="source-L105"></a>そのような各点各点の力学変数を量子化するのが場の量子化である  

<a id="source-L107"></a>量子力学は1体問題  
<a id="source-L108"></a>場の量子論は多体問題という捉え方もできる  
<a id="source-L109"></a>具体的にはシュレディンガー方程式を満たす粒子の多体問題を考えて、それを場の理論の形で定式化できることを示す  
<a id="source-L110"></a>第1量子化の波動関数の各成分を弟2量子化の生成・消滅演算子を置き換えるという方法で第1量子化→第2量子化と進める  

<a id="source-L112"></a>シュレディンガー場とKlein-Gordon場の正準量子化  
<a id="source-L113"></a>場の作用から出発する  
<a id="source-L114"></a>作用からハミルトニアンを経由して、Poisson括弧から交換関係への置き換えを使って量子化を行うことを正準量子化という  

<a id="source-L116"></a>第1量子化では波動関数だったが、ここでは演算子として扱われている  
<a id="source-L117"></a>量子化は力学変数を演算子で置き換えること、場の１つ１つの成分は力学変数だから場の量子化でψが演算子となるのは当然  

<a id="source-L119"></a>シュレディンガー方程式は非相対論的な方程式なので、シュレディンガー場は非相対論的な場である  
<a id="source-L120"></a>そこで相対論的な方程式であるKlein-Gordon方程式に対応するKlein-Gordon場の場合を考える  

<a id="source-L122"></a>Bose統計、Fermi統計について  

<a id="source-L124"></a>場の理論の経路積分  
<a id="source-L125"></a>シュレディンガー場やKlein-Gordon場の量子化を、経路積分を使って実行することができる  
<a id="source-L126"></a>というのも、場の理論は量子力学を無限自由度にしたものであるから  

<a id="source-L128"></a>経路積分の中に場の量を挟んで積分することで粒子の伝播が計算できるのはなぜかという問題を、今考えた経路積分がどのような積分になっているかを考えることで示す  

<a id="source-L130"></a>何度も計算を繰り返すのを避けるために母関数という考え方がある  

<a id="source-L132"></a>Dirac場の正準量子化  
<a id="source-L133"></a>フェルミオンの正準量子化ではいくつかの問題が出る場合がある  
<a id="source-L134"></a>ここでは単純な複素Dirac場の場合でそれを示す  



<a id="source-L137"></a>

### 第4章 場の相互作用

<a id="source-L138"></a>相互作用する場のとりあつかい  
<a id="source-L139"></a>場の理論のハゼンベルグ表示、シュレディンガー表示、相互作用表示  
<a id="source-L140"></a>前章では場の理論をハイゼンベルグ表示で扱ったが量子力学同様、これをシュレディンガ表示で扱うこともできる  

<a id="source-L142"></a>演算子形式での計算  
<a id="source-L143"></a>生成演算子と消滅演算子があるとき必ず生成演算子の方が左側にあるようにする並べ方を正規積という  

<a id="source-L145"></a>Feynman Rule  
<a id="source-L146"></a>以上のように、演算子が２つあればそれをプロパゲーターに置き換えていくという方法でどんなオーダーであっても計算できる  

<a id="source-L148"></a>経路積分による計算  
<a id="source-L149"></a>経路積分について  

<a id="source-L151"></a>相互作用が力を伝えることの模型  
<a id="source-L152"></a>ここまでは1種類の粒子だけを考えて自己相互作用を考えたが、現実の宇宙では荷電粒子と光子の相互作用によって核力が生じたりする  
<a id="source-L153"></a>静的な力は仮想的な粒子によって伝播される  



<a id="source-L156"></a>

### 第5章 電磁場と物質場の相互作用

<a id="source-L157"></a>ゲージ原理  
<a id="source-L158"></a>電場と磁場は結びついているので4元ベクトルで表せる  
<a id="source-L159"></a>物理的内容を不変に保つ変換をゲージ変換という  

<a id="source-L161"></a>非相対論的な場と電磁場の相互作用  
<a id="source-L162"></a>電荷qを持ったFermi粒子の場の理論を非相対論的に考えていく  

<a id="source-L164"></a>相対論的な場と電磁場の相互作用  
<a id="source-L165"></a>Dirac粒子の作用を共変微分に置き換える  

<a id="source-L167"></a>電磁場のローレンツ共変な量子化  
<a id="source-L168"></a>先の節ではCoulombゲージをとった場合について考えたが、以下ではローレンツ共変な電磁場の量子化を考える  



<a id="source-L171"></a>

### 第6章 くりこみ

<a id="source-L172"></a>Feynman図の発散  
<a id="source-L173"></a>計算のテクニックとして次元法がある  

<a id="source-L175"></a>具体例：φ^4理論  
<a id="source-L176"></a>4次元のφ^4相互作用の理論のくりこみを考える  
<a id="source-L177"></a>相互作用の影響により、理論に含まれる定数の値がずれるというのがくりこみの考え方である  

<a id="source-L179"></a>くりこみは計算のテクニックとみられがちだが、くりこみ群などの方法を使うと、物理的な相互作用への影響として考えることができ、単なる計算のテクニック以上のものを持っているという考え方もある  

<a id="source-L181"></a>具体例2：Schwinger Model  
<a id="source-L182"></a>くりこみ、すなわち量子効果が非常に重要となる例としてSchwinger Modelと呼ばれる模型がある  
<a id="source-L183"></a>このモデルは2次元の粒子電磁力学で質量0のフェルミオンが電荷eを持っているようなモデルである  

<a id="source-L185"></a>アノマリーが現れる理由は量子化の手続きの途中で常に対称性を尊重した計算が実行することができないからである  

<a id="source-L187"></a>経路積分によるアノマリーの計算  
<a id="source-L188"></a>古典的対称性が量子論で破れる現象がアノマリーである  
<a id="source-L189"></a>これは経路積分ではどのように表されるのかを考える  





> <a id="source-L195"></a>授業のHP  

<a id="source-L196"></a>場の量子論  
<a id="source-L197"></a><http://www-hep.phys.s.u-tokyo.ac.jp/~hama/lectures/2019_QFT.html>  



> <a id="source-L201"></a>別の授業  

<a id="source-L203"></a>場の量子論  

<a id="source-L205"></a>相対論的場の量子論を中心に場の量子論の基礎を扱う。第２量子化、相対論的量子力学、場の正準量子化、経路積分、ファインマン則、摂動論、繰り込みなどの基本的事項の理解を目指す。  

<a id="source-L207"></a>１．Schrodinger場と第２量子化  

> <a id="source-L208"></a>１−１Bose粒子系  
> <a id="source-L209"></a>１−２Fermi粒子系  

<a id="source-L210"></a>２．拘束系の量子化  

> <a id="source-L211"></a>２−１正準形式  
> <a id="source-L212"></a>２−２Constraint  
> <a id="source-L213"></a>２−３量子化  

<a id="source-L214"></a>３．相対論的粒子  

> <a id="source-L215"></a>３−１Lagrangian  
> <a id="source-L216"></a>３−２Proper time quantization  
> <a id="source-L217"></a>３−３摂動論  

<a id="source-L218"></a>４．Klein-Gordon場  

> <a id="source-L219"></a>４−１自由場の量子化  
> <a id="source-L220"></a>４−２Noether's theorem  

<a id="source-L221"></a>５．Dirac場  

> <a id="source-L222"></a>５−１Dirac方程式  
> <a id="source-L223"></a>５−２自由Dirac場の量子化  
> <a id="source-L224"></a>５−３CPT  

<a id="source-L225"></a>６．Maxwell場  

> <a id="source-L226"></a>６−１Gupta-Bleuler形式  
> <a id="source-L227"></a>６−２他の共変形式  

<a id="source-L228"></a>７．相互作用  

> <a id="source-L229"></a>７−１漸近場  
> <a id="source-L230"></a>７−２LSZ reduction formula  
> <a id="source-L231"></a>７−３摂動論（Feynman-Dyson）  

<a id="source-L232"></a>８．経路積分  

> <a id="source-L233"></a>８−１量子力学  
> <a id="source-L234"></a>８−２場の経路積分  
> <a id="source-L235"></a>８−３Green関数の生成汎関数  

<a id="source-L236"></a>９．繰り込み  
<a id="source-L237"></a>１０．繰り込み群  




<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

[原文107行目](#source-L107)の「量子力学は1体問題」は限定しすぎで、固定粒子数の多体系も扱える。[152行目](#source-L152)の荷電粒子と光子による相互作用は、通常ここでは核力ではなく電磁相互作用。[158行目](#source-L158)では、電磁場の反対称テンソル $F_{\mu\nu}$ と、スカラー・ベクトルポテンシャルをまとめた四元ポテンシャルを区別する。

「状態＝ベクトル空間」ではなく、純粋状態はHilbert空間のベクトルの位相・規格化の同値類として表す。「どっかのPDF」は未同定のまま残し、今回の出典と混同しない。確認資料：[Feynman II-25](https://www.feynmanlectures.caltech.edu/II_25.html)。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [量子論](quantum-theory.md)
- [量子情報](quantum-information.md)
- [量子統計力学](../thermal-statistical/quantum-statistical-mechanics.md)
- [量子力学](quantum-mechanics.md)
- [量子アニーリング](quantum-annealing.md)
- [一般相対論](../relativity-cosmology/general-relativity.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
