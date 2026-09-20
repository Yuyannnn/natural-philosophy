---
title: "代数の基礎"
status: draft
tags: [scrapbox, algebra]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E4%BB%A3%E6%95%B0%E3%81%AE%E5%9F%BA%E7%A4%8E"
source_created: "2023-01-21T18:33:06Z"
source_updated: "2025-05-26T20:19:19Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 代数の基礎

同値関係から群・環・体へ進む授業メモ。

原ページ作成：2023-01-21 ／ 最終更新：2025-05-26（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/algebra-foundations.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E4%BB%A3%E6%95%B0%E3%81%AE%E5%9F%BA%E7%A4%8E)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

**原文に埋め込み欠落記号が64か所あります。** 取得時点で内容を特定できないため、本文中で位置を示しています。推測した図や式に置き換えていません。

<details>
<summary>本文の見出しから探す</summary>

- [代数数理工学](#source-L10)
- [1.値関関係](#source-L14)
- [2.束](#source-L16)
- [3.群](#source-L18)
- [4.環](#source-L22)
- [5.体](#source-L25)
- [1.関係](#source-L29)
- [2.束](#source-L31)
- [3.群](#source-L33)
- [4.環](#source-L35)
- [5.体](#source-L37)
- [6.有限体と応用](#source-L39)
- [7.組合せ論](#source-L41)
- [第一講](#source-L46)
- [第二講](#source-L67)
- [1.2.2 単位元と逆元](#source-L94)
- [1.2.3 代表的な代数系](#source-L123)
- [2.2 関係](#source-L134)
- [第3講](#source-L171)
- [第4講](#source-L198)
- [第5講](#source-L202)
- [第6講](#source-L206)
- [第1章 代数系](#source-L217)
- [1.1 代数系](#source-L218)
- [1.2 代表的な代数系](#source-L239)
- [1.3 同値関係と商構造](#source-L256)
- [第2章 束](#source-L276)
- [2.1 順序と朿](#source-L278)
- [第4章 群](#source-L303)
- [4.2 正規部分群と準同型](#source-L318)
- [4.3 巡回群](#source-L339)
- [第5章 環と体](#source-L368)
- [5.1 整域と商体](#source-L369)
- [5.3 イデアルと剰余環](#source-L384)
- [5.4 ユークリッド整域と単項イデアル環](#source-L409)
- [5.5 一意分解整域](#source-L425)
- [第6章 拡大体](#source-L451)
- [「代数学入門 -花木章秀-」](#source-L478)
- [1 記号と準備](#source-L480)
- [2 群](#source-L512)
- [3 環と体](#source-L524)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 代数の基礎

<a id="source-L2"></a>[線形代数](../linear-algebra/linear-algebra.md)  
<a id="source-L3"></a>[関数解析](../analysis/functional-analysis.md)  
<a id="source-L4"></a>[Lie代数](lie-algebras.md)  
<a id="source-L5"></a>[圏論](category-theory.md)  
<a id="source-L6"></a>[ガロア理論](galois-theory.md)  




<a id="source-L10"></a>

### 代数数理工学

<a id="source-L11"></a>Algebra Mathematical Engineering  



<a id="source-L14"></a>

### 1.値関関係

> <a id="source-L15"></a>同係，順序関係  

<a id="source-L16"></a>

### 2.束

> <a id="source-L17"></a>モジュラ束，分配束  

<a id="source-L18"></a>

### 3.群

> <a id="source-L19"></a>部分群，Lagrangeの定理，  
> <a id="source-L20"></a>正規部分群，組成列，  
> <a id="source-L21"></a>置換群，Burnsideの定理  

<a id="source-L22"></a>

### 4.環

> <a id="source-L23"></a>整域，イデアル，素因子分解，  
> <a id="source-L24"></a>Euclidの互除法，単因子標準形  

<a id="source-L25"></a>

### 5.体

> <a id="source-L26"></a>代数拡大，代数的独立性，  
> <a id="source-L27"></a>作図可能性  


<a id="source-L29"></a>

### 1.関係

> <a id="source-L30"></a>集合の中に構造が入る仕組みを学ぶ。  

<a id="source-L31"></a>

### 2.束

> <a id="source-L32"></a>束というもっとも基本的な構造とその性質を学ぶ。  

<a id="source-L33"></a>

### 3.群

> <a id="source-L34"></a>一つの演算だけを持つ代数系としての群の基本的性質を学ぶ。群は、ほとんどすべての代数系の基礎となる構造である。  

<a id="source-L35"></a>

### 4.環

> <a id="source-L36"></a>二つの演算を持つ代数系の中でもっとも基本的な環とその性質を学ぶ。  

<a id="source-L37"></a>

### 5.体

> <a id="source-L38"></a>環より少し強い性質を持つ体について学ぶ。  

<a id="source-L39"></a>

### 6.有限体と応用

> <a id="source-L40"></a>体の性質を利用して、誤り訂正符号や疑似乱数が設計できることなどを学ぶ。  

<a id="source-L41"></a>

### 7.組合せ論

> <a id="source-L42"></a>離散構造の代表としてのマトロイド、その性質、その応用などを学ぶ。  




<a id="source-L46"></a>

### 第一講


<a id="source-L48"></a>代数系：算法、同型、群、結合法則、単位元、逆元  
<a id="source-L49"></a>写像と関係：同値関係、準同型定理、順序関係、束  
<a id="source-L50"></a>群：部分群、剰余群、同型定理、整域、多項式環、素元  
<a id="source-L51"></a>環：イデアル、剰余環、同型定理、整域、多項式環l、  
<a id="source-L52"></a>体  
<a id="source-L53"></a>多変数多項式  

<a id="source-L55"></a>全射、単射、全単射について説明した  

<a id="source-L57"></a>部分集合の写像や逆写像について説明していた  
<a id="source-L58"></a>ここら辺はわかってる  

<a id="source-L60"></a>こっから先代数系というものを定義する  

<a id="source-L62"></a>逆写像は全単射じゃないと定義できないが、集合間の演算は全単射じゃなくても定義できる  





<a id="source-L67"></a>

### 第二講

<a id="source-L68"></a>ある集合の写像の逆写像が元の集合になるとは限らない、というのも、小さくなるような写像が考えられるので  
<a id="source-L69"></a>集合の上に算法が入ったものを代数系という  

<a id="source-L71"></a>定義1.1 算法  
<a id="source-L72"></a>Aを集合Eの直積として、A→Eの写像を算法という  

<a id="source-L74"></a>定義1.3 代数系  
<a id="source-L75"></a>集合Eに対して算法が定義されているとすると、集合と算法の組みを代数系という  

<a id="source-L77"></a>定義2.5 準同型  
<a id="source-L78"></a>ある代数系があったときにその代数系がどのくらい似ているのかに興味があるので、準同型という概念を導入する  
<a id="source-L79"></a>f(a○b) = f(a)○f(b)が成り立つときに準同型写像という  
<a id="source-L80"></a>Eの代数系と、E’の代数系という2つの代数系があるが、演算がfによってどれだけ保たれているかの指標となる  

<a id="source-L82"></a>定義2.6 全単射  
<a id="source-L83"></a>さらにfが全単射のときfを同型写像という  
<a id="source-L84"></a>EとE’は演算も含めて同じ構造であるということ  
<a id="source-L85"></a>同型のときはfの逆写像f’も同型写像となる  
<a id="source-L86"></a>(証明  

<a id="source-L88"></a>例2.4  
<a id="source-L89"></a>Nと2Nは同型  

<a id="source-L91"></a>同型定理の多くは、準同型かつ全単射なのを示すことを目的としている  
<a id="source-L92"></a>演算+どういう構造が入っていたら、どういうことができるのかを見ていく  


<a id="source-L94"></a>

### 1.2.2 単位元と逆元


<a id="source-L96"></a>定義1.4 結合的  
<a id="source-L97"></a>(a○b)○C = a○(b○c)のとき結合的という  

<a id="source-L99"></a>定義1.5 可換  
<a id="source-L100"></a>a○b = b○aが成り立つことを可換という  

<a id="source-L102"></a>定義1.6 単位元、逆元  
<a id="source-L103"></a>a○e = e○a = aを満たすeを単位元という  

<a id="source-L105"></a>定理1.2  
<a id="source-L106"></a>１つの算法に対して単位元は高々１つ  
<a id="source-L107"></a>(証明  

<a id="source-L109"></a>定義1.7 逆元  
<a id="source-L110"></a>a,bに対して、a○b = b○a = eの関係があるときbを算法○に関するaの逆元という  
<a id="source-L111"></a>同様にaはbの逆元である  

<a id="source-L113"></a>定理1.3  
<a id="source-L114"></a>統合的な算法において逆元は高々1個である  
<a id="source-L115"></a>証明はaの逆元をb,b’として成り立つ演算のルールだけを使ってこれらが等しいことを示せば良い  
<a id="source-L116"></a>足し算の逆元は-xと書く、掛け算はx-1  

<a id="source-L118"></a>定理1.4  
<a id="source-L119"></a>(E,○)が結合法則を満たすとすると  
<a id="source-L120"></a>その逆元が存在すれば(x-1)-1=xとなる  
<a id="source-L121"></a>証明はx○y = y○x = eより  


<a id="source-L123"></a>

### 1.2.3 代表的な代数系

<a id="source-L124"></a>定義1.9 半群  
<a id="source-L125"></a>結合的な算法を持つ代数を半群という  

<a id="source-L127"></a>定義1.10 モノイド  
<a id="source-L128"></a>単位元を持つ半群をモノイドという  

<a id="source-L130"></a>定義1.11 群  
<a id="source-L131"></a>モノイドEの全ての元が逆元を持つとき、Eを群という  



<a id="source-L134"></a>

### 2.2 関係

<a id="source-L135"></a>定義2.7  
<a id="source-L136"></a>集合Eに対して、E×Eの部分集合RをEの上の関係という  
<a id="source-L137"></a>a,b∈Eに対して、(a,b)∈Rのとき、  
<a id="source-L138"></a>aRbまたはa\~bとかく  

<a id="source-L140"></a>定義2.8 同値関係  
<a id="source-L141"></a>同値関係があると、Eをその関係で分類することがよく使われる  
<a id="source-L142"></a>集合Eの上の関係\~が以下の3条件を満たすとき、\~を同値関係という  
<a id="source-L143"></a>(1) 任意のaに対して、a\~aが成り立つ（反射率）  
<a id="source-L144"></a>(2) 任意のa,bに対してa\~bならばb\~a（対象律）  
<a id="source-L145"></a>(3) 任意のa,b,cに対して、a\~bかつb\~cならばa\~cが成り立つ（推移律）  

<a id="source-L147"></a>定義2.9  
<a id="source-L148"></a>関係\~を集合E上の同値関係とする  
<a id="source-L149"></a>a\~bのとき、aとbは同値であるという  

<a id="source-L151"></a>同値類全体からなる集合をE/\~で表し、これを\~に関する商集合という  
<a id="source-L152"></a>集合を１つの元と見ることもできる  
<a id="source-L153"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L154"></a>こうすることで、関係を与えたときに、同値関係によって新しくグループを作るということができる  

<a id="source-L156"></a>定理2.1 同値類に関して以下が成り立つ  
<a id="source-L157"></a>(1) 任意のa∈Eに対してa∈&lt;a&gt;\~  
<a id="source-L158"></a>(2) b∈&lt;a&gt;\~ならば&lt;a&gt;\~ = &lt;b&gt;\~  
<a id="source-L159"></a>(3) aとbがnot\~ &lt;a&gt;\~ ∩ &lt;b&gt;\~ = 空集合  
<a id="source-L160"></a>これは同値関係の３つの反射律、対称律、推移律で証明される  
<a id="source-L161"></a>(1)は反射律でわかる  
<a id="source-L162"></a>(2)  

<a id="source-L164"></a>つまり同値類で分類すれば、交わりのない綺麗な分類ができる  

<a id="source-L166"></a>必要十分条件の同値とは別の話  
<a id="source-L167"></a>by先生  
<a id="source-L168"></a>今答えた通りですが、「２条件の同値」という関係（と呼んでいいかはさておき）は、反射律とかは成り立ちますね。  



<a id="source-L171"></a>

### 第3講


<a id="source-L173"></a>定義2.10  
<a id="source-L174"></a>x\~x’, y\~y’ならばx○y \~ x’○y’のとき、関係\~と算法○は成立するという  

<a id="source-L176"></a>定理2.2  
<a id="source-L177"></a>関係\~と算法○が両立しているとする  
<a id="source-L178"></a>このとき、xの同値類とyの同値類にx○yの同値類を他愛王させる算法はE/\~上の算法となる  

<a id="source-L180"></a>上記の算法により小集合E/\~上にサダあめらえる代数系を\~によるEの商構造という  

<a id="source-L182"></a>代数系の話として最も大事な話は準同型と同値の関係である  
<a id="source-L183"></a>準同型写像によって自然に同値関係が作れる  

<a id="source-L185"></a>定理2.4(準同型写像によって生成される同値関係)  
<a id="source-L186"></a>fを代数系(E,○)から(F,○’)への準同型写像とする  
<a id="source-L187"></a>x,y ∈ Eに対して、f(x) = f(y)のときx\~yと定義する  
<a id="source-L188"></a>このとき\~はEの算法と両立する同値関係である  

<a id="source-L190"></a>定義  
<a id="source-L191"></a>上で定義される関係\~を準同型写像fによって生成される同値関係という  

<a id="source-L193"></a>定理5.30 (準同型定理)  
<a id="source-L194"></a>f:E→Fを代数系EからFへの準同型写像とする  
<a id="source-L195"></a>fによって生成される同値関係\~によるEの商構造は像f(E)と同型である  



<a id="source-L198"></a>

### 第4講





<a id="source-L202"></a>

### 第5講

<a id="source-L203"></a>群について  



<a id="source-L206"></a>

### 第6講

<a id="source-L207"></a>Kerとか出てきてた  




<a id="source-L212"></a>——————————————————————————————  

<a id="source-L214"></a>代数  



<a id="source-L217"></a>

### 第1章 代数系


<a id="source-L218"></a>

### 1.1 代数系

<a id="source-L219"></a>定義1.1 内算法  
<a id="source-L220"></a>要するに演算のこと  

<a id="source-L222"></a>定義1.2 代数系  
<a id="source-L223"></a>集合と算法の組みを代数系という  

<a id="source-L225"></a>定義1.3 準同型と同型  
<a id="source-L226"></a>演算の線形性が保たれるものを準同型  
<a id="source-L227"></a>準同型かつ全単射なものを同型という  

<a id="source-L229"></a>定義1.4 結合的  

<a id="source-L231"></a>定義1.5 可換  

<a id="source-L233"></a>定義1.6 単位元  

<a id="source-L235"></a>定義1.7 逆元  




<a id="source-L239"></a>

### 1.2 代表的な代数系

<a id="source-L240"></a>定義1.8 半群  
<a id="source-L241"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L243"></a>定義1.9 群  
<a id="source-L244"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L246"></a>定義1.10 環  
<a id="source-L247"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L249"></a>定義1.11 体  
<a id="source-L250"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L252"></a>定義1.12 束  
<a id="source-L253"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  



<a id="source-L256"></a>

### 1.3 同値関係と商構造

<a id="source-L257"></a>定義1.13 関係  
<a id="source-L258"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L260"></a>定義1.14 同値関係  
<a id="source-L261"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L263"></a>定義1.15 同値類と商集合  
<a id="source-L264"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L266"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L268"></a>定理1.1 準同型定理  
<a id="source-L269"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  







<a id="source-L276"></a>

### 第2章 束



<a id="source-L278"></a>

### 2.1 順序と朿

<a id="source-L279"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L281"></a>定義2.2 束から導かれる半順序  
<a id="source-L282"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L284"></a>定義2.3 ハッセ図  
<a id="source-L285"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L287"></a>定義2.4 モジュラ束  
<a id="source-L288"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L290"></a>定義2.7 部分朿  
<a id="source-L291"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L293"></a>定義2.8 商束  
<a id="source-L294"></a>定理2.8 デデキントの同型定理  
<a id="source-L295"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  








<a id="source-L303"></a>

### 第4章 群

<a id="source-L304"></a>定義4.1 部分群  
<a id="source-L305"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L307"></a>定理4.1  
<a id="source-L308"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L310"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L312"></a>ラグランジュの定理  
<a id="source-L313"></a>有限群Gの部分群の位数はGの位数の約数である  
<a id="source-L314"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  




<a id="source-L318"></a>

### 4.2 正規部分群と準同型

<a id="source-L319"></a>定義4.3 正規部分群  
<a id="source-L320"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L322"></a>定理4.2 Hを群Gの正規部分群とするとき、GのHによる剰余類の全体は群をなす  
<a id="source-L323"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L325"></a>定理4.3 群の準同型定理  
<a id="source-L326"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L328"></a>定理4.4 群の第一同型定理  
<a id="source-L329"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L331"></a>定理4.5 群の第二同型定理  
<a id="source-L332"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L334"></a>定理4.6 群の第三同型定理  
<a id="source-L335"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  




<a id="source-L339"></a>

### 4.3 巡回群

<a id="source-L340"></a>定義4.4 位数  
<a id="source-L341"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L343"></a>定義4.5 生成元  
<a id="source-L344"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L346"></a>定理4.7 巡回群Gの部分群Hもまた巡回群となる  
<a id="source-L347"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L349"></a>定理4.8 有限群Gの位数は、Gの位数|G|の約数となる  
<a id="source-L350"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L352"></a>定理4.9 有限アーベル群Gの元の位数の最大値をmとすると、Gの任意の元の位数はmの約数である  
<a id="source-L353"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L355"></a>定理4.10 群Gの位数が素数pであるとき、Gは巡回群である  
<a id="source-L356"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L358"></a>定理4.11 群の直積分解  
<a id="source-L359"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L361"></a>定理4.12 巡回群Gの位数がmnでm,nが互いに素なら、この巡回群は位数mと位数nの２つの巡回群の直積に分解される  
<a id="source-L362"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  






<a id="source-L368"></a>

### 第5章 環と体


<a id="source-L369"></a>

### 5.1 整域と商体

<a id="source-L370"></a>定義5.1 部分環  
<a id="source-L371"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L373"></a>定義5.2 零因子  
<a id="source-L374"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L376"></a>定義5.3 整域  

<a id="source-L378"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L379"></a>定理5.1 整体  
<a id="source-L380"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  




<a id="source-L384"></a>

### 5.3 イデアルと剰余環

<a id="source-L385"></a>イデアルの定義1  
<a id="source-L386"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L388"></a>イデアルの定義2  
<a id="source-L389"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L391"></a>イデアル1による同値類  
<a id="source-L392"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L394"></a>定理5.3 剰余環  
<a id="source-L395"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L397"></a>定理5.4 環の準同型定理  
<a id="source-L398"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L400"></a>定理5.5  
<a id="source-L401"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L402"></a>定理5.6 極大イデアルは素イデアルである  
<a id="source-L403"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L404"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  





<a id="source-L409"></a>

### 5.4 ユークリッド整域と単項イデアル環


<a id="source-L411"></a>定義5.4 整域Iと関数gが次の性質を満たすとき、Iをユークリッド整域という  
<a id="source-L412"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L414"></a>定義5.5 Rを単位元を持つ可換環とする  
<a id="source-L415"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L417"></a>定義5.6 ただ１つの元aで生成されるイデアルaを単項イデアルという  
<a id="source-L418"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L420"></a>定理5.7 ユークリッド整域は単項イデアル整域である  
<a id="source-L421"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  




<a id="source-L425"></a>

### 5.5 一意分解整域

<a id="source-L426"></a>定義5.7 約元  
<a id="source-L427"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L429"></a>定義5.8 同伴  
<a id="source-L430"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L432"></a>定義5.9 素元  
<a id="source-L433"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L435"></a>定義5.10 既約元  
<a id="source-L436"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L438"></a>定義5.11 一意分解整域  
<a id="source-L439"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L441"></a>定義5.12 最小公約元、最小高倍元  
<a id="source-L442"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L444"></a>定理5.9  
<a id="source-L445"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  






<a id="source-L451"></a>

### 第6章 拡大体

<a id="source-L452"></a>定義6.1 標数  
<a id="source-L453"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L455"></a>定理6.1 体の標数pは0または素数である  
<a id="source-L456"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L458"></a>定理6.2 対E1,E2が体Fの部分体であるとき、E1かつE2も部分体となる  
<a id="source-L459"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L461"></a>定理6.3 任意の体はFの最小の部分体がPであ流とき、Pを体Fの素体という  
<a id="source-L462"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L464"></a>定理6.3  
<a id="source-L465"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L467"></a>定理6.9   
<a id="source-L468"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  






<a id="source-L475"></a>———————————————————————————————————————————  



<a id="source-L478"></a>

### 「代数学入門 -花木章秀-」



<a id="source-L480"></a>

### 1 記号と準備


<a id="source-L482"></a>この講義では現代数学の基礎となる群、環、体の定義及び基本的な性質や例を理解することを目標とする  
<a id="source-L483"></a>これらは幾何学、解析学、情報科学、物理学などの広い分野で応用される基本的かつ重要なものである  
<a id="source-L484"></a>数学においては、ある対象の持つ基本的な性質のみに注目し、その性質だけを考えた理論を構築し、そこで得られた理論をもとに問題に応用するといった手法がとられる  
<a id="source-L485"></a>つまり、全く違う対象が類似の性質を持った場合にその共通の性質だけに注目して得られた結果はそのどちらにも適用できる  
<a id="source-L486"></a>したがって多くの対象が持つ性質を考え、それに関する一般論を構築しておけば、その適用範囲は広くなり、その重要性は増すことになる  
<a id="source-L487"></a>このような考えから、定義され、研究されてきたのが、「群」「環」「体」である  

<a id="source-L489"></a>例えば、n次元ベクトル全体の集合は加法や減法が定義されるが、乗法や除法は定義されないのでこれは群である  

<a id="source-L491"></a>n次の正方行列全体の集合Rには加法と減法が定まっているので群である  
<a id="source-L492"></a>また、これには乗法も定まっているので、Rを単に群として見ているのでは乗法に関する情報が得られない  
<a id="source-L493"></a>つまりこれを環とみる  
<a id="source-L494"></a>n次正方行列には一般に逆行列が存在するわけではないので、Rに除法を定めることはできない  

<a id="source-L496"></a>有数全体、実数全体、複素数全体などのように除法も考えられるものも少なくはない  
<a id="source-L497"></a>このように四則演算が行える対象を体と定める  

<a id="source-L499"></a>1-1 集合  
<a id="source-L500"></a>1-2 整数  
<a id="source-L501"></a>1-3 写像  
<a id="source-L502"></a>1-4 同値関係と同値類  
<a id="source-L503"></a>1-5 順序集合とZornの補題  
<a id="source-L504"></a>1-6 二項演算  
<a id="source-L505"></a>1-7 半群とモノイド  







<a id="source-L512"></a>

### 2 群


<a id="source-L514"></a>2-1 群の定義と例  
<a id="source-L515"></a>2-2 加群  
<a id="source-L516"></a>2-3 部分群  
<a id="source-L517"></a>2-4 剰余類  
<a id="source-L518"></a>2-5 剰余群  






<a id="source-L524"></a>

### 3 環と体


<a id="source-L526"></a>3-1 定義と例  
<a id="source-L527"></a>3-2 整数の合同によって定義される環  
<a id="source-L528"></a>3-3 部分環  
<a id="source-L529"></a>3-4 イデアルと剰余環  
<a id="source-L530"></a>3-5 多項式環  
<a id="source-L531"></a>3-6 色々な体  




<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

商を作るときは、同値類の集合を作れることと、元の演算がその上で well-defined になることを分ける。群の商では正規部分群、環の商ではイデアルという条件が、その確認に関わる。整数の偶奇の二つの類で足し算を試し、「代表元を変えても結果の類が変わらない」を確かめるとよい。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [線形代数](../linear-algebra/linear-algebra.md)
- [関数解析](../analysis/functional-analysis.md)
- [Lie代数](lie-algebras.md)
- [圏論](category-theory.md)
- [ガロア理論](galois-theory.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
