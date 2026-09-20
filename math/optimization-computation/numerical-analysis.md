---
title: "数値解析"
status: draft
tags: [scrapbox, optimization-computation]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E6%95%B0%E5%80%A4%E8%A7%A3%E6%9E%90"
source_created: "2023-01-21T10:43:20Z"
source_updated: "2023-01-21T10:48:09Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 数値解析

精度と計算量を意識した講義メモ。途中でメモを続ける負担が増えたことも残る。

原ページ作成：2023-01-21 ／ 最終更新：2023-01-21（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/numerical-analysis.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E6%95%B0%E5%80%A4%E8%A7%A3%E6%9E%90)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

## 思考の手がかり

> 途中でメモがだるくなってしまった

[本文の該当箇所へ](#source-L6)

<details>
<summary>本文の見出しから探す</summary>

- [第1回 数値解析とは](#source-L8)
- [第2回 数値の表現と誤差](#source-L57)
- [第3回 連立一次方程式の解法（直接法）](#source-L131)
- [第4回 連立一次方程式の解法（反復法）](#source-L184)
- [第5回 固有値問題の解法](#source-L241)
- [第6回 固有値問題、非線型方程式](#source-L287)
- [第7回 非線型方程式](#source-L309)
- [第8回 関数の近似と補間](#source-L331)
- [第9回 数値積分](#source-L353)
- [第10回 常微分方程式の数値解法](#source-L380)
- [第11回 偏微分方程式の数値解法](#source-L406)
- [第12回 偏微分方程式の数値解法](#source-L435)
- [1. Simultaneous Equations (Direct method) (連立方程式(直接法))](#source-L465)
- [2. Simultaneous Equations (Iterative method) (連立方程式(反復法))](#source-L466)
- [3. Non-linear problems (非線形方程式の解法)](#source-L467)
- [4. Non-linear problems (非線形方程式の解法)](#source-L468)
- [5. Eigenvalue problems (固有値問題)](#source-L469)
- [6. Numerical Errors (数値誤差)](#source-L470)
- [7. Numerical Difference (差分)](#source-L471)
- [8. Numerical Interpolation (数値補間)](#source-L472)
- [9. Numerical Integration (数値積分)](#source-L473)
- [10. Ordinal Differential Equations (常微分方程式)](#source-L474)
- [11. Eigenvalue problems (固有値問題)](#source-L475)
- [12. Eigenvalue problems (固有値問題)](#source-L476)
- [13. Ordinal Differential Equations (常微分方程式)](#source-L477)
- [14. Partial Differential Equations (偏微分方程式)](#source-L478)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 数値解析


> <a id="source-L3"></a>神講座をみましょう！  

> > <a id="source-L4"></a><https://elf-c.he.u-tokyo.ac.jp/courses/226>  
> > <a id="source-L5"></a>以下メモ  
> > <a id="source-L6"></a>途中でメモがだるくなってしまった  


<a id="source-L8"></a>

### 第1回 数値解析とは


<a id="source-L10"></a>1-1 数値解析について  
<a id="source-L11"></a>数値解析　＝　問題を数値的に解析する  

<a id="source-L13"></a>ゴール  
<a id="source-L14"></a>・数値解析の用途  
<a id="source-L15"></a>・数値解析の使い方  
<a id="source-L16"></a>・数値解析の数理  
<a id="source-L17"></a>を理解し、使えるようになる  

<a id="source-L19"></a>いつかどこかで数値解析をする羽目になるので、聞いておくべき  
<a id="source-L20"></a>１００万円かかるプログラムを書くか、１万円で住むプログラムを書くのはを決める  

<a id="source-L22"></a>線形計算、非線形方程式と最適化、関数近似と関連アルゴリズム、常微分方程式を理解して初めて偏微分方程式が溶けるようになる  

<a id="source-L24"></a>数学、情報科学、諸科学を知ると数値解析ができるようになり様々なものに応用できる  
<a id="source-L25"></a>![元メモの画像](../assets/scrapbox/63cbc217ef728e001e0bbed5.png) ([画像の出典](<https://scrapbox.io/files/63cbc217ef728e001e0bbed5.png>))  
<a id="source-L26"></a>![元メモの画像](../assets/scrapbox/63cbc21fc4d028001d132771.png) ([画像の出典](<https://scrapbox.io/files/63cbc21fc4d028001d132771.png>))  


<a id="source-L29"></a>1-2 数値解析の難しさ  
<a id="source-L30"></a>数値解析では、計算過程の解析もする  
<a id="source-L31"></a>これをしないとひどい目にある  

<a id="source-L33"></a>根本的な困難：有限のメモリ、有限の数値、有限の手順、四則演算など、全ては無限との戦いである  
<a id="source-L34"></a>もっと厳密には、足し算と引き算しか理解できない  
<a id="source-L35"></a>大体の計算機では有効数字15桁ほど  

<a id="source-L37"></a>計算量は極めて大事、O(n^3)はまだ頑張ればなんとかなるが、O(n^4)以上はやりたくなさすぎる  

<a id="source-L39"></a>1-3 数値計算の落とし穴  
<a id="source-L40"></a>漸化式は特性根求めて、係数を求めるだけ  
<a id="source-L41"></a>だが、漸化式でもおかしいことが起こるこの惨事の原因は計算機の有限性である  

<a id="source-L43"></a>1-4 落とし穴の対処法と教訓  
<a id="source-L44"></a>例えば、漸化式やbessel関数の計算は前から後ろに計算してはいけない  
<a id="source-L45"></a>これは工夫すれば解ける  
<a id="source-L46"></a>無限を前提に組み立てた数学の世界から見ると有限しか許されない故に不完全で壊れている  
<a id="source-L47"></a>数値解析学者は、誤差収拾人ではなく、優れた分析官である  

<a id="source-L49"></a>1-5 数値解析例まとめ  
<a id="source-L50"></a>自然は最小を好む、という思想で物理法則を組み立てると、今のところ矛盾なくうまくいっている  
<a id="source-L51"></a>超電導現象の計算例  






<a id="source-L57"></a>

### 第2回 数値の表現と誤差

<a id="source-L58"></a>2-1 浮動小数点数の導入  
<a id="source-L59"></a>浮動小数点数  

<a id="source-L61"></a>2-2 単精度/倍精度で表現できる数  
<a id="source-L62"></a>単精度で表現できる数の範囲  
<a id="source-L63"></a>最小の数：2^-126 \~ 1.175\*10^-38  
<a id="source-L64"></a>最大の数：2^127\*2 \~ 3.4\*10^38  
<a id="source-L65"></a>有効数字桁数：2^24 \~ 10^7  
<a id="source-L66"></a>倍精度  
<a id="source-L67"></a>最小：2.225\*10^-308  
<a id="source-L68"></a>最大：1.798\*10^308  
<a id="source-L69"></a>有効数字桁数：10^15  

<a id="source-L71"></a>有効数字桁数が一番大事  
<a id="source-L72"></a>アンダーフローよりもオーバーフローの方が怖い  
<a id="source-L73"></a>大きな数の世界ではスカスカな数で計算をしている  

<a id="source-L75"></a>2-3 Machine epsilon  
<a id="source-L76"></a>machine epsilonは相対誤差  
<a id="source-L77"></a>x\_f/x = 1 + ε\_xで表現できる  
<a id="source-L78"></a>単精度であれば、εは10^-7ぐらい、倍精度なら10^-15ぐらい  

<a id="source-L80"></a>2-4 丸め誤差  
<a id="source-L81"></a>浮動小数点数が線形空間を成さないので、無理やり線形空間に入れるための誤差  
<a id="source-L82"></a>１０回計算したら有効数字が１桁ずれる可能性がある  

<a id="source-L84"></a>2-5 桁落ち誤差  
<a id="source-L85"></a>近い数の引き算で発生する、著しい有効数字減少  
<a id="source-L86"></a>例えば、二次方程式の解の公式でb &gt;&gt; acのとき  
<a id="source-L87"></a>プラスか、マイナスかどちらかが悪い時は、分子を有利化すべし  

<a id="source-L89"></a>2-6 積み残し  
<a id="source-L90"></a>大きな数と小さな数を足したら小さな数が無視される  
<a id="source-L91"></a>良い例として、バーゼル問題  
<a id="source-L92"></a>うしろから足したり、より収束の早い表現を探したりする  

<a id="source-L94"></a>2-7 区間演算  
<a id="source-L95"></a>区間演算というのはどこまでの範囲であるか、を示す演算方法  
<a id="source-L96"></a>expなどが混じると何も言っていないことになる  

<a id="source-L98"></a>2-8 連立一次方程式を解くとは  
<a id="source-L99"></a>線形代数的に連立一次方程式が解けるということと、科学者が連立一次方程式を計算機に解かせるには大きなギャップがあり、まだ一般解は存在しない  

<a id="source-L101"></a>2-9 Cramerの公式  
<a id="source-L102"></a>理論的にきれいでも、数値計算の役に立たない時がある  
<a id="source-L103"></a>detを計算する計算量はO(n!)なので無理ゲー  

<a id="source-L105"></a>2-10 逆行列を用いる方法  
<a id="source-L106"></a>A-1bで解く催促手順よりも、Ax=bを最速手順で解く方が早い  
<a id="source-L107"></a>数値計算の世界にきたら、逆行列を使うことは基本的にない  

<a id="source-L109"></a>2-11 行列とベクトルのノルム  
<a id="source-L110"></a>連立一次方程式を数値的に解けるかどうかで何が重要か  
<a id="source-L111"></a>距離を入れる方法がノルムである  
<a id="source-L112"></a>作用素にノルムを入れる時はsupで定義する時が多い  

<a id="source-L114"></a>2-12 摂動により生じる誤差の評価  
<a id="source-L115"></a>行列と係数ベクトルを少しずらして考える  
<a id="source-L116"></a>εを変えるごとに解も動く  
<a id="source-L117"></a>Aが正則なら十分小さなεに対してA+ε Fも正則  
<a id="source-L118"></a>テイラー展開したものを持ち手評価する  
<a id="source-L119"></a>「AとA^-1のノルム」が大きいと、誤差が拡大し、これを条件数と呼ぶ  
<a id="source-L120"></a>これをまず調べるべきである  
<a id="source-L121"></a>A^-1のノルムを計算するのは難しいので、これを評価する方法が色々と考えられている  

<a id="source-L123"></a>2-13 条件数のイメージと例  
<a id="source-L124"></a>条件数が大きいというのは、直線の交わりの角度が小さいということ  
<a id="source-L125"></a>計算機の中は脆い実数上で動いている  






<a id="source-L131"></a>

### 第3回 連立一次方程式の解法（直接法）


<a id="source-L133"></a>3-1 連立一次方程式の直接法  

<a id="source-L135"></a>3-2 Gaussの消去法  
<a id="source-L136"></a>上三角行列にすれば求まる  
<a id="source-L137"></a>これを前進消去という  

<a id="source-L139"></a>3-3 Gaussの消去法：前進消去  
<a id="source-L140"></a>アルゴリズムで表せる形に消去の手順をシステマティックに書いていく  

<a id="source-L142"></a>3-4 Gaussの消去法：後退代入  
<a id="source-L143"></a>後退代入するときに0割をケアする  

<a id="source-L145"></a>3-5 Gaussの消去法：より一般の場合  
<a id="source-L146"></a>仮定をおいたが、その仮定が満たされていないときは考えられなかった  
<a id="source-L147"></a>このケア方法と、常にケアできるということを説明する  

<a id="source-L149"></a>3-6 Gaussの消去法：枢軸択付き  
<a id="source-L150"></a>対角成分が0になることや、0に近くなるのを避ける  
<a id="source-L151"></a>行を適切に入れ替えながら進めていく  

<a id="source-L153"></a>3-7 Gaussの消去法：計算量  
<a id="source-L154"></a>前進消去はO(n^3)、後退代入はO(n^2)となるので、Gaussの消去法の計算量は行列の大きさをnとしたときにO(n^3)であると覚えておく  

<a id="source-L156"></a>3-8 LU分解：導入と存在の証明  
<a id="source-L157"></a>実はGaussの消去法は別表現がある  
<a id="source-L158"></a>Gaussの消去法 = LU分解 + 後退代入  

<a id="source-L160"></a>3-9 LU分解：枢軸選択付き  
<a id="source-L161"></a>行方向を入れ替える  

<a id="source-L163"></a>3-10 LU分解：利点  
<a id="source-L164"></a>PA = LUに基づくAx = bの解法が使える  
<a id="source-L165"></a>一度LU分解をすれば高速に解けるようになる  

<a id="source-L167"></a>3-11 計算量の比較  

<a id="source-L169"></a>逆行列からxを求める積極的な理由は存在しない  
<a id="source-L170"></a>LUルートを通るべきである  

<a id="source-L172"></a>3-12 注意点：fill in  
<a id="source-L173"></a>疎→密にする  
<a id="source-L174"></a>反復法はn^3に耐えられないときに使う  

<a id="source-L176"></a>3-13 注意点：Cholesky分解  
<a id="source-L177"></a>LU分解の特別な場合  
<a id="source-L178"></a>名前だけ覚えておく  

<a id="source-L180"></a>3-14 LU分解：アルゴリズム  




<a id="source-L184"></a>

### 第4回 連立一次方程式の解法（反復法）

<a id="source-L185"></a>4-1 反復法  
<a id="source-L186"></a>直接法はO(n^3)で答えが出る  
<a id="source-L187"></a>fill-inで疎性がこわれる  
<a id="source-L188"></a>反復法はO(n^2)の反復を行うが、厳密解にはいかない  
<a id="source-L189"></a>直接法は「密」で「小」  
<a id="source-L190"></a>反復法は「疎」で「大」  

<a id="source-L192"></a>反復法  
<a id="source-L193"></a>・定常反復法：Jacobi, GS, SOR  
<a id="source-L194"></a>・非定常反復法：CG  


<a id="source-L197"></a>4-2 Jacobi法  
<a id="source-L198"></a>一番簡単  

<a id="source-L200"></a>4-3 Gauss-Seidel法  
<a id="source-L201"></a>計算する際に最新の値を用いる  

<a id="source-L203"></a>4-4 SOR法  
<a id="source-L204"></a>物理やさんがよく使う手法  
<a id="source-L205"></a>わかりにくい  

<a id="source-L207"></a>4-5 反復法の収束  
<a id="source-L208"></a>収束するかわからかんけど、漸化式立ててみたっていうのが上の３つである  
<a id="source-L209"></a>それについて数学的に言える定理がある  

<a id="source-L211"></a>上の3つはHとCの取り方が違うだけ  

<a id="source-L213"></a>4-6 反復法の収束と縮小写像の原理との関係  
<a id="source-L214"></a>縮小写像の原理はBanachの不動点定理ともいう  
<a id="source-L215"></a>実は反復法の収束と縮小写像の原理は関係がある  

<a id="source-L217"></a>4-7 Jacobi法の収束  
<a id="source-L218"></a>Aが狭義優対角であればJacobi法は収束する  

<a id="source-L220"></a>4-8 SOR法の収束  
<a id="source-L221"></a>SOR法の収束のための必要条件 0 &lt; ω &lt; 2  
<a id="source-L222"></a>実際のωは経験則  

<a id="source-L224"></a>4-9 CG法のアルゴリズム  
<a id="source-L225"></a>最急降下法の親戚のようなアルゴリズム  

<a id="source-L227"></a>4-10 CG法の意味1  

<a id="source-L229"></a>4-11 CG法の意味2  

<a id="source-L231"></a>4-12 CG法の直接法的側面と反復法的側面  
<a id="source-L232"></a>非常にうまいアルゴリズムである  

<a id="source-L234"></a>反復法であるが、計算量の上限は有限である  
<a id="source-L235"></a>丸め誤差に弱くなっているので、真の解に行かないこともある  

<a id="source-L237"></a>固有値が全てのにているときに、真の解に近づくスピードがあがる  




<a id="source-L241"></a>

### 第5回 固有値問題の解法


<a id="source-L243"></a>5-1 CG法の収束性  
<a id="source-L244"></a>最急降下方向は真円じゃないとうまくいかないことがあるので、やめましょうというのがCG法である  
<a id="source-L245"></a>CG法では、マルメごさがなければ有限回で終わる！！  
<a id="source-L246"></a>反復法はどういう時に有益かというと、次元数より小さいところで計算を打ち切ることを期待している  
<a id="source-L247"></a>早い場合とは、条件数が小さい場合  
<a id="source-L248"></a>つまり、ドカンを落ちるのを期待している  

<a id="source-L250"></a>実際、CG法を使う時には、そのまま使うわけではなく、前処理というものをする  

<a id="source-L252"></a>5-2 前処理  
<a id="source-L253"></a>CG法では、前処理はパッケージとしてついてくるのでそれを選択できれば良い  
<a id="source-L254"></a>これスキー分解できればもう解けていることになるので、それをどうサボるか考えるのが数理の考え方  

<a id="source-L256"></a>5-3 非対称行列のCG法  
<a id="source-L257"></a>いろいろな研究がされている  
<a id="source-L258"></a>前処理行列がケースバイケースなのが問題である  
<a id="source-L259"></a>フローチャートが存在する  
<a id="source-L260"></a>それを辿っていくとお勧めの方法がわかる  
<a id="source-L261"></a>数値計算では、スーパー解法がなく、ケースバイケースの世界である  
<a id="source-L262"></a>完全だった数学の世界を計算機に入れると辺なことがいっぱい起こる  

<a id="source-L264"></a>5-4 固有値問題の導入  
<a id="source-L265"></a>数学的にわかっていることと計算機で解けることにはギャップがある  
<a id="source-L266"></a>代数方程式の根は係数の摂動で大きく動く  
<a id="source-L267"></a>数学では、不変部分空間を求めるときはjordan標準形を求めることがゴールだが、数値計算ではそうではない  

<a id="source-L269"></a>5-5 相似変換  


<a id="source-L272"></a>5-6 QR法に向かって  

<a id="source-L274"></a>5-7 べき乗法  

<a id="source-L276"></a>5-8 逆反復法  

<a id="source-L278"></a>5-9 Gram-Schmidtの直交化法  

<a id="source-L280"></a>5-10 同時反復法  

<a id="source-L282"></a>5-11 行列のHesseberg化  





<a id="source-L287"></a>

### 第6回 固有値問題、非線型方程式

<a id="source-L288"></a>6-1 QR法の続き1  

<a id="source-L290"></a>6-2 QR法の続き2  

<a id="source-L292"></a>6-3 非線型方程式の導入  

<a id="source-L294"></a>6-4 不動点反復  

<a id="source-L296"></a>6-5 縮小写像の原理の証明  

<a id="source-L298"></a>6-6 縮小写像の原理の解説1  

<a id="source-L300"></a>6-7 縮小写像の原理の解説2  

<a id="source-L302"></a>6-8 Newton法1  

<a id="source-L304"></a>6-9 Newton法2  





<a id="source-L309"></a>

### 第7回 非線型方程式

<a id="source-L310"></a>7-1 Householder変換  

<a id="source-L312"></a>7-2 Householder変換によるHessenberg化  

<a id="source-L314"></a>7-3 Householder変換によるQR分解  

<a id="source-L316"></a>7-4 HessenbergQR法の各反復の計算量  

<a id="source-L318"></a>7-5 Newton法の収束速度  

<a id="source-L320"></a>7-6 関数の近似とは  

<a id="source-L322"></a>7-7 Lagrange補間とは  

<a id="source-L324"></a>7-8 Lagrange補間の表現1  

<a id="source-L326"></a>7-9 Lagrange補間の表現2  

<a id="source-L328"></a>7-10 Lagrange補間の表現3  



<a id="source-L331"></a>

### 第8回 関数の近似と補間

<a id="source-L332"></a>8-1 Lagrange補間の誤差評価  

<a id="source-L334"></a>8-2 誤差評価の定理の証明  

<a id="source-L336"></a>8-3 多項式補間の失敗  

<a id="source-L338"></a>8-4 Lagrange補間の近似度1  

<a id="source-L340"></a>8-5 Lagrange補間の近似度2  

<a id="source-L342"></a>8-6 スプライン補間  

<a id="source-L344"></a>8-7 数値積分の導入  

<a id="source-L346"></a>8-8 補間に基づく積分公式  

<a id="source-L348"></a>8-9 補間に基づく積分公式（重み関数付き）  





<a id="source-L353"></a>

### 第9回 数値積分

<a id="source-L354"></a>9-1 直交多項式の性質  

<a id="source-L356"></a>9-2 Gauss公式  

<a id="source-L358"></a>9-3 Gauss公式の誤差評価  

<a id="source-L360"></a>9-4 DE公式  

<a id="source-L362"></a>9-5 DE公式の離散化誤差  

<a id="source-L364"></a>9-6 DE公式の打ち切り誤差  

<a id="source-L366"></a>9-7 誤差のトレードオフとDE公式の有用性  

<a id="source-L368"></a>9-8 常微分方程式の数値解放  

<a id="source-L370"></a>9-9 解の存在定理  

<a id="source-L372"></a>9-10 高階の常微分方程式  

<a id="source-L374"></a>9-11 陽的Euler法と陰的Euler法  

<a id="source-L376"></a>9-12 台形則と陰的中点則  




<a id="source-L380"></a>

### 第10回 常微分方程式の数値解法

<a id="source-L381"></a>10-1 常微分方程式の数値解法  


<a id="source-L384"></a>10-2 解法の精度（次数）  

<a id="source-L386"></a>10-3 4次Runge-kutta法  

<a id="source-L388"></a>10-4 解法の図示：陽的・陰的Euler法  

<a id="source-L390"></a>10-5 解法の図示：陰的中点則・台形則  

<a id="source-L392"></a>10-6 解法の図示：４次Runge-kutta法  

<a id="source-L394"></a>10-7 多段法  

<a id="source-L396"></a>10-8 安定性の観察  

<a id="source-L398"></a>10-9 安定性解析：陽的中点則  

<a id="source-L400"></a>10-10 安定性解析：陽的・陰的Euler法  

<a id="source-L402"></a>10-11 安定性解析：Runge-kutta法  




<a id="source-L406"></a>

### 第11回 偏微分方程式の数値解法

<a id="source-L407"></a>11-1 マシンイプシロンの数値実験  

<a id="source-L409"></a>11-2 積み残しの数値実験  

<a id="source-L411"></a>11-3 Newton法の数値実験  

<a id="source-L413"></a>11-4 Lagrange補間の数値実験  

<a id="source-L415"></a>11-5 陽的Euler法の数値実験  

<a id="source-L417"></a>11-6 陰的Euler法の数値実験  

<a id="source-L419"></a>11-7 陽的中点則と台形則の数値実験  

<a id="source-L421"></a>11-8 偏微分方程式の型  

<a id="source-L423"></a>11-9 偏微分方程式の数値解法の導入  

<a id="source-L425"></a>11-10 Poisson方程式と差分  

<a id="source-L427"></a>11-11 1次元Poisson方程式に対する差分法  

<a id="source-L429"></a>11-12 2次元Poisson方程式に対する差分法  

<a id="source-L431"></a>11-13 複雑な境界形状の取り扱い  




<a id="source-L435"></a>

### 第12回 偏微分方程式の数値解法


<a id="source-L437"></a>12-1 楕円型偏微分方程式の解法1  

<a id="source-L439"></a>12-2 楕円型偏微分方程式の解法2  

<a id="source-L441"></a>12-3 双曲型偏微分方程式の解法  

<a id="source-L443"></a>12-4 陽的Eulerスキームの安定性  

<a id="source-L445"></a>12-5 その他のスキームの例  

<a id="source-L447"></a>12-6 放物型偏微分方程式の解法  



> <a id="source-L451"></a>「数値解析とは何か？」  

<a id="source-L453"></a>コンピュータは離散的な値しか扱えないので数式ではなく数値によらなければならない  
<a id="source-L454"></a>しかし数値で扱うには誤差などの要因を考えなければならない  

<a id="source-L456"></a>複雑な数式から簡単な代数式に置き換え、解そのものを数値だけで扱う  

<a id="source-L458"></a>誤差→単一方程式→連立方程式→微分積分＋（補完法）→状微分方程式→偏微分方程式  



> <a id="source-L462"></a>機械系数値解析  

<a id="source-L463"></a>Mechanic Numerical Analysis  


<a id="source-L465"></a>

### 1. Simultaneous Equations (Direct method) (連立方程式(直接法))


<a id="source-L466"></a>

### 2. Simultaneous Equations (Iterative method) (連立方程式(反復法))


<a id="source-L467"></a>

### 3. Non-linear problems (非線形方程式の解法)


<a id="source-L468"></a>

### 4. Non-linear problems (非線形方程式の解法)


<a id="source-L469"></a>

### 5. Eigenvalue problems (固有値問題)


<a id="source-L470"></a>

### 6. Numerical Errors (数値誤差)


<a id="source-L471"></a>

### 7. Numerical Difference (差分)


<a id="source-L472"></a>

### 8. Numerical Interpolation (数値補間)


<a id="source-L473"></a>

### 9. Numerical Integration (数値積分)


<a id="source-L474"></a>

### 10. Ordinal Differential Equations (常微分方程式)


<a id="source-L475"></a>

### 11. Eigenvalue problems (固有値問題)


<a id="source-L476"></a>

### 12. Eigenvalue problems (固有値問題)


<a id="source-L477"></a>

### 13. Ordinal Differential Equations (常微分方程式)


<a id="source-L478"></a>

### 14. Partial Differential Equations (偏微分方程式)




<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

問題そのものの敏感さ（条件）と、アルゴリズムが誤差をどう増幅するか（安定性）を区別する。可逆行列 $A$ の条件数は、選んだ行列ノルムに対して $\kappa(A)=\|A\|\,\|A^{-1}\|$。原文の「ノルムが大きい」という説明には、この積とノルムの指定を補う。相対残差が小さくても、悪条件なら相対誤差が大きいことがある。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [同じ分野のノート](README.md)：最適化・数値計算。

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
