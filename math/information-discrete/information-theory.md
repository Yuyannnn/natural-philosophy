---
title: "情報理論"
status: draft
tags: [scrapbox, information-discrete]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E6%83%85%E5%A0%B1%E7%90%86%E8%AB%96"
source_created: "2023-01-16T06:44:02Z"
source_updated: "2025-06-09T02:09:08Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 情報理論

情報を量として捉え、符号化・エントロピー・量子情報へ進む記録。

原ページ作成：2023-01-16 ／ 最終更新：2025-06-09（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/information-theory.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E6%83%85%E5%A0%B1%E7%90%86%E8%AB%96)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 情報理論

<a id="source-L2"></a>[統計的機械学習](../probability-statistics/statistical-machine-learning.md)  
<a id="source-L3"></a>[信号処理工学](https://scrapbox.io/MistMavGamer/%E4%BF%A1%E5%8F%B7%E5%87%A6%E7%90%86%E5%B7%A5%E5%AD%A6)  
<a id="source-L4"></a>[確率](../probability-statistics/probability.md)  
<a id="source-L5"></a>[統計学](../probability-statistics/statistics.md)  
<a id="source-L6"></a>[画像符号化](https://scrapbox.io/MistMavGamer/%E7%94%BB%E5%83%8F%E7%AC%A6%E5%8F%B7%E5%8C%96)  
<a id="source-L7"></a>[計算量理論](computational-complexity.md)  
<a id="source-L8"></a>[量子情報](https://scrapbox.io/MistMavGamer/%E9%87%8F%E5%AD%90%E6%83%85%E5%A0%B1)  
<a id="source-L9"></a>[next-token predictionはAGIの夢を見るか？](https://scrapbox.io/MistMavGamer/next-token%20prediction%E3%81%AFAGI%E3%81%AE%E5%A4%A2%E3%82%92%E8%A6%8B%E3%82%8B%E3%81%8B%EF%BC%9F)  
<a id="source-L10"></a>[熱力学](https://scrapbox.io/MistMavGamer/%E7%86%B1%E5%8A%9B%E5%AD%A6)  
<a id="source-L11"></a>[情報熱力学](https://scrapbox.io/MistMavGamer/%E6%83%85%E5%A0%B1%E7%86%B1%E5%8A%9B%E5%AD%A6)  
<a id="source-L12"></a>[関数解析](../analysis/functional-analysis.md)  
<a id="source-L13"></a>[微分積分学](../analysis/calculus.md)  



> <a id="source-L17"></a>基本  

<a id="source-L18"></a>あるデータがあった時にそのデータの情報量を定量的に評価できるようになることが情報理論の柱である。これによって情報技術をサイエンスとして扱える  

<a id="source-L20"></a>chapter1 情報源符号化  
<a id="source-L21"></a>どれだけ効率的に符号化できるのかを考えるのがこの章の内容  

<a id="source-L23"></a>離散数学的な証明は図で書くとわかるが、定式化で解こうとすると難しい  

<a id="source-L25"></a>D元情報源符号化とは写像 C: X→D\*のこと  
<a id="source-L26"></a>C(x)をxに対する符号語  
<a id="source-L27"></a>Cが単射のとき正則であるという  
<a id="source-L28"></a>Cの拡張C\*を定める  

<a id="source-L30"></a>w1がw2の語頭であるとは、あるvについてw2 = w1 || vとなること  

<a id="source-L32"></a>語頭符号＝接頭符号＝瞬時符号  

<a id="source-L34"></a>Cについて語頭符号→一意復号可能→正則  

<a id="source-L36"></a>Cが一意復号可能であれば、クラフトの不等式が成り立つ  

<a id="source-L38"></a>Cを一意復号可能とすると語頭符号　Cで、大きさが同じとなるものが存在する  


<a id="source-L41"></a>Xに対する符号Cの平均符号語長を定める L(C)  
<a id="source-L42"></a>L(C)を最小化したい  

<a id="source-L44"></a>D元ハフマン符号を以下で構成する  

<a id="source-L46"></a>定理1.5  
<a id="source-L47"></a>(1)C1,C2をXに対するハフマン符号とするとC1,C2は語頭符号で、L(C1) = L(C2)  
<a id="source-L48"></a>(2)CをXのD元一意復号可能符号、ChをXのハフマン符号とするとL(Ch)&lt;=L(C)  

<a id="source-L50"></a>Xの情報エントロピー（シャノンエントロピー）を H(X) = - Σp(xi)log2p(xi)で定義  

<a id="source-L52"></a>Iを実線型空間の凸集合とすると、f:I→Rが下に凸であるとは、f(λx + (1-λ)y) &lt;= λf(x) + (1-λ)f(y)  

<a id="source-L54"></a>定理 Jensenの定理  

<a id="source-L56"></a>補題1.7  
<a id="source-L57"></a>f:\[a,b\]→Rが連続、(a,b)上で二回微分可能かつf’’&gt;0であれば、fは\[a,b\]上で真に下に凸  

<a id="source-L59"></a>命題1.8   
<a id="source-L60"></a>(1)エントロピー関数は真に上に凸である  
<a id="source-L61"></a>(2)H(p1,…,pn) &lt;= log2nで等号成立  

<a id="source-L63"></a>定義  
<a id="source-L64"></a>X上のX,Yのカルバック・ライブラー情報量  

<a id="source-L66"></a>定理1.9  
<a id="source-L67"></a>D(p||q) &gt;= 0で等号 ⇄ p=q  


<a id="source-L70"></a>エントロピー関数を使えば、ハフマン符号長の評価ができる  

<a id="source-L72"></a>通信路符号化  
<a id="source-L73"></a>AカラBに情報を送るとき、ある形にエンコードして情報を送れば少しぐらいノイズが混じっても復元できるように  
<a id="source-L74"></a>通信路について数学的に表現していく  

<a id="source-L76"></a>定理1.10  
<a id="source-L77"></a>r.v. Xに対する一意復号可能なD元符号Cについて、L(C) &gt;= (1/log2D) \* H(X)  

<a id="source-L79"></a>定理1.11  
<a id="source-L80"></a>r.v. X上のD元ハフマン符号Cについて、  


<a id="source-L83"></a>chapter2 通信路符号化定理  

<a id="source-L85"></a>定義  
<a id="source-L86"></a>離散無記憶通信路とは、x∈Xごとに定まるY上の条件付き確率関数の族のことと定める  

<a id="source-L88"></a>定義  
<a id="source-L89"></a>・メッセージ集合  
<a id="source-L90"></a>・符号化関数 Enc  
<a id="source-L91"></a>・復号関数 Dec  
<a id="source-L92"></a>の組Cを通信路符号という  
<a id="source-L93"></a>Cのレートを R = log2M/n  
<a id="source-L94"></a>復号誤り確率を err(w) = Σ p(y | Enc(w))で定める  

<a id="source-L96"></a>定義  
<a id="source-L97"></a>達成可能なレートRの上限をこの通信路の容量という  

<a id="source-L99"></a>定義  
<a id="source-L100"></a>条件付きエントロピー  
<a id="source-L101"></a>相互情報量  

<a id="source-L103"></a>定理2.2 通信路符号化定理  
<a id="source-L104"></a>離散無記憶通信路を一つ固定する  
<a id="source-L105"></a>I = supI(X;Y)とすると、この通信路の容量はIである  

<a id="source-L107"></a>マルコフの不等式  

<a id="source-L109"></a>大数の弱法則  

<a id="source-L111"></a>通信路符号化定理  

<a id="source-L113"></a>命題2.3  
<a id="source-L114"></a>(1)I(X, Y)はp(y | x)を固定するとpxについて連続で上に凸  
<a id="source-L115"></a>(2)I(X;Y)は、p(y|x)を固定するとpxについて連続、上に凸  
<a id="source-L116"></a>(3)I(X;Y)はpxを固定するとp(y|x)について連続、下に凸  

<a id="source-L118"></a>補題2.4 マルコフの不等式  

<a id="source-L120"></a>定理2.5 大数の弱法則  

<a id="source-L122"></a>通信路符号化定理(1)  

<a id="source-L124"></a>補題2.6  

<a id="source-L126"></a>定義 条件付き相互情報量  

<a id="source-L128"></a>補題2.7 連鎖律  

<a id="source-L130"></a>定義 マルコフ連鎖  
<a id="source-L131"></a>X1 → X2 → X3(M.C.)  
<a id="source-L132"></a>X2の値が決まっているとき、X1とX3は独立  

<a id="source-L134"></a>補題2.8 マルコフ連鎖の拡張  

<a id="source-L136"></a>命題2.9  
<a id="source-L137"></a>マルコフ連鎖のときの相互情報量  

<a id="source-L139"></a>定理2.10 ファノの不等式  

<a id="source-L141"></a>通信路符号化定理(2)  


<a id="source-L144"></a>chapter3 具体的な通信路符号化方式  
<a id="source-L145"></a>離散無記憶通信路を仮定する。メッセージMに対する平均復号誤り確率をなるべく小さくしたい  

<a id="source-L147"></a>定義  
<a id="source-L148"></a>Enc:μ → C と M上のr.v. Mについて、受診後yに対する最尤復号を定義する  

<a id="source-L150"></a>命題3.1  
<a id="source-L151"></a>最尤復号と別の復号関数の関係  

<a id="source-L153"></a>定義  
<a id="source-L154"></a>q元線型符号  
<a id="source-L155"></a>符号集合 C = Enc(μ)がF  

<a id="source-L157"></a>定義  
<a id="source-L158"></a>ハミング距離、ハミング重み  

<a id="source-L160"></a>命題3.2  
<a id="source-L161"></a>ハミング距離の性質  

<a id="source-L163"></a>定義  
<a id="source-L164"></a>最小距離復号:d(w,y)が最小となるw∈Cに復号する方法  

<a id="source-L166"></a>定理3.3  
<a id="source-L167"></a>一様なメッセージ分布について最小距離復号は最尤復号である  

<a id="source-L169"></a>定義  
<a id="source-L170"></a>t重誤り訂正符号  

<a id="source-L172"></a>定理3.4  
<a id="source-L173"></a>Cを線型符号とし、dmin = dmin(C) = min  

<a id="source-L175"></a>補題3.5 チェルノフの不等式  

<a id="source-L177"></a>定義  
<a id="source-L178"></a>パリティ検査行列  
<a id="source-L179"></a>シンドローム  

<a id="source-L181"></a>補題3.6  
<a id="source-L182"></a>シンドローム復号  


<a id="source-L185"></a>定義  
<a id="source-L186"></a>生成行列  

<a id="source-L188"></a>リード・ソロモン符号  

<a id="source-L190"></a>定義  
<a id="source-L191"></a>リードソロモン符号を定める  

<a id="source-L193"></a>命題3.7  
<a id="source-L194"></a>リードソロモン復号について  

<a id="source-L196"></a>ユークリッド復号  

<a id="source-L198"></a>定理3.9  
<a id="source-L199"></a>ユークリッド復号はt個以下の誤りを訂正できる  

<a id="source-L201"></a>補題3.8  


<a id="source-L204"></a>chapter4 有歪み情報源符号化  

<a id="source-L206"></a>歪み関数 d(x,x\_hat) = 1/n(Σd(xi, xi\_hat))  

<a id="source-L208"></a>定義  
<a id="source-L209"></a>(2^nR, n)レート歪み符号とは、  
<a id="source-L210"></a>・符号化関数 fn: X → μ  
<a id="source-L211"></a>・再生関数 gn: μ → X\_hat  
<a id="source-L212"></a>の組C  
<a id="source-L213"></a>Cの歪みを D(C) = Ex\[d(X^n, gn(fn(X^n)))\]と定める  

<a id="source-L215"></a>定義  
<a id="source-L216"></a>R = レート歪み関数  

<a id="source-L218"></a>定義  
<a id="source-L219"></a>情報レート歪み関数  
<a id="source-L220"></a>上のinfを実現するp(x\_hat|x)が存在する  

<a id="source-L222"></a>定理（レート歪み定理）  
<a id="source-L223"></a>(1)  
<a id="source-L224"></a>(2)  

<a id="source-L226"></a>補題4.2  
<a id="source-L227"></a>式？  


<a id="source-L230"></a>定理4.1 Rについて  

<a id="source-L232"></a>命題4.3  


<a id="source-L235"></a>系4.4  


<a id="source-L238"></a>計算と情報  

<a id="source-L240"></a>チューリングマシン  
<a id="source-L241"></a>δ:{内部状態}✖️{文字}　→ {内部状態} ✖️ {文字} ✖️ {移動}  

<a id="source-L243"></a>事実  
<a id="source-L244"></a>この計算モデルは他の自然な計算モデルと等価  

<a id="source-L246"></a>定義  
<a id="source-L247"></a>万能チューリング機械とは、組(&lt;M&gt;, x)を入力とする TM Uで、  
<a id="source-L248"></a>・M(x)が停止するときU(&lt;M&gt;, x)も停止してM(x)を出力  
<a id="source-L249"></a>・しないとき、出力しない  

<a id="source-L251"></a>事実  
<a id="source-L252"></a>万能チューリング機械は存在する  

<a id="source-L254"></a>定義  
<a id="source-L255"></a>TM Mに関するビット列 s のコルモゴロフ複雑度Km(s)を  
<a id="source-L256"></a>Km(s) = min{|x| : M(x) = s}で定める  

<a id="source-L258"></a>命題5.1  
<a id="source-L259"></a>Uを万能TM、MをTMとすると、定数cで「どのsについてもKu(s) &lt;= Km(s) + c」なるものが存在する  

<a id="source-L261"></a>系5.2  
<a id="source-L262"></a>Uが万能TMのとき、「sについて常にKu(s) &lt;= |s| + c」となる定数cが存在する  

<a id="source-L264"></a>定義  
<a id="source-L265"></a>万能TM Uを決めたとき、sがアルゴリズム的にランダムであるとは、Ku(s) &gt;= |s|であることと定める  

<a id="source-L267"></a>命題5.3  
<a id="source-L268"></a>万能TM Uについてアルゴリズム的にランダムなビット列が存在する  

<a id="source-L270"></a>定理5.5  
<a id="source-L271"></a>各ビットをベルヌーイ分布で独立に選んだnビットの分布をX&lt;n&gt;とかく  
<a id="source-L272"></a>このとき  

<a id="source-L274"></a>補題5.4  
<a id="source-L275"></a>不等式の関係  

<a id="source-L277"></a>定理5.6  
<a id="source-L278"></a>Uを万能TMとするとき、Ku(s)を計算するTMは存在しない  

<a id="source-L280"></a>系5.7 停止問題の計算不可能性  
<a id="source-L281"></a>TM Mとxを与えたときにM(x)が停止するかどうかを判定するTMは存在しない  


<a id="source-L284"></a>chapter 情報理論的に安全な暗号技術  

<a id="source-L286"></a>・暗号技術には、共通鍵暗号、公開鍵暗号などがあり、共通鍵暗号の中にも情報理論的安全や計算量的安全がある  

<a id="source-L288"></a>定義  
<a id="source-L289"></a>共通鍵暗号化方式とは以下の仕様を満たすアルゴリズムの組と定める（Π）  
<a id="source-L290"></a>・Gen（鍵生成）：鍵空間Kから鍵kを選んで出力する  
<a id="source-L291"></a>・Enc（暗号化）：鍵kと平文mを入力として、暗号文c = Enck(m)を出力する  
<a id="source-L292"></a>・Dec（復号）：鍵kと暗号文cを入力として、Deck(c)は平文または失敗を出力する  

<a id="source-L294"></a>定義  
<a id="source-L295"></a>Πが正当であるとは、どの鍵とどの平文mについていも常にDeck(Enck(m)) = mを満たすことと定める  

<a id="source-L297"></a>例 ワンタイムパッド  

<a id="source-L299"></a>定義  
<a id="source-L300"></a>Πがperfect secrecyを持つとは、鍵の分布Kと平文のどの分布Mについても暗号文の分布 C = Enck(M)がI(M;C) = 0を満たすことと定める  

<a id="source-L302"></a>補題6.1  
<a id="source-L303"></a>Πについて以下は同値  
<a id="source-L304"></a>(1) ΠはPerfect Secrecyを持つ  
<a id="source-L305"></a>(2)m1, m2とcについて常に、確率？  

<a id="source-L307"></a>定理6.2  
<a id="source-L308"></a>ワンタイムパッドはPerfect Secrecyを持つ  

<a id="source-L310"></a>定理6.3  
<a id="source-L311"></a>ΠがPerfect Secrecyを持つとき|K| &gt;= |μ|  

<a id="source-L313"></a>定義  
<a id="source-L314"></a>(t,n)-しきい値型秘密分散方式(secret sharing)とは、以下のようなアルゴリズムShare, Reconstの組みをなす  
<a id="source-L315"></a>・Share：秘密情報mを入力としてn個のシェアを出力する  
<a id="source-L316"></a>・Reconst：t個のシェアを入力としてμの元を出力する  

<a id="source-L318"></a>正当性：Share(m) = (s1, s2, ,,,)のときどのt個についても常にreconst() = m  

<a id="source-L320"></a>安全性：μ上のr.v. M、対応するsiのsiについてどのt-1個についても  

<a id="source-L322"></a>命題6.4  
<a id="source-L323"></a>これは正当かつ安全である  

<a id="source-L325"></a>補題6.5 ラグランジュ補完  
<a id="source-L326"></a>Fを体、nを自然数として、f(ai) = biとなるn-1次多項式がただ１つ存在する  

<a id="source-L328"></a>定義  
<a id="source-L329"></a>シャミアの(t,n)：方式  

<a id="source-L331"></a>定理6.6  
<a id="source-L332"></a>この方式は正当かつ安全  


<a id="source-L335"></a>量子情報理論  
<a id="source-L336"></a>・量子計算  
<a id="source-L337"></a>・量子通信  
<a id="source-L338"></a>・dense coding  
<a id="source-L339"></a>・量子暗号  
<a id="source-L340"></a>・量子エントロピー  

<a id="source-L342"></a>量子状態はヒルベルト空間上の線型演算子  
<a id="source-L343"></a>純粋状態はHの単位ベクトル  

<a id="source-L345"></a>定義  
<a id="source-L346"></a>二次元ヒルベくと空間に対応する量子系を量子ビットといい  
|0&gt;、|1&gt;を計算基底という

<a id="source-L349"></a>定義  
<a id="source-L350"></a>Hの正規直交基底をb0,,,とすると、この基底に関する状態の測定とは  
<a id="source-L351"></a>・測定結果は{0,1,・・・,n-1}の元  
<a id="source-L352"></a>・結果iが得られたとき状態は|bi&gt;に変化する  

<a id="source-L354"></a>定義  
<a id="source-L355"></a>量子ビット系H1とH2とそれらの計算基底をとる、このとき以下の性質を持つ有限次元ヒルベルト空間h1✖️h2が存在する  
<a id="source-L356"></a>これをH1とH2のテンソル積といい、対応する量子系を２量子ビット系という  

<a id="source-L358"></a>定義  
<a id="source-L359"></a>量子系Hにおける閉じた操作はH上のユニタリ演算子で表される  
<a id="source-L360"></a>特にこの操作は可逆である  

<a id="source-L362"></a>量子テレポーテーション  

<a id="source-L364"></a>量子鍵配達  
<a id="source-L365"></a>定理7.1 複製不可能定理  
<a id="source-L366"></a>Hをc2とc2の2量子ビット系とする  
<a id="source-L367"></a>H上のユニたり演算子Uで、どの単位ベクトルについてもU(|Ψ&gt;)　(ry を満たすものは存在しない  

<a id="source-L369"></a>BB84プロトコル  




> <a id="source-L374"></a>It’s about time: a thermodynamic information criterion (TIC)  

<a id="source-L375"></a><https://arxiv.org/pdf/2506.04519>  


<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

離散分布のShannonエントロピーは $H(X)=-\sum_xp(x)\log_2p(x)$（$0\log 0=0$）で、単位はbit。連続変数の微分エントロピーとは性質が異なるため、同じ直感を無条件に移さない。本文の情報熱力学へのリンクは関心のつながりとして保ち、物理的なエントロピーとの対応はモデル・単位・条件を別途定めて考える。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [統計的機械学習](../probability-statistics/statistical-machine-learning.md)
- [確率](../probability-statistics/probability.md)
- [統計学](../probability-statistics/statistics.md)
- [計算量理論](computational-complexity.md)
- [関数解析](../analysis/functional-analysis.md)
- [微分積分学](../analysis/calculus.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
