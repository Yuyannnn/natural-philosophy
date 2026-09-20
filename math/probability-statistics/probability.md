---
title: "確率"
status: draft
tags: [scrapbox, probability-statistics]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E7%A2%BA%E7%8E%87"
source_created: "2023-01-21T18:33:44Z"
source_updated: "2024-12-07T13:32:35Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 確率

確率空間から期待値や分布へ進み、工学応用も意識した記録。

原ページ作成：2023-01-21 ／ 最終更新：2024-12-07（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/probability.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E7%A2%BA%E7%8E%87)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

**原文に埋め込み欠落記号が3か所あります。** 取得時点で内容を特定できないため、本文中で位置を示しています。推測した図や式に置き換えていません。

<details>
<summary>本文の見出しから探す</summary>

- [確率過程](#source-L14)
- [確率数理工学2](#source-L243)
- [第1講](#source-L263)
- [第2講](#source-L381)
- [第3講](#source-L460)
- [第4講](#source-L541)
- [1 定義関数の積分](#source-L582)
- [2 定義関数の期待値](#source-L583)
- [3 その極限をとることで任意の確率変数の積分を定義する](#source-L584)
- [第5講](#source-L623)
- [第6講](#source-L633)
- [第7講](#source-L651)
- [第8講](#source-L670)
- [第9講](#source-L686)
- [第10講](#source-L691)
- [第11講](#source-L729)
- [第12講](#source-L733)
- [第13講](#source-L737)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 確率

<a id="source-L2"></a>[確率過程](stochastic-processes.md)  
<a id="source-L3"></a>[確率ロボティクス](https://scrapbox.io/MistMavGamer/%E7%A2%BA%E7%8E%87%E3%83%AD%E3%83%9C%E3%83%86%E3%82%A3%E3%82%AF%E3%82%B9)  
<a id="source-L4"></a>\[確率的プログラミング言語\]  
<a id="source-L5"></a>[統計的機械学習](statistical-machine-learning.md)  
<a id="source-L6"></a>[統計学](statistics.md)  


> <a id="source-L9"></a>確率論 筑波大学  

> > <a id="source-L10"></a>[https://www.youtube.com/playlist?list=PL38KibqB_aSBQn0M41mm2rTNoI_RuiTkm](<https://www.youtube.com/playlist?list=PL38KibqB_aSBQn0M41mm2rTNoI_RuiTkm>)  

> <a id="source-L12"></a>わかりやすいらしい  


<a id="source-L14"></a>

### 確率過程

<a id="source-L15"></a>Stochastic process 1  

<a id="source-L17"></a>確率は自然現象のモデル化または乱択法と言った工学応用にも欠かせない数学的道具である  
<a id="source-L18"></a>物理モデリング、ML、統計学、アルゴリズム、高速計算、量子力学、暗号セキュリティなどに応用できる  

<a id="source-L20"></a>chap1 確率空間  

<a id="source-L22"></a>試行  

<a id="source-L24"></a>標本空間  
<a id="source-L25"></a>試行の結果を全て集めたもの  

<a id="source-L27"></a>標本点  
<a id="source-L28"></a>ある試行の結果  

<a id="source-L30"></a>確率事象  

<a id="source-L32"></a>これからの戦略として、  
<a id="source-L33"></a>有限・離散は問題ない  
<a id="source-L34"></a>→無限・連続を扱いたい、極限をとりたい  
<a id="source-L35"></a>→それらが行える数学的土台を整備する  

<a id="source-L37"></a>σ-加法族  

<a id="source-L39"></a>borel集合族  
<a id="source-L40"></a>σ-加法族の中でも重要なのがBorel集合族である  

<a id="source-L42"></a>可測空間  
<a id="source-L43"></a>Fを集合族として(Ω,F)を可測空間という  

<a id="source-L45"></a>確率測度  

<a id="source-L47"></a>3は分割の仕方によらないことを言っており、有限から無限に矛盾なく繋げられるので重要である  
<a id="source-L48"></a>測度論的確率論は全てこの公理に立脚している  

<a id="source-L50"></a>確率測度の性質  
<a id="source-L51"></a>まあ常識  
<a id="source-L52"></a>劣加法性  
<a id="source-L53"></a>和の公式  
<a id="source-L54"></a>和の公式、幇助原理  
<a id="source-L55"></a>確率の連続性  




<a id="source-L60"></a>chap2 確率変数  
<a id="source-L61"></a>確率変数  

<a id="source-L63"></a>可測関数  

<a id="source-L65"></a>分布関数  

<a id="source-L67"></a>分布関数の性質  

<a id="source-L69"></a>連続分布  

<a id="source-L71"></a>絶対連続  

<a id="source-L73"></a>radon-nikodymの定理  

<a id="source-L75"></a>密度関数の性質  

<a id="source-L77"></a>特異連続  

<a id="source-L79"></a>離散分布  

<a id="source-L81"></a>同時分布  

<a id="source-L83"></a>確率変数の独立性  

<a id="source-L85"></a>条件付き確率  

<a id="source-L87"></a>事象の独立性  





<a id="source-L93"></a>chap3 期待値と特性関数  

<a id="source-L95"></a>期待値  

<a id="source-L97"></a>期待値の性質  

<a id="source-L99"></a>条件付き期待値  

<a id="source-L101"></a>条件付き期待値の性質  

<a id="source-L103"></a>分散の性質  

<a id="source-L105"></a>短調収束定理、fatouの補題、優秀測定理、fubiniの定理  

<a id="source-L107"></a>モーメント母関数  
<a id="source-L108"></a>モーメント母関数とモーメントの関係  

<a id="source-L110"></a>特性関数  

<a id="source-L112"></a>特性関数の性質  

<a id="source-L114"></a>キュムランと母関数  

<a id="source-L116"></a>キュムラントと平均値周りのモーメントの関係  

<a id="source-L118"></a>歪みと尖り  

<a id="source-L120"></a>特性関数と分布関数の関数  

<a id="source-L122"></a>levyの反転公式  

<a id="source-L124"></a>独立な確率変数の和の特性関数  

<a id="source-L126"></a>独立な確率変数と特性関数  




<a id="source-L131"></a>Chap4 さまざまな分布  

<a id="source-L133"></a>指数分布  

<a id="source-L135"></a>ガンマ分布  

<a id="source-L137"></a>カイ二乗分布  

<a id="source-L139"></a>離散分布  

<a id="source-L141"></a>二項分布  

<a id="source-L143"></a>Poisson分布  







<a id="source-L151"></a>Chp5 変数変換  
<a id="source-L152"></a>1変数  

<a id="source-L154"></a>多変数  





<a id="source-L160"></a>Chap6 確率変数に関する不等式  

<a id="source-L162"></a>凸関数  

<a id="source-L164"></a>劣微分  

<a id="source-L166"></a>jensenの不等式  

<a id="source-L168"></a>youngの不等式  

<a id="source-L170"></a>holderの不等式  

<a id="source-L172"></a>minkowskiの不等式  

<a id="source-L174"></a>cauchy-schwartzの不等式  

<a id="source-L176"></a>Markovの不等式,chebyshevの不等式  

<a id="source-L178"></a>hoeffdingの不等式  

<a id="source-L180"></a>bernsteinの不等式  







<a id="source-L188"></a>Chap7 確率変数列の収束  





<a id="source-L194"></a>Chap8 大数の法則と中心極限定理  




<a id="source-L199"></a>chap9 確率過程  
<a id="source-L200"></a>加法仮定  

<a id="source-L202"></a>定常過程  

<a id="source-L204"></a>マルコフ過程  





<a id="source-L210"></a>chap10 マルコフ連鎖  
<a id="source-L211"></a>離散時間、離散状態であるマルコフ過程をマルコフ連鎖という  

<a id="source-L213"></a>相互到達可能の同地関係性  

<a id="source-L215"></a>再帰性  

<a id="source-L217"></a>再帰性と既約性  

<a id="source-L219"></a>Aが有限で閉かつ既約ならAに含まれる任意の状態は再帰的である  

<a id="source-L221"></a>一致団結の性質  

<a id="source-L223"></a>既約成分への分解定理  

<a id="source-L225"></a>再帰性と平均到達時間  

<a id="source-L227"></a>吸収確率  

<a id="source-L229"></a>平均再帰時間の性質と正再帰性の条件  

<a id="source-L231"></a>定常分布の存在条件  

<a id="source-L233"></a>大数の強法則  

<a id="source-L235"></a>マルコフ連鎖は既約とする  





<a id="source-L241"></a>—————————————————————————————————————————  


<a id="source-L243"></a>

### 確率数理工学2



<a id="source-L246"></a>講義ノート  
<a id="source-L247"></a><http://ibis.t.u-tokyo.ac.jp/suzuki/lecture/2020/index.html>  

<a id="source-L249"></a>本講義の目的は、データの生成過程や確率的現象を数理的にモデリングするために必要な数学的道具である「確率論」の基本を教えることにある。確率論は、自然や社会の不確実な現象を記述する言語であると同時に工学的応用にも広く用いられ、その利用範囲は広い。学習範囲は、確率および確率過程の初等的な範囲を十分カバーし、推定や検定は扱わない。現実問題への適用を意識して、機械学習やデータマイニングへの応用事例も講義の中で紹介する。確率論の基本的要素とその現実の利用方法を学ぶことにより統計・情報理論・データ解析といった諸分野において確率を用いた議論を展開する素養を身に着ける。  

<a id="source-L251"></a>１．確率空間、基本公式、条件付き確率、独立性  
<a id="source-L252"></a>２．確率変数、分布関数，確率密度関数、同時分布，周辺分布  
<a id="source-L253"></a>３．母関数、特性関数、モーメント、キュムラント  
<a id="source-L254"></a>４．連続分布（正規分布、指数分布、ガンマ分布、ベータ分布、コーシー分布）  
<a id="source-L255"></a>離散分布（二項分布、ポアッソン分布、超幾何分布） ５．和の分布、畳み込み分布、変数変換、複合分布  
<a id="source-L256"></a>６．Holderの不等式、Chebyshevの不等式、 Hoeffdingの不等式、Markov不等式、Chernoff型不等式  
<a id="source-L257"></a>７．概収束、確率収束、法則収束  
<a id="source-L258"></a>８．Levyの連続性定理、大数の法則とその証明、中心極限定理とその証明  
<a id="source-L259"></a>９．確率過程、ポアソン過程、再生過程、計数過程  
<a id="source-L260"></a>１０．マルコフ連鎖  



<a id="source-L263"></a>

### 第1講

<a id="source-L264"></a>昔は確率を数学的な扱いができていなかった  

<a id="source-L266"></a>そこで、測度論という数学を使って確率を定式化した  

<a id="source-L268"></a>確率を自然現象とすると難しくなるが、確率を確率測度であると定式化する  
<a id="source-L269"></a>これで確率が純粋な数学的問題になる  

<a id="source-L271"></a>サイコロを振るといった１つの試行の結果、観測される事象の確率を定める  

<a id="source-L273"></a>試行  
<a id="source-L274"></a>標本空間Ω：試行の結果全体の集合  
<a id="source-L275"></a>標本点ω：試行の結果  

<a id="source-L277"></a>標本空間の部分集合を事象という  
<a id="source-L278"></a>余事象、和事象、積事象も同様に定義する  

<a id="source-L280"></a>事象に確率を定めたい  
<a id="source-L281"></a>→標本空間が有限集合なら難しくない  
<a id="source-L282"></a>→連続、無限も扱いたいが、下手にやると矛盾が起こることが知られている（普通は、バラバラに分割してそれらを合体してもとの大きさにならに例が作れる）（Banach-Tarskiのパラドックス）  
<a id="source-L283"></a>→確率を定義しても矛盾が生じない閉じた入れ物を用意する  
<a id="source-L284"></a>→「σ加法族」「可測空間」「確率測度」  

<a id="source-L286"></a>これらの天下りの前提がないと確率論は成り立たない  
<a id="source-L287"></a>これらの公理が必要だよねってことは納得するのが今日の目標  

<a id="source-L289"></a>なぜσ加法族を導入するかというと、確率が定まっていて欲しい集合の集合を考える  
<a id="source-L290"></a>Fの各元に確率が定まっていてほしいという気持ちになる  

<a id="source-L292"></a>Def σ加法族(完全加法族)  
<a id="source-L293"></a>Ωの部分集合族Fがσ加法族  
<a id="source-L294"></a>(1) Ω ∈ F  
<a id="source-L295"></a>(2) A ∈ F → Ac ∈ F  
<a id="source-L296"></a>(3) A1,A2,,,, ∈ F → それらの和集合 ∈ F(ただし可算無限個)  
<a id="source-L297"></a>(3)が一番重要  
<a id="source-L298"></a>可算無限個の元は重複を許すので、Fは有限個でもok  
<a id="source-L299"></a>(3)をσ-加法性（完全加法性）という  
<a id="source-L300"></a>なぜ(3)が必要なのかというと、極限操作を考えたい  
<a id="source-L301"></a>我々は和しかない  
<a id="source-L302"></a>和から積分を定義しようとすると、間で必ず極限を考えなければいけなくなる  
<a id="source-L303"></a>極限を矛盾なく考えるためにはσ加法族が必要になる  
<a id="source-L304"></a>確率測度に入るとσ加法族の必要性がわかる  

<a id="source-L306"></a>変なσ加法族を持ってきて、その上で確率を考えることも許される  
<a id="source-L307"></a>有限集合なら簡単だが、実数の場合を考えてみる  

<a id="source-L309"></a>σ加法族の中でもBorel集合族が重要  
<a id="source-L310"></a>R上のBorel集合族B(R)はRの任意の開集合を含む最小のσ-加法族である  
<a id="source-L311"></a>Borel集合族の元をBorel修吾いうという  

<a id="source-L313"></a>確率は面積だと思っとけ  
<a id="source-L314"></a>開区間の面積ぐらいは定まっていて欲しいと思う  
<a id="source-L315"></a>任意の開区間を含む最小のσ加法族もBorel集合族  
<a id="source-L316"></a>さすがに区間ぐらいは面積が定まっているよなあ？  

<a id="source-L318"></a>F1, F2：σ加法族が任意の開集合を含むとする  
<a id="source-L319"></a>このとき、F1∩F2も任意の開集合を含むことはF1、F2の条件からすぐわかる  
<a id="source-L320"></a>さらにF1∩F2はσ加法族にもなっている  

<a id="source-L322"></a>F1∩F2はF1,F2よりも小さいと言えるので、開集合を全て含むσ加法族を全て集めてきて、それらの共通部分をとれば最小のσ加法族を構築できる  

<a id="source-L324"></a>構成の仕方から  
<a id="source-L325"></a>１、B(R)はσ加法族  
<a id="source-L326"></a>２、B(R)は任意の開集合を含む  
<a id="source-L327"></a>さらにB(R)より小さくそのような条件を満たすσ加法族は存在しない  

<a id="source-L329"></a>ボレル測度を用いると、実数上の確率測度が定まる  
<a id="source-L330"></a>実数上のσ加法族としてBorel集合族を覚える  

<a id="source-L332"></a>Ωとその上のσ加法族Fの組みを可測空間という  
<a id="source-L333"></a>この可測空間に確率を定める  
<a id="source-L334"></a>可測空間というのは、面積を測れるという意味  

<a id="source-L336"></a>σ加法族に今後確率を定義して、σ加法族と確率が定義できる集合を対応させる  

<a id="source-L338"></a>集合の包含関係の定義も覚えておけ  

<a id="source-L340"></a>Fの上に確率を定めていく  

<a id="source-L342"></a>Def 確率測度  
<a id="source-L343"></a>確率測度とは、Fの元を受け取って、ある実数を返す関数  
<a id="source-L344"></a>以下の条件を満たす  
<a id="source-L345"></a>(1) ∀A∈Fで 0&lt;=P(A)&lt;=1  
<a id="source-L346"></a>(2) P(Ω) = 1  
<a id="source-L347"></a>(3) A1,A2,,,∈ Fが互いに排反 → P(∪An) = ΣP(An)  

<a id="source-L349"></a>和集合の確率が、それぞれの確率の和に分解できる  
<a id="source-L350"></a>つまり、Pの外側で極限をとるのと、内側で極限をとるのが可換であると言っている  
<a id="source-L351"></a>(3)の性質をσ-加法性と呼ぶ  
<a id="source-L352"></a>σ加法族として変な集合を持ってくると、これが成り立たない  

<a id="source-L354"></a>σ-加法性が成り立つ(Ω, F, P)と制限して議論する  
<a id="source-L355"></a>F自身は非可算無限でもOK  

<a id="source-L357"></a>この３つからいろいろなことが言えるのが面白いところ  
<a id="source-L358"></a>確率測度の基本公式９つが導ける！！！  

<a id="source-L360"></a>(8)確率の連続性1  
<a id="source-L361"></a>(9)確率の連続性2  
<a id="source-L362"></a>が超大事  

<a id="source-L364"></a>中にあったlimを外に持ってこれた  
<a id="source-L365"></a>これを確率の連続性という  

<a id="source-L367"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L369"></a>なぜこれを連続性というのかというと、連続関数の定義とアナロジーがあるから  

<a id="source-L371"></a>これらの9つの公式は3つの公理から全て導出できる  
<a id="source-L372"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L374"></a>振り返ると、σ加法族の性質がなぜ必要だったのかを理解することができる  

<a id="source-L376"></a>σ加法性は無限和のことしか言っていないので、有限で止めてはいけない  
<a id="source-L377"></a>止めてもいいかもしれないが、そのことは公理ではいっていない  
<a id="source-L378"></a>有限でもいいということは、示せる  



<a id="source-L381"></a>

### 第2講

<a id="source-L382"></a>確率変数はわかりにくいかも知れないが合理的な定義になっている  
<a id="source-L383"></a>まずは関数であるというふうに定義する  

<a id="source-L385"></a>確率変数のとる値がどの範囲にどれだけの確率で含まれるかがわかって欲しいのでこの条件が課される  
<a id="source-L386"></a>このような確率がわかっていれば、引き算することでいろいろな範囲の確率が求められる  
<a id="source-L387"></a>というのも、σ加法族は演算に関して閉じているので  

<a id="source-L389"></a>可測はFに含まれるという意味  
<a id="source-L390"></a>つまり「確率変数 = 可測関数」  

<a id="source-L392"></a>任意のボレル集合に対し、その集合の元の逆像がFに含まれることは、上記の定義と同値になっている  

<a id="source-L394"></a>行く前と行った後の空間に関して、それが可測のとき、F/F’可測関数と呼ぶ  

<a id="source-L396"></a>復習  
<a id="source-L397"></a>「X&lt;=xである確率は測れて欲しい」  
<a id="source-L398"></a>「ボレル集合の元である確率は測れる」  

<a id="source-L400"></a>任意のボレル集合に対して、その逆像がFに入ることを証明  
<a id="source-L401"></a>この証明をすることで、ボレル集合の気持ちを理解したい  

<a id="source-L403"></a>測度論的確率論では、とある集合上で成り立つことが、それを含む最小のσ加法族、つまりボレル集合上に拡張するという議論がいくつも出てくる  

<a id="source-L405"></a>実は連続関数が可測関数である  
<a id="source-L406"></a>開集合の逆像が開集合というのが連続関数の定義である  

<a id="source-L408"></a>F(x) = P()を（累積）分布関数という  

<a id="source-L410"></a>分布関数の性質として、  
<a id="source-L411"></a>(1)単調非減少  
<a id="source-L412"></a>(2)右連続  
<a id="source-L413"></a>(3)lim-∞F(x) = 0, lim∞F(x) = 1  

<a id="source-L415"></a>xを左からaに近づけていくと、F(x) = F(a)とは限らないが、左極限は存在する  

<a id="source-L417"></a>右連続であるのは、確率変数や分布関数の不等号に等号が含まれていることに関係がある  
<a id="source-L418"></a>また、不等号の部分に等号を含めずに定義すると左連続になる  

<a id="source-L420"></a>逆に、(1)\~(3)を満たすF(x)があるとする  
<a id="source-L421"></a>それに対応する(R, B(R))上の確率測度Qが一意に存在する  
<a id="source-L422"></a>これで、R上の確率測度の存在が保証される  
<a id="source-L423"></a>ここは補足資料にのっている  

<a id="source-L425"></a>Qを調べる代わりにFを調べた方が楽なことが多いので、（弱収束など）Fを考える  

<a id="source-L427"></a>Pを身長を選ぶ確率とすると、Qは身長の分布になる  

<a id="source-L429"></a>確率分布の種類は３つある  
<a id="source-L430"></a>・絶対連続  
<a id="source-L431"></a>・特異連続  
<a id="source-L432"></a>・離散  
<a id="source-L433"></a>今回は連続なものを紹介する  

<a id="source-L435"></a>絶対連続分布  
<a id="source-L436"></a>F(x) =   
<a id="source-L437"></a>fを確率密度関数という  
<a id="source-L438"></a>連続分布な定義としてもう１つが、Radom-Nikodymの定理というものがある  
<a id="source-L439"></a>これを定義としてもよい  

<a id="source-L441"></a>絶対連続な分布の例  
<a id="source-L442"></a>・一様分布  
<a id="source-L443"></a>・正規分布  
<a id="source-L444"></a>正規分布の累積分布関数を誤差関数という  

<a id="source-L446"></a>この講義では、連続といえば絶対連続しか考えないので確率密度関数が存在しているとして良い  
<a id="source-L447"></a>連続分布だからといって密度関数があるとは限らない  

<a id="source-L449"></a>反例として悪魔の階段がある  
<a id="source-L450"></a>・Bernoulli分布  
<a id="source-L451"></a>・二項分布：n回のコイン投げで表が出た回数kの分布  
<a id="source-L452"></a>・Poisson分布：稀に起こる現象が一定期間内に起きる回数の分布、向上で1日に生産される不良品の数、宇宙船を１時間に観測する回数  

<a id="source-L454"></a>この中間はなくて、ルベーグの分解定理というものが成り立つ  
<a id="source-L455"></a>要素としては、絶対連続か、特異連続か、離散かしかない  
<a id="source-L456"></a>この３つさえ抑えておけば全て表せるぜ  




<a id="source-L460"></a>

### 第3講

<a id="source-L461"></a>今までやってきたのは、確率測度を定義してきた  
<a id="source-L462"></a>確率測度と  
<a id="source-L463"></a>確率空間を作ったらその上に可測関数の確率変数ををいた  
<a id="source-L464"></a>そのあとは分布関数を定義した  
<a id="source-L465"></a>これから逆に辿る  

<a id="source-L467"></a>X(ω) &lt; xであることが可測であるといった  
<a id="source-L468"></a>あるボレル集合に入ってるものも可測であると言えるようになった  
<a id="source-L469"></a>X(ω)があるボレル集合に入るのが可測であると拡張できた  

<a id="source-L471"></a>分布関数は、単調性、右連続性、  

<a id="source-L473"></a>分布関数を定義するモチベーションとして、分布関数Fさえもっとけば確率測度Pの情報を損なうことがない  

<a id="source-L475"></a>集合半環について  
<a id="source-L476"></a>分布関数による区間は集合半環になっている  

<a id="source-L478"></a>どの集合族までPを矛盾なく拡張できるかを考える  
<a id="source-L479"></a>答えとしては、Sを含む最小のσ加法族まで拡張される  
<a id="source-L480"></a>それがボレル集合族である  

<a id="source-L482"></a>半開区間の確率を定めば、Sを含む最小のσ加法族まで確率測度が拡張される  
<a id="source-L483"></a>どのように示されるのかというと、  

<a id="source-L485"></a>SはS上でσ加法的という  
<a id="source-L486"></a>区間a,bは安全な議論ができる  
<a id="source-L487"></a>そこから、Hopσの拡張定理で拡張する  
<a id="source-L488"></a>Sを含む最小のσ加法族上の確率測度へ一意に拡張される  
<a id="source-L489"></a>これで自然に出てくることが言えた  

<a id="source-L491"></a>こうして拡張されたPおよびその定義域であるボレル州豪族の性質を抜き出して書き下すと、２講めで出てきら定義が出てくる  

<a id="source-L493"></a>確率空間が定義されたら、確率変数を定義できた  
<a id="source-L494"></a>確率変数をどこまで拡張できるのかという小tを考えると、ボレル集合族まで拡張できる  
<a id="source-L495"></a>これはHopsの定義と同じようなこと  

<a id="source-L497"></a>ボレル集合族が何なのかは掴みにくいと思う  
<a id="source-L498"></a>それの証明を追ってみる  
<a id="source-L499"></a>これはR内で有理数が稠密であることが本質である  

<a id="source-L501"></a>加算な稠密部分集合を持つ時、可分であるという  
<a id="source-L502"></a>なぜ分けられるのかというと、数えられる集合に分けられるからそう言えるのでは  

<a id="source-L504"></a>下手に非可算無限の和集合をとるとボレル集合でない集合の元一つ一つとってきて非加算を取ると任意の集合を作れるようになっちゃう  
<a id="source-L505"></a>可算無限であることが大切  

<a id="source-L507"></a>ここまではこれまでの復習である  

<a id="source-L509"></a>多変量確率変数を定義する  
<a id="source-L510"></a>２つの定義があり、これらが同じことを証明する  
<a id="source-L511"></a>普通に確率変数を並べたものであると思っても良いが、もっと情報量が多い定義がある  

<a id="source-L513"></a>直積σ加法族を定義する  

<a id="source-L515"></a>それに対する分布関数が定義できる  
<a id="source-L516"></a>同時分布関数という  
<a id="source-L517"></a>例えば身長170以下かつ年収500万以下みたいな  

<a id="source-L519"></a>特にそれが積分でかけるとき、同時確率密度関数という  
<a id="source-L520"></a>１次元の場合と同様に性質1,2,3を満たすFが与えられれば、それに対応する確率測度が一意に決まる  
<a id="source-L521"></a>ボレル集合  

<a id="source-L523"></a>並べたうちで、１つ１つの変数の分布を周辺分布という  
<a id="source-L524"></a>関数fkで表すときは、周辺確率密度関数という  

<a id="source-L526"></a>確率変数の独立性  
<a id="source-L527"></a>同時分布が、それぞれの確率変数の掛け算に分解できる  
<a id="source-L528"></a>これだけだと使いにくいのでいくつか同値な定義がある  
<a id="source-L529"></a>紹介した２つの定理が等しいことを証明する  
<a id="source-L530"></a>そのためにπ-λ定理を用いる  

<a id="source-L532"></a>事象の独立性は数式で定義する  
<a id="source-L533"></a>このように定義すると確率変数の独立性が、事象の独立性でかける  

<a id="source-L535"></a>独立の定義を使い分けることもある  

<a id="source-L537"></a>各集合の元が持つべき性質を１つ１つ確認していくとわかっていくはず  




<a id="source-L541"></a>

### 第4講

<a id="source-L542"></a>少し前回の終わってない部分をやる  
<a id="source-L543"></a>前回は分布関数が与えられると、確率測度が定まるという話をした  
<a id="source-L544"></a>確率関数の引き算で区間がの確率がわかるので、これを貼り合わせていく  
<a id="source-L545"></a>開区間でも、無限和を取ることで定めることができる  
<a id="source-L546"></a>区間をどんどん足していけば  

<a id="source-L548"></a>まとめ  
<a id="source-L549"></a>区間の確率を定めましょう  
<a id="source-L550"></a>→それを切りはりすることで、開区間などの確率が一意に定まる  
<a id="source-L551"></a>その裏にhopsの拡張定理がある  

<a id="source-L553"></a>ここから先は確率測度はあるという前提で話を進める  
<a id="source-L554"></a>まずは条件付き確立を定義する  

<a id="source-L556"></a>この定義だとP(B)=0の時はwell-definedではない  
<a id="source-L557"></a>その時は確率密度を考える  
<a id="source-L558"></a>条件付き確率密度というものもある  
<a id="source-L559"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L561"></a>条件付き確率の公式として、積の公式とBayesの公式がある  
<a id="source-L562"></a>Bayesの公式は原因から結果の確率がわかれば、結果から原因の確率を逆算できる  

<a id="source-L564"></a>例えば、ロボットアームの自己位置推定や、人工衛星が景色から場所を推定することなどに使われる  

<a id="source-L566"></a>今回は期待値を定義する  
<a id="source-L567"></a>するとモーメントが出てくる  
<a id="source-L568"></a>特性関数を使うと色々な分布の特徴がわかる  

<a id="source-L570"></a>φが可測じゃないと積分が定義できない  

<a id="source-L572"></a>ここから先はφ(x)をxとする  
<a id="source-L573"></a>今はY(ω) = yとしている  
<a id="source-L574"></a>Yはωの変数  

<a id="source-L576"></a>リーマン積分だと、拡張できないので、ルベーグ積分を定義する  
<a id="source-L577"></a>ルベーグ積分の表記は独特なので、慣れるしかない  

<a id="source-L579"></a>可算無限しか持っていないので、和を取るということだけで積分を定義することを目指していくう  
<a id="source-L580"></a>なんとかして和の極限として積分を定義することを考える  


<a id="source-L582"></a>

### 1 定義関数の積分


<a id="source-L583"></a>

### 2 定義関数の期待値


<a id="source-L584"></a>

### 3 その極限をとることで任意の確率変数の積分を定義する

<a id="source-L585"></a>この流れを抑えておく  

<a id="source-L587"></a>E(x) = Aの面積\*高さ1  = Aの面積 = P(A)  
<a id="source-L588"></a>このようにするとσ加法性が成り立つ  

<a id="source-L590"></a>次は有限和をとってきてその期待値を定める  
<a id="source-L591"></a>単関数は無限和は許さない  
<a id="source-L592"></a>単関数の期待値をちゃんと定義した  

<a id="source-L594"></a>次は拡張して非負の確率変数のときの期待値を考える  
<a id="source-L595"></a>近似する単関数の単調列が作れるので、それの極限として定義する  
<a id="source-L596"></a>これは単関数れつの取り方によらない  

<a id="source-L598"></a>積分をちゃんと定義するためには可測性が必要だった  

<a id="source-L600"></a>両方とも有限であるとき可積分という  
<a id="source-L601"></a>ここまででXの積分を定義した  
<a id="source-L602"></a>任意の単関数に関して矛盾なく期待値が定まることは証明しておけ  
<a id="source-L603"></a>グラフを覚えておけば良い  

<a id="source-L605"></a>積分が定義できたので、平均値、モーメント、平均値周りのモーメント、分散が定義できる  
<a id="source-L606"></a>分散は平均値周りのモーメントの１つの例  

<a id="source-L608"></a>期待値の性質  
<a id="source-L609"></a>線形性  
<a id="source-L610"></a>単調性  
<a id="source-L611"></a>a.s.は確率1でっていう意味  

<a id="source-L613"></a>単調収束定理  
<a id="source-L614"></a>Fatouの補題  
<a id="source-L615"></a>優収束定理  

<a id="source-L617"></a>Fatouの補題は優収束定理の証明に使える  

<a id="source-L619"></a>こっから先は、モーメントとからの性質を調べるための母関数を定義して、そっから中心曲限定理に持ってく  




<a id="source-L623"></a>

### 第5講

<a id="source-L624"></a>前回は、単関数の期待値の極限として、  

<a id="source-L626"></a>最初は分散の性質を考える  
<a id="source-L627"></a>分散の性質が大数の逆法則を示唆している  

<a id="source-L629"></a>ここで、積分がwell-defineであることの証明をする  




<a id="source-L633"></a>

### 第6講

<a id="source-L634"></a>キュムナント母関数について  
<a id="source-L635"></a>キュムナントは平均値周りの母関数で書くことができる  

<a id="source-L637"></a>尖りというのは正規分布に比べてどれくらい裾が広いかなどを表す  

<a id="source-L639"></a>分布が等しければキュムナントも等しい  
<a id="source-L640"></a>逆にキュムナントが等しければ分布が等しい  

<a id="source-L642"></a>分布を調べる代わりに特性関数を調べることを考える  

<a id="source-L644"></a>Levyの反転公式という、強い主張をいう定理がある  

<a id="source-L646"></a>和の特性関数は特性関数の積  

<a id="source-L648"></a>いろいろな分布を紹介した  



<a id="source-L651"></a>

### 第7講

<a id="source-L652"></a>前回は、特性関数を定義して、特性関数の性質を論じた  
<a id="source-L653"></a>特性関数の微分とかを考えるとモーメントとかがでてくる（微分可能であれば）  
<a id="source-L654"></a>分布と特性関数は１対１対応というすごい性質があった  
<a id="source-L655"></a>その中で和の分布の特性関数はそれぞれの特性関数の積でかけるので有用であった  
<a id="source-L656"></a>１対１を示すときに、Levyの反転公式というものがあった  
<a id="source-L657"></a>フーリエ変換の一般化みたいなやつ  

<a id="source-L659"></a>分布の関係は抑えておけ  
<a id="source-L660"></a>確率を学ぶと、ギャンブルはよくないなあと考えだす  

<a id="source-L662"></a>変数変換について  

<a id="source-L664"></a>畳み込み分布  
<a id="source-L665"></a>和の分布は畳み込み分布になる  

<a id="source-L667"></a>確率評価に関する不等式  



<a id="source-L670"></a>

### 第8講


<a id="source-L672"></a>KL-divを一般化してf(1)=0なる凸関数を持ちチアものをf-ダイバージェンスという  
<a id="source-L673"></a>fとしてlogをもってくるとKL-divとなる  
<a id="source-L674"></a>fとしてある関数を持ってくると対称性が成り立つ  
<a id="source-L675"></a>これをJensen-shanonエントロピーといい、GANに用いられている  
<a id="source-L676"></a>深層学習でjensen-shanonエントロピーが０になるように学習させる  

<a id="source-L678"></a>確率集中不等式  

<a id="source-L680"></a>確率変数列の収束  
<a id="source-L681"></a>非常に重要  
<a id="source-L682"></a>いろんな定義がある  
<a id="source-L683"></a>4つの収束がある  



<a id="source-L686"></a>

### 第9講






<a id="source-L691"></a>

### 第10講

<a id="source-L692"></a>確率変数列には収束の概念がある  
<a id="source-L693"></a>４つの収束が大切である  
<a id="source-L694"></a>概収束が成り立てば確率収束、確率収束すれば法則収束  
<a id="source-L695"></a>Lp収束すれば確率収束  
<a id="source-L696"></a>これは全然意味が違う、ギャンブラーが言う確率が収束してきたというのは法則収束  
<a id="source-L697"></a>法則収束は弱収束や分岐収束という言い方もある  

<a id="source-L699"></a>Levyの連続性定理  
<a id="source-L700"></a>特性関数が各点収束すれば法則収束する  
<a id="source-L701"></a>こういうのを使えば中心極限定理が証明できる  
<a id="source-L702"></a>中心極限定理は平均と分散が存在する確率変数を考えている  

<a id="source-L704"></a>選挙の速報は中心極限定理で説明できる  
<a id="source-L705"></a>世論調査の結果をベイズ統計してるかも！？  
<a id="source-L706"></a>1/1000を開票しても20σぐらいで予測できる  

<a id="source-L708"></a>質問  
<a id="source-L709"></a>「法則収束がどれくらい速いのかわからないと1万人で正規分布に収束しているかはわからないと思うのですが、その点は信じるということですか？」  
<a id="source-L710"></a>→実は収束のスピードもなんとかなんとかの定理で√nであると知られている  
<a id="source-L711"></a>投票はiidではない、だがiidだと近似する  

<a id="source-L713"></a>中心極限定理と対極の法則といてPoissonの小数の法則というものがある  
<a id="source-L714"></a>不良品が出る確率が低い製品を大量に生産するとその中に入っている不良品の個数は大体ポアソン分布  

<a id="source-L716"></a>Delta法  

<a id="source-L718"></a>こっから先は確率過程の話  
<a id="source-L719"></a>最終的にはマルコフ過程の話をしたい  
<a id="source-L720"></a>マルコフ連鎖は確率過程の１種類  

<a id="source-L722"></a>加法過程  
<a id="source-L723"></a>増分が独立である過程  

<a id="source-L725"></a>例 ブラウン運動  




<a id="source-L729"></a>

### 第11講





<a id="source-L733"></a>

### 第12講





<a id="source-L737"></a>

### 第13講



<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

確率変数と、その実現値を区別する。条件付き確率 $P(A\mid B)=P(A\cap B)/P(B)$ をこの式で定義するには $P(B)>0$ が必要。また独立なら無相関になるのは必要なモーメントが存在する場合で、逆は一般に成り立たない。モデルの独立性仮定を、観測したデータの印象だけで置かないようにする。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [確率過程](stochastic-processes.md)
- [統計的機械学習](statistical-machine-learning.md)
- [統計学](statistics.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
