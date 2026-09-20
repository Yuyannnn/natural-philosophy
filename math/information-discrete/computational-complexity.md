---
title: "計算量理論"
status: draft
tags: [scrapbox, information-discrete]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E8%A8%88%E7%AE%97%E9%87%8F%E7%90%86%E8%AB%96"
source_created: "2023-01-16T06:47:19Z"
source_updated: "2024-12-18T17:27:09Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 計算量理論

計算できること・効率よく計算できることを区別するための記録。

原ページ作成：2023-01-16 ／ 最終更新：2024-12-18（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/computational-complexity.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E8%A8%88%E7%AE%97%E9%87%8F%E7%90%86%E8%AB%96)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<details>
<summary>本文の見出しから探す</summary>

- [1.チューリングマシン](#source-L44)
- [1. 和集合演算](#source-L88)
- [2. 連結演算](#source-L89)
- [3. スター演算](#source-L90)
- [1. アルファベットΣに属するa](#source-L95)
- [2. ε](#source-L96)
- [3. ゼロ集合](#source-L97)
- [4. R1とR2を正規表現としてR1UR2](#source-L98)
- [5. ..R1⚪︎R2](#source-L99)
- [6. ..R1*](#source-L100)
- [1. i&gt;=0について xy^iz ∈ A](#source-L114)
- [2. |y| &gt; 0 (⇔ y ∈/ ε)](#source-L115)
- [3. |xy| &lt;= p ](#source-L116)
- [1. Vは変数の有限集合](#source-L126)
- [2. Σは終端記号の有限集合](#source-L127)
- [3. Rは書き換え規則の有限集合](#source-L128)
- [4. Sは開始記号の有限集合](#source-L129)
- [1.多テープTM(MTL)](#source-L181)
- [2.非決定性チューリングマシン(NDTM)](#source-L185)
- [1.TMで実行できる](#source-L191)
- [2.解法がある（解くTMがある）](#source-L192)
- [1. 後者関数](#source-L272)
- [2. ゼロ関数](#source-L273)
- [3. 射影関数](#source-L274)
- [1. 合成](#source-L276)
- [2. 原始帰納](#source-L277)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 計算量理論

<a id="source-L2"></a>[競技プログラミング](https://scrapbox.io/MistMavGamer/%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0)  
<a id="source-L3"></a>[情報理論](information-theory.md)  
<a id="source-L4"></a>[記号論理学(数学基礎論の基礎of基礎?)](../foundations/symbolic-logic.md)  
<a id="source-L5"></a>[コンピュータの基礎](https://scrapbox.io/MistMavGamer/%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF%E3%81%AE%E5%9F%BA%E7%A4%8E)  


<a id="source-L8"></a>計算論を知っていると、プログラミングで使える正規表現の限界を理解できる  

<a id="source-L10"></a>判定に必要な時間によって言語を分類するためクラスを導入する  
<a id="source-L11"></a>t:N⇨R^tとすると、TIME(t(n))はO(t(n))時間TM（単一テープTM）で判定される全ての言語の集合を表す  
<a id="source-L12"></a>t(n)をt(n)&gt;nである関数とする。全てのt(n)時間複数テープTMに対して、O(t(n)^2)時間単一テープTMが存在する  
<a id="source-L13"></a>非決定性TMに関する計算時間を考える  
<a id="source-L14"></a>NをNDTM Nを判定装置とする。Nの動作時間がf(n)であるとは、長さnの入力に対する計算で使う最大ステップ数である  
<a id="source-L15"></a>全てのt(n)時間NDTMに対して、それと等価な2^O(t(n))時間単一テープNDTMが存在する  

<a id="source-L17"></a>・クラスP  
<a id="source-L18"></a>Pは決定性単一テープTMで多項式時間で判定できる問題の集合である  
<a id="source-L19"></a>Pは現実的に解ける問題のクラスにほぼ対応  


<a id="source-L22"></a>言語は非決定性多項式時間TMで判定されるとき、かつそのときに限り言語はNPである  

<a id="source-L24"></a>NPは多項式時間検証装置を持つ言語のクラス  
<a id="source-L25"></a>HAMPATHはNP  

> <a id="source-L27"></a>P：要素があるかどうかを多項式時間で判定できる  

<a id="source-L28"></a>NP：要素であることを多項式時間で検証できる、要素かどうかをNDTMで多項式時間で判定できる  

<a id="source-L30"></a>NP完全性  
<a id="source-L31"></a>NPの中で一番難しい問題のクラス、P/=Nと信じらレているので、ある問題がNP完全であれば、多項式時間で解けない可能性が高い  

<a id="source-L33"></a>充足可能性問題(SAT)  
<a id="source-L34"></a>論理式をTrueに評価するような変数の割り当てが存在するとき、その式は充足可能という  

<a id="source-L36"></a>Cook Levinの定理  
<a id="source-L37"></a>SATはNP完全である  
<a id="source-L38"></a>P=NPのとき、かつそのときに限りSATがPに含まれる  

<a id="source-L40"></a>次回は一時間ぐらいでCook Levinの定理の証明をする  




<a id="source-L44"></a>

### 1.チューリングマシン


<a id="source-L46"></a>計算論＝TMの限界を知る  

<a id="source-L48"></a>・アルファベット  
<a id="source-L49"></a>記号の有限集合をアルファベットといい、Σで表す。文字列とは、アルファベットを重複を許して並べたもの  
<a id="source-L50"></a>長さが0の文字列を空列という  
<a id="source-L51"></a>空列は空集合とは違う  

<a id="source-L53"></a>・言語  
<a id="source-L54"></a>言語とはアルファベット上の有限・無限集合を表す  
<a id="source-L55"></a>Mを機械とし、言語AをMが受理する全ての文字列の集合とすると、言語AはMの言語であるといい、L(M)=Aで表す  

<a id="source-L57"></a>・有限オートマトン  
<a id="source-L58"></a>有限個の状態と遷移動作  

<a id="source-L60"></a>・決定性有限オートんマトン(DFA:Deterministic Finite Automation)  
<a id="source-L61"></a>与えられた文字列xを読み込み最後に受理または拒否を表す  
<a id="source-L62"></a>あるDFAで受理される言語を正規言語という  
<a id="source-L63"></a>M = (Q, Σ, δ, q0, F)  
<a id="source-L64"></a>Qは状態の有限集合  
<a id="source-L65"></a>Σはアルファベットの有限集合  
<a id="source-L66"></a>δはQとΣを引数とする遷移関数  
<a id="source-L67"></a>q0は開始状態  
<a id="source-L68"></a>Fは受理状態の集合  

<a id="source-L70"></a>・非決定性有限オートマトン(NFA: Nondeterministic Finite Automation)  
<a id="source-L71"></a>DFAは入力文字を読むと状態が一意に決まるがNFAでは複数の選択肢がある  
<a id="source-L72"></a>DFAは状態と入力文字に対して、次の状態を与える  
<a id="source-L73"></a>NFAは状態と入力文字または空列に対して次の状態集合を与える  
<a id="source-L74"></a>P(Q)ですべての部分集合の集合を表す（べき集合）  
<a id="source-L75"></a>Σε = ΣU{ε}とする  
<a id="source-L76"></a>NFAの遷移関数はδ:Q×Σε→P(Q)  
<a id="source-L77"></a>NFAも(Q, Σ, δ, q0, F)で与えられる  
<a id="source-L78"></a>入力を終了した時点でどれか１つでも受理状態にあればNFAは入力を受理する  

<a id="source-L80"></a>・NFAとDFAの等価性  
<a id="source-L81"></a>DFAとNFAは同じ言語クラスを受理する  
<a id="source-L82"></a>証明のアイディア：NFAのk個の状態に対して部分集合を2^k個列挙しDFAに変換する  
<a id="source-L83"></a>よってあるNFAによって受理される言語も正規言語である  

<a id="source-L85"></a>・正規演算  
<a id="source-L86"></a>言語の対する演算  
<a id="source-L87"></a>AとBを言語とすると、以下の３つの演算を正規演算という  

<a id="source-L88"></a>

### 1. 和集合演算


<a id="source-L89"></a>

### 2. 連結演算


<a id="source-L90"></a>

### 3. スター演算

<a id="source-L91"></a>正規言語は正規演算に対して閉じている  

<a id="source-L93"></a>・正規表現(Refular Expression)  
<a id="source-L94"></a>正規言語を記述するための言語、正規表現は帰納的に定義される  

<a id="source-L95"></a>

### 1. アルファベットΣに属するa


<a id="source-L96"></a>

### 2. ε


<a id="source-L97"></a>

### 3. ゼロ集合


<a id="source-L98"></a>

### 4. R1とR2を正規表現としてR1UR2


<a id="source-L99"></a>

### 5. ..R1⚪︎R2


<a id="source-L100"></a>

### 6. ..R1\*

<a id="source-L101"></a>言語は正規表現で記述される時かつその時に限り正規  

<a id="source-L103"></a>・RE⇨NFAの変換  

<a id="source-L105"></a>・NFA⇨RE  

<a id="source-L107"></a>・非正規言語  
<a id="source-L108"></a>有限オートマトンは状態が有限個なので、認識可能な言語は限られる  
<a id="source-L109"></a>数学的にある言語が正規でないことを示す方法がある  
<a id="source-L110"></a>ポンピング補題はすべての正規言語が満たすべき定理  

<a id="source-L112"></a>・ポンピング補題  
<a id="source-L113"></a>Aが正規言語ならば、ある数P（ポンピング長）が存在して、Sが少なくとも長さPであるAの任意の文字列であるときにSは以下の条件を満たす断片s = xyzに分割できる  

<a id="source-L114"></a>

### 1. i&gt;=0について xy^iz ∈ A


<a id="source-L115"></a>

### 2. |y| &gt; 0 (⇔ y ∈/ ε)


<a id="source-L116"></a>

### 3. |xy| &lt;= p 


<a id="source-L118"></a>・捕捉  
<a id="source-L119"></a>機械Mが言語Aを認識する⇔AがMの受理するすべての文字列である L(M) = A  

<a id="source-L121"></a>・文脈自由文法(CFG:Context Free Grammar)  
<a id="source-L122"></a>CFGは正規表現より複雑な言語を生成可能  
<a id="source-L123"></a>CFGは人の元gのを解析するために考案されたモデル  
<a id="source-L124"></a>CFGはプッシュダウンオートマトンPDAと同じクラスの言語を認識可能である  
<a id="source-L125"></a>CFGは(V, Σ, R, S)で定義される  

<a id="source-L126"></a>

### 1. Vは変数の有限集合


<a id="source-L127"></a>

### 2. Σは終端記号の有限集合


<a id="source-L128"></a>

### 3. Rは書き換え規則の有限集合


<a id="source-L129"></a>

### 4. Sは開始記号の有限集合

<a id="source-L130"></a>書き換え規則は A→αで表現される  
<a id="source-L131"></a>Rを開始記号Sに適用することで文を生成する  

<a id="source-L133"></a>・正規言語⊂文脈自由言語  
<a id="source-L134"></a>任意の正規言語Lに対して、それを受理するDFAからLを生成するCFGを構成できる  

<a id="source-L136"></a>・最左導出  
<a id="source-L137"></a>言語Gの文字列wの導出において、最左の変数に規則を適用する制限  
<a id="source-L138"></a>最左導出という制限でも文法Gが生成するすべての文字列なら導出可  
<a id="source-L139"></a>文字列wが2つ以上最左導出を持つ場合、その文法は曖昧であるという  

<a id="source-L141"></a>・チョムスキー標準形(CNF:Chomsky Normal Form)  
<a id="source-L142"></a>CFGの書き換え規則は様々であるが、CNFは標準化した記法  

<a id="source-L144"></a>・グライバッハ標準形(GNF:Greibach Normal Form)  

<a id="source-L146"></a>・一般のCFGからCNFへの変換  

<a id="source-L148"></a>・CFGのポンピング補題  

<a id="source-L150"></a>・プッシュダウンオートマトン(PDA:Push Down Automation)  
<a id="source-L151"></a>NFAと似たオートマトンでスタックと呼ばれる記憶装置を持つPDAとCFGの能力は等しい  
<a id="source-L152"></a>PFAとCFGの能力は等しい  
<a id="source-L153"></a>スタックはLast In First Outである  
<a id="source-L154"></a>PDAは M = (Q, Σ, Γ, δ, q0, Z0, F)で表される  

<a id="source-L156"></a>・CFGとPDAの等価性  
<a id="source-L157"></a>あるPDAがある言語を受理するときかつそのときに限り、言語は文脈自由  

<a id="source-L159"></a>・チューリングマシン  
<a id="source-L160"></a>TMは無限の長さを持つテープと、テープに対して読み書きする制御部（ヘッド）から構成される  
<a id="source-L161"></a>TMはテープに読み書き両方ができる  
<a id="source-L162"></a>ヘッドは左右どちらにも動ける  
<a id="source-L163"></a>テープの長さは無限  
<a id="source-L164"></a>拒否・受理状態になると停止する  
<a id="source-L165"></a>TMは (Q, Σ, Γ, δ, q\_0, q\_accept, q\_reject)で定義される  
<a id="source-L166"></a>TMは入力がテープに書き込まれた状態からスタートする（左端から書き込まれ、他は空白）  
<a id="source-L167"></a>テープに現れる最初の空白文字は入力の終わりを意味する  
<a id="source-L168"></a>テープの左端よりもさらに左には移動できない  

<a id="source-L170"></a>・ヘッドの移動  

<a id="source-L172"></a>・チューリング認識とチューリング判定  
<a id="source-L173"></a>チューリングマシンMが受理する文字列の集合をMの言語といい、L(M)と表す  
<a id="source-L174"></a>言語に対して、それを受理するTMがある場合、チューリング認識という  
<a id="source-L175"></a>TMは受理、拒否、停止しないの３つの場合がある  
<a id="source-L176"></a>受理、拒否を行う機械を判定装置という  
<a id="source-L177"></a>任意の言語に対してそれを判定するTMがある場合、チューリング判定可能という  
<a id="source-L178"></a>チューリング認識は止まるとは限らず、チューリング判定は必ず止まるという違いに注意  

<a id="source-L180"></a>・TMのバリエーション  

<a id="source-L181"></a>

### 1.多テープTM(MTL)

<a id="source-L182"></a>複数のテープを持つ。初期状態ではテープ１に入力が書いてある  
<a id="source-L183"></a>MTMの遷移関数は複数のテープに対してδ系る  
<a id="source-L184"></a>MTMはTMでシュミレート可能  

<a id="source-L185"></a>

### 2.非決定性チューリングマシン(NDTM)

<a id="source-L186"></a>NFAと同様に非決定的な遷移関数を持つ  
<a id="source-L187"></a>NDTMの能力はDTMの能力と等しい  

<a id="source-L189"></a>・アルゴリズム  
<a id="source-L190"></a>チャーチチューリングの提唱から以下のように定義される  

<a id="source-L191"></a>

### 1.TMで実行できる


<a id="source-L192"></a>

### 2.解法がある（解くTMがある）


<a id="source-L194"></a>・判定可能性  
<a id="source-L195"></a>正規言語について  
<a id="source-L196"></a>DFAの受理問題を考える  
<a id="source-L197"></a>文脈自由言語について  

<a id="source-L199"></a>・停止問題  
<a id="source-L200"></a>判定できない言語が存在する  

<a id="source-L202"></a>・対角線論法  
<a id="source-L203"></a>可算無限集合：自然数Nと１対１対応あり  
<a id="source-L204"></a>不可算無限集合：自然数Nと１対1対応なし  

<a id="source-L206"></a>・チューリング認識できない言語  

<a id="source-L208"></a>・停止問題の判定不可能性  

<a id="source-L210"></a>・チューリング認識できない言語の具体例  

<a id="source-L212"></a>・計算量  
<a id="source-L213"></a>ある問題が判定可能であるとき、判定するまでに必要なステップ数の最悪ケース  
<a id="source-L214"></a>Mをすべての入力で停止するTMとする  
<a id="source-L215"></a>Mの計算量は f:N→Nによって表される  
<a id="source-L216"></a>f(N)は長さNの入力に対してMの判定に必要な最大ステップ数  
<a id="source-L217"></a>f(n)の厳密な計算は難しいので漸近的な記法を用いる  

<a id="source-L219"></a>・クラス  
<a id="source-L220"></a>判定に必要な時間によって言語を分類するためにクラスを導入する  
<a id="source-L221"></a>tをt: N→RとするとTIME(t(n))はO(t(n))時間TMで判定されるすべての言語の集合である  
<a id="source-L222"></a>t(n)をt(n) &gt;= nである関数とする  
<a id="source-L223"></a>すべてのt(n)時間複数テープTMに対して、等価なO(t(n^2))時間単一テープTMが存在する  
<a id="source-L224"></a>同様に非決定性TMに関する計算時間を考える  
<a id="source-L225"></a>NをNDTMの判定装置とする  
<a id="source-L226"></a>Nの動作時間がf(n)であるとは、長さnの入力に対する計算の枝においてNが使う最大ステップ数がf(n)であることをいう  
<a id="source-L227"></a>NDTMで判定可能な問題はDTMでも判定可能  
<a id="source-L228"></a>必要な計算時間は異なる  
<a id="source-L229"></a>t(n)をt(n)&gt;=nである関数とすると、すべてのt(n)時間NDTMに対して、等価な2^O(t(n))時間単一テープDTMが存在する  

<a id="source-L231"></a>・クラスP  
<a id="source-L232"></a>指数関数か多項式関数かのみで分類する  
<a id="source-L233"></a>クラスPとは単一テープDTMで多項式時間で判定できる問題の集合である  
<a id="source-L234"></a>問題の符号化：TMに問題を与えるとき、問題を文字列にするが、多項式時間の変換を仮定する  

<a id="source-L236"></a>・クラスNP  
<a id="source-L237"></a>HAMPATH問題のこと  
<a id="source-L238"></a>HamiltonPathが多項式時間で解けるかどうかはまだわかっていない  
<a id="source-L239"></a>HamiltonPathは多項式時間検証可能性という特徴を持つ  

<a id="source-L241"></a>・検証装置  
<a id="source-L242"></a>言語AをアルゴリズムVを用いて、以下のように定義できるとき、VをAの検証装置という  
<a id="source-L243"></a>A = {w | vはある文字列cに対して&lt;w, c&gt;を受理}  
<a id="source-L244"></a>cは補助情報、言語が多項式時間検証装置を持つとき、多項式検証言語という  
<a id="source-L245"></a>クラスNPは多項式時間検証装置を持つ言語のクラスである  
<a id="source-L246"></a>NPはNondeterministic Polynomial Timeに由来する  
<a id="source-L247"></a>NDTMによっても定義される  

<a id="source-L249"></a>・NPの２つの定義が等しいことの証明  

<a id="source-L251"></a>・NP完全性  
<a id="source-L252"></a>NPの中で一番難しい問題のクラス  
<a id="source-L253"></a>P /= であることが信じられているのでNP完全なら、多項式時間で解けない強力な根拠となる  

<a id="source-L255"></a>・多項式時間帰着可能性  
<a id="source-L256"></a>任意の入力wに対して、f(w)を計算して停止する多項式時間TMがあるとき、fは多項式時間計算可能関数という  
<a id="source-L257"></a>言語Aと言語  

<a id="source-L259"></a>・COOK-LEVINの定理  
<a id="source-L260"></a>SATはNP完全である  
<a id="source-L261"></a>計算機自体をシミュレートし、その動作をSATに落としこむ  

<a id="source-L263"></a>・帰納関数論  
<a id="source-L264"></a>これまで、TMを考えることで計算を考えてきた  
<a id="source-L265"></a>これに対して、帰納関数では基本的な関数をもとに複雑な関数を構成する  
<a id="source-L266"></a>これらの操作で得られる関数を帰納関数という  
<a id="source-L267"></a>TMで計算可能　＝　帰納関数  

<a id="source-L269"></a>・原始帰納関数（PRF）  
<a id="source-L270"></a>帰納関数を構成する基本的関数をPRFという  
<a id="source-L271"></a>PRFは３つの初期関数から作られる  

<a id="source-L272"></a>

### 1. 後者関数


<a id="source-L273"></a>

### 2. ゼロ関数


<a id="source-L274"></a>

### 3. 射影関数

<a id="source-L275"></a>PRFは２つの操作に関して閉じている  

<a id="source-L276"></a>

### 1. 合成


<a id="source-L277"></a>

### 2. 原始帰納


<a id="source-L279"></a>・定理 すべてのPRFはTMで計算できる  

<a id="source-L281"></a>・最小化関数  
<a id="source-L282"></a>条件を満たす最小の自然数を探す関数  

<a id="source-L284"></a>・割り算  
<a id="source-L285"></a>普通の割り算は全域関数ではない  
<a id="source-L286"></a>そこで以下の割り算を考える  

<a id="source-L288"></a>・ゲーデル数  
<a id="source-L289"></a>数の列を１つの数に一意にエンコードする方法  

<a id="source-L291"></a>・計算可能部分関数  
<a id="source-L292"></a>PRFは全域関数である  
<a id="source-L293"></a>よってすべての入力に対して権威さんして値を返す  
<a id="source-L294"></a>しかしTMは入力によっては停止しない  
<a id="source-L295"></a>よってPRFの集合でTMに含まれない計算できる関数の集合  

<a id="source-L297"></a>・限定なしの最小化関数  
<a id="source-L298"></a>以前の最小化関数は探索が限られていたが、その限定を外したもの  

<a id="source-L300"></a>・帰納関数（μRF）  
<a id="source-L301"></a>全域関数であるPRFを部分関数に拡張したもの  
<a id="source-L302"></a>PRFに限定なし最小化を入れたもの  

<a id="source-L304"></a>・すべてのμRFはTMによって計算可能⇔μRFとして定義できない関数は計算できない  

<a id="source-L306"></a>・λ計算  
<a id="source-L307"></a>計算モデルの１つで、計算を作用と抽象化でモデル化したもの  
<a id="source-L308"></a>λ計算 by チャーチ→ML,Lisp  
<a id="source-L309"></a>帰納関数 by エルブラン、ゲーデル、クリーね  
<a id="source-L310"></a>TM by チューリング →Fortran, Pascal  

<a id="source-L312"></a>・λ計算の定義  

<a id="source-L314"></a>・作用  

<a id="source-L316"></a>・抽象化  

<a id="source-L318"></a>・省略記法  

<a id="source-L320"></a>・β簡約  

<a id="source-L322"></a>・λ計算の能力  

<a id="source-L324"></a>・μRFに必要な関数  

<a id="source-L326"></a>・初期関数はλ定義可能  

<a id="source-L328"></a>・λ定義可能な関数は合成に対して閉じている  

<a id="source-L330"></a>・不動点定理  
<a id="source-L331"></a>原始帰納のために必要な定理  

<a id="source-L333"></a>・原始帰納はλ定義可能関数に対して閉じている  

<a id="source-L335"></a>・最小化関数はλ定義可能  

<a id="source-L337"></a>・簡約  

<a id="source-L339"></a>・チャーチ・ロッサーの定理  

<a id="source-L341"></a>・正規化定理  
<a id="source-L342"></a>Mがβ-nfを持つならば、最左β基を簡約することでβ-nfが得られる  

<a id="source-L344"></a>・λ計算における部分関数  






> <a id="source-L351"></a>Neural Networks and the Chomsky Hierarchy  

<a id="source-L352"></a><https://arxiv.org/abs/2207.02098>  







> <a id="source-L360"></a>PCP定理とその証明 (証明概要編)  

<a id="source-L361"></a><https://mathlog.info/articles/VkzP9IiwDislThzr2FZ0>  










<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

NPは「多項式時間で解けない問題」の略ではない。多項式時間で検証できる証拠を持つ判定問題として捉え、Pとの関係を区別する。PとNPが等しいかは、[Clay Mathematics Instituteの問題ページ](https://www.claymath.org/millennium/p-vs-np/)で未解決とされている（2026-09-20確認）。本文の「P/=N」は文脈上PとNPの比較と読む。多項式時間でも実用上遅いことがあり、NP困難でも特定の入力は解きやすいことがある。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [情報理論](information-theory.md)
- [記号論理学(数学基礎論の基礎of基礎?)](../foundations/symbolic-logic.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
