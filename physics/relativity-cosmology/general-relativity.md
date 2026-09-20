---
title: "一般相対論"
status: draft
tags: [scrapbox, relativity-cosmology]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E4%B8%80%E8%88%AC%E7%9B%B8%E5%AF%BE%E8%AB%96"
source_created: "2023-01-18T10:51:26Z"
source_updated: "2024-12-01T13:59:14Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 一般相対論

線素の直感から多様体・曲率・重力場の方程式へ進むメモ。

原ページ作成：2023-01-18 ／ 最終更新：2024-12-01（UTC、取得時点）

[物理学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/general-relativity.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E4%B8%80%E8%88%AC%E7%9B%B8%E5%AF%BE%E8%AB%96)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 一般相対論

<a id="source-L2"></a>[scrapboxまとめ(物理)](../learning-paths/original-physics-index.md)  
<a id="source-L3"></a>[特殊相対性理論](special-relativity.md)  
<a id="source-L4"></a>[現代物理学入門](../learning-paths/modern-physics.md)  
<a id="source-L5"></a>[解析力学](../mechanics-waves/analytical-mechanics.md)  
<a id="source-L6"></a>[多様体・微分幾何・情報幾何](../../math/geometry/information-geometry.md)  
<a id="source-L7"></a>[電磁気学](../electromagnetism-matter/electromagnetism.md)  




> <a id="source-L12"></a>Einsteins's Field Equations of General Relativity Explained  

<a id="source-L13"></a>[https://www.youtube.com/watch?v=UfThVvBWZxM](<https://www.youtube.com/watch?v=UfThVvBWZxM>)  


> <a id="source-L16"></a>一般相対論の授業リンク    <http://www.resceu.s.u-tokyo.ac.jp/~yokoyama/gg2019.html>  


> <a id="source-L19"></a>Einsteins Field Equations     [https://www.youtube.com/watch?v=foRPKAKZWx8](<https://www.youtube.com/watch?v=foRPKAKZWx8>)  



> <a id="source-L23"></a>一般相対論入門     <https://www.youtube.com/watch?v=CJafAIIG26s&list=PLe-uzN5oHeCCrF15alQZFmJ7xgNAU1Pwq>  

<a id="source-L25"></a>その1  
<a id="source-L26"></a>三平方の定理からブラックホールの数式を考察する  
<a id="source-L27"></a>三平方に、  
<a id="source-L28"></a>無限小→極座標→3次元→曲がった空間の効果→時間の項と付け加えてブラックホールの式  

<a id="source-L30"></a>その2  
<a id="source-L31"></a>無限小にする  
<a id="source-L32"></a>要するに局所化する  
<a id="source-L33"></a>なぜなら、空間の歪み具合は場所によって異なるので  

<a id="source-L35"></a>その3  

> <a id="source-L36"></a>ブラックホールは丸いので、極座標にしたい  

<a id="source-L38"></a>その4  
<a id="source-L39"></a>歪んだ空間になると線素を表す数式が複雑になる  
<a id="source-L40"></a>線素の一般形を考える  

<a id="source-L42"></a>相対性理論では時間を0番目にもっていく(ct)  

<a id="source-L44"></a>一般化することで線素をかっこよくかけた  

<a id="source-L46"></a>その5  
<a id="source-L47"></a>極座標変換についての補足  

<a id="source-L49"></a>その6  
<a id="source-L50"></a>3次元極座標  

<a id="source-L52"></a>その7  
<a id="source-L53"></a>三角比、三角関数  

<a id="source-L55"></a>その8  
<a id="source-L56"></a>微分について  

<a id="source-L58"></a>曲線は直線の集合  

<a id="source-L60"></a>二次元球面に接するのは面  
<a id="source-L61"></a>これを三次元で考えると、接空間となる（自由度は3つ）  

<a id="source-L63"></a>三次元空間を、三次元ユークリッド空間で近似的に捉える  
<a id="source-L64"></a>そう捉えられると、特殊相対性理論などが適用できる  

<a id="source-L66"></a>その9  
<a id="source-L67"></a>偏微分  

<a id="source-L69"></a>その10  
<a id="source-L70"></a>全微分  



> <a id="source-L74"></a>「特殊および一般相対性理論」 どっかのPDF  



> <a id="source-L78"></a>「一般相対性理論」 どっかのPDF  

<a id="source-L80"></a>1章 概観  
<a id="source-L81"></a>ガリレイ変換  
<a id="source-L82"></a>ガリレイの相対性原理  

<a id="source-L84"></a>特殊相対論  
<a id="source-L85"></a>相対性原理と光速度不変の原理から２つの慣性系を結ぶ関係式を求める  

<a id="source-L87"></a>一般相対論  
<a id="source-L88"></a>加速度系まで含めた一般の座標変換を扱うにはさらなる拡張が必要  
<a id="source-L89"></a>また重力は他の力とは異なる  
<a id="source-L90"></a>空間の各点で局所慣性系をとり、それらを貼り合わせた結果、曲がった空間となる  

<a id="source-L92"></a>一般相対論  
<a id="source-L93"></a>ブラックホール  
<a id="source-L94"></a>宇宙論  
<a id="source-L95"></a>重力波  
<a id="source-L96"></a>超弦理論  
<a id="source-L97"></a>GNSS  


<a id="source-L100"></a>2章 多様体とテンソル場  
<a id="source-L101"></a>多様体  
<a id="source-L102"></a>多様体は局所的にユークリッド空間とみなせるような図形のこと  

<a id="source-L104"></a>多様体上のベクトル  
<a id="source-L105"></a>多様体上では空間の変位としてベクトルを定義することができない  
<a id="source-L106"></a>したがって、多様体上のある点近傍で、無限小変位として接ベクトルを定義し、その接ベクトルのなす接ベクトル空間の性質について学ぶ  

<a id="source-L108"></a>テンソルと計量テンソル  
<a id="source-L109"></a>変位ベクトルの概念からテンソルの概念を導くことができる  
<a id="source-L110"></a>多くの物理量は変位に線型に依存する  
<a id="source-L111"></a>磁場はベクトル、もっと正確に言えば双対ベクトルと考えることができる  
<a id="source-L112"></a>双対ベクトルは、空間の変位のベクトルの基底に伴う３つの量の集合と定義できる  
<a id="source-L113"></a>空間変位ベクトルに線型に依存するが、１つ以上のベクトルに依存するものとして応力テンソルなどがある  
<a id="source-L114"></a>有限次元ベクトル空間に対して双対空間を定義して、それを利用して多重線型写像としてテンソルを定義する  

<a id="source-L116"></a>計量の概念は直感的には無限小変位と関係する無限小2乗距離のようなもの  

<a id="source-L118"></a>抽象添字記法  
<a id="source-L119"></a>高階のテンソルは多くのベクトルと双対ベクトルの関数  


<a id="source-L122"></a>3章 曲率  
<a id="source-L123"></a>曲率の直観的な概念は3次元ユークリッド空間に埋め込まれた2次元曲面からきているが計量gabを持つ時空間の多様体Mは高次元多様体に自然には埋め込まれていない  
<a id="source-L124"></a>よって高次元空間への埋め込みなしに任意の多様体に当てはまる曲率の内在的な概念を定義したい  
<a id="source-L125"></a>そのような曲率の概念は平行移動で定義できる  
<a id="source-L126"></a>曲線に沿ってベクトルがどのように平行移動するか調べれば良い  
<a id="source-L127"></a>多様体として構造を与えただけでは平行移動を自然に定義できないので平行移動の定義には多様体の構造以上のものが要求される  

<a id="source-L129"></a>微分演算子と平行移動  
<a id="source-L130"></a>多様体M上の微分演算子(共変微分)は滑らかなテンソル場を別のタイプのテンソル 場に移す写像である  

<a id="source-L132"></a>曲率  
<a id="source-L133"></a>平行移動の経路の依存性を曲率の概念を定義するのに用いることができる  
<a id="source-L134"></a>双対ベクトル場に複数の微分操作を続けて施した時に交換しないことからRiemann曲率テンソルを定義することで始める  

<a id="source-L136"></a>測地線  
<a id="source-L137"></a>直観的には測地線は最も短い曲線である  

<a id="source-L139"></a>曲率の計算方法  
<a id="source-L140"></a>座標成分法  
<a id="source-L141"></a>正規直交基底法  


<a id="source-L144"></a>4章 アインシュタイン方程式  
<a id="source-L145"></a>相対論以前の空間の幾何学  
<a id="source-L146"></a>デカルト座標  
<a id="source-L147"></a>空間は平坦なRiemann計量が定義されている多様体R3である  

<a id="source-L149"></a>特殊相対論  
<a id="source-L150"></a>時間が座標に入った  
<a id="source-L151"></a>時空間の計量が定義される  
<a id="source-L152"></a>Lorentz符号数の平坦な計量のR4多様体  
<a id="source-L153"></a>特殊相対論では連続的な物質分布はストレスエネルギー運動量テンソルと呼ばれる対称テンソルで記述される  

<a id="source-L155"></a>一般相対論  
<a id="source-L156"></a>特殊相対論で前提にされていたのとは異なり、時空間計量は平坦ではなく、重力場で自由落下する物体の世界線は単に曲がった時空間計量の測地線にすぎない  
<a id="source-L157"></a>重力を力の場として記述する意味のある方法を我々は何も持たない  
<a id="source-L158"></a>一般相対論では時空間はローレンツ計量が定義されている多様体Mである  
<a id="source-L159"></a>一般共変性原理が基本  
<a id="source-L160"></a>時空間はその上にローレンツ計量が定義された多様体M  
<a id="source-L161"></a>gabの曲率は空間の物質分布とEinstein方程式で関係づけられる  

<a id="source-L163"></a>重力の線形化  
<a id="source-L164"></a>重力の弱い近似を扱う  
<a id="source-L165"></a>線形近似では一般相対論は質量のないスピン2の場の理論の帰着する  

<a id="source-L167"></a>重力が弱い時はNewton重力の基礎方程式に一致する  



<a id="source-L171"></a>5章 一様等方宇宙  
<a id="source-L172"></a>一様性と等方性  
<a id="source-L173"></a>宇宙論の観点からは過去の光円錐の一部の情報をもたらしているだけ  

<a id="source-L175"></a>一様で等方な宇宙の動力学  
<a id="source-L176"></a>時空間の計量をEinstein方程式に代入して宇宙の動力学的発展についての予言を求めることが目標  
<a id="source-L177"></a>一般相対論は宇宙はビッグバンではじまったという観点に行きつく  

<a id="source-L179"></a>宇宙の赤方偏移；地平線  
<a id="source-L180"></a>宇宙膨張の最も直接的な観測的証拠は離れた銀河のスペクトル線の赤方偏移に由来している  

<a id="source-L182"></a>我々の宇宙の進化  
<a id="source-L183"></a>宇宙はその歴史を通して、Robertson-Walker解でよく記述される  


<a id="source-L186"></a>6章 シュワルツシルト解  
<a id="source-L187"></a>シュワルツシルト解の導出  
<a id="source-L188"></a>静的で級対称な物体外部の重力場を記述するEinstein方程式の全ての解を探す  




<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

原文の「局所化して線素を考える」流れを残す。局所座標が $\mathbb R^4$ に見えることと、計量がEuclid計量であることは別。相対論の時空はLorentz符号の計量を持つ。一点で接続係数を消せても、曲率や潮汐効果を一般に消せるわけではない。

[原文137行目](#source-L137)の測地線も一律に最短経路ではない。Lorentz時空の時間的測地線は固有時の停留条件を持ち、適切な局所条件では最大になる。計量や曲率の符号規約を宣言してから式を読む。確認資料：[Einstein Onlineの等価原理](https://www.einstein-online.info/en/spotlight/equivalence_principle/)。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [scrapboxまとめ(物理)](../learning-paths/original-physics-index.md)
- [特殊相対性理論](special-relativity.md)
- [現代物理学入門](../learning-paths/modern-physics.md)
- [解析力学](../mechanics-waves/analytical-mechanics.md)
- [多様体・微分幾何・情報幾何](../../math/geometry/information-geometry.md)
- [電磁気学](../electromagnetism-matter/electromagnetism.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
