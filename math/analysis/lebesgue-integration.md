---
title: "ルベーグ積分"
status: draft
tags: [scrapbox, analysis]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E3%83%AB%E3%83%99%E3%83%BC%E3%82%B0%E7%A9%8D%E5%88%86"
source_created: "2023-01-21T18:33:37Z"
source_updated: "2023-02-01T03:37:45Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# ルベーグ積分

集合の大きさを測る発想から、収束と積分の交換へ進む記録。

原ページ作成：2023-01-21 ／ 最終更新：2023-02-01（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/lebesgue-integration.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E3%83%AB%E3%83%99%E3%83%BC%E3%82%B0%E7%A9%8D%E5%88%86)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<details>
<summary>本文の見出しから探す</summary>

- [「よくわかる測度論とルベーグ積分」](#source-L5)
- [0.測度論の心](#source-L10)
- [1.測度の定義](#source-L20)
- [2.ルベーグ積分の定義](#source-L35)
- [3.重要な定理](#source-L56)
- [4.終わりに](#source-L71)
- [「Lebesgue Integral(Collatz PDF)」](#source-L80)
- [1 測度論](#source-L82)
- [1.1  実数の構成](#source-L87)
- [1.2 集合列](#source-L91)
- [1.3 集合体](#source-L94)
- [1.4 測度](#source-L97)
- [2 Lebesgure積分論](#source-L101)
- [2.1 Lebesgue測度](#source-L102)
- [2.2 Borel集合](#source-L112)
- [2.3 可測関数](#source-L116)
- [2.4 階段関数](#source-L120)
- [2.5 Lebesgue積分](#source-L123)
- [2.6 Lebesgueの単調収束定理](#source-L126)
- [2.7 Lebesgueの優収束定理](#source-L129)
- [2.8 Lebesgue積分とLiemann積分の関係](#source-L132)
- [2.9 複素数値関数の積分](#source-L136)
- [3 L^2空間](#source-L141)
- [3.1 L^2空間の定義と構成](#source-L142)
- [3.2 直交基底の定義と性質](#source-L143)
- [3.3 Dirichlet核の定義](#source-L144)
- [3.4 fourier級数の各点収束](#source-L145)
- [「ルベーグ積分—面積とは何か？—」](#source-L152)
- [「測度論のお気持ちを最短で理解する」](#source-L192)
- [「測度論-Wikipedia-」](#source-L224)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### ルベーグ積分


<a id="source-L3"></a><http://watanabeckeiich.hatenablog.com/entry/2016/10/08/214834>  


<a id="source-L5"></a>

### 「よくわかる測度論とルベーグ積分」


<a id="source-L7"></a>測度論は解析系や統計系では必須の道具である  
<a id="source-L8"></a>Fubiniの定理、単調収束定理、ルベーグの収束定理、積分記号下での微分をゴールに解説する  


<a id="source-L10"></a>

### 0.測度論の心


<a id="source-L12"></a>ざっくりいうと、測度論の試みは集合のサイズを測ることである  
<a id="source-L13"></a>そのサイズの性質や測り方を数学的に厳密に考えようというのが測度論である  
<a id="source-L14"></a>その測度論を基礎に作られたのがルベーグ積分である  
<a id="source-L15"></a>ルベーグ積分ではヘンテコな関数も積分できることになる  
<a id="source-L16"></a>例えば、2重積分の積分順序を変更する際、リーマン積分の時よりもチェックすべき条件が簡単になる  




<a id="source-L20"></a>

### 1.測度の定義

<a id="source-L21"></a>測度とは集合のサイズである  
<a id="source-L22"></a>測度の定義の前に、測る集合族の性質（完全加法族）を定める  
<a id="source-L23"></a>これを定めておくことでいろいろな議論がスムーズにいく  

<a id="source-L25"></a>1-1 完全加法族(σ加法族)  

<a id="source-L27"></a>1-2 測度  

<a id="source-L29"></a>1-3 測度空間  

<a id="source-L31"></a>1-4 測度の性質  




<a id="source-L35"></a>

### 2.ルベーグ積分の定義

<a id="source-L36"></a>高校までのリーマン積分では、考える領域を短冊のように細かく縦に分割することで積分を定義した  
<a id="source-L37"></a>一方でルベーグ積分は考える領域を玉ねぎのように横にスライスし、分割することで積分を定義する  
<a id="source-L38"></a>つまり、ルベーグ積分では定義域ではなく、値域を分割する  
<a id="source-L39"></a>こうすることで、定義域が無理数のような変な関数もきちんと積分できるようになる  

<a id="source-L41"></a>本来なら、ルベーグ積分に入る前に、外測度やルベーグ測度や可測関数などについて色々学習しなければいけないが、先ほどの測度の性質さえわかっていればなんとかなるので省略する  

<a id="source-L43"></a>2-1 特性関数  

<a id="source-L45"></a>2-2 階段関数  

<a id="source-L47"></a>2-3 ルベーグ積分の定義  

<a id="source-L49"></a>2-4 リーマン積分とルベーグ積分の関係  

<a id="source-L51"></a>2-5 almost everywhere  





<a id="source-L56"></a>

### 3.重要な定理

<a id="source-L57"></a>それぞれの定理の証明はとても難しいのでここでは省略する  

<a id="source-L59"></a>3-1 ルベーグの収束定理  

<a id="source-L61"></a>3-2 単調収束定理  

<a id="source-L63"></a>3-3 積分記号下での微分  

<a id="source-L65"></a>3-4 Fubiniの定理  






<a id="source-L71"></a>

### 4.終わりに

<a id="source-L72"></a>測度論の講義がFubiniの定理などの重要な定理の紹介や使い方で終わることが多い  
<a id="source-L73"></a>Fubiniの定理の後に続く発展的な事項としてはRandon-Nikodymの定理  
<a id="source-L74"></a>解析系なら、Lebesqe空間やSobelov空間の理論やBochner積分、統計系なら確率論などがあげられる  



<a id="source-L78"></a>———————————————————————————————————————————————————  


<a id="source-L80"></a>

### 「Lebesgue Integral(Collatz PDF)」



<a id="source-L82"></a>

### 1 測度論


<a id="source-L84"></a>Dirichlet関数のような関数はRiemann積分では積分不可能であるが、Lebesgue積分では積分可能なのである  
<a id="source-L85"></a>この違いに答えるのがLebesgue積分を学ぶ中で大切な測度、Lebesgue測度という概念である  


<a id="source-L87"></a>

### 1.1  実数の構成


<a id="source-L89"></a>集合・位相を参照  


<a id="source-L91"></a>

### 1.2 集合列




<a id="source-L94"></a>

### 1.3 集合体




<a id="source-L97"></a>

### 1.4 測度





<a id="source-L101"></a>

### 2 Lebesgure積分論


<a id="source-L102"></a>

### 2.1 Lebesgue測度



<a id="source-L105"></a>Riemann級数和に対する収束定理は非常に強力な定理  
<a id="source-L106"></a>絶対収束しないならば、和の順序を入れ替えることで上極限及び下極限を任意の値に収束させることができるというものである  
<a id="source-L107"></a>牛腸先生が言っていたやつや！  





<a id="source-L112"></a>

### 2.2 Borel集合





<a id="source-L116"></a>

### 2.3 可測関数





<a id="source-L120"></a>

### 2.4 階段関数




<a id="source-L123"></a>

### 2.5 Lebesgue積分




<a id="source-L126"></a>

### 2.6 Lebesgueの単調収束定理




<a id="source-L129"></a>

### 2.7 Lebesgueの優収束定理




<a id="source-L132"></a>

### 2.8 Lebesgue積分とLiemann積分の関係





<a id="source-L136"></a>

### 2.9 複素数値関数の積分






<a id="source-L141"></a>

### 3 L^2空間


<a id="source-L142"></a>

### 3.1 L^2空間の定義と構成


<a id="source-L143"></a>

### 3.2 直交基底の定義と性質


<a id="source-L144"></a>

### 3.3 Dirichlet核の定義


<a id="source-L145"></a>

### 3.4 fourier級数の各点収束





<a id="source-L150"></a>———————————————————————————————————————————————————————  


<a id="source-L152"></a>

### 「ルベーグ積分—面積とは何か？—」


<a id="source-L154"></a><https://www.youtube.com/watch?v=D1alpuVt-gs>  


<a id="source-L157"></a>曲面で囲まれたものであればRiemann積分で求められる  

<a id="source-L159"></a>ルベーグ積分では点で囲まれた領域も面積が求められる  

<a id="source-L161"></a>積分可能と原始関数が存在することは無関係  

<a id="source-L163"></a>リーマン積分可能であることとリーマン和が収束することは同値  

<a id="source-L165"></a>リーマン積分可能であるための必要十分条件はほとんど至る所で連続  

<a id="source-L167"></a>ディレクれ関数は極限を使った式で表すことができる  

<a id="source-L169"></a>ルベーグ積分を一言でいうと、たてのものを横にすることである  

<a id="source-L171"></a>Siの計測がルベーグ測度である  


<a id="source-L174"></a>測度とは面積・体積を一般化したもの  

<a id="source-L176"></a>測度0の集合をゼロ集合という  

<a id="source-L178"></a>ゼロ集合を取り除いても測度は変わらない  

<a id="source-L180"></a>可算集合はゼロ集合である  

<a id="source-L182"></a>非可算集合にもゼロ集合は存在する（非可算集合であるゼロ集合の１つがカントール集合）  


<a id="source-L185"></a>ルベーグ積分不可能でも、広義リーマン積分可能な関数は存在する  


<a id="source-L188"></a>————————————————————————————————————————————————————————————  

<a id="source-L190"></a><https://qiita.com/mo-mo-666/items/731bf1d58a7720aa7739>  


<a id="source-L192"></a>

### 「測度論のお気持ちを最短で理解する」


<a id="source-L194"></a>\[0,1\]上で定義された1\_Qという関数はリーマン積分できないことを確認した  
<a id="source-L195"></a>しかし、この関数はあとで定義するルベーグ積分はできる  

<a id="source-L197"></a>測度とは、長さや面積の重み付である  
<a id="source-L198"></a>そして測度はちゃんと積分の概念が広がるような性質の良いものであるとする  

<a id="source-L200"></a>リーマン積分可能な関数はルベーグ積分しても同じ値になるので慣習で同じ記号が使われる  

<a id="source-L202"></a>almost everywhereという考え方  
<a id="source-L203"></a>面積の重みを定式化することで重みゼロという概念についても考えることができるようになる  
<a id="source-L204"></a>重みゼロの部分はテキトーにいじっても全体の面積に影響を及ぼさない  


<a id="source-L207"></a>実は無理数の数は有理数の数より圧倒的に多い  
<a id="source-L208"></a>ルベーグ測度で測ると、有理数の集合には面積の重みがないことがいえる  

<a id="source-L210"></a>ルベーグ積分は横に切るとよく言われる  
<a id="source-L211"></a>横にきるイメージを持つのはほとんど意味がない  

<a id="source-L213"></a>今までは面積の重みづけと言っていたが、ルベーグ測度では厳密には長さの重み付けである  

<a id="source-L215"></a>積分の概念を広げたことによるメリット  
<a id="source-L216"></a>・limと積分の交換が容易  
<a id="source-L217"></a>・重みをいじることができる  




<a id="source-L222"></a>——————————————————————————————————————————  


<a id="source-L224"></a>

### 「測度論-Wikipedia-」


<a id="source-L226"></a>測度論は数学の実解析における一分野で測度とそれに関連する概念(完全加法族、可測関数、積分)などを研究する  
<a id="source-L227"></a>測度とは、面積、体積、個数といった大きさに関する概念を精緻化したものである  

<a id="source-L229"></a>また、測度の概念は確率を数学的に定式化する際にも用いられるため（コルモゴロフの公理）、確率論や統計学においても測度論は重要である  

<a id="source-L231"></a>与えられた集合上の測度は２段階のステップで定義される  
<a id="source-L232"></a>(1)その集合の部分集合で測度が定義可能なもの（可測集合）はどれであるかを決めて、次にそれらの部分集合に対して具体的に測度を定義する  

<a id="source-L234"></a>測度の定義は操作的・形式的に与えられ、必要とされる要件は空集合の測度が0であることとnこのdisjointな集合の測度の和がそれらの集合の和集合の測度と一致することだけである  
<a id="source-L235"></a>重要なのは上の定義でnが可算個であっても良いということである  

<a id="source-L237"></a>数学的構造(X, A, μ)は測度空間と呼ばれる  

<a id="source-L239"></a>測度空間が有限であるとは、μ(Ω)が有限値であること  

<a id="source-L241"></a>・完備性  
<a id="source-L242"></a>可測集合Sがμ(S)=0であるとき零集合という  
<a id="source-L243"></a>測度μが完備であるとは零集合の全ての部分集合が可測であることである  
<a id="source-L244"></a>測度を完備測度に拡張することは簡単である  

<a id="source-L246"></a>・例  
<a id="source-L247"></a>数え上げ測度  
<a id="source-L248"></a>ルベーグ測度  
<a id="source-L249"></a>ハール測度  
<a id="source-L250"></a>零測度  
<a id="source-L251"></a>確率測度  

<a id="source-L253"></a>・一般化  
<a id="source-L254"></a>バナッハ空間に値をとる測度はスペクトル測度と呼ばれ、関数解析においてスペクトル定理などに用いられる  

<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

極限と積分は無条件には交換できない。例として $f_n(x)=n\mathbf{1}_{(0,1/n)}(x)$ を $(0,1)$ 上で考えると、各点では0へ収束するが積分は常に1。優収束定理では、可積分な共通の上界などの条件が必要になる。元メモの「交換できるようにする」という動機を、どの定理の仮定を満たすかまで書き足して使う。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [同じ分野のノート](README.md)：解析・微分方程式。

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
