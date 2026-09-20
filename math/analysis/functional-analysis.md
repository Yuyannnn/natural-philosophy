---
title: "関数解析"
status: draft
tags: [scrapbox, analysis]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E9%96%A2%E6%95%B0%E8%A7%A3%E6%9E%90"
source_created: "2023-01-21T18:32:10Z"
source_updated: "2024-05-13T03:20:59Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 関数解析

関数空間・作用素から半群へ進み、学んだ内容を説明できるようになりたいという記録。

原ページ作成：2023-01-21 ／ 最終更新：2024-05-13（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/functional-analysis.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E9%96%A2%E6%95%B0%E8%A7%A3%E6%9E%90)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

## 思考の手がかり

> ヒルベルト空間よりもまずはルベーグ空間を勉強したい

[本文の該当箇所へ](#source-L1199)

> 熱半群ぐらいはマスターしたい

[本文の該当箇所へ](#source-L1234)

<details>
<summary>本文の見出しから探す</summary>

- [解析数理工学](#source-L7)
- [第１講](#source-L26)
- [第2講](#source-L46)
- [第3講](#source-L69)
- [第4講](#source-L89)
- [第５講](#source-L111)
- [第6講](#source-L140)
- [第7講](#source-L165)
- [第8講](#source-L193)
- [第１講でかじったやつ](#source-L212)
- [第9講](#source-L218)
- [1.|f|&lt;=g a.e.かつgが可積分ならばfは可積分](#source-L224)
- [2.fが可積分ならば|f|&lt;∞ a.e.](#source-L225)
- [第10講](#source-L241)
- [11.Fubiniの定理(概要)](#source-L243)
- [第11講](#source-L263)
- [12.2 関数空間](#source-L278)
- [第12講 ](#source-L301)
- [第13講 ](#source-L307)
- [「Collatz(Functional Analysis) PDF」](#source-L319)
- [1 解析学の基本事項](#source-L321)
- [2 Banach空間](#source-L360)
- [2.1 線形空間](#source-L362)
- [1.　Xの任意この線型部分空間の共通部分は再び１つの線型部分空間となる](#source-L379)
- [2.MをSによって張られる線型部分空間とすると、MはSを含む線型部分空間全体の共通部分となる](#source-L380)
- [2.2 Banach空間](#source-L393)
- [1.収束Xの上の点列がxに収束する](#source-L405)
- [2.xnをX上の点列とする](#source-L406)
- [3.X0が集積点](#source-L407)
- [4.近傍](#source-L408)
- [5.稠密](#source-L409)
- [3 線型作用素](#source-L451)
- [3.1 線型作用素の定義](#source-L453)
- [3.2 連続性と有界性](#source-L475)
- [1.Tはx0の一点で連続](#source-L484)
- [2.Tは連続作用素](#source-L485)
- [3.Tは有界作用素](#source-L486)
- [3.3 作用素の和と積](#source-L511)
- [「Collatz(Introduction of Analysis2) PDF」](#source-L536)
- [1 解析における基本概念](#source-L545)
- [1.1 距離空間としての実数](#source-L549)
- [1.2 数列の収束](#source-L569)
- [1.3 最大値、上限](#source-L581)
- [2 に変数以上の関数の微分](#source-L588)
- [2.1 連続関数](#source-L589)
- [2.2 偏微分](#source-L619)
- [2.3 全微分](#source-L620)
- [2.4 極値](#source-L621)
- [2.5 陰関数](#source-L622)
- [3 二変数以上の関数の積分](#source-L629)
- [3.1 一変数の積分](#source-L631)
- [3.2 二変数の積分](#source-L639)
- [3.3 面積](#source-L655)
- [3.4 置換積分](#source-L668)
- [3.5 広義積分](#source-L672)
- [3.6 発展的話題](#source-L673)
- [4 曲面積/体積](#source-L679)
- [「Collatz(関数解析)」](#source-L694)
- [1 Xを任意個の線型部分空間の共通部分は再び線型部分空間となる](#source-L792)
- [1.完備かどうか](#source-L1134)
- [2.同相かどうか](#source-L1135)
- [「関数解析について」](#source-L1176)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 関数解析

<a id="source-L2"></a>[微分積分学](calculus.md)  
<a id="source-L3"></a>[集合と位相](../foundations/sets-and-topology.md)  
<a id="source-L4"></a>[多様体論入門](../geometry/introduction-to-manifolds.md)  



<a id="source-L7"></a>

### 解析数理工学

<a id="source-L8"></a>Analysis Mathematical Engineering  

<a id="source-L10"></a>I ルベーグ積分概論  
<a id="source-L11"></a>１ リーマン積分の弱点  
<a id="source-L12"></a>２ 測度  
<a id="source-L13"></a>３ 可測関数  
<a id="source-L14"></a>４ ルベーグ積分の定義  
<a id="source-L15"></a>５ ルベーグ積分の性質 ： 収束定理， 微分と積分の順序交換定理  
<a id="source-L16"></a>６ フビニの定理  
<a id="source-L17"></a>II 関数解析入門  
<a id="source-L18"></a>１ ノルム空間　  
<a id="source-L19"></a>２ ヒルベルト空間  
<a id="source-L20"></a>３ 線形作用素  
<a id="source-L21"></a>４ 一様有界性定理  





<a id="source-L26"></a>

### 第１講


<a id="source-L28"></a>定理1.1(Darboux)  
<a id="source-L29"></a>不足和、過剰和、下積分、上積分  

<a id="source-L31"></a>定理1.2(Riemann)  
<a id="source-L32"></a>Riemann可積分の定義  

<a id="source-L34"></a>定理1.3  
<a id="source-L35"></a>積分と極限の交換条件（一様収束）  

<a id="source-L37"></a>定理1.4(Arzela)  
<a id="source-L38"></a>同じく（各点収束）  

<a id="source-L40"></a>定理1.5(Lebesque)  
<a id="source-L41"></a>Fの条件はいらない  





<a id="source-L46"></a>

### 第2講


<a id="source-L48"></a>定理2.1(Lebesque)  

<a id="source-L50"></a>定義2.2(区間)  

<a id="source-L52"></a>定義2.3(区間塊（基本集合）)  

<a id="source-L54"></a>補題2.2  
<a id="source-L55"></a>Disjointな区間塊でAは表せる  

<a id="source-L57"></a>定理2.3（区間塊の性質）  
<a id="source-L58"></a>単調性、有限劣加法性、有限加法性  

<a id="source-L60"></a>定理2.4  
<a id="source-L61"></a>Jordan可測である条件  

<a id="source-L63"></a>定理2.5(Jordan可測集合の性質)  






<a id="source-L69"></a>

### 第3講


<a id="source-L71"></a>定理2.6(Jordan測度の性質)  
<a id="source-L72"></a>単調性、有限劣加法性、有限加法性  

<a id="source-L74"></a>定義3.1(Lebesque外測度)  

<a id="source-L76"></a>定理3.1(Lebesque外測度の性質)  

<a id="source-L78"></a>定理3.2  
<a id="source-L79"></a>有限区間塊ならばLebesque外測度とJordan測度が等しい  

<a id="source-L81"></a>定理3.3（有限区間列の性質）  

<a id="source-L83"></a>定理3.4  
<a id="source-L84"></a>要するに有限加法性  





<a id="source-L89"></a>

### 第4講


<a id="source-L91"></a>定義4.1(Lebesque内測度の定義)  

<a id="source-L93"></a>定理4.1  
<a id="source-L94"></a>Lebesque内測度はIの取り方によらない  

<a id="source-L96"></a>定理4.2(Lebesque内測度の性質)  

<a id="source-L98"></a>定理4.3(Jordan測度とLebesque測度の関係)  

<a id="source-L100"></a>系  
<a id="source-L101"></a>AがJordan可測ならJordan測度とLebesque内/外測度が一致する  

<a id="source-L103"></a>定理4.4 (Lebesque外測度と集合の関係)  

<a id="source-L105"></a>定理4.5(Lebesque内測度と集合の関係)  






<a id="source-L111"></a>

### 第５講


<a id="source-L113"></a>定義5.1(Lebesque可測の定義)  

<a id="source-L115"></a>定理5.1  
<a id="source-L116"></a>Jordan可測集合はLebesque可測  

<a id="source-L118"></a>定理5.2(Lebesque外測度とLebesque可測の関係)  

<a id="source-L120"></a>補題5.3  
<a id="source-L121"></a>区間列の性質  

<a id="source-L123"></a>定理5.4(Lebesque外測度の性質)  

<a id="source-L125"></a>補題5.5(Lebesque外測度と内測度の性質)  

<a id="source-L127"></a>定理5.6(Lebesque可測の性質)  

<a id="source-L129"></a>系  
<a id="source-L130"></a>Lebesque可測の時の有限加法性  

<a id="source-L132"></a>定理5.7  
<a id="source-L133"></a>Lebesque可測な集合とLebesque測度の関係  

<a id="source-L135"></a>定理5.8  
<a id="source-L136"></a>Lebesque可測度の性質  




<a id="source-L140"></a>

### 第6講


<a id="source-L142"></a>定理6.1  
<a id="source-L143"></a>Lebesque可測のときの性質  

<a id="source-L145"></a>定理6.2  
<a id="source-L146"></a>開集合はLebesque可測  

<a id="source-L148"></a>系  
<a id="source-L149"></a>閉集合はLebesque可測  

<a id="source-L151"></a>定理6.3  
<a id="source-L152"></a>Lebesque可測と同値な性質  

<a id="source-L154"></a>定義7.1  
<a id="source-L155"></a>関数が可測である定義  

<a id="source-L157"></a>定理7.1  
<a id="source-L158"></a>関数が可即であるのと同値な条件  







<a id="source-L165"></a>

### 第7講


<a id="source-L167"></a>定理7.2  
<a id="source-L168"></a>可測な関数の性質  

<a id="source-L170"></a>定理7.3  
<a id="source-L171"></a>可測な関数の性質  

<a id="source-L173"></a>定理7.4（可測な関数列の性質）  
<a id="source-L174"></a>積分と関数列の極限の交換を考える時、可測集合がσ加法族をなすのがポイントである  

<a id="source-L176"></a>定理7.5  
<a id="source-L177"></a>fが可測関数のときの性質  

<a id="source-L179"></a>定理7.6  
<a id="source-L180"></a>関数列と関数の極限と可測性の関係  

<a id="source-L182"></a>定理8.1  
<a id="source-L183"></a>前やった  

<a id="source-L185"></a>定義8.1  
<a id="source-L186"></a>定義2.1と同じ  







<a id="source-L193"></a>

### 第8講


<a id="source-L195"></a>定理8.2  
<a id="source-L196"></a>測度の性質  

<a id="source-L198"></a>定理8.3  
<a id="source-L199"></a>積分の性質  

<a id="source-L201"></a>定理8.4  
<a id="source-L202"></a>積分の性質  

<a id="source-L204"></a>定理8.5  
|f|の積分の性質

<a id="source-L207"></a>補題8.6(chebishevの不等式)  

<a id="source-L209"></a>定理8.7(線型性)  

<a id="source-L211"></a>定理8.8(有限収束定理)  

<a id="source-L212"></a>

### 第１講でかじったやつ







<a id="source-L218"></a>

### 第9講


<a id="source-L220"></a>定理9.1  
<a id="source-L221"></a>Fと|f|の可積分は同値  

<a id="source-L223"></a>定理9.2  

<a id="source-L224"></a>

### 1.|f|&lt;=g a.e.かつgが可積分ならばfは可積分


<a id="source-L225"></a>

### 2.fが可積分ならば|f|&lt;∞ a.e.


<a id="source-L227"></a>定理9.3  
<a id="source-L228"></a>FがRiemann可積分ならLebesque可積分でその値は一致する  

<a id="source-L230"></a>補題10.1  
|f|の積分を0にするような可測なAが取れる

<a id="source-L233"></a>定理10.2(優収束定理)  
<a id="source-L234"></a>つまりは極限と積分の入れ替え  







<a id="source-L241"></a>

### 第10講



<a id="source-L243"></a>

### 11.Fubiniの定理(概要)

<a id="source-L244"></a>ちゃんとやるには直積測度の定義と完備化しないといけないがここでは流石に時間がない。  
<a id="source-L245"></a>ここからは関数解析の基礎  
<a id="source-L246"></a>線形代数っぽいことを無限次元の空間でやる、無限次元の空間を考えると関数の集合に線形代数のような手法を使うことができるようになる  

<a id="source-L248"></a>定義12.1(ノルム空間)  

<a id="source-L250"></a>定義12.2(Banach空間)  
<a id="source-L251"></a>完備なノルム空間  
<a id="source-L252"></a>完備とは、任意のコーシー列がその空間内に収束先を持つこと  

<a id="source-L254"></a>定義12.3(内積空間)  
<a id="source-L255"></a>ここでの条件は、要請する、と考える  
<a id="source-L256"></a>内積を使えば、ノルムを定義できるので、内積空間はノルム空間である  







<a id="source-L263"></a>

### 第11講


<a id="source-L265"></a>Banach空間:ノルム空間で完備  
<a id="source-L266"></a>Hirbert空間;内積空間で完備  
<a id="source-L267"></a>今回はRで考えるがCへの移行は容易である  



<a id="source-L271"></a>完備性の証明の定石  
<a id="source-L272"></a>Step1 収束先の候補xを探す  
<a id="source-L273"></a>Step2-1 xが元の空間に入ることを示す  
<a id="source-L274"></a>Step2-2 その空間の定義において列が収束先に収束する  

<a id="source-L276"></a>実数の完備性は知っていることにする  


<a id="source-L278"></a>

### 12.2 関数空間

<a id="source-L279"></a>定理12.1  
<a id="source-L280"></a>連続関数はBanach空間になる  

<a id="source-L282"></a>これで、連続関数について示したので、次は可測集合について示す。  

<a id="source-L284"></a>定義12.5 Lebesque空間  
<a id="source-L285"></a>L^p(E)では、f=g a.eの時fとgは等しいとみなす。つまり同値類の集合を考える。  
<a id="source-L286"></a>これは解析学では基礎的な役割を果たすのでどの教科書にも出てくる  
<a id="source-L287"></a>今回はこれがBanach空間であることを示して終わり。  
<a id="source-L288"></a>・がノルムになることを示す  

<a id="source-L290"></a>補題12.2 (Youngの不等式)これが準備1  
<a id="source-L291"></a>凸等式を用いる（イェンゼン不等式）  

<a id="source-L293"></a>補題12.3 (Holderの不等式)準備2  

<a id="source-L295"></a>補題12.4(Minkowskiの不等式)準備3  






<a id="source-L301"></a>

### 第12講 







<a id="source-L307"></a>

### 第13講 


<a id="source-L309"></a>一様有界性定理の証明はトリッキーで難しい  


<a id="source-L312"></a>試験は8:30でA4自筆1枚を持ち込み可  
<a id="source-L313"></a>試験はんいは中間レポートよりも後ろの部分（関数解析と線形要素解析）  



<a id="source-L317"></a>-----------------------------------------------------------  


<a id="source-L319"></a>

### 「Collatz(Functional Analysis) PDF」



<a id="source-L321"></a>

### 1 解析学の基本事項


<a id="source-L323"></a>定義1.1 最大値  

<a id="source-L325"></a>定理1.1 最大値の一意性  
<a id="source-L326"></a>最大値の定義から簡単に証明できる  

<a id="source-L328"></a>定義1.2  上限  

<a id="source-L330"></a>定理1.2 関節比較  

<a id="source-L332"></a>定理1.3 上限の一意性  
<a id="source-L333"></a>上限が存在しているとすると、その上限は一意的に決まる  
<a id="source-L334"></a>その上限をsupAとかく  

<a id="source-L336"></a>定義1.3 距離  

<a id="source-L338"></a>定義 1.4 anの収束  

<a id="source-L340"></a>定義1.5 Cauchy列  

<a id="source-L342"></a>定理1.4 数列の収束について  

<a id="source-L344"></a>定理1.6 compact性の遺伝  
<a id="source-L345"></a>連続関数fにおいて、compact集合の像はcompact集合である  

<a id="source-L347"></a>補題2  
<a id="source-L348"></a>fが連続関数であることを必要十分条件は位相を用いて定義される  
<a id="source-L349"></a>Heine-boreの定理も確かめておく  

<a id="source-L351"></a>系1 最大値・最小値の存在定理  
<a id="source-L352"></a>閉区間上で連続な関数において最大値・最小値が存在する  

<a id="source-L354"></a>定理1.7 f,gが連続関数とするときの性質  






<a id="source-L360"></a>

### 2 Banach空間



<a id="source-L362"></a>

### 2.1 線形空間

<a id="source-L363"></a>定義2.1 線形空間  
<a id="source-L364"></a>ある集合Xについて、和が一意に定まっており、積も一意に定まっているとき、線形空間という  

<a id="source-L366"></a>定理2.1  
<a id="source-L367"></a>線形空間をXとしたときの性質  

<a id="source-L369"></a>定義2.2 線型部分空間  

<a id="source-L371"></a>定義2.3 一次結合  

<a id="source-L373"></a>補題3  
<a id="source-L374"></a>SをXの部分集合とする  
<a id="source-L375"></a>Sの任意有限個の元の一次結合全体の集合をMとするとき、MはXの線型部分空間になる  
<a id="source-L376"></a>このMをSによって張られる線型部分空間という  

<a id="source-L378"></a>定理2.2  

<a id="source-L379"></a>

### 1.　Xの任意この線型部分空間の共通部分は再び１つの線型部分空間となる


<a id="source-L380"></a>

### 2.MをSによって張られる線型部分空間とすると、MはSを含む線型部分空間全体の共通部分となる


<a id="source-L382"></a>定義2.4 一次独立  

<a id="source-L384"></a>定義2.5 線形空間の次元  

<a id="source-L386"></a>補題4  
<a id="source-L387"></a>線形空間Vをn次元とするとき、n+1個の元は一時従属になる  

<a id="source-L389"></a>定理2.3 次元の一意性  




<a id="source-L393"></a>

### 2.2 Banach空間

<a id="source-L394"></a>定義2.6 ノルム空間  
<a id="source-L395"></a>ノルムの定まっている線形空間をノルム空間という  
<a id="source-L396"></a>ノルムは写像である  

<a id="source-L398"></a>定理2.4  
<a id="source-L399"></a>Vをノルム空間とする  
<a id="source-L400"></a>このときdをd:V\*V → ||x - y||と定めるとこれは距離関数になっている  
<a id="source-L401"></a>つまり、(V,d)は距離空間である  

<a id="source-L403"></a>補題5  
<a id="source-L404"></a>Xをノルム空間とする  

<a id="source-L405"></a>

### 1.収束Xの上の点列がxに収束する


<a id="source-L406"></a>

### 2.xnをX上の点列とする


<a id="source-L407"></a>

### 3.X0が集積点


<a id="source-L408"></a>

### 4.近傍


<a id="source-L409"></a>

### 5.稠密


<a id="source-L411"></a>定理2.5  
<a id="source-L412"></a>収束しているときの性質  

<a id="source-L414"></a>定義2.7 閉線型部分空間  

<a id="source-L416"></a>定理2.6  
<a id="source-L417"></a>Mをノルム空間Xの線型部分空間とするとMの閉包M-は閉線型部分空間になる  

<a id="source-L419"></a>定義2.8 Sによって張られる閉線型部分空間  

<a id="source-L421"></a>定義2.9 Cauchy列  

<a id="source-L423"></a>定義2.10 Banach空間  
<a id="source-L424"></a>ノルム空間X上の全てのCauchy列がX上に収束するとき完備であるといい、完備なノルム空間をBanach空間という  

<a id="source-L426"></a>定理2.7 Minkowski不等式  

<a id="source-L428"></a>主張  
<a id="source-L429"></a>ノルムをいつも見てる形で定めると、VnはR上のノルム空間になっていて、とくにBanach空間になっている  

<a id="source-L431"></a>主張 収束数列空間c  

<a id="source-L433"></a>主張 l^p空間  

<a id="source-L435"></a>主張 l∞空間  
<a id="source-L436"></a>実数列の中で有界なもの全体の集合をl∞空間という  

<a id="source-L438"></a>定理2.8 Jensenの不等式  

<a id="source-L440"></a>主張 L∞空間  

<a id="source-L442"></a>定義2.11 一様収束  

<a id="source-L444"></a>定理 2.9  
<a id="source-L445"></a>一様収束する関数列の極限関数は連続関数になっている  






<a id="source-L451"></a>

### 3 線型作用素



<a id="source-L453"></a>

### 3.1 線型作用素の定義


<a id="source-L455"></a>定義3.1 作用素  
<a id="source-L456"></a>X,Yを線形空間とし、DをXの部分集合とする  
<a id="source-L457"></a>このとき、f:D→f(x)  
<a id="source-L458"></a>を作用素という  

<a id="source-L460"></a>定義3.2 線型作用素  
<a id="source-L461"></a>線型写像のような性質のある作用素を線型作用素という  

<a id="source-L463"></a>主張  
<a id="source-L464"></a>作用素T:D → Yが線型作用素であるための必要十分条件は  

<a id="source-L466"></a>系2  
<a id="source-L467"></a>T:D→Yを線型作用素という  

<a id="source-L469"></a>定理3.1  
<a id="source-L470"></a>X,Yを線形空間とし、DをXの線型部分空間とする  
<a id="source-L471"></a>線型作用素をT:D→Yとすると、R(T)はY内の線型部分空間となる  




<a id="source-L475"></a>

### 3.2 連続性と有界性

<a id="source-L476"></a>定義3.3 連続/連続作用素  
<a id="source-L477"></a>X,Yをノルム空間とし、DをXのノルム部分空間とする  
<a id="source-L478"></a>またT:D→Yを線型作用素とする  

<a id="source-L480"></a>定義3.4 有界/有界作用素  

<a id="source-L482"></a>定理3.2  
<a id="source-L483"></a>X,Yをノルム空間とし、T: X → Yを線型作用素とすると次は同値である  

<a id="source-L484"></a>

### 1.Tはx0の一点で連続


<a id="source-L485"></a>

### 2.Tは連続作用素


<a id="source-L486"></a>

### 3.Tは有界作用素


<a id="source-L488"></a>定義3.5 有界線型作用素のノルム  

<a id="source-L490"></a>主張  
<a id="source-L491"></a>有界線型作用素において次が成り立つ  

<a id="source-L493"></a>定理3.3  
<a id="source-L494"></a>X0をノルム空間Xの稠密な線型部分空間とし、YをBanach空間とする  
<a id="source-L495"></a>T: X0 → Yを有界線型作用素とするとき、XからYへの有界作用素T-がただ１つだけ存在する  

<a id="source-L497"></a>定義3.6 逆作用素  
<a id="source-L498"></a>Dを線形空間Xの部分集とし、Yも線形空間とする  
<a id="source-L499"></a>作用素Tが一対一写像のとき、逆作用素が存在する  

<a id="source-L501"></a>定理3.4  
<a id="source-L502"></a>X,Yを線形空間とし、X0をXの線型部分空間とする  
<a id="source-L503"></a>線型作用素Tが逆作用素を持つ必要十分条件は  

<a id="source-L505"></a>系3  
<a id="source-L506"></a>T^-1が有界線型作用素になるための必要十分条件は  





<a id="source-L511"></a>

### 3.3 作用素の和と積

<a id="source-L512"></a>定義3.7 作用素の和と定数倍  

<a id="source-L514"></a>定義3.8 積  
<a id="source-L515"></a>X,Y,Zを線形空間とし、Tが  

<a id="source-L517"></a>主張  
<a id="source-L518"></a>STは線型作用素である  

<a id="source-L520"></a>補題6  
<a id="source-L521"></a>(1)T1, T2  
<a id="source-L522"></a>(2)T:X→Y, S:Y→Zを有界線型作用素とするとき  

<a id="source-L524"></a>定理3.5  
<a id="source-L525"></a>YがBanach空間であるときB(X,Y)もBanach空間になる  






<a id="source-L532"></a>———————————————————————————————————————————————————————————  




<a id="source-L536"></a>

### 「Collatz(Introduction of Analysis2) PDF」


<a id="source-L538"></a>定理・補題・系について  
<a id="source-L539"></a>いずれも大枠としては定理である  
<a id="source-L540"></a>定義した事柄から証明される内容  
<a id="source-L541"></a>次の定理の証明にだけ用いられるような定理を強調して補題という  
<a id="source-L542"></a>逆にある強力な定理を用いるとほとんど自動的に証明されるような定理を系という  
<a id="source-L543"></a>何を系と思い、何を補題とするかは著者の主義による部分も多い  


<a id="source-L545"></a>

### 1 解析における基本概念

<a id="source-L546"></a>数学というのは何を目的とするかでその導入方法が変わっていく  



<a id="source-L549"></a>

### 1.1 距離空間としての実数

<a id="source-L550"></a>極限操作を議論するために必要な道具として距離がある  
<a id="source-L551"></a>定義1.1 距離  

<a id="source-L553"></a>定理1.1  
<a id="source-L554"></a>d, d∞について  

<a id="source-L556"></a>PとP1の距離が0に近づいていく様子は２つの距離の測り方では同じということ  
<a id="source-L557"></a>位相空間として、２つの距離空間は同じである  

<a id="source-L559"></a>補題1  
<a id="source-L560"></a>R2上の２点の距離は、d1, d2, d∞においては平行移動しても不変である  

<a id="source-L562"></a>補題2  
<a id="source-L563"></a>距離関数の大小関係について  

<a id="source-L565"></a>定理1.2  
<a id="source-L566"></a>d1, d2, d∞がそれぞれ自然に定める位相は全て同相である。  



<a id="source-L569"></a>

### 1.2 数列の収束

<a id="source-L570"></a>定義1.2  
<a id="source-L571"></a>xy平面内の点列の収束について  

<a id="source-L573"></a>定理1.3  
<a id="source-L574"></a>点列がある点に収束することの必要十分条件はコーシーれつが収束すること  

<a id="source-L576"></a>定義1.3 関数の収束について  
<a id="source-L577"></a>極限操作とは「aではないa付近の世界の情報からf(a)の世界の情報を得る操作」である  




<a id="source-L581"></a>

### 1.3 最大値、上限

<a id="source-L582"></a>定理1.10 上限/下限の線形性  

<a id="source-L584"></a>定理1.11 上限/下限の線形性 続き  




<a id="source-L588"></a>

### 2 に変数以上の関数の微分


<a id="source-L589"></a>

### 2.1 連続関数

<a id="source-L590"></a>定義2.1 連続の定義  

<a id="source-L592"></a>定理2.1  
<a id="source-L593"></a>fが連続関数とすると、次が成り立つ  

<a id="source-L595"></a>定理2.2 最大値/最小値の定理  

<a id="source-L597"></a>系1  

<a id="source-L599"></a>定理2.3 連続関数の四則  

<a id="source-L601"></a>補題3 射影の連続性  
<a id="source-L602"></a>直積集合から、直積集合の元となる集合への写像を射影という  

<a id="source-L604"></a>系2  
<a id="source-L605"></a>任意の有理関数は連続である  

<a id="source-L607"></a>定義2.3 曲線  
<a id="source-L608"></a>R2の部分集合をDとする  
<a id="source-L609"></a>γがD曲線であるとは次の条件  

<a id="source-L611"></a>定義2.4 孤状連結  
<a id="source-L612"></a>R2内の部分集合Dが弧状連結であるとは、D内の任意の二点が曲線で結べることをいう  

<a id="source-L614"></a>補題4 直積写像の連続性  

<a id="source-L616"></a>定理2.4 中間値の定理  



<a id="source-L619"></a>

### 2.2 偏微分


<a id="source-L620"></a>

### 2.3 全微分


<a id="source-L621"></a>

### 2.4 極値


<a id="source-L622"></a>

### 2.5 陰関数








<a id="source-L629"></a>

### 3 二変数以上の関数の積分



<a id="source-L631"></a>

### 3.1 一変数の積分


<a id="source-L633"></a>高校数学では、微分するとf(x)になるものを原始関数といい、そのように積分を定めたのであるがこれは実用的ではない  
<a id="source-L634"></a>そこで、区分求積法の分割方法を任意というところまで条件を緩めて定義し直す  
<a id="source-L635"></a>この定義であれば、極限の存在の有無を用いて、積分不可能であることがより解析できることになるし、どのような関数が積分可能であるかもより詳しく見ていくことができる  




<a id="source-L639"></a>

### 3.2 二変数の積分


<a id="source-L641"></a>この補題は解析学ではよく使う評価方法である  

<a id="source-L643"></a>これで積分可能という定義と同値な条件を手に入れることができたので、どのような関数が具体的に積分可能か考えていく  

<a id="source-L645"></a>この定理は有限次元に限られた定理である  
<a id="source-L646"></a>より一般にはコンパクト集合（全有界かつ完備）な集合上では連続関数は一葉連続になる  

<a id="source-L648"></a>積分可能かどうかと一葉連続性は強く関係しあっている  

<a id="source-L650"></a>ここまでで、積分の定義と積分可能であるということをちゃんと導いたことになるが、積分を長方形上でしか定義できていないということに注意  
<a id="source-L651"></a>多変数となると、定義域が複雑な図形になるので、もう一度面積という言葉に立ち返って、どのようにして様々な定義域上で積分を考えられるのかを考える  




<a id="source-L655"></a>

### 3.3 面積


<a id="source-L657"></a>ニュートンやライプニッツが物理現象を説明するために微分と積分を定義したとき、積分というものに面積の概念はほとんど含まれていなかった  
<a id="source-L658"></a>その後Riemannが「グラフとx軸に囲まれた部分の面積とはその定積分に一致する」というのを定式化して明確な定義を与えるに至った  
<a id="source-L659"></a>Riemannが行った積分の定義は驚くべき有用でいくつかの未解決問題に対して直ちにその解を与えるに至った  
<a id="source-L660"></a>だが、Riemannの面積の定義はいくつかの点で不都合な問題があった  
<a id="source-L661"></a>Riemannの面積の定義は極限との相性が悪かった  
<a id="source-L662"></a>これを解決したのがLebesgueである  
<a id="source-L663"></a>Lebesgueは測度という概念を用いて定義し直した  

<a id="source-L665"></a>難しい定義を行うとそれと同等の同値な命題を必要とする  



<a id="source-L668"></a>

### 3.4 置換積分





<a id="source-L672"></a>

### 3.5 広義積分


<a id="source-L673"></a>

### 3.6 発展的話題







<a id="source-L679"></a>

### 4 曲面積/体積


<a id="source-L681"></a>曲線の長さの定義がこれであると思った方が良い  
<a id="source-L682"></a>いくらか短い直線に分けて、そこでピタゴラスの定理を用いてその短い直線の長さを総和を曲線の長さと定義する  

<a id="source-L684"></a>定義すると書いたが、実は証明できる  
<a id="source-L685"></a>証明の議論は結構微妙なので、もういっそ定義するとかいた  





<a id="source-L691"></a>——————————————————————  



<a id="source-L694"></a>

### 「Collatz(関数解析)」


<a id="source-L696"></a>・解析学の基本事項  
<a id="source-L697"></a>関数の性質を調べるのが解析学の目標である  
<a id="source-L698"></a>一個一個の関数を調べるのではなく、関数全体の集合を持ってきてその集合の性質を調べるのがてっとり早い  
<a id="source-L699"></a>まず、どこからどこへの関数によって変わる  
<a id="source-L700"></a>R→R  
<a id="source-L701"></a>R→C  
<a id="source-L702"></a>C→C  
<a id="source-L703"></a>さらにその定義域や地域の中で、連続関数や、C1級、、、、などいろいろな性質で関数が分けられる  
<a id="source-L704"></a>これらの関数全体の集合の性質を調べるのが目標  

<a id="source-L706"></a>知ってることとして、  
<a id="source-L707"></a>線形空間であることと、距離空間であることがわかる  
<a id="source-L708"></a>距離はいろいろなものを導入できて、理解しやすい距離を導入する  
<a id="source-L709"></a>R⇨Rなら、supf  
<a id="source-L710"></a>C→Cなら、exp(-w(s-t))など  

<a id="source-L712"></a>def：最大値  

<a id="source-L714"></a>def：上限  

<a id="source-L716"></a>def：距離を定義  

<a id="source-L718"></a>この講義では、Rとかけば距離が定まっているものとする  

<a id="source-L720"></a>def：数列の収束  

<a id="source-L722"></a>def：Cauchy列  


<a id="source-L725"></a>Rでは、Cauchy列であれば収束するものとする  
<a id="source-L726"></a>収束することを示したいときに、Cauchy列であることを示す方が楽である例がいくつも存在する  

<a id="source-L728"></a>{an},{bn}が、α,βに収束するならば、{an+bn}はα+βに収束する  
<a id="source-L729"></a>これは意外に、大事で、数列は線形空間に入っていることを主張している  
<a id="source-L730"></a>数列から定義される連続関数の自ずと線形空間と似たような性質を有することがわかる  

<a id="source-L732"></a>def：連続関数  

<a id="source-L734"></a>有限個しかない集合には最大値が存在する  
<a id="source-L735"></a>まあ、有限回大小比較をすれば良い  

<a id="source-L737"></a>定義域をRからCやQなどにすると、証明を書き直さなければならない  
<a id="source-L738"></a>ここで、例えば、Rの全ての性質を使ってしまうと、その全ての性質を新しい世界で確認しなければいけないが、実は、2つぐらいの性質しか使ってない場合もある  

<a id="source-L740"></a>連続関数を定義する  

<a id="source-L742"></a>最大値・最小値の存在定理  
<a id="source-L743"></a>ハイネボレルの被覆定理を用いて証明をする  
<a id="source-L744"></a>半分に分けて行って、一点に収束するという性質は別の性質で表現できる  
<a id="source-L745"></a>有界閉区間はコンパクト集合である、逆も成り立つ  
<a id="source-L746"></a>連続関数においてcompactの像は再びcompactである  
<a id="source-L747"></a>この二つを証明すれば最大値・最小値の存在定理になる  
<a id="source-L748"></a>この証明でも少し仮定を多くしてしまっている  

<a id="source-L750"></a>閉集合と完備は同値  
<a id="source-L751"></a>有界と全有界にはちょっとした差がある  

<a id="source-L753"></a>開集合の逆像が開集合になっていることと連続性は同値  

<a id="source-L755"></a>連続関数の性質  
<a id="source-L756"></a>連続関数全体の性質は体  

<a id="source-L758"></a>fは関数、f(x)は値としてみることもある  

<a id="source-L760"></a>sup(A+B) = supA + supBが成り立たないと、ノルム空間が定まらなくなってしまう  




<a id="source-L765"></a>・Banach空間の定義  

<a id="source-L767"></a>集合にある構造が定まったものを空間と呼ぶ  
<a id="source-L768"></a>Banach空間とは、数列や関数が存在する空間である  
<a id="source-L769"></a>関数が存在する空間ということは、線形空間であるということと、距離よりは少し弱いノルムというものを定義する  

<a id="source-L771"></a>和と積が一意に定まっているとき線形空間という  

<a id="source-L773"></a>R^nやC^nはR上線形空間  
<a id="source-L774"></a>連続関数全体の集合も線形空間  

<a id="source-L776"></a>def：線型部分空間  

<a id="source-L778"></a>def：一次結合  


<a id="source-L781"></a>補題  
<a id="source-L782"></a>SをXの部分集合とする  
<a id="source-L783"></a>Sの任意有限個の元の一次結合全体の集合をMとするとき、MはXの線型部分空間になる  
<a id="source-L784"></a>このMをSによって張られる線型部分空間という  
<a id="source-L785"></a>微分方程式の解はSによって張られる空間であり、  
<a id="source-L786"></a>Sの求め方が固有多項式というような、行列の固有値を求めるときと似たような計算が出てくる  
<a id="source-L787"></a>線型方程式は全て行列に書き直せ、行列の固有値がexpに乗っている  
<a id="source-L788"></a>つまり、その微分方程式によって指定される部分線形空間はその元が張る空間である  


<a id="source-L791"></a>定理  

<a id="source-L792"></a>

### 1 Xを任意個の線型部分空間の共通部分は再び線型部分空間となる

<a id="source-L793"></a>2 1よりMをSによって張られる線型空間とすると、MはSによって張られる線形空間とすると、MはSを含む  
<a id="source-L794"></a>つまりSによっては一意に定まる  

<a id="source-L796"></a>Mに入るのは無限個だが、Sは有限個なので、自分が調べたい空間に対して、それを張る部分集合が見つけられればそれを調べれば良い  

<a id="source-L798"></a>def：一次独立/一次従属  

<a id="source-L800"></a>def：線形空間の次元  

<a id="source-L802"></a>何個でも一次独立な元を用意できるとき、それを無限次元の線形空間という  
<a id="source-L803"></a>関数の空間は無限次元である  
<a id="source-L804"></a>行列が意味をなすのは有限次元である  

<a id="source-L806"></a>直観主義的数学には、背理法である排中律が存在しない  
<a id="source-L807"></a>代数学の基本定理は背理法で証明される  
<a id="source-L808"></a>直観主義の人たちには代数学の基本定理が証明できない  
<a id="source-L809"></a>ゲーデルの不完全性定理：証明の規則を決めてもその証明規則では証明できない命題が作れる  
<a id="source-L810"></a>ガロアは５次方程式の解は構成できないことを示したが、複素関数論では、limを使って表現できる  
<a id="source-L811"></a>直観主義数学は、実際に作って構成しないと認めないという数学だが、コンピューターが登場してから意味を持ち始めた  

<a id="source-L813"></a>大体代数学の自然数に関する命題は数学的帰納法で証明できる  
<a id="source-L814"></a>なぜなら、自然数の構成法に数学的帰納法が含まれているから  

<a id="source-L816"></a>n次元の線形空間で、n+1この元は線型従属になることを数学的帰納法で証明する  

<a id="source-L818"></a>次元の一意性を証明する  

<a id="source-L820"></a>これからは幾何学の話をする  

<a id="source-L822"></a>def：ノルム  
<a id="source-L823"></a>ノルムとは、距離よりも少し性質が厳しいものである  
<a id="source-L824"></a>絶対値のある意味の一般化である  
<a id="source-L825"></a>ベクトル空間の定義は、高校生はベクトルの向きと大きさが定まったものとしているが、ここではじめて大きさが定義される  
<a id="source-L826"></a>ノルムが定まると距離が定まる、距離が定まると数列のことを考える、数列を考えると完備かどうかを気にする  
<a id="source-L827"></a>完備な線形空間をBanach空間という  

<a id="source-L829"></a>ノルムの定まっている線形空間をノルム空間という  
<a id="source-L830"></a>Vをノルム空間とする、d:V✖️V→Rをd(x,y) = ||x - y||とすると、これは距離関数となり、(V,d)は距離空間となる  
<a id="source-L831"></a>分離公理が定まっているのでいくらか近傍に君は入ってこれない  

<a id="source-L833"></a>数列を無限個足すなんて無理なので、無限個足し合わせた結果を極限で定義しましょうということを言っている  

<a id="source-L835"></a>def：集積点  
<a id="source-L836"></a>点xがx0の集積点であるとは、x0の元を使ってxに収束するものを作れるということ  
<a id="source-L837"></a>触点であるのと同じ定義である  
<a id="source-L838"></a>これは解析的な定義である  

<a id="source-L840"></a>また、集積点全てからなる集合を閉包といい、x0にxo-となるx0を閉集合という  

<a id="source-L842"></a>近傍、開球を定義する  
<a id="source-L843"></a>開球の定義に=を踏めてはいけない  


<a id="source-L846"></a>def：開集合  

<a id="source-L848"></a>def：稠密  

<a id="source-L850"></a>def：有界  

<a id="source-L852"></a>ノルム空間についての点列の性質を証明する  

<a id="source-L854"></a>線形空間に幾何的な概念を導入したので、幾何的な定義なども考えていく  

<a id="source-L856"></a>def：閉線型部分空間  
<a id="source-L857"></a>自分の考えている集合が閉集合であることがわかったら、よくわからないことは起こらない  
<a id="source-L858"></a>点列という操作において統一した理論の中で話が済む  
<a id="source-L859"></a>例えば、開集合である有理数での点列から無理数が出てきてしまうが、それも含めて実数とすることで閉集合になる  
<a id="source-L860"></a>だから閉集合か開集合かを考えることは重要である  

<a id="source-L862"></a>閉ではないときはノルム空間の線型部分空間という  
<a id="source-L863"></a>閉線型部分空間は閉と言っている時点で、距離空間を考えているので、ノルムが定まっているという意味が含まれている  

<a id="source-L865"></a>Mをノルム空間Xの線型部分空間とすると、Mの閉包M-は閉線型部分空間になる  
<a id="source-L866"></a>縁のない集合が線型部分空間だったとすると、縁を込めても線型部分空間になるということ  

<a id="source-L868"></a>Sによって張られる線形空間Mの閉包をSによって張られる線型部分空間という  
<a id="source-L869"></a>Xの任意個の閉線型部分空間の共通部分わ再び閉線型部分空間になる  

<a id="source-L871"></a>def：ノルム空間上でCauchy列  
<a id="source-L872"></a>完備なノルム空間をBanach空間という  
<a id="source-L873"></a>閉集合は常に完備である  
<a id="source-L874"></a>Banach空間の閉線型部分空間はまたBanach空間になる  
<a id="source-L875"></a>完備かした結果線形性やノルムが壊れていないか証明しなければいけない  
<a id="source-L876"></a>Qを完備化するのは、1次元のBanach空間となる  
<a id="source-L877"></a>R\*に線形性を定めたものを、  
<a id="source-L878"></a>構成した立場からいったのと、定めたものと一致することを確認  

<a id="source-L880"></a>Minkouskiの不等式(Cauchy-Shwartzの定理の一般化)  
<a id="source-L881"></a>Youngの不等式から証明  
<a id="source-L882"></a>Youngの不等式は、凸解析や重み付きそうか相乗平均から証明する  
<a id="source-L883"></a>また、Minkowskiの不等式はΣを∫に書き換えても成り立つ  
<a id="source-L884"></a>ここでの積分はRiemann積分よりも広義の積分である  
<a id="source-L885"></a>これで、関数同士の距離（ノルム）が定まっている  
<a id="source-L886"></a>というのもこれは三角不等式の形なので  
<a id="source-L887"></a>p=2とすると、コーシーシュワルツの不等式  
<a id="source-L888"></a>これで定めた空間をLp空間という  
<a id="source-L889"></a>lp：離散  
<a id="source-L890"></a>Lp：連続  
<a id="source-L891"></a>L∞：supはルベーグ積分上のsupの意味  

<a id="source-L893"></a>これはLebesgue積分上のsupなので、少し意味が違う  
<a id="source-L894"></a>連続関数はL∞空間の閉線型部分空間なので、連続関数を見ている限り、変なことは出てこない  




<a id="source-L899"></a>・Banach空間の例  

<a id="source-L901"></a>n個の実数の組の全体からなる集合V^nにおいてノルムを定義する  
<a id="source-L902"></a>このとき、V^nはR上のノルム空間になっている  
<a id="source-L903"></a>特にBanach空間になっている  
<a id="source-L904"></a>Cauchy列を改訂して、どんなCauchy列も収束先をR^nの内部に持つことを証明する  

<a id="source-L906"></a>収束数列空間cは、||x|| = sup(数列)とするとBanach空間となっている  
<a id="source-L907"></a>前と同様に完備であることを証明する  

<a id="source-L909"></a>絶対収束するもはこう別積分できる、また項別微分できる  
<a id="source-L910"></a>一様収束しているかどうかは絶対収束しているかどうかみれば良い  

<a id="source-L912"></a>lp空間：実数列の中で和が絶対収束しているものの全体の集合  
<a id="source-L913"></a>l∞空間：実数列の中で有界なもの全体の集合  

<a id="source-L915"></a>イェンゼンの不等式  

<a id="source-L917"></a>ここまでが数列空間  

<a id="source-L919"></a>ここからは関数空間  
<a id="source-L920"></a>R上の\[a,b\]で定義された連続関数全体の集合をCと書く  
<a id="source-L921"></a>これは線形空間である  
<a id="source-L922"></a>また、最大値最小の存在値定理から、||f|| = sup(f(x))とすると、ノルムを定めている  
<a id="source-L923"></a>特にBanach空間になっている  
<a id="source-L924"></a>完備であることを示す  


<a id="source-L927"></a>def：（狭義）一様収束  
<a id="source-L928"></a>一様収束は、論理式で命題を書けば、各点収束よりもNを作る材料が少ないことがわかる  
<a id="source-L929"></a>一般に関数列の収束先を極限関数という  


<a id="source-L932"></a>一様収束する関数列の極限関数は連続関数になっている  

<a id="source-L934"></a>これから、次のことが出てくる  
<a id="source-L935"></a>{fn}が一様収束かつ絶対収束しているとき、  
<a id="source-L936"></a>項別積分可能である  


<a id="source-L939"></a>Taylor展開を、1,x,x^2という基底ベクトルの和で書けるという見方も出来る  
<a id="source-L940"></a>だが、これらの基底はどんな内積を定めても直交基底ではない  

<a id="source-L942"></a>ヒルベルト空間は、線形空間で内積も定義されている、いわゆるBanach空間の特殊な場合  

<a id="source-L944"></a>フーリエ変換は、正規直交基底で全ての関数を書こうとしている  
<a id="source-L945"></a>ヒルベルト空間の理論である  
<a id="source-L946"></a>定数関数も、パルス波も、普通の関数もかける  
<a id="source-L947"></a>それが正しいかどうかを調べるために関数解析が発展した  
<a id="source-L948"></a>そして、フーリエ級数をオイラーの式で書き直すと、複素解析の技を使うことができるようになり、調和関数である  
<a id="source-L949"></a>ことがわかり、フーリエ級数展開可能であることがわかる  
<a id="source-L950"></a>オイラーの公式で複素解析とフーリエ変換がつながっている  
<a id="source-L951"></a>調和関数はフーリエ解析可能で、フーリエ解析可能な関数は調和関数に限る  

<a id="source-L953"></a>ある点の周りの周積分は、その周りの平均をとっているという意味になる  
<a id="source-L954"></a>その点が平均値であるとき、その関数は平均的であるという  





<a id="source-L960"></a>・線形作用素の連続・有界  
<a id="source-L961"></a>Banach空間の間に定義される写像について  

<a id="source-L963"></a>関数が所属している空間と別の空間との写像を考えたい、定義域の元が写像なので、それも写像と呼ぶのは紛らわしいので線形空間で定義される写像のことは作用素という  

<a id="source-L965"></a>X,Yを線形空間とし、DをXの部分集合とするこのとき  
<a id="source-L966"></a>f: D:x → f(x):Y  
<a id="source-L967"></a>を作用素という  
<a id="source-L968"></a>DをD(f),fの値域をR(f)とかく  
<a id="source-L969"></a>また、単射のとき一対一であるといい、fが全射のとき、上への作用素であるという  
<a id="source-L970"></a>f:A→Bなる写像を考えたとき、新たな写像をg:A→f(A)とすると、gは全射となる  
<a id="source-L971"></a>つまり、全射は定義域と値域に依存するけっこう曖昧な性質である  

<a id="source-L973"></a>線型作用素とは、線型写像の性質を満たすような作用素  

<a id="source-L975"></a>線型作用素は線形性を保つ写像なので、地域が線型部分空間なら、R(T)も線型部分空間となる  

<a id="source-L977"></a>これからは作用素の連続性というものを考える  
<a id="source-L978"></a>定義域の連続性を担保するのはどんな性質があるのかを考えていく  
<a id="source-L979"></a>また、それが簡単な形に書き換えられないかを考えていく  
<a id="source-L980"></a>実は連続性と有界性が一緒であることが証明される  

<a id="source-L982"></a>連続・連続作用素  
<a id="source-L983"></a>X,Yをノルム空間とし、点列の像の極限は、点列の極限の像としてオーソドックスな定義をする  

<a id="source-L985"></a>これと以下の命題が同値であることを証明する  
<a id="source-L986"></a>世の中には連続の度合いによっていくつかの定義がある  
<a id="source-L987"></a>・連続  
<a id="source-L988"></a>・一様連続  
<a id="source-L989"></a>・ヘルダー連続  
<a id="source-L990"></a>・リプシッツ連続  
<a id="source-L991"></a>三角関数はリプシッツ連続である  

<a id="source-L993"></a>リプシッツ連続であるとき、作用素Tは有界であるという  
<a id="source-L994"></a>次は同値  
<a id="source-L995"></a>・Tは1点で連続  
<a id="source-L996"></a>・Tは連続作用素  
<a id="source-L997"></a>・Tは有界作用素  
<a id="source-L998"></a>これはだいぶ強い条件  
<a id="source-L999"></a>複素関数は有界であれば定数関数  
<a id="source-L1000"></a>線型作用素は一点で決まると、そこに乗っている直線の性質は全て決まってくる  

<a id="source-L1002"></a>有界線型作用素のノルムを定義する  
<a id="source-L1003"></a>リプシッツ連続の定義から、定義できる  

<a id="source-L1005"></a>定義域は全領域なのに、円周上だけを考えるだけで、ノルムが定まるというすごいことを言っている  

<a id="source-L1007"></a>微分も線型作用素である  
<a id="source-L1008"></a>積分も線型作用素の一種  

<a id="source-L1010"></a>X0をノルム空間Xの稠密な線型部分空間とし、YをBanach空間とする  
<a id="source-L1011"></a>T：X0→Yを有界線型作用素とするとき、XからYの有界線型作用素Tがただ一つ存在する  




<a id="source-L1016"></a>・逆作用素・Banach環（見直すとしたらここらへんからが良さそう）  

<a id="source-L1018"></a>写像でいう逆写像が逆作用素と呼ばれる  
<a id="source-L1019"></a>作用素が一対一写像のとき逆作用T-1が定まる  

<a id="source-L1021"></a>線型作用素Tが逆作用素を持つ必要十分条件  

<a id="source-L1023"></a>T-1が有界線型作用素になるための必要十分条件  

<a id="source-L1025"></a>作用素の和と積  

<a id="source-L1027"></a>線型作用素全体の集合は線形空間をなす  

<a id="source-L1029"></a>合成写像のようなものを定義する  

<a id="source-L1031"></a>和と積のノルムを定義する  

<a id="source-L1033"></a>有界線型作用素全体の集合に作用素ノルムを定めたものはノルム空間になっている！  
<a id="source-L1034"></a>じゃあ完備性は？  

<a id="source-L1036"></a>YがBanach空間であるとき、B(X,Y)もBanach空間となる  

<a id="source-L1038"></a>ノルム空間XからXへの有界線型作用素全体の集合を特にB(X)  
<a id="source-L1039"></a>前定理より、X自身がBanach空間であればB(X)はBanach空間になる  

<a id="source-L1041"></a>線形空間は加法群の定義を満たす  
<a id="source-L1042"></a>群に足し算を引き算が定まるとき群という  
<a id="source-L1043"></a>整数は群であり、環である  
<a id="source-L1044"></a>掛け算が定まると環である  
<a id="source-L1045"></a>割り算が定まると体になる  

<a id="source-L1047"></a>B(X)はbanach Algebraになる（Banach環）  

<a id="source-L1049"></a>作用素の指数を定義する  

<a id="source-L1051"></a>ノイマンの級数  
<a id="source-L1052"></a>ノルムを測るというのは関数がどれだけ近いかを測っている  
<a id="source-L1053"></a>陰関数定理のようなもの  




<a id="source-L1058"></a>・一様有界性定理  

<a id="source-L1060"></a>フーリエ解析を理解するためにはbanach空間では少し足りないので、公理を付け加えてヒルベルト空間を考える  
<a id="source-L1061"></a>Pn(R)はn次以下の多項式全体の集合  
<a id="source-L1062"></a>だが、多項式ではどうしようもないので、  
<a id="source-L1063"></a>(1,x,x^2,,,)という基底を取り、多項式とベクトルと同一視する  
<a id="source-L1064"></a>つまり、R^nに同一視してその特性を調べるのが線形代数の目的である  
<a id="source-L1065"></a>例えば、基底をルジャンドル多項式でとると直交する基底になることがわかる  

<a id="source-L1067"></a>だが、関数空間を同一視するためにはR^∞が必要となるので、これは数列を同一視する  
<a id="source-L1068"></a>フーリエ解析可能なのは、L^2空間である  
<a id="source-L1069"></a>l^2空間に必要な性質は可分であること  
<a id="source-L1070"></a>ここで、sinやcosをとると、有限次元で相当するルジャンドル多項式のようなものが出てくる  

<a id="source-L1072"></a>BaireのCategory定理  
<a id="source-L1073"></a>(X,d)を完備な距離空間とする  
<a id="source-L1074"></a>Xの可算個の閉部集合{Xn}がXを被っているならば、少なくとも１つあるてんのある近傍を含む  

<a id="source-L1076"></a>一様有界性定理  
<a id="source-L1077"></a>XをBanach空間、Yをnorm空間とし、Aを無限集合とする  
<a id="source-L1078"></a>一様に収束すると、項別微分や項別積分ができる  

<a id="source-L1080"></a>これは結構すごい定理である  
<a id="source-L1081"></a>一様収束性定理はBaireのCategory定理を使って証明する  

<a id="source-L1083"></a>系1  

<a id="source-L1085"></a>上極限と下極限は色々と定義がある  
<a id="source-L1086"></a>lim sup an = inf(sup ak)  
<a id="source-L1087"></a>単調減少数列のinfをみるということは、その収束先を見るということ  
<a id="source-L1088"></a>{an}の部分列で収束するものを全て構成し、その収束先の集合を集積集合という  
<a id="source-L1089"></a>形式的に∞や-∞を含めても良い  
<a id="source-L1090"></a>その収束集合の最大値という定義の仕方もある  

<a id="source-L1092"></a>Banach-Steinhousの定理  
<a id="source-L1093"></a>X,Yをbanach空間とし、{Tn}をXからYへの有界線型作用素の列とする  
<a id="source-L1094"></a>X0をXの稠密部分空間とし、(ry  




<a id="source-L1099"></a>・開写像定理  

<a id="source-L1101"></a>開写像の像が開集合になるのが開写像  
<a id="source-L1102"></a>向こうの情報を戻せるのが連続  
<a id="source-L1103"></a>Banach空間では一様有界なら開写像である  

<a id="source-L1105"></a>-  

<a id="source-L1107"></a>開写像定理  
<a id="source-L1108"></a>X,YをBanach空間とし、T：X→Yを有界線型作用素とする  
<a id="source-L1109"></a>このとき、集合族の集合oに対して、T(0)はYの開集合族に含まれる  

<a id="source-L1111"></a>X,YをBanach空間とし、T：X→Yを一対一、上への有界線型作用素とする  
<a id="source-L1112"></a>このとき、T-1は有界線型作用素となる  

<a id="source-L1114"></a>一対一、上への線型有界作用素があれば、どのbanach空間は同相であることがわかる  
<a id="source-L1115"></a>開写像定理はたくさんの応用がある  
<a id="source-L1116"></a>複素関数でいうと、正則関数は開写像定理を  




<a id="source-L1121"></a>・閉グラフ定理  

<a id="source-L1123"></a>閉作用素というものを考える  
<a id="source-L1124"></a>考える妥当性を議論する  

<a id="source-L1126"></a>Xを線形空間としNormを||・||xとかく  
<a id="source-L1127"></a>(X, ||・||x)でbanach空間とする  
<a id="source-L1128"></a>T：X→Yが線型作用素  
<a id="source-L1129"></a>Xのnormとして、次のようなものを考える  
<a id="source-L1130"></a>像のほうの条件をnormの定理に使うとき、グラフノルムという  
<a id="source-L1131"></a>もし(X, ||・||y)がBanach空間なら有界  

<a id="source-L1133"></a>距離を取り替えているので、いくつか注意しなければいけないことがある  

<a id="source-L1134"></a>

### 1.完備かどうか


<a id="source-L1135"></a>

### 2.同相かどうか

<a id="source-L1136"></a>つまり、同相な空間であれば、実はその空間に適したノルムを入れてやればよかったということがわかる  
<a id="source-L1137"></a>1と2を満たすような作用素を考えるときに閉作用素や閉グラフ定理がある  

<a id="source-L1139"></a>直積空間を定義する  
<a id="source-L1140"></a>直積集合に演算を定めると直積空間になる  
<a id="source-L1141"></a>Zornの補題：どの部分集合を見ても有界になっている集合があればそれは極大元が存在する  

<a id="source-L1143"></a>グラフ/閉作用素  
<a id="source-L1144"></a>X,YをNorm空間とし、T：線型作用素がD(T)  
<a id="source-L1145"></a>G(T)がX×Y上の閉集合となるとき、Tを閉作用素という  

<a id="source-L1147"></a>閉集合は大切である  
<a id="source-L1148"></a>コンパクト性や完備性を写すことができる  
<a id="source-L1149"></a>ハウスドロフ空間のコンパクト集合は閉集合に限る  
<a id="source-L1150"></a>コンパクト空間の閉集合は再びコンパクトになる  

<a id="source-L1152"></a>閉作用素の必要十分条件  
<a id="source-L1153"></a>定義域上の点列が収束している  
<a id="source-L1154"></a>点列の像からできる点列が収束している  

<a id="source-L1156"></a>\[0,1\]上で定義される一回微分可能で導関数が連続なる関数空間から同館σぬうを対応される作用素は閉作用素  
<a id="source-L1157"></a>微分作用素は線型作用素  

<a id="source-L1159"></a>X,YをNorm空間とし  

<a id="source-L1161"></a>閉グラフ定理  
<a id="source-L1162"></a>X,YをBanach空間とし、Tを閉作用素とする  
<a id="source-L1163"></a>このときD(T) = XならばTは有界線型作用素である  

<a id="source-L1165"></a>閉作用素をどの範囲で考えるかが重要になってくる  
<a id="source-L1166"></a>閉作用素性を壊さずに定義域を拡張できるなら拡張しても良い  
<a id="source-L1167"></a>定義域をいじれば、閉作用素は有界線型作用素になるという主張  






<a id="source-L1174"></a>———————————————————————————————————————————————————————————  


<a id="source-L1176"></a>

### 「関数解析について」


<a id="source-L1178"></a><http://watanabeckeiich.hatenablog.com/entry/2017/09/01/202658>  

<a id="source-L1180"></a>関数解析は無限次元の線形代数と呼ばれる  
<a id="source-L1181"></a>線形代数では、行列の成分が定数であったが、成分が微分とかになった場合でも線形代数と同様の理論は成り立つのか？というのが関数解析のモチベーションである  
<a id="source-L1182"></a>関数解析は無限次元のベクトル空間を扱う  
<a id="source-L1183"></a>大雑把にいうと、関数解析には線形代数になかった操作、例えば微分などがあるために線形代数では成り立っていたことが成り立たないという問題が発生する  
<a id="source-L1184"></a>それを解決するのがコンパクトという概念である  
<a id="source-L1185"></a>今までよく使っていた位相が強すぎることがあるので、弱位相が登場し、弱収束などを学ぶ  

<a id="source-L1187"></a>・Banach空間とは  
<a id="source-L1188"></a>Banach空間とは完備なノルム空間である  
<a id="source-L1189"></a>なぜ完備性を仮定するのかというと、完備性は非線形偏微分方程式の解の存在を保証するからである  
<a id="source-L1190"></a>まずはBanach空間の理論を理解することが大切  

<a id="source-L1192"></a>・どの順に勉強すれば良いのか  
<a id="source-L1193"></a>-Banach空間  
<a id="source-L1194"></a>Banach空間の具体例にたくさん触れたい  
<a id="source-L1195"></a>まずは、数列空間についての理解と、そこで出てくる不等式の評価のテクニックを勉強  
<a id="source-L1196"></a>Minkowskiの不等式や、Jesnsenの不等式など有名な不等式を覚える  

<a id="source-L1198"></a>-ルベーグ空間  
<a id="source-L1199"></a>ヒルベルト空間よりもまずはルベーグ空間を勉強したい  
<a id="source-L1200"></a>ここでは、測度論やルベーグ積分の知識が必要となる  

<a id="source-L1202"></a>-ヒルベルト空間  
<a id="source-L1203"></a>ヒルベルト空間は特別な空間  
<a id="source-L1204"></a>ヒルベルト空間の最大の特徴は内積を考えられるということ  
<a id="source-L1205"></a>まずはシュワルツの不等式の証明ができることをゴールに切り上げるべき  

<a id="source-L1207"></a>-線形作用素  
<a id="source-L1208"></a>作用素のノルムについて、有界性についてたくさん学ぶ  
<a id="source-L1209"></a>ゴールは、Barieのカテゴリー定理と閉鎖要素を理解することである  

<a id="source-L1211"></a>-線形汎関数  
<a id="source-L1212"></a>Hahn-Banachと共役作用素を学ぶ  

<a id="source-L1214"></a>-レゾルベントとスペクトル  
<a id="source-L1215"></a>レゾルベントとスペクトルの違いは分かるようになるべき  
<a id="source-L1216"></a>ここでは、方程式を解くためのテクニックを習得する  
<a id="source-L1217"></a>スペクトルは固有値のイメージ  

<a id="source-L1219"></a>-フーリエ解析  
<a id="source-L1220"></a>留数定理を復習  
<a id="source-L1221"></a>微分が多項式に変わるフィーリングを掴む  
<a id="source-L1222"></a>ラプラス変換も理解したい  
<a id="source-L1223"></a>ラプラス変換とレゾルベントの関連を見出す  

<a id="source-L1225"></a>-コンパクト作用素  
<a id="source-L1226"></a>コンパクトがガッツリ出てくる  
<a id="source-L1227"></a>コンパクトの定義、Ascoli-Arzelaの定理  
<a id="source-L1228"></a>コンパクト作用素の導入  
<a id="source-L1229"></a>ソボレフ空間、特にソボレフの埋蔵定理を理解したい  
<a id="source-L1230"></a>コンパクト性という強い性質を考えてるので、線形代数と似たような結果が出てくる  
<a id="source-L1231"></a>Riez-Schauderの定理まで勉強すべき  

<a id="source-L1233"></a>-半群  
<a id="source-L1234"></a>熱半群ぐらいはマスターしたい  
<a id="source-L1235"></a>これまでに勉強したことがたくさん出てくる  
<a id="source-L1236"></a>ヒレ・吉田の定理と、解析半群は何かということを他人にスラスラ説明できるようになるべき  



<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

「Cauchy列だから収束する」と言うには、扱う空間の完備性が必要。Banach空間は完備なノルム空間、Hilbert空間は内積からのノルムで完備な空間である。作用素を扱うときは定義域も対象の一部として記す。無限次元では、どのノルムや収束を使うかを省略できない。本文末尾の半群・熱半群への関心は、途中の空間論とつなぐ再開点として残す。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [微分積分学](calculus.md)
- [集合と位相](../foundations/sets-and-topology.md)
- [多様体論入門](../geometry/introduction-to-manifolds.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
