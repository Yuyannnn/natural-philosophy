---
title: "統計学"
status: draft
tags: [scrapbox, probability-statistics]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E7%B5%B1%E8%A8%88%E5%AD%A6"
source_created: "2023-01-21T18:33:31Z"
source_updated: "2025-10-27T16:53:07Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 統計学

データから何がわかるか、誤差と因果関係をどう扱うかに関する読書・講義メモ。

原ページ作成：2023-01-21 ／ 最終更新：2025-10-27（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/statistics.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E7%B5%B1%E8%A8%88%E5%AD%A6)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

**原文に埋め込み欠落記号が47か所あります。** 取得時点で内容を特定できないため、本文中で位置を示しています。推測した図や式に置き換えていません。

<details>
<summary>本文の見出しから探す</summary>

- [統計学が最強の学問](#source-L12)
- [第1章 なぜ統計学が最強の学問なのか？](#source-L15)
- [第2章 サンプリングが情報コストを激減させる](#source-L21)
- [第3章 誤差と因果関係が統計学の肝](#source-L26)
- [第4章 ランダム化という最強の武器](#source-L38)
- [第5章 ランダム化できなかったらどうするか](#source-L48)
- [第6章 統計家たちの仁義なき戦い](#source-L67)
- [第7章 巨人の肩に立つ方法](#source-L76)
- [「基礎統計」](#source-L84)
- [1. 1次元データの整理・要約　](#source-L91)
- [2. 2次元データの整理・要約　](#source-L93)
- [3. 確率](#source-L95)
- [4. 確率変数と確率分布　](#source-L97)
- [5. 独立同一分布](#source-L99)
- [6. 統計量](#source-L101)
- [7. 標本分布（母集団と標本の概念、統計量、標本平均の平均と分散など）](#source-L103)
- [8. 統計的推定](#source-L104)
- [9. 統計的検定論](#source-L106)
- [「数理手法1」](#source-L115)
- [1.	確率・確率分布・確率変数(1)。「確率・統計I」1-2章。](#source-L118)
- [2.	確率・確率分布・確率変数(2)「Excelによる確率入門」3章。](#source-L119)
- [3.	パソコン・Excelの使い方の復習。「Excelによる統計入門」1-4章。](#source-L120)
- [4.	データの整理と記述統計の演習。「Excelによる統計入門」5-8章。](#source-L121)
- [5.	大数の法則と中心極限定理。「確率・統計I」3章。](#source-L122)
- [6.	標本分布、推定と検定。「確率・統計I」4,5章「Excelによる統計入門」11-12章。](#source-L123)
- [7.	回帰分析。「確率・統計I」4,5章「Excelによる統計入門」13章。](#source-L124)
- [ヨビノリ統計学](#source-L143)
- [第1講 母集団と標本](#source-L147)
- [第2講 点推定](#source-L150)
- [第3講 区間推定(分散が既知)](#source-L155)
- [第4講 区間推定(分散が未知)](#source-L162)
- [第5講 区間推定(母集団分布が未知)](#source-L169)
- [第6講 母比率の推定](#source-L176)
- [第7講 母分散の推定](#source-L182)
- [第8講 母平均の推定](#source-L188)
- [第9講 ウェルチの検定](#source-L194)
- [「統計検定資料」](#source-L226)
- [「統計検定1級に合格する方法」](#source-L234)
- [「統計検定準1級に合格するための方法」](#source-L246)
- [1 確率の基礎](#source-L256)
- [2 確率変数](#source-L258)
- [3 多次元の確率分布](#source-L260)
- [4 推定と検定](#source-L262)
- [5 異なった母集団の同一性の検定とF分布](#source-L264)
- [6 回帰分析](#source-L266)
- [7 ベクトルと行列を使った回帰分析](#source-L268)
- [1 実験計画法](#source-L276)
- [2 時系列解析](#source-L278)
- [1 統計モデルと尤度](#source-L284)
- [2 推定](#source-L286)
- [3 検定とモデル選択](#source-L288)
- [4 確率の基礎](#source-L290)
- [5 Markov連鎖](#source-L292)
- [6 Brown運動と確率積分](#source-L294)
- [7 伊藤の公式と確率微分方程式](#source-L296)
- [8 拡散過程](#source-L298)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 統計学

<a id="source-L2"></a>[確率](probability.md)  
<a id="source-L3"></a>[確率過程](stochastic-processes.md)  
<a id="source-L4"></a>[微分積分学](../analysis/calculus.md)  
<a id="source-L5"></a>[線形代数](../linear-algebra/linear-algebra.md)  
<a id="source-L6"></a>[統計的機械学習](statistical-machine-learning.md)  
<a id="source-L7"></a>[ベイズ統計](bayesian-statistics.md)  
<a id="source-L8"></a>[時系列解析](time-series-analysis.md)  
<a id="source-L9"></a>[因果推論](causal-inference.md)  



<a id="source-L12"></a>

### 統計学が最強の学問

<a id="source-L13"></a>Statistics is Most important  


<a id="source-L15"></a>

### 第1章 なぜ統計学が最強の学問なのか？

<a id="source-L16"></a>どんな分野の議論でもデータを分析することで最速で最善の答えが出せる  
<a id="source-L17"></a>統計学はエビデンスが出せる  
<a id="source-L18"></a>ITと結びついて花が開いた  



<a id="source-L21"></a>

### 第2章 サンプリングが情報コストを激減させる

<a id="source-L22"></a>ビッグデータを全て解析するのはコストがかかりすぎる  
<a id="source-L23"></a>サンプリングをして誤差を求めれば良い  



<a id="source-L26"></a>

### 第3章 誤差と因果関係が統計学の肝

<a id="source-L27"></a>・何らかの要因が変化すれば利益が向上するのか  
<a id="source-L28"></a>・そうした変化を起こすような行動は実際に可能なのか  
<a id="source-L29"></a>・変化を起こす行動が可能だとしてもその利益がコストを上回るのか？  
<a id="source-L30"></a>データをビシネスに使うにはこの３つの問いに答えることが大事  
<a id="source-L31"></a>実際には何の差もないのに誤差や偶然によってたまたまデータのような差が生じる確率をp値と呼び、5%以下を目指せ  
<a id="source-L32"></a>また、適切な比較をするのも大切  
<a id="source-L33"></a>比較している集団がフェアじゃないので因果関係がわからない  
<a id="source-L34"></a>わからなくても仮説を立てられるので有望  
<a id="source-L35"></a>これに対する解決策は、「考えられうる条件を考え、その条件ではフェアに比較」と「データの取りかたの時点でフェアに揃える」という２パターンある  



<a id="source-L38"></a>

### 第4章 ランダム化という最強の武器

<a id="source-L39"></a>人間の制御しうる何事においても因果関係を推論できるのでランダム化実験はすごい  
<a id="source-L40"></a>誤差への３つのアプローチ  
<a id="source-L41"></a>・実際のデータを全く扱わず、仮説やこういう事例がありましたというものをもとにして理論モデルを作る  
<a id="source-L42"></a>・うまくいった事例のみを報告  
<a id="source-L43"></a>・ランダムかを用いて因果関係を確立的に表現する  
<a id="source-L44"></a>ランダム化の３つの限界  
<a id="source-L45"></a>現実、倫理、感情  



<a id="source-L48"></a>

### 第5章 ランダム化できなかったらどうするか

<a id="source-L49"></a>揃え切れていない条件にどこまでこだわるべきか  
<a id="source-L50"></a>t検定、カイ二条検定、分散分析、回帰分析は全て一般化線型モデルという広義の回帰分析の考え方で統一的に理解できる  
<a id="source-L51"></a>データの関係性を記述するのが回帰分析という考え方  
<a id="source-L52"></a>得られた回帰係数にもばらつきが存在するという考え方  
<a id="source-L53"></a>フィッシャーはたまたまデータから得られた統計量がどの程度の誤差で真値を推定しているかを数学的に整理することで無限にデータを集めることなく適切な判断が下せるという考え方を示した  
<a id="source-L54"></a>回帰係数の推定値：真値を推定した結果  
<a id="source-L55"></a>標準誤差：推定値の誤差の大きさ  
<a id="source-L56"></a>95%信頼区間：p値が5%以下となる真値としてはあり得ない値とならない範囲  
<a id="source-L57"></a>p値：回帰係数が0だった婆にデータのばらつきだけでこの回帰系すうが推定されてしまう確立  
<a id="source-L58"></a>説明変数と結果変数さえ決まれば、用いるべき分析手法は簡単に選べる  
<a id="source-L59"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L60"></a>どの方法でも同じp値が得られる  
<a id="source-L61"></a>性別によって点数が平均的に何点異なるのかを推定すれば層別に分けなくても良くなる  
<a id="source-L62"></a>複数の回帰係数はお互いに相乗効果がなかったと仮定した場合の値である  
<a id="source-L63"></a>もともと0か1かという二値の結果変数を変換し、連続的な変数として扱うことで重回帰分析を行えるようにしたのがロジスティック回帰の大まかな考え方である  
<a id="source-L64"></a>回帰モデルを使うときは交互作用に注意する  



<a id="source-L67"></a>

### 第6章 統計家たちの仁義なき戦い

<a id="source-L68"></a>①実態把握を行う社会調査法  
<a id="source-L69"></a>②原因究明のための疫学・生物統計学  
<a id="source-L70"></a>③抽象的なものを測定する心理統計学  
<a id="source-L71"></a>④機械的分類のためのデータマイニング  
<a id="source-L72"></a>⑤自然言語処理のためのテキストマイニング  
<a id="source-L73"></a>⑥演繹に関心を寄せる計量経済学  



<a id="source-L76"></a>

### 第7章 巨人の肩に立つ方法

<a id="source-L77"></a>メタアナリシス、系統的レビューが最高のエビデンス  
<a id="source-L78"></a>最高の答えは公開されている  






<a id="source-L84"></a>

### 「基礎統計」


<a id="source-L86"></a>統計の基礎  

<a id="source-L88"></a>本講義では、初めて統計学を学ぶ学生を対象に、データ解析・統計学の考え方と実際について、その基本事項を解説する。対象は文理を問わない。専門学部で諸科学を学ぶ際に特に重要な、確率分布（＝現象のモデル化）、独立同一分布性（＝同一条件の下での繰り返し実験）、統計的推測（＝データから母集団への推論）の考え方を理解することに焦点を当てる。  



<a id="source-L91"></a>

### 1. 1次元データの整理・要約　

<a id="source-L92"></a>(平均、分散、標準偏差、基準化、歪度、尖度など)  

<a id="source-L93"></a>

### 2. 2次元データの整理・要約　

<a id="source-L94"></a>(共分散、相関係数、回帰直線など)  

<a id="source-L95"></a>

### 3. 確率

<a id="source-L96"></a>（確率、条件付確率、事象の独立など）  

<a id="source-L97"></a>

### 4. 確率変数と確率分布　

<a id="source-L98"></a>（確率変数、確率分布、期待値、確率変数の平均と分散、Bernoulli 試行、2項分布、Poisson分布、幾何分布、正規分布、指数分布など）  

<a id="source-L99"></a>

### 5. 独立同一分布

<a id="source-L100"></a>（同時確率分布、独立同一分布、和の分布など）  

<a id="source-L101"></a>

### 6. 統計量

<a id="source-L102"></a>（母集団、標本、標本分布、正規母集団、中心極限定理、大数法則など）  

<a id="source-L103"></a>

### 7. 標本分布（母集団と標本の概念、統計量、標本平均の平均と分散など）


<a id="source-L104"></a>

### 8. 統計的推定

<a id="source-L105"></a>（点推定、区間推定、不偏推定量など）  

<a id="source-L106"></a>

### 9. 統計的検定論

<a id="source-L107"></a>（正規母集団に関する検定、2項母集団に関する検定、カイ2乗検定など）  




<a id="source-L112"></a>———————————————————————  



<a id="source-L115"></a>

### 「数理手法1」


<a id="source-L117"></a>内容：  

<a id="source-L118"></a>

### 1.	確率・確率分布・確率変数(1)。「確率・統計I」1-2章。


<a id="source-L119"></a>

### 2.	確率・確率分布・確率変数(2)「Excelによる確率入門」3章。


<a id="source-L120"></a>

### 3.	パソコン・Excelの使い方の復習。「Excelによる統計入門」1-4章。


<a id="source-L121"></a>

### 4.	データの整理と記述統計の演習。「Excelによる統計入門」5-8章。


<a id="source-L122"></a>

### 5.	大数の法則と中心極限定理。「確率・統計I」3章。


<a id="source-L123"></a>

### 6.	標本分布、推定と検定。「確率・統計I」4,5章「Excelによる統計入門」11-12章。


<a id="source-L124"></a>

### 7.	回帰分析。「確率・統計I」4,5章「Excelによる統計入門」13章。

<a id="source-L125"></a>受講者は、教養学部の「基礎統計」を履修したか、同等程度の確率・統計の知識があることが望ましい。「基礎統計」を履修していない学生は、東大教養学部編「統計学入門」などで、その基礎を復習視しておくこと。  
<a id="source-L126"></a>教科書は、  
<a id="source-L127"></a>縄田和満著、「確率・統計I」東京大学工学教程、2013年、丸善出版。  
<a id="source-L128"></a>縄田和満著、「Excelによる統計入門(Excel2007対応版)」、朝倉書店、2007年  

<a id="source-L130"></a>である。参考書は、  

> <a id="source-L131"></a>東大教養学部編、「統計学入門」、東大出版会、1991年  
> <a id="source-L132"></a>縄田和満著、「Excelによる確率入門」、朝倉書店、2003年  

<a id="source-L133"></a>である。　  


<a id="source-L136"></a>確率・統計  
<a id="source-L137"></a>Excel  



<a id="source-L141"></a>—————————————————————————————————————————  


<a id="source-L143"></a>

### ヨビノリ統計学


<a id="source-L145"></a><https://www.youtube.com/watch?v=Bj8fkq533Dc&list=PLDJfzGjtVLHmx7qMP410-9gx0weC9d90X>  


<a id="source-L147"></a>

### 第1講 母集団と標本

<a id="source-L148"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  


<a id="source-L150"></a>

### 第2講 点推定

<a id="source-L151"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L152"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L153"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  


<a id="source-L155"></a>

### 第3講 区間推定(分散が既知)

<a id="source-L156"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L157"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L158"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L159"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L160"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  


<a id="source-L162"></a>

### 第4講 区間推定(分散が未知)

<a id="source-L163"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L164"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L165"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L166"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  



<a id="source-L169"></a>

### 第5講 区間推定(母集団分布が未知)

<a id="source-L170"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L171"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L172"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L173"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  



<a id="source-L176"></a>

### 第6講 母比率の推定

<a id="source-L177"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L178"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L179"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L180"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  


<a id="source-L182"></a>

### 第7講 母分散の推定

<a id="source-L183"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L184"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L185"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L186"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  


<a id="source-L188"></a>

### 第8講 母平均の推定

<a id="source-L189"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L190"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L191"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L192"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  


<a id="source-L194"></a>

### 第9講 ウェルチの検定

<a id="source-L195"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L196"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L197"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L198"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L200"></a>チェビシェフの不等式  
<a id="source-L201"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L202"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L203"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L204"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L206"></a>中心極限定理  
<a id="source-L207"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L208"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L210"></a>ベイズの定理  
<a id="source-L211"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L212"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L213"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  

<a id="source-L215"></a>ベイジアンネットワーク  
<a id="source-L216"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L217"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  
<a id="source-L218"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  


<a id="source-L221"></a>------------------  

<a id="source-L223"></a>統計検定1級  
<a id="source-L224"></a>Statistics Test 1 Kyu  


<a id="source-L226"></a>

### 「統計検定資料」


<a id="source-L228"></a>統計検定1級に合格  
<a id="source-L229"></a><https://qiita.com/convolm/items/4a76d9e212362271ade9>  


<a id="source-L232"></a>———————————————————————————————  


<a id="source-L234"></a>

### 「統計検定1級に合格する方法」

<a id="source-L235"></a><https://qiita.com/drken/items/089b8443305df047b44e>  

> <a id="source-L237"></a>確立分布の扱いに習熟することが大切  

<a id="source-L239"></a>すうり統計学に立脚した検定論・推定論を腰を据えて学ぶ  

<a id="source-L241"></a>理工学を選ぶべき  


<a id="source-L244"></a>——————————————————————————————  


<a id="source-L246"></a>

### 「統計検定準1級に合格するための方法」

<a id="source-L247"></a><https://id.fnshr.info/2016/07/19/stat-cerf-j1q/>  

<a id="source-L249"></a>--------------------------------------------------  

<a id="source-L251"></a>確率統計  
<a id="source-L252"></a>Probability Statistics  

<a id="source-L254"></a>**〔原文の埋め込み欠落記号 U+FFFC〕**  


<a id="source-L256"></a>

### 1 確率の基礎



<a id="source-L258"></a>

### 2 確率変数



<a id="source-L260"></a>

### 3 多次元の確率分布



<a id="source-L262"></a>

### 4 推定と検定



<a id="source-L264"></a>

### 5 異なった母集団の同一性の検定とF分布



<a id="source-L266"></a>

### 6 回帰分析



<a id="source-L268"></a>

### 7 ベクトルと行列を使った回帰分析



<a id="source-L271"></a>————————————————————————  


<a id="source-L274"></a>確率統計2  


<a id="source-L276"></a>

### 1 実験計画法



<a id="source-L278"></a>

### 2 時系列解析


<a id="source-L280"></a>———————————————————  

<a id="source-L282"></a>確率統計3  


<a id="source-L284"></a>

### 1 統計モデルと尤度



<a id="source-L286"></a>

### 2 推定



<a id="source-L288"></a>

### 3 検定とモデル選択



<a id="source-L290"></a>

### 4 確率の基礎



<a id="source-L292"></a>

### 5 Markov連鎖



<a id="source-L294"></a>

### 6 Brown運動と確率積分



<a id="source-L296"></a>

### 7 伊藤の公式と確率微分方程式



<a id="source-L298"></a>

### 8 拡散過程






> <a id="source-L304"></a>現代数理統計学の基礎   

<a id="source-L305"></a><https://www.amazon.co.jp/現代数理統計学の基礎-共立講座-数学の魅力-久保川達也-ebook/dp/B0BD6PB8QX/ref=tmm_kin_swatch_0>  




> <a id="source-L310"></a>統計学入門 (基礎統計学Ⅰ)   

<a id="source-L311"></a><https://www.amazon.co.jp/統計学入門-基礎統計学Ⅰ-東京大学教養学部統計学教室/dp/4130420658>  


<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

「どんな分野でも最速で最善」という原文の表現は、読書メモとして残し、統計学の一般的な保証にはしない。推定の誤差だけでなく、標本の取り方、欠測、測定、モデルの仮定を確認する必要がある。相関を予測に使うことと、介入の効果を推定することも別。再開時には、推定したい量とデータの集まり方を一行ずつ添える。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [確率](probability.md)
- [確率過程](stochastic-processes.md)
- [微分積分学](../analysis/calculus.md)
- [線形代数](../linear-algebra/linear-algebra.md)
- [統計的機械学習](statistical-machine-learning.md)
- [ベイズ統計](bayesian-statistics.md)
- [時系列解析](time-series-analysis.md)
- [因果推論](causal-inference.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
