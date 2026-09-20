---
title: "電磁気学"
status: draft
tags: [scrapbox, electromagnetism-matter]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E9%9B%BB%E7%A3%81%E6%B0%97%E5%AD%A6"
source_created: "2023-01-18T11:03:50Z"
source_updated: "2025-07-08T07:26:04Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 電磁気学

場の法則、回路、電磁波を、基礎法則からまとめようとした記録。

原ページ作成：2023-01-18 ／ 最終更新：2025-07-08（UTC、取得時点）

[物理学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/electromagnetism.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E9%9B%BB%E7%A3%81%E6%B0%97%E5%AD%A6)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<details>
<summary>本文の見出しから探す</summary>

- [1.プロローグ](#source-L121)
- [2.静電場](#source-L124)
- [3.定常電流と磁場](#source-L127)
- [4.時間変化する電磁場](#source-L130)
- [5.マクスウェルの方程式と電磁波](#source-L133)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 電磁気学

<a id="source-L2"></a>[力学・機械力学](../mechanics-waves/classical-mechanics.md)  
<a id="source-L3"></a>[熱力学](../thermal-statistical/thermodynamics.md)  
<a id="source-L4"></a>[ベクトル解析](../../math/geometry/vector-calculus.md)  
<a id="source-L5"></a>[特殊相対性理論](../relativity-cosmology/special-relativity.md)  
<a id="source-L6"></a>[電気の理論の地図](electrical-theory-map.md)  
<a id="source-L7"></a>[電子回路](https://scrapbox.io/MistMavGamer/%E9%9B%BB%E5%AD%90%E5%9B%9E%E8%B7%AF)  
<a id="source-L8"></a>[一般相対論](../relativity-cosmology/general-relativity.md)  
<a id="source-L9"></a>[常微分方程式](../../math/analysis/ordinary-differential-equations.md)  
<a id="source-L10"></a>[偏微分方程式](../../math/analysis/partial-differential-equations.md)  
<a id="source-L11"></a>\[設計者に必要なメカトロニクスの基礎知識\]  


> <a id="source-L14"></a>高校  


<a id="source-L17"></a>電磁気学  
<a id="source-L18"></a>・電磁気学の世界  
<a id="source-L19"></a>・電場と電位  
<a id="source-L20"></a>・コンデンサー  
<a id="source-L21"></a>・電流  
<a id="source-L22"></a>・直流回路  
<a id="source-L23"></a>・荷電粒子の運動  
<a id="source-L24"></a>・電流と磁場  
<a id="source-L25"></a>・電磁誘導  
<a id="source-L26"></a>・交流回路  

<a id="source-L28"></a>電磁気学の世界  
<a id="source-L29"></a>電磁気力とは電荷が電磁場から受ける力である。電荷は粒子の基本性質で電磁場は空間の性質である。  
<a id="source-L30"></a>全ての情報は有限の時間で伝わるので、粒子の相対位置の関数とするには無理がある。そこで、空間に力を及ぼす性質があるとしたらうまく説明できる、というのが電磁気学の発想であり、その性質を電磁場という。  
<a id="source-L31"></a>その表現  F=q(E+v×B)  

<a id="source-L33"></a>・電荷の性質  
<a id="source-L34"></a>①	電気素量eが存在し、この整数倍の電荷しかない  
<a id="source-L35"></a>②	孤立系の電荷の合計は保存する  

<a id="source-L37"></a>流体の流れなどのベクトル場というものを考えると、次の２つに分類される。  
<a id="source-L38"></a>①	わき出し、吸い込みがある場  
<a id="source-L39"></a>②	渦のある場  

<a id="source-L41"></a>電磁場の法則  
<a id="source-L42"></a>①	電場は正電荷からわき出て、負電荷に吸い込まれる  
<a id="source-L43"></a>②	磁場は正磁荷からわき出て、負磁荷に吸い込まれる  
<a id="source-L44"></a>→しかし、これまで磁荷は発見されておらず、とりあえず磁場のわき出し吸い込みはないとしておく  
<a id="source-L45"></a>③	電場は磁流と磁場の時間変化の周りに渦巻く  
<a id="source-L46"></a>④	磁場は電流と電場の時間変化の周りに渦巻く  
<a id="source-L47"></a>③と④より電磁場が導かれる。振動電流の周りに振動磁場ができ、その周りに振動電流ができ、、、というように空間を振動電磁場が伝わる現象を電磁波という。  
<a id="source-L48"></a>なぜこれらのことが成り立つか、ではなくこのように考えたらつじつまが合うからこれらが基礎法則となっている。  
<a id="source-L49"></a>電磁気学は電磁気力と電磁場の法則①〜④で描ける美しい世界である。  

<a id="source-L51"></a>電磁場の法則①  
<a id="source-L52"></a>電場は正電荷から出て負電荷に吸い込まれる。  
<a id="source-L53"></a>これを静止した電荷の周りのて以上になった電場の場合について４つの例で確認しておく。  
<a id="source-L54"></a>点電荷の周り、球対称電荷分布の周り、無限に長い直線上に一様分布した電荷の周り、無限に広い平面状に一様分布した電荷の周り  

<a id="source-L56"></a>・ポテンシャルエネルギーについて  
<a id="source-L57"></a>力Fの仕事が始点、終点の位置のみで決まり、経路依存性がないとき、Fを保存力という。  
<a id="source-L58"></a>人間は保存力のする力、つまり加速度がわかっても運動を想像できないので、保存量の仕事は決定しているので、始めから、位置と速度のエネルギー情報を書いた方が現象が見やすい。保存力の重ね合わせが成り立つとき、ポテンシャルエネルギーも重ね合わせが成り立ち、ベクトルの重ね合わせよりもスカラー量の重ね合わせの方が楽である。よってポテンシャルエネルギーから逆算するのが楽である。またポテンシャルエネルギーのグラフと物体の運動は対応する。  

<a id="source-L60"></a>⑤  

<a id="source-L62"></a>電場と電位  
<a id="source-L63"></a>電位の定義は、単位電荷あたりに換算した静電気力のポテンシャルエネルギーである。  


<a id="source-L66"></a>コンデンサー  
<a id="source-L67"></a>静電エネルギーとは考えている電荷分布を電荷分布が０の状態から作るのに必要な静電気力につりあわせる外力の仕事である  

<a id="source-L69"></a>電気力線はベクトル場である電場の様子を視覚的に表すために用いられる仮想敵な線である。  

<a id="source-L71"></a>コンデンサーの基本  
<a id="source-L72"></a>導体内電場が０→導体内が等電位、電荷分布は表面  

<a id="source-L74"></a>電磁気の第一法則から導かれる導体表面の電荷綿密度と電荷の関係はすぐかけるべきである。  

<a id="source-L76"></a>導体内に電荷を移動させ、保持したとき、これらの導体はコンデンサーを形成するという。  
<a id="source-L77"></a>C は極板の形、配置及び、極板間の物体の分布とその電気的性質によって決まる。  
<a id="source-L78"></a>誘電体は表面に分極電荷±qが表れ、これのつくる電場が、真電荷±Qのつくる電場を弱める。Eを何分の１に弱めているかという値を誘電率という。  
<a id="source-L79"></a>起電力Vというのは電位差をVにキープする物体であると同時に、それをキープするために電荷を無理やり動かす仕事をする仕組みを持ったもの、ということである。  
<a id="source-L80"></a>コンデンサー回路では一般的に電荷保存と電位の関係を考えればいいが、実践的には暗算を用いて楽に計算するべき。コンデンサーは電源電圧よりも高い電圧が生める。  


<a id="source-L83"></a>電流  
<a id="source-L84"></a>電流の定義  
<a id="source-L85"></a>大きさ:単位時間あたりに断面を通過する正味の電気量  
<a id="source-L86"></a>向き:正電荷の流れの向き  

<a id="source-L88"></a>電圧降下:動線内の電場により、単位電荷がそこを通るときになされる仕事  

<a id="source-L90"></a>導線中の自由電子は、電場から加速されるが、陽イオンとの散乱で減速し、平均的にはEと逆向きに一定の移動速度で移動していると考えられる。  
<a id="source-L91"></a>このとき、この導線の抵抗をR=V/Iと定める。  


<a id="source-L94"></a>直流回路  
<a id="source-L95"></a>導線中を移動する自由電子は、単位時間あたり、電場からP=IVの仕事をされるが、これを陽イオンとの散乱で失う。よって単位時間あたりにこの散乱で失われるエネルギーは、P=IV  

<a id="source-L97"></a>電磁波が無視できる時の回路の考え方  
<a id="source-L98"></a>電流&gt;&gt;変位電流のとき、電荷、電流を仮定し、  
<a id="source-L99"></a>・孤立系の電荷保存  
<a id="source-L100"></a>・任意のループで「ループ1周の起電力＝ループ1周の電圧降下」小さなループの数だけの式があれば、全ての情報がもとまる。電荷保存を考えるより、ループ電流の重ね合わせと考える方が楽。  

<a id="source-L102"></a>特性曲線の問題は、連立方程式の解はグラフの共有点であり、IとVの関数関係が簡単な時には、連立方程式を解けば早いが、関数関係が難しくなるとIとVのグラフと特性曲線の共有点を求めることになる。  

<a id="source-L104"></a>ホイートストーンブリッジ回路:抵抗測定器に用いられる。公式など知らなくても、そもそも３つのループ電流をおけば全て求まると一般的に考えるべきである。  


<a id="source-L107"></a>荷電粒子の運動  
<a id="source-L108"></a>荷電粒子の電磁場中での運動  
<a id="source-L109"></a>ma=q(E+v×B)の表記より、  


<a id="source-L112"></a>電流と磁場  
<a id="source-L113"></a>電磁誘導  
<a id="source-L114"></a>交流回路  




> <a id="source-L119"></a>学部のときの授業  


<a id="source-L121"></a>

### 1.プロローグ

<a id="source-L122"></a>静電場のクーロンの法則、ベクトル三重積、勾配ベクトル、div、rot 、ポアソンの方程式、grad,div,rotの応用公式、ガウスの発散定理、ストークスの定理  


<a id="source-L124"></a>

### 2.静電場

<a id="source-L125"></a>点電荷がrだけ離れた点電荷qに及ぼすクーロン力、ガウスの法則、静電場と電位の関係、電位の重ね合わせの原理、導体平板と鏡像方、導体球面の鏡像法、平行平板コンデンサーの４つの公式、静電場のエネルギー密度、真空と誘電体の系での電束密度とマクスウェル方程式、電場と電束密度の屈折の法則  


<a id="source-L127"></a>

### 3.定常電流と磁場

<a id="source-L128"></a>電流の3つの表現、電荷の保存則、マクスウェルの方程式、一般化されたアンペールの法則、定常電流による磁場に関するマクスウェルの方程式、静磁場のクーロンの法則、ビオ・サバールの法則、積分形によるビオ・サバールの法則、磁場のベクトルポテンシャル、アンペールの力、ローレンツ力  


<a id="source-L130"></a>

### 4.時間変化する電磁場

<a id="source-L131"></a>マクスウェルの方程式、ファラデーの電磁誘導の法則、レンツの法則、磁束と磁束密度、マクスウェルの方程式、ソレノイドコイルの自己誘導による逆起電力、相互誘導、相互インダクタンスの相反定理、コイルに蓄えられている磁場のエネルギー、磁場のエネルギー密度、LC回路におけるエネルギー保存則と平均消費電力  


<a id="source-L133"></a>

### 5.マクスウェルの方程式と電磁波

<a id="source-L134"></a>真空中を伝播する電場と磁場のマクスウェル方程式、真空中を伝播する電場と磁場の波動方程式、ダランベールの解、電場と磁場の１次元波動方程式、電場と磁場の一次元波動方程式の解、ポインティングベクトル  


<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

[原文43行目](#source-L43)付近は、磁荷を導入しない通常のMaxwell方程式として整理する。真空中では $\nabla\cdot E=\rho/\varepsilon_0$、$\nabla\cdot B=0$、$\nabla\times E=-\partial_tB$、$\nabla\times B=\mu_0J+\mu_0\varepsilon_0\partial_tE$。電磁波の伝播に伝導電流が空間全体で流れる必要はない。

「導体内の電場0」は静電平衡の条件。誘電率 $\varepsilon$ と無次元の比誘電率 $\varepsilon_r=\varepsilon/\varepsilon_0$ も区別する。[ベクトル解析](../../math/geometry/vector-calculus.md)へ戻って、場の時間変化と電荷保存の関係を追える。確認資料：[Feynman II-18](https://www.feynmanlectures.caltech.edu/II_18.html)。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [力学・機械力学](../mechanics-waves/classical-mechanics.md)
- [熱力学](../thermal-statistical/thermodynamics.md)
- [ベクトル解析](../../math/geometry/vector-calculus.md)
- [特殊相対性理論](../relativity-cosmology/special-relativity.md)
- [電気の理論の地図](electrical-theory-map.md)
- [一般相対論](../relativity-cosmology/general-relativity.md)
- [常微分方程式](../../math/analysis/ordinary-differential-equations.md)
- [偏微分方程式](../../math/analysis/partial-differential-equations.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
