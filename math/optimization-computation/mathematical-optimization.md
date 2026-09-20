---
title: "数理最適化"
status: draft
tags: [scrapbox, optimization-computation]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E6%95%B0%E7%90%86%E6%9C%80%E9%81%A9%E5%8C%96"
source_created: "2023-01-21T09:40:13Z"
source_updated: "2024-08-27T14:30:19Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 数理最適化

変数・目的・制約から問題を立て、連続・離散の解法へ進む講義メモ。

原ページ作成：2023-01-21 ／ 最終更新：2024-08-27（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/mathematical-optimization.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E6%95%B0%E7%90%86%E6%9C%80%E9%81%A9%E5%8C%96)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<details>
<summary>本文の見出しから探す</summary>

- [第1回 最適化の概要、連続最適化：無制約最適化1](#source-L16)
- [1 何を決めていきたいか？ー決定変数](#source-L20)
- [2 どうするのが理想的か？ー目的変数の最小化or最大化](#source-L21)
- [3 まもるべき条件は何か？ー制約条件](#source-L22)
- [第2回 連続最適化：無制約最適化2](#source-L62)
- [第3回 連続最適化：無制約最適化3](#source-L93)
- [第4回 連続最適化：無制約最適化4](#source-L132)
- [第5回 連続最適化：無制約最適化5,制約付き最適化1](#source-L176)
- [第6回 連続最適化：制約付き最適化2](#source-L210)
- [第7回 凸計画1](#source-L253)
- [第8回 凸計画2](#source-L302)
- [第9回 凸計画3](#source-L346)
- [第10回 ネットワーク計画1](#source-L389)
- [第11回 ネットワーク計画2、組み合わせ最適化1](#source-L439)
- [第12回 組み合わせ最適化の近似解法2、整数計画1](#source-L488)
- [第13回 整数計画2](#source-L530)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 数理最適化

<a id="source-L2"></a>[数理最適化と機械学習の融合](optimization-and-machine-learning.md)  

> <a id="source-L4"></a>神公開講座  

> > <a id="source-L5"></a><https://ocwx.ocw.u-tokyo.ac.jp/course_11412/>  
> > <a id="source-L6"></a>以下めも  


> <a id="source-L9"></a>東工大の数理最適化テキスト  

> > <a id="source-L10"></a><http://www.me.titech.ac.jp/~mizu_lab/text.html>  


> <a id="source-L13"></a>双対問題  

> > <a id="source-L14"></a><https://twitter.com/tmaehara/status/1624861889380421632?s=20&t=c9Z6WqpKmFDOVsuyKKsS6g>  


<a id="source-L16"></a>

### 第1回 最適化の概要、連続最適化：無制約最適化1


<a id="source-L18"></a>1-1 最適化問題の着眼点  
<a id="source-L19"></a>３つの着眼点  

<a id="source-L20"></a>

### 1 何を決めていきたいか？ー決定変数


<a id="source-L21"></a>

### 2 どうするのが理想的か？ー目的変数の最小化or最大化


<a id="source-L22"></a>

### 3 まもるべき条件は何か？ー制約条件


<a id="source-L24"></a>1-2 最適化問題の例１：乗り換え案内  
<a id="source-L25"></a>決定変数：各辺を使うか使わないか  
<a id="source-L26"></a>目的関数：各辺の重みを足したものを最小化  
<a id="source-L27"></a>制約条件：途中で途切れない  

<a id="source-L29"></a>1-3 最適化問題の例2：配車計画  
<a id="source-L30"></a>各トラックがどの配送先をどの順に訪れるのか  
<a id="source-L31"></a>トラックの走行距離の総和を最小化  
<a id="source-L32"></a>トラックの積載容量  
<a id="source-L33"></a>配送時間帯の指定  
<a id="source-L34"></a>運転手の労働条件など  

<a id="source-L36"></a>1-4 最適化問題の例3 ：最適設計  
<a id="source-L37"></a>コート掛け問題  
<a id="source-L38"></a>設計領域をたくさんの小領域に分割し、それぞれの小領域の色を決定する  
<a id="source-L39"></a>構造物の設計の過程に最適化を利用する  
<a id="source-L40"></a>最適化問題として定式化すればあとはそれを解くだけで良い  
<a id="source-L41"></a>それなので、直感では難しい問題でも解けることがある  

<a id="source-L43"></a>1-5 最適化問題の例4 ：一変数の場合  
<a id="source-L44"></a>最適化では多変数の場合に興味がある  
<a id="source-L45"></a>グラフは書けないのが前提  
<a id="source-L46"></a>コンピュータを用いて数値的に解く  

<a id="source-L48"></a>1-6 最適化問題の分類  
<a id="source-L49"></a>・連続最適化  
<a id="source-L50"></a>無制約と制約付きがある  

<a id="source-L52"></a>・離散最適化  
<a id="source-L53"></a>ネットワーク計画、組み合わせ最適化、整数計画がある  

<a id="source-L55"></a>1-7 無制約最適化の基本  
<a id="source-L56"></a>局所最適解と大域最適解がある  

<a id="source-L58"></a>1-8 最適解が同じ最適化問題  
<a id="source-L59"></a>習慣上、最大かよりも最小化について考えることが多い  



<a id="source-L62"></a>

### 第2回 連続最適化：無制約最適化2


<a id="source-L64"></a>2-1 応用例(回帰分析)  

<a id="source-L66"></a>2-2 多変数の場合  
<a id="source-L67"></a>等高線から多変数の図について理解する  

<a id="source-L69"></a>2-3 勾配とヘッセ行列、テイラー展開  
<a id="source-L70"></a>勾配とヘッセ行列を定義する  
<a id="source-L71"></a>勾配を縦ベクトルで書く習慣がある  

<a id="source-L73"></a>2-4 多変数関数の例  
<a id="source-L74"></a>コンピューターでプロットして説明していた  

<a id="source-L76"></a>2-5 1次の最適性条件  
<a id="source-L77"></a>xが局所最適解だとすると勾配がゼロベクトルとなる  

<a id="source-L79"></a>2-6 勾配の意味  
<a id="source-L80"></a>勾配は等高線に直交している  
<a id="source-L81"></a>増えていく方向のベクトルが勾配  

<a id="source-L83"></a>2-7 停留点  
<a id="source-L84"></a>xがfの停留点であることと勾配が0になることは必要十分  

<a id="source-L86"></a>2-8 対称行列の正定値性  

<a id="source-L88"></a>2-9 正定値行列の例  





<a id="source-L93"></a>

### 第3回 連続最適化：無制約最適化3


<a id="source-L95"></a>3-1 最適性条件  
<a id="source-L96"></a>前回の復習  

<a id="source-L98"></a>3-2 2次の最適性条件  
<a id="source-L99"></a>牛腸さんが言ってたようなこと  
<a id="source-L100"></a>見えないf(x)をP^2と近似して考えればすぐ出る  

<a id="source-L102"></a>3-3 最適性判定の例題、2×2行列の正定値性  

<a id="source-L104"></a>3-4 最適性判定の例題  
<a id="source-L105"></a>計算するだけ  

<a id="source-L107"></a>3-5 2次関数の勾配とヘッセ行列  
<a id="source-L108"></a>便利なので、覚えておく  
<a id="source-L109"></a>計算のテクニック  

<a id="source-L111"></a>3-6 数値解法：反復法の枠組み  
<a id="source-L112"></a>これからは、最適解をどのように見つけるのか？という話をする  

<a id="source-L114"></a>探索方向を決めるのは、いろんなバリエーションがあり、その違いが解法の違いにつながってくる  

<a id="source-L116"></a>3-7 最急降下法  
<a id="source-L117"></a>探索方向を勾配に-をつけたものにするというのが最急降下法である  

<a id="source-L119"></a>3-8 ２次元の例、正確な直線探索  
<a id="source-L120"></a>イメージを持つ  
<a id="source-L121"></a>最小にするαをαkとするのが正確な直線探索という  

<a id="source-L123"></a>3-9 最急降下法のアルゴリズム  

<a id="source-L125"></a>3-10 実用的な直線探索  
<a id="source-L126"></a>アルミホの条件を満たすαを見つけてαkとするのが実用的な直線探索である  






<a id="source-L132"></a>

### 第4回 連続最適化：無制約最適化4


<a id="source-L134"></a>4-1 最急降下法  

<a id="source-L136"></a>4-2 最急降下法の例題  
<a id="source-L137"></a>イメージを膨らませる  

<a id="source-L139"></a>4-3 最急降下法のアルゴリズムの実行例  
<a id="source-L140"></a>収束するまで繰り返すとどんなようになるのかをPCで確認する  

<a id="source-L142"></a>4-4 最急降下法の長所と短所  
<a id="source-L143"></a>最急降下法 + 実用的な直線探索  
<a id="source-L144"></a>→x0をどう選んでも局所最適解に収束する  
<a id="source-L145"></a>これを大域的収束性という  
<a id="source-L146"></a>必ず大域最適解が得られるという意味ではない  
<a id="source-L147"></a>どの局所最適解が得られるかは、初期点に依存  

<a id="source-L149"></a>収束が遅いという欠点がある  

<a id="source-L151"></a>4-5 ニュートン法  
<a id="source-L152"></a>次は反復回数をどう小さくするかということを考えていく  
<a id="source-L153"></a>最急降下法と探索方向の決め方が異なる  

<a id="source-L155"></a>簡単にいうとテイラー展開の２次の項まで見て小さくすることを考えるのがNewton法  

<a id="source-L157"></a>最急降下法は一次近似した関数を見ている  
<a id="source-L158"></a>ニュートン法は２次近似した関数を見ている  

<a id="source-L160"></a>4-6 ニュートン法の例題  

<a id="source-L162"></a>4-7 ニュートン法の長所と短所  
<a id="source-L163"></a>ニュートン法は収束が早い  
<a id="source-L164"></a>二次関数であれば１反復で収束する  

<a id="source-L166"></a>ニュートン方程式を解く手間が必要  
<a id="source-L167"></a>f(xk+1)が小さくなるとは限らないので局所最適解にすら収束するとは限らない  

<a id="source-L169"></a>4-8 降下方向  

<a id="source-L171"></a>なんとか正定値にしたいというのが準ニュートン法  





<a id="source-L176"></a>

### 第5回 連続最適化：無制約最適化5,制約付き最適化1


<a id="source-L178"></a>5-1 準ニュートン法  
<a id="source-L179"></a>最急降下法とニュートン法の良いとこどりをしようとした  
<a id="source-L180"></a>fの二階微分をあるBkで近似しようとした  

<a id="source-L182"></a>5-2 ヘッセ行列の近似の仕方：正定値対称  
<a id="source-L183"></a>Bkを正定値対象とするとdkはfのxkにおける降下方向  

<a id="source-L185"></a>5-3 ヘッセ行列の近似の仕方：セカント条件  
<a id="source-L186"></a>Bkを単位行列にすると最急降下法になってしまう  

<a id="source-L188"></a>5-4 ヘッセ行列の近似の仕方：注意点、BFGS公式  
<a id="source-L189"></a>Bk+1を決めるときは、xkとxk+1は既知  
<a id="source-L190"></a>上の１と２だけではBk+1は一意には決まらない→様々な公式がある  

<a id="source-L192"></a>5-5 準ニュートン法の例、無制約最適化の数値解法の比較  
<a id="source-L193"></a>PCで動き方を見る  

<a id="source-L195"></a>5-6 収束速度  
<a id="source-L196"></a>1次収束と2次収束  

<a id="source-L198"></a>5-7 最急降下法の加速法  

<a id="source-L200"></a>5-8 制約付き最適化の基本  

<a id="source-L202"></a>5-9 等式制約のみの場合  
<a id="source-L203"></a>g=0上の点で、目的関数と勾配が同じ向きになっているのが最適解でありそうなことが図を書けばわかる  

<a id="source-L205"></a>5-10 ラグランジュの乗数法  
<a id="source-L206"></a>これが多制約、多変数のときに同じことが成り立つ  
<a id="source-L207"></a>これがラグランジュ乗数法である  



<a id="source-L210"></a>

### 第6回 連続最適化：制約付き最適化2

<a id="source-L211"></a>6-1 ラグランジュ乗数法、制約想定  

<a id="source-L213"></a>6-2 ラグランジュ乗数法の証明の概略1  
<a id="source-L214"></a>陰関数定理を使う  
<a id="source-L215"></a>実行可能解の中で少し動いて目的関数値がどのように変化するのかを観察する  

<a id="source-L217"></a>6-3 ラグランジュ乗数法の証明の概略2  
<a id="source-L218"></a>線形代数の知識を用いる  

<a id="source-L220"></a>6-4 不等式制約を持つ場合  

<a id="source-L222"></a>6-5 最適性条件の観察  
<a id="source-L223"></a>=のときはラグランジュの未定乗数法と同じ  

<a id="source-L225"></a>不等号のときは、最適解ではラグランジュ乗数が正のときであると図でわかる  

<a id="source-L227"></a>h1とh2がどちらも非有効である場合はh1とh2のgradの一次結合でfが表せるはず  

<a id="source-L229"></a>6-6 KKT条件  
<a id="source-L230"></a>１〜３の考察で分かったことをまとめてみる  
<a id="source-L231"></a>最後の式が等式制約を違う場合  
<a id="source-L232"></a>これは有効、非有効から生じている  
<a id="source-L233"></a>相補性条件という  
<a id="source-L234"></a>非常によく出てくるので重要である  
<a id="source-L235"></a>最適解の性質はKKT条件で決まってくる  

<a id="source-L237"></a>6-7 ラグランジュ関数  

<a id="source-L239"></a>ラグランジュ関数は6-6の式を覚え方とも取れるが、実は双対問題を解くときに使うという深いことがある  

<a id="source-L241"></a>6-8 一般の制約付き最適化問題の解法  

<a id="source-L243"></a>・逐次2次計画  
<a id="source-L244"></a>2次計画問題で、近似することを繰り返す  
<a id="source-L245"></a>2次計画問題は後でやる  

<a id="source-L247"></a>・内点法：後で線型計画のところでやる  

<a id="source-L249"></a>pythonでpyOptを使うなど、現にあるパッケージを使えば良い  
<a id="source-L250"></a>自分でアルゴリズムを書く必要はない  



<a id="source-L253"></a>

### 第7回 凸計画1


<a id="source-L255"></a>7-1 凸計画の導入  
<a id="source-L256"></a>前回は、最適解がKKT条件でかけることが分かった  
<a id="source-L257"></a>KKT条件は局所最適解が満たすべき条件であった  

<a id="source-L259"></a>一般に大域的最適解の保証は困難であるが  
<a id="source-L260"></a>ある性質を満たしているときに保証できることがある  
<a id="source-L261"></a>それが凸計画である  
<a id="source-L262"></a>大域的最適解を求めやすい問題のクラスである  

<a id="source-L264"></a>7-2 凸関数の定義  


<a id="source-L267"></a>7-3 凸関数の例  
<a id="source-L268"></a>二次関数や、折れ線やその組み合わせ、直線、  

<a id="source-L270"></a>三次関数はダメ  

<a id="source-L272"></a>7-4 凸関数の特徴づけ  

<a id="source-L274"></a>7-5 凸集合  

<a id="source-L276"></a>7-6 凸集合の例  
<a id="source-L277"></a>全空間や一次不等式何本かで定義される多面体  
<a id="source-L278"></a>凸集合の共通部分は凸  

<a id="source-L280"></a>7-7 凸計画問題の基本  
<a id="source-L281"></a>凸は非線型も含んでいる  

<a id="source-L283"></a>7-8 線型計画問題の基本  
<a id="source-L284"></a>凸計画問題の一種である  
<a id="source-L285"></a>大規模でも容易に解ける  

<a id="source-L287"></a>どんなLPも等式標準形に変形できるので、上の形に限定して議論して良い  

<a id="source-L289"></a>7-9 等式標準形への変形例  

<a id="source-L291"></a>7-10 線型計画問題の実行可能領域と最適解  

<a id="source-L293"></a>一般にLPの実行可能領域は多面体で、その最適解はどこかの頂点である  
<a id="source-L294"></a>頂点の数は有限個なので、ある頂点から出発して、目的関数が減る方向の隣の頂点に移動することを考える  
<a id="source-L295"></a>それを繰り返すと、最適解が求まる  
<a id="source-L296"></a>これが単体法と呼ばれる方法  

<a id="source-L298"></a>7-11 線型計画問題の例  
<a id="source-L299"></a>一次式しか扱えないのは条件が厳しいと思われるが、一見一次式には見えない問題も工夫をして線型計画問題に直すことができる  



<a id="source-L302"></a>

### 第8回 凸計画2


<a id="source-L304"></a>8-1 線型計画  
<a id="source-L305"></a>要するに線型計画問題に帰着させれば簡単！  

<a id="source-L307"></a>8-2 線型計画問題の例：絶対値の和  
<a id="source-L308"></a>上界を考えるということをよくやる  

<a id="source-L310"></a>8-3 基底追跡  
<a id="source-L311"></a>上記は基底追跡という名前の問題  

<a id="source-L313"></a>8-4 線型計画問題の例：いくつかの一次関数の最大値  

<a id="source-L315"></a>8-5 線型計画問題の例：多面体のChebyshev中心  

<a id="source-L317"></a>8-6 CVXPYによる線型計画問題の解き方  

<a id="source-L319"></a>8-7 線型計画の双対性  

<a id="source-L321"></a>主問題と双対問題は相対的である  
<a id="source-L322"></a>というのも双対問題の双対問題は主問題である  

<a id="source-L324"></a>8-8 線型計画の強双対性  
<a id="source-L325"></a>不等号で双対問題の話をしていたが、実は等号で成り立ち、これを強双対性という  

<a id="source-L327"></a>8-9 線型計画の最適性条件  

<a id="source-L329"></a>この４つの条件を満たすxとyを見つければ、xは主問題の最適解、yは双対問題の最適解となる  

<a id="source-L331"></a>8-10 内点法  
<a id="source-L332"></a>どうやって最適解を見つけるのか？  
<a id="source-L333"></a>単体法と並んでよく使われる線型計画の解き方  
<a id="source-L334"></a>要するに4つの条件を満たす点を見つければ良い  
<a id="source-L335"></a>上２行は線型なので、簡単  
<a id="source-L336"></a>相補性条件は非線型なので扱うのが難しい  

<a id="source-L338"></a>内点法では、扱いにくいところを変形する  
<a id="source-L339"></a>μを動かすと、枝分かれしない曲線となることを示すことができる  

<a id="source-L341"></a>線形近似を考える  





<a id="source-L346"></a>

### 第9回 凸計画3

<a id="source-L347"></a>9-1 ２次計画の基本  
<a id="source-L348"></a>二次の目的関数を持っている問題  
<a id="source-L349"></a>制約も二次式の時があるが、この講義では制約は一次式とする  
<a id="source-L350"></a>Q：n次対称、半正定値  
<a id="source-L351"></a>Q=0の場合が線型計画である  

<a id="source-L353"></a>二次計画にも双対定理が成り立ち、似たような最適条件や効率よく解ける方法がある  

<a id="source-L355"></a>9-2 回帰分析：最小二乗法  
<a id="source-L356"></a>二次計画の理論はやらないことにする  
<a id="source-L357"></a>今回は二次計画の応用例を考えていく  

<a id="source-L359"></a>9-3 回帰分析：RIdge,Lasso解析  

<a id="source-L361"></a>9-4 CVXPYによる二次計画問題の解き方  

<a id="source-L363"></a>9-5 SVM：基本、直線での分離可能性  

<a id="source-L365"></a>9-6 SVM：分離可能な場合  

<a id="source-L367"></a>これは二次計画  
<a id="source-L368"></a>これを解くことで分離可能なときは二次計画を解けば簡単にSVMが解ける  

<a id="source-L370"></a>9-7 SVM：分離不可能な場合  

<a id="source-L372"></a>9-8 確率線型計画  

<a id="source-L374"></a>パレート最適化という  
<a id="source-L375"></a>何を選ぶかは価値観が入ってくる  
<a id="source-L376"></a>世の中の多くの決定問題はこのような形式になっている  

<a id="source-L378"></a>9-9 半正定値計画  
<a id="source-L379"></a>半正定値計画は凸計画となる  

<a id="source-L381"></a>9-10 半正定値計画の応用例  
<a id="source-L382"></a>固体の釣り合い形状は一般に変分原理により求められる  
<a id="source-L383"></a>応力テンソルは常に半正定値→半正定値計画で定式化できる  
<a id="source-L384"></a>半正定値計画問題を解くことで変形形状が求められる  
<a id="source-L385"></a>このほかにもロバスト最適化、制御、データマイニング、計算化学、非凸な最適化問題の緩和などいろいろ応用がある  




<a id="source-L389"></a>

### 第10回 ネットワーク計画1

<a id="source-L390"></a>10-1 最短路問題  
<a id="source-L391"></a>今回からは離散的な最適化問題を扱う  

<a id="source-L393"></a>10-2 最適性の原理  

<a id="source-L395"></a>最短路の途中の路は、その中の最短路  
<a id="source-L396"></a>つまり、sから各点までの最短路を近い順に確定していける  

<a id="source-L398"></a>10-3 ダイクストラ法1  
<a id="source-L399"></a>隣接する点の数字をどんどん更新していく  

<a id="source-L401"></a>10-4 ダイクストラ法2  
<a id="source-L402"></a>2^nを列挙は無理なので、ダイクストラを使う  

<a id="source-L404"></a>10-5 グラフ  

<a id="source-L406"></a>10-6 木  
<a id="source-L407"></a>木は連結で、閉路を持たないグラフである  
<a id="source-L408"></a>連結と閉路は読んで字のごとく  

<a id="source-L410"></a>10-7 全域木、カット  
<a id="source-L411"></a>Gの全域木はGの部分グラフで、Vの全てを持つ木  
<a id="source-L412"></a>全域木の性質として、  
<a id="source-L413"></a>・辺は|V-1|  
<a id="source-L414"></a>・辺を１本追加すると閉路ができる  
<a id="source-L415"></a>・辺を１本取り除くと２つの連結成分に分解する  

<a id="source-L417"></a>Gのカットについて  
<a id="source-L418"></a>カットは、頂点を２つの集合に分けたときの概念  
<a id="source-L419"></a>カットは辺の集合  
<a id="source-L420"></a>SとV-Sを繋いでる辺の集合である  

<a id="source-L422"></a>10-8 最小全域木  
<a id="source-L423"></a>重みの総和が最小の全域木を考える  
<a id="source-L424"></a>最小木はある性質を持っており、その性質を使えばこの問題が解決する  

<a id="source-L426"></a>Gのカットの重み最小の辺を考える  
<a id="source-L427"></a>その重み最小の辺は最小木に含まれる  
<a id="source-L428"></a>これが任意のSの選び方について成り立つ  

<a id="source-L430"></a>10-9 最小木の性質の証明  
<a id="source-L431"></a>全域木に辺を１つ追加すると閉路ができる  
<a id="source-L432"></a>閉路のカットを考えると必ず2本以上の辺をとおる  

<a id="source-L434"></a>10-10 プリムのアルゴリズム  
<a id="source-L435"></a>この性質を利用して最小木問題を解く方法として２つぐらいよく知られた方法がある  
<a id="source-L436"></a>１つ目がプリム法である  



<a id="source-L439"></a>

### 第11回 ネットワーク計画2、組み合わせ最適化1


<a id="source-L441"></a>11-1 最小木問題  
<a id="source-L442"></a>前回の復習  

<a id="source-L444"></a>11-2 クラスカルのアルゴリズム  
<a id="source-L445"></a>・重みの小さい辺から順に採用  
<a id="source-L446"></a>・閉路ができるときはその辺をスキップする  
<a id="source-L447"></a>これだけ  
<a id="source-L448"></a>Gの中での重みが最小の辺は、必ずどんなカットの中でも重みが最小  
<a id="source-L449"></a>どんなカットの中で重みが最小の辺は最小木に含まれるので、これは最小全域木2に入る  
<a id="source-L450"></a>このようなアルゴリズムと貪欲法という  
<a id="source-L451"></a>良い要素から順に採用して解を構築するのが貪欲法  

<a id="source-L453"></a>11-3 NetworkXによるネットワーク計画問題の解き方  
<a id="source-L454"></a>NetworkXというPythonのライブラリを使うと、ネットワーク計画問題が簡単に解ける  

<a id="source-L456"></a>11-4 階層的クラスタリング  
<a id="source-L457"></a>最小木の応用である  

<a id="source-L459"></a>似たもの同士のグループに分けることをクラスタリングという  
<a id="source-L460"></a>クラスター間の距離を最大化したい  

<a id="source-L462"></a>11-5 階層的クラスタリング：クラスカルのアルゴリズムによる解法  
<a id="source-L463"></a>実は上記のような問題はクラスカルのアルゴリズムで解ける  


<a id="source-L466"></a>11-6 組み合わせ最適化：巡回セールスマン問題  
<a id="source-L467"></a>問題  
<a id="source-L468"></a>ちょうど一回ずつ通って元に戻る重み最小の閉路は？  
<a id="source-L469"></a>これは、N!通りあるのでまず全探索は無理ゲー  

<a id="source-L471"></a>11-7 巡回セールスマン問題：貪欲算法の適用例  
<a id="source-L472"></a>クラスカルのような貪欲法をやれば最適解が求まるのではないか？と思うが、そうでもない  
<a id="source-L473"></a>nearest neighborとよばれるまだ訪れていない最も近い頂点に移動するものは最適解にはならない  

<a id="source-L475"></a>巡回セールスマン問題は厳密に解くのは難しい難問題とされている  

<a id="source-L477"></a>11-8 巡回セールスマン問題：近似解法  
<a id="source-L478"></a>厳密に解くのは難しいので、近似解法を考えていく  
<a id="source-L479"></a>仮定として、重みが三角不等式を満たすことを仮定する  

<a id="source-L481"></a>11-9 巡回セールスマン問題：近似比  
<a id="source-L482"></a>これはある閉路を見つけただけに見えるが、ある精度保証ができる  
<a id="source-L483"></a>また、簡単である  
<a id="source-L484"></a>より１に近い解法がいくつか考えられている  
<a id="source-L485"></a>近似比が2の近似解法のことを2-近似解法という  



<a id="source-L488"></a>

### 第12回 組み合わせ最適化の近似解法2、整数計画1


<a id="source-L490"></a>12-1 最遠点クラスタリング  
<a id="source-L491"></a>似たもの同士は同じクラスター内＝各くらすたーは小さい  
<a id="source-L492"></a>つまりクラスタ内で一番遠い距離の点同士の距離が小さいことを目指す  

<a id="source-L494"></a>12-2 最遠点クラスタリング：近似解法(farthest-first traversel)  
<a id="source-L495"></a>各クラスターの代表点を順番に決めていくアルゴリズムである  

<a id="source-L497"></a>12-3 最遠点クラスタリング：近似比  
<a id="source-L498"></a>新しい代表点を作り、最も近い座標点までの距離をδとおく  

<a id="source-L500"></a>12-4 最遠点クラスタリング：近似比の説明  
<a id="source-L501"></a>気になったら動画を見返す  

<a id="source-L503"></a>12-5 ナップサック問題  
<a id="source-L504"></a>これは整数計画というものでかける  
<a id="source-L505"></a>変数が整数になっている計画問題は整数計画という  

<a id="source-L507"></a>12-6 サップサック問題：具体例  
<a id="source-L508"></a>厳密解は後でやるが、今は先に近似解法をやる  

<a id="source-L510"></a>x^lpは整数計画の解ではないが、一応書いておく  
<a id="source-L511"></a>これはある意味貪欲算法である  

<a id="source-L513"></a>12-7 ナップサック問題：緩和問題の解  

<a id="source-L515"></a>12-8 ナップサック問題：近似解法  
<a id="source-L516"></a>そもそもナップサックに入らないものは除外しておく  

<a id="source-L518"></a>12-9 整数計画  
<a id="source-L519"></a>線型計画+整数制約  

<a id="source-L521"></a>x1,,,xnが0か1の時、0-1計画という  
<a id="source-L522"></a>0,1に限っても十分表現力がある  
<a id="source-L523"></a>連続変数も含むときは、混合整数計画という  

<a id="source-L525"></a>12-10 連続緩和問題  
<a id="source-L526"></a>実は緩和問題では、厳密解を求めるためにつける  
<a id="source-L527"></a>分枝限定法という  



<a id="source-L530"></a>

### 第13回 整数計画2


<a id="source-L532"></a>13-1 整数計画  
<a id="source-L533"></a>整数計画を解く時の道具として使われるものとして緩和問題がある  

<a id="source-L535"></a>13-2 連続緩和問題  
<a id="source-L536"></a>離散的なものがあると問題が難しくなるので、0\~1の間という風に緩和する  

<a id="source-L538"></a>13-3 分枝限定法1  
<a id="source-L539"></a>緩和問題を利用する厳密解法  

<a id="source-L541"></a>13-4 分枝限定法2  

<a id="source-L543"></a>13-5 分枝限定法3  

<a id="source-L545"></a>それより下に、最適解があるはずないので調べる必要はない  
<a id="source-L546"></a>緩和問題から、調べる範囲を絞ることでしらみつぶしをするのが分枝限定法  

<a id="source-L548"></a>13-6 分枝限定法の注意点  
<a id="source-L549"></a>・限定操作ができるのかは、分枝をたどる順番に依存する  
<a id="source-L550"></a>最終的に解かなければいけない線型計画問題の数は変わる  
<a id="source-L551"></a>一般には、小数になる変数は１つだけではない  

<a id="source-L553"></a>13-7 ソルバーによる整数計画問題の解き方  
<a id="source-L554"></a>整数計画問題は、ソルバーを利用すれば良い  
<a id="source-L555"></a>分枝限定法や切除平面法を実装した良いソルバーがたくさんある  

<a id="source-L557"></a>13-8 整数計画の応用例：部屋割り問題1  
<a id="source-L558"></a>整数計画を使ってどのような問題を表現できるのかを講義して終わりにする  
<a id="source-L559"></a>整数計画は、記述能力が高く、組み合わせの性質を持っているいろんな問題を解くことができる  
<a id="source-L560"></a>組み合わせ最適化の問題の多くは整数計画をつかって記述することができる  

<a id="source-L562"></a>部屋割を決める問題を考える  
<a id="source-L563"></a>溢れる人を最小化したい  

<a id="source-L565"></a>13-9 整数計画の応用例：部屋割り問題2  





> <a id="source-L571"></a>数理計画法  

<a id="source-L572"></a><http://www.dais.is.tohoku.ac.jp/~shioura/teaching/mp11/mp11-06.pdf>  

<a id="source-L574"></a>組み合わせ最適化  
<a id="source-L575"></a>最小木問題、巡回セールスマン問題など  

<a id="source-L577"></a>解きやすい問題の場合  
<a id="source-L578"></a>→多項式時間アルゴリズムを構築  

<a id="source-L580"></a>解きにくい問題の場合  
<a id="source-L581"></a>・最適解が必要  
<a id="source-L582"></a>→分枝限定法、動的計画法  
<a id="source-L583"></a>・ある程度良い解であれば十分  
<a id="source-L584"></a>→精度保証付き近似アルゴリズム、ヒューリスティックス  

<a id="source-L586"></a>動的計画法：同一の部分問題を繰り返し解かない  
<a id="source-L587"></a>分枝限定法：ある部分問題から最適解が得られないことがわかったらその部分問題は無視する  

<a id="source-L589"></a>分枝限定法  
<a id="source-L590"></a>分枝操作によりたくさんの部分問題が生成  
<a id="source-L591"></a>解く必要のない部分問題が検出されたらさらなる分枝操作をストップ  
<a id="source-L592"></a>暫定解の保持と緩和問題の利用により無駄をチェック  
<a id="source-L593"></a>緩和問題とは、元の数理計画問題の制約条件の一部を緩和して得られる問題  
<a id="source-L594"></a>例えば、連続ナップサック問題は線形計画問題なので多項式時間で解ける  
<a id="source-L595"></a>緩和問題は元の問題よりときやすく、緩和問題の最適値は元の問題の最適値の上界  
<a id="source-L596"></a>緩和問題の最適解を修正することにより元の問題の実行可能解を作ることが可能なケースが多い  
<a id="source-L597"></a>分枝限定法の検討事項  
<a id="source-L598"></a>・部分問題の探索法  
<a id="source-L599"></a>・限定操作のやり方  
<a id="source-L600"></a>・分枝操作のやり方  


> <a id="source-L603"></a>整数計画による定式化入門  

> > <a id="source-L604"></a><http://web.tuat.ac.jp/~miya/fujie_ORSJ.pdf>  
> > <a id="source-L605"></a><http://www.dais.is.tohoku.ac.jp/~shioura/teaching/mp14/index.html>  

<a id="source-L606"></a>ネットワーク最適化  
<a id="source-L607"></a>最小木問題  
<a id="source-L608"></a>最短路問題  
<a id="source-L609"></a>最大流問題  
<a id="source-L610"></a>最小費用流問題  
<a id="source-L611"></a>割り当て問題  



> <a id="source-L615"></a>60分で数理最適化  

> > <a id="source-L616"></a><https://speakerdeck.com/umepon/mathematical-optimization-in-60-minutes?slide=13>  



> <a id="source-L620"></a>関数解析と最適化  

> > <a id="source-L621"></a><https://kito.wordpress.ncsu.edu/files/2018/04/funa3.pdf>  



> <a id="source-L625"></a>リーマン多様体上の最適化―特異値分解の例を通して―  

> > <a id="source-L626"></a><https://mirucacule.hatenablog.com/entry/2022/07/10/180000>  



> <a id="source-L630"></a>数理最適化ことはじめ  

<a id="source-L631"></a><https://speakerdeck.com/e869120/introduction-to-mathematical-optimization-5cdef842-50f6-4e46-ab2d-549cf85c1b81>  



> <a id="source-L635"></a>実務につなげる数理最適化  

<a id="source-L636"></a><https://speakerdeck.com/umepon/mathematical-optimization-for-real-applications>  


> <a id="source-L639"></a>pulp  

<a id="source-L640"></a><https://qiita.com/SaitoTsutomu/items/070ca9cb37c6b2b492f0>  



> <a id="source-L644"></a>Googleの数理最適化ツールOR-Toolsを使ってみる  

<a id="source-L645"></a><https://qiita.com/kira4845/items/44990a64089bd4a5fd32>  










<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

停留点と最適解を区別する。無制約で微分可能な関数の内点の局所最適解では勾配が0になるが、逆は一般に成り立たない。例は $f(x)=x^3$ の $x=0$。制約付き問題では境界や制約資格条件も関わる。凸性、実行可能性、最適性条件を明示して読むと、元メモの問題の立て方を解法へつなげられる。[Boyd・Vandenberghe, Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/)を参照。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [数理最適化と機械学習の融合](optimization-and-machine-learning.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
