---
title: "群論"
status: draft
tags: [scrapbox, algebra]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E7%BE%A4%E8%AB%96"
source_created: "2023-02-01T04:26:44Z"
source_updated: "2024-12-07T07:59:04Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 群論

演算の構造を調べ、群同士の関係へ進む記録。

原ページ作成：2023-02-01 ／ 最終更新：2024-12-07（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/group-theory.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E7%BE%A4%E8%AB%96)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

**原文に埋め込み欠落記号が14か所あります。** 取得時点で内容を特定できないため、本文中で位置を示しています。推測した図や式に置き換えていません。

<details>
<summary>本文の見出しから探す</summary>

- [「Collatz(Group theory)」](#source-L8)
- [1 とある演算で閉じている](#source-L20)
- [2 操作の順序を入れ替えられる](#source-L21)
- [3 単位元が存在する](#source-L22)
- [4 逆元が存在する](#source-L23)
- [1 群論の基礎](#source-L27)
- [1.1 群の定義](#source-L28)
- [1.2 部分群](#source-L68)
- [1.3 剰余類](#source-L104)
- [1.4 正規部分群](#source-L142)
- [2 準同型写像](#source-L151)
- [2.1 準同型写像の定義](#source-L159)
- [2.2 準同型定理](#source-L200)
- [2.3 第二同型定理](#source-L212)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 群論

<a id="source-L2"></a>[線形代数](../linear-algebra/linear-algebra.md)  
<a id="source-L3"></a>[Lie代数](lie-algebras.md)  
<a id="source-L4"></a>[代数の基礎](algebra-foundations.md)  
<a id="source-L5"></a>[圏論](category-theory.md)  



<a id="source-L8"></a>

### 「Collatz(Group theory)」


<a id="source-L10"></a>ブルバギは数学的考察を向ける対象に備わるべき構造として、３種類の構造に注目した  
<a id="source-L11"></a>・位相構造  
<a id="source-L12"></a>・線型構造  
<a id="source-L13"></a>・代数構造  
<a id="source-L14"></a>代数構造で学ぶのが、群論である  
<a id="source-L15"></a>群論では演算について学ぶ  
<a id="source-L16"></a>結局は集合にある構造が備わって群と読んでいるのであるが、その構造が今回は演算によって定まっている  
<a id="source-L17"></a>数学の世界では数多くの操作が用いられるが、群論はそのような操作をわかりやすく分解する技を与えてくれる  

<a id="source-L19"></a>定義（群の公理）  

<a id="source-L20"></a>

### 1 とある演算で閉じている


<a id="source-L21"></a>

### 2 操作の順序を入れ替えられる


<a id="source-L22"></a>

### 3 単位元が存在する


<a id="source-L23"></a>

### 4 逆元が存在する


<a id="source-L25"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  


<a id="source-L27"></a>

### 1 群論の基礎


<a id="source-L28"></a>

### 1.1 群の定義


<a id="source-L30"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L32"></a>演算をどのように捉えるかというのはかなり基本的な問題であり、これからの議論にも大きく響く  
<a id="source-L33"></a>演算を規則ではなく写像として考える  

<a id="source-L35"></a>a:告白する  
<a id="source-L36"></a>b:キスする  
<a id="source-L37"></a>c:ハグする  
<a id="source-L38"></a>というように考えてみると、物事の順序はとても重要であることがわかる  
<a id="source-L39"></a>数学の世界では何か特徴的なもの（最大値、上限、導関数）を定義すると、それは一意かどうかを非常に気にする  
<a id="source-L40"></a>一意性を示すときは、a,bを仮定して定義を用いて同じことを示すのが良さそう　　  

<a id="source-L42"></a>補題1.1.1  
<a id="source-L43"></a>単位元は一意に定まる  
<a id="source-L44"></a>また逆元も一意に定まる  

<a id="source-L46"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L48"></a>補題1.1.2  
<a id="source-L49"></a>aが群に含まれるとすると、(a^-1)-1 = aである  

<a id="source-L51"></a>交換法則を一般の群の定義に組み込まないのは、この性質を満たす演算は数学において特殊だからである  
<a id="source-L52"></a>引き算や割り算、行列の積は交換法則を満たさない  
<a id="source-L53"></a>つまり交換法則が成り立つような演算はある意味特殊な条件を満たしているような群である  
<a id="source-L54"></a>そのような群をAbel群という  

<a id="source-L56"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L57"></a>先の話になるが、Abel群には普通の群には見出せない面白い性質がある  

<a id="source-L59"></a>定義1.4 部分集合に関する演算  

<a id="source-L61"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L63"></a>今までは濃度という言葉を用いてきたが、代数学では群の位数という  





<a id="source-L68"></a>

### 1.2 部分群

<a id="source-L69"></a>集合にとある構造がもたらされた時、その部分集合で構造が引き継がれるようなものは何か、ということは数学における自然なストーリーの流れである  
<a id="source-L70"></a>ここで、群のどのような部分集合が群の構造をうまく引き継いでいるのだろうかと考えてみると、結合法則が成り立つのは群の部分集合として自明なので、組み込まない  
<a id="source-L71"></a>よって残りの3つの公理を満たすものを部分群という  

<a id="source-L73"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L75"></a>定理1.2.1  
<a id="source-L76"></a>Hが(G,\*)の部分群であるための必要十分条件は、  
<a id="source-L77"></a>xy-1 が Hに含まれることである  

<a id="source-L79"></a>部分群に関しては今までの数学のストーリーとは違う展開がある  
<a id="source-L80"></a>群論においては有限性が重要視される場面がある  

<a id="source-L82"></a>定理1.2.2  
<a id="source-L83"></a>Gの空でない有限部分集合Hが部分群になっているための必要十分条件は abがHに含まれること  

<a id="source-L85"></a>定義1.7 巡回群  
<a id="source-L86"></a>巡回群であるとき、ある1つの元を繰り返し演算を行うことで全ての元を表現できる  

<a id="source-L88"></a>補題1.2.1  
<a id="source-L89"></a>群において、任意のgに関してg^nは巡回部分群になっている  

<a id="source-L91"></a>ここでいかなる群においても部分群が存在することになる  
<a id="source-L92"></a>この部分群の特徴はもちろんその生成元に集約されているのでこの巡回群の位数は元の個数と思っても良いが、&lt;g&gt;の群の位数として定義しても良いことが分かる  

<a id="source-L94"></a>補題1.2.2  

<a id="source-L96"></a>定理1.2.4  
<a id="source-L97"></a>Gを群とし、SをGの部分集合とする  
<a id="source-L98"></a>このとき、Gに含まれる部分群で、Sを含む最小の群が存在する  

<a id="source-L100"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  




<a id="source-L104"></a>

### 1.3 剰余類

<a id="source-L105"></a>ここから先は群の構造をより見やすくする努力をしてみる  
<a id="source-L106"></a>modのように、いくつかの仲間に分けることでその性質を見るのは有限個だけ見ておけば良くなるような仲間分けは行えないかを考えていく  

<a id="source-L108"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L110"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L112"></a>補題1.3.2  

<a id="source-L114"></a>補題1.3.3  
<a id="source-L115"></a>Gを群とし、HをGの部分群とする。  
<a id="source-L116"></a>HとHの任意の剰余類の間には全単射が存在する  
<a id="source-L117"></a>つまり、Gの位数と剰余類の位数は等しい  

<a id="source-L119"></a>定理1.3.1  
<a id="source-L120"></a>GとS×H（直積集合）の濃度は等しい  
<a id="source-L121"></a>つまり全単射写像が構成できる  

<a id="source-L123"></a>系1  


<a id="source-L126"></a>系2 Lagrangeの定理  
<a id="source-L127"></a>Gを有限群とする。  
<a id="source-L128"></a>Gの任意の部分群の位数はGの位数の約数である  

<a id="source-L130"></a>剰余類は非常に重要な役割を果たしている  
<a id="source-L131"></a>Hに関する剰余類はHの位数に関する情報を持っているとも考えられる  
<a id="source-L132"></a>そこで、H自身を調べるのではなく、その剰余類の性質を調べることには大きな意味がある  

<a id="source-L134"></a>定義1.11 群の指数  
<a id="source-L135"></a>Gを群とし、Hを部分群とする  
<a id="source-L136"></a>Hに関する剰余類の濃度をHの指数という  

<a id="source-L138"></a>株価指数などで利用される意味合いでの指数  
<a id="source-L139"></a>つまりHの性質を指し示すような数  



<a id="source-L142"></a>

### 1.4 正規部分群

<a id="source-L143"></a>剰余類についてもう少し考える  
<a id="source-L144"></a>剰余類は簡単に分かるが、剰余類は群になることもあればならないこともある  
<a id="source-L145"></a>ここで、群になるためにはどのような構造が必要かと言うことが問題になる  
<a id="source-L146"></a>剰余類の構造をもたらすのはどの部分群でわるかということだけなので剰余類の性質は部分群に強く依存する  





<a id="source-L151"></a>

### 2 準同型写像

<a id="source-L152"></a>ある１つの構造を導入し、（ここでは演算構造）その構造や性質を定義し、調べてきた  
<a id="source-L153"></a>次に数学では何をやるかというと、その構造を壊さないような写像とは何かということである  
<a id="source-L154"></a>線形空間には線型写像  
<a id="source-L155"></a>位相空間(距離空間)には同相写像というものがあった  
<a id="source-L156"></a>群論でこのような写像に対応する写像はなんだろうか？  
<a id="source-L157"></a>演算構造を壊さないような写像とは準同型写像のことである  


<a id="source-L159"></a>

### 2.1 準同型写像の定義


<a id="source-L161"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L163"></a>群同士の関係を導入したので、その２つの関係が同値関係かどうかが気になる  

<a id="source-L165"></a>恒等写像は同型写像になっている  

<a id="source-L167"></a>fが同型写像なら、f-1も同型写像になる  
<a id="source-L168"></a>また、準同型写像の合成写像も準同型写像となる  

<a id="source-L170"></a>２つの郡の間に定義される関係：同型は同値関係になっている  

<a id="source-L172"></a>元を１つだけ含む郡の間には同型写像が存在する  

<a id="source-L174"></a>このことより元を１つしか含まない郡の間にはそれが郡であるという条件だけから全て同型であることが示される  
<a id="source-L175"></a>そこで、この１つしか元を含まない群に自明な軍という名前をつけておく  

<a id="source-L177"></a>ここで、面白い定理を証明するためにいくつか準備をする  

<a id="source-L179"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L181"></a>fを準同型写像とすると、Ker(f)はG内の正規部分群である  

<a id="source-L183"></a>核を調べるということから、f自身の性質を導けることがある  

<a id="source-L185"></a>補題：fが単射であることの必要十分条件はKer(f) = {1G}が成り立つことである  

<a id="source-L187"></a>つまり核を調べるだけでその準同型写像が単射かどうか判定できる  
<a id="source-L188"></a>（これは線形代数でも似たようなものがあるのでは）  
<a id="source-L189"></a>核とは押しつぶした元であり、核の元が多いというのは、押しつぶした元の数が多いということになり、乱暴な写像であることが導かれる  

<a id="source-L191"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L193"></a>写像の像であるから、f(G)を書いても良い  
<a id="source-L194"></a>だが、準同型写像というだけで強い制約を受けるので、像でもそのようなことが起こる  
<a id="source-L195"></a>よってIm(f)という書き方をする  

<a id="source-L197"></a>Im(f)もG’内の部分群である  



<a id="source-L200"></a>

### 2.2 準同型定理

<a id="source-L201"></a>準同型定理は群論を学ぶ一番最初の山場である  

<a id="source-L203"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L205"></a>代表系が選べるかどうかは数学そのものの構造に関わる問題である  
<a id="source-L206"></a>それが可能だと思って、上のような写像を考えている  






<a id="source-L212"></a>

### 2.3 第二同型定理

<a id="source-L213"></a>同型定理と呼ばれるものは他にもいくつかある  

<a id="source-L215"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  




<a id="source-L220"></a>—————————————————————————————————————————————————————————  

> <a id="source-L222"></a><https://www.youtube.com/watch?v=PxctoJHzfcg>  

<a id="source-L224"></a>古賀正樹さんの動画  



<a id="source-L228"></a>————————————————————————————————————————————————————————  
<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

群の公理にある結合法則 $(ab)c=a(bc)$ と、交換法則 $ab=ba$ を区別する。本文の「操作の順序を入れ替えられる」は、一般の群の公理としては不正確。交換法則まで成り立つ群が可換群である。置換の合成を小さく計算すると、順序を変えると結果が変わる例を作れる。[Judson, Abstract Algebra](https://judsonbooks.org/aata-files/aata-html/aata.html)の群の定義を参照。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [線形代数](../linear-algebra/linear-algebra.md)
- [Lie代数](lie-algebras.md)
- [代数の基礎](algebra-foundations.md)
- [圏論](category-theory.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
