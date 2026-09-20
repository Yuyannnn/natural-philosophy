---
title: "グリーン関数と摂動問題"
status: draft
tags: [scrapbox, mechanics-waves]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E3%82%B0%E3%83%AA%E3%83%BC%E3%83%B3%E9%96%A2%E6%95%B0%E3%81%A8%E6%91%82%E5%8B%95%E5%95%8F%E9%A1%8C"
source_created: "2023-02-01T03:30:19Z"
source_updated: "2024-12-26T11:07:27Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# グリーン関数と摂動問題

テンソルの計算規則、外力への応答、摂動法をたどる授業・読書メモ。

原ページ作成：2023-02-01 ／ 最終更新：2024-12-26（UTC、取得時点）

[物理学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/green-functions-and-perturbation.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E3%82%B0%E3%83%AA%E3%83%BC%E3%83%B3%E9%96%A2%E6%95%B0%E3%81%A8%E6%91%82%E5%8B%95%E5%95%8F%E9%A1%8C)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<details>
<summary>本文の見出しから探す</summary>

- [機械屋の数学](#source-L9)
- [1. Introduction and Fundamentals of Tensor Analysis #1　（テンソル解析の基礎1）](#source-L13)
- [2. Fundamentals of Tensor Analysis #2　（テンソル解析の基礎2）](#source-L14)
- [3. Homogeneous and Nonhomogeneous Differential Equations　（同次・非同次方程式）](#source-L15)
- [4. Non-Homogeneous Differential Equations and Green’s Functions　](#source-L16)
- [5. Green’s Functions for Ordinary Differential Equations](#source-L18)
- [6. Green’s Functions for Heat Equations and Laplace Equations](#source-L20)
- [7. Partial Differential Equations and Green’s Function　 (偏微分方程式とグリーン関数）](#source-L22)
- [8. Regular Perturbation and Domain Perturbation Technique  (正則摂動及び領域摂動法)](#source-L23)
- [10. Boundary-Layer-Type Singular Perturbation Problems　　（境界層型特異摂動問題）](#source-L25)
- [12. Fractal Structure and Renormalization Method　　（フラクタル構造と繰り込み法）](#source-L26)
- [14. Final Exam　（期末テスト）](#source-L28)
- [第1講](#source-L31)
- [第2講](#source-L36)
- [第2講](#source-L67)
- [第3講](#source-L88)
- [第4講](#source-L105)
- [第5講](#source-L114)
- [第6講](#source-L133)
- [1 Weak Convergence](#source-L151)
- [第7講](#source-L165)
- [第8講](#source-L183)
- [第9講](#source-L194)
- [第10講](#source-L205)
- [第11講](#source-L213)
- [第12講](#source-L222)
- [「機械系のための数学」](#source-L231)
- [1.1 勾配・発散・回転](#source-L234)
- [1.2 テンソルの添字演算1](#source-L238)
- [1.3 テンソルの添字演算2](#source-L245)
- [1.4 ベクトルの積分定理](#source-L251)
- [1.5 空間曲線・曲面と曲率](#source-L257)
- [2.1 微分方程式の分類](#source-L263)
- [2.2 振動の方程式](#source-L270)
- [2.3 その他の常微分方程式](#source-L273)
- [2.4 解の定性的理論の基礎](#source-L276)
- [3.1 行列の固有値・固有ベクトル](#source-L281)
- [3.2 行列の固有値問題から演算子の固有値問題へ](#source-L284)
- [3.3 演算子の固有値・固有関数](#source-L287)
- [4.1 機械工学で用いられる偏微分方程式](#source-L292)
- [4.2 双曲型方程式](#source-L298)
- [4.3 放物型方程式](#source-L302)
- [4.4 楕円型方程式](#source-L305)
- [4.5 非線形方程](#source-L309)
- [5.1 汎関数](#source-L315)
- [5.2 超関数とデルタ関数](#source-L318)
- [5.3 デルタ関数の公式](#source-L321)
- [5.4 クロネッカーのデルタとディラックのデルタ](#source-L324)
- [6.1 フーリエ級数](#source-L330)
- [6.2 フーリエ変換](#source-L333)
- [6.3 フーリエ変換の重要な関係式](#source-L336)
- [6.4 フーリエ変換による常微分方程式の解法](#source-L339)
- [6.5 非同次スツルム・リウビル型微分方程式とグリーン関数](#source-L342)
- [6.6 フーリエ変換による偏微分方程式の解法](#source-L345)
- [6.7 よく用いられる微分方程式とそのグリーン関数](#source-L348)
- [7.1 汎関数微分と変分問題](#source-L353)
- [7.2 オイラー・ラグランジュの微分方程式](#source-L356)
- [7.3 拘束条件のある場合の変分法](#source-L359)
- [7.4 近似解の計算法](#source-L362)
- [7.5 有限要素法](#source-L366)
- [8.1 単純摂動展開](#source-L375)
- [8.2 領域摂動法](#source-L379)
- [8.3 特異摂動法](#source-L383)
- [8.4 くりこみ群の基礎](#source-L394)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### グリーン関数と摂動問題

<a id="source-L2"></a>[常微分方程式](../../math/analysis/ordinary-differential-equations.md)  
<a id="source-L3"></a>[偏微分方程式](../../math/analysis/partial-differential-equations.md)  
<a id="source-L4"></a>[フーリエ変換とラプラス変換](../../math/analysis/fourier-and-laplace-transforms.md)  
<a id="source-L5"></a>[関数解析](../../math/analysis/functional-analysis.md)  
<a id="source-L6"></a>[解析力学](analytical-mechanics.md)  



<a id="source-L9"></a>

### 機械屋の数学

<a id="source-L10"></a><https://www.jsme.or.jp/kaisi-tag/%E6%A9%9F%E6%A2%B0%E5%B1%8B%E3%81%AE%E6%95%B0%E5%AD%A6/>  

<a id="source-L12"></a>Contents:  

<a id="source-L13"></a>

### 1. Introduction and Fundamentals of Tensor Analysis #1　（テンソル解析の基礎1）


<a id="source-L14"></a>

### 2. Fundamentals of Tensor Analysis #2　（テンソル解析の基礎2）


<a id="source-L15"></a>

### 3. Homogeneous and Nonhomogeneous Differential Equations　（同次・非同次方程式）


<a id="source-L16"></a>

### 4. Non-Homogeneous Differential Equations and Green’s Functions　

<a id="source-L17"></a>（非同次方程式とグリーン関数）  

<a id="source-L18"></a>

### 5. Green’s Functions for Ordinary Differential Equations

<a id="source-L19"></a>（常微分方程式に対するグリーン関数）  

<a id="source-L20"></a>

### 6. Green’s Functions for Heat Equations and Laplace Equations

<a id="source-L21"></a>（熱伝導方程式とラプラス方程式に対するグリーン関数）  

<a id="source-L22"></a>

### 7. Partial Differential Equations and Green’s Function　 (偏微分方程式とグリーン関数）


<a id="source-L23"></a>

### 8. Regular Perturbation and Domain Perturbation Technique  (正則摂動及び領域摂動法)

<a id="source-L24"></a>9. Multiple-Time-Scale-Type Singular Perturbation Problems 　（多重時間スケール型特異摂動問題）  

<a id="source-L25"></a>

### 10. Boundary-Layer-Type Singular Perturbation Problems　　（境界層型特異摂動問題）


<a id="source-L26"></a>

### 12. Fractal Structure and Renormalization Method　　（フラクタル構造と繰り込み法）

<a id="source-L27"></a>13. Renormalization Method for Singular Perturbation Problems　（特異摂動問題に対する繰り込み法）  

<a id="source-L28"></a>

### 14. Final Exam　（期末テスト）




<a id="source-L31"></a>

### 第1講


<a id="source-L33"></a>毎回小さな宿題がある  



<a id="source-L36"></a>

### 第2講


<a id="source-L38"></a>Linear Operator Theory on Hilbert Space  

<a id="source-L40"></a>Fundamentals of Tensor Analysis  

<a id="source-L42"></a>１、Kronecker Delta  

<a id="source-L44"></a>２、Eddington’s Epsilon  

<a id="source-L46"></a>３、Einstein’s Summation Notation  

<a id="source-L48"></a>４、Inner Product  

<a id="source-L50"></a>5、Cross Product  

<a id="source-L52"></a>６、Differential Operators  

<a id="source-L54"></a>Graradient, Divergence, Rotation  

<a id="source-L56"></a>まず意味を考えて、答えがわかるべき  
<a id="source-L57"></a>イプシロンの添字を交代させると、値が-になるので、これを利用して0を示すことが多い  

<a id="source-L59"></a>ナブラで基底を省くのは、free-indexを見れば次元がわかるから  

<a id="source-L61"></a>ナブラの二乗はinner product  

<a id="source-L63"></a>try to use the English  




<a id="source-L67"></a>

### 第2講

<a id="source-L68"></a>some incorrect answers  

<a id="source-L70"></a>順番を変えてはいけない  
<a id="source-L71"></a>二乗にしてはいけない  
<a id="source-L72"></a>ちゃんとindexを二回  
<a id="source-L73"></a>というのも添字の数でEinsteinの規則を適用しているので  
<a id="source-L74"></a>indexは2つまで  
<a id="source-L75"></a>4つ以上はおかしい  

<a id="source-L77"></a>(4)が正解  

<a id="source-L79"></a>(4)が一番大事で、覚えるべき  

<a id="source-L81"></a>ベクトル解析を公式を使うと、式をうまく変形できることがある  

<a id="source-L83"></a>()をかってにとってはいけない  
<a id="source-L84"></a>あと、δとεの順番は変えていいが、文字の順番は変えてはいけない！！  




<a id="source-L88"></a>

### 第3講


<a id="source-L90"></a>宿題の１つ目はGreenの定理であり、ストークスの定理やガウスの定理と関係ある？  

<a id="source-L92"></a>同次微分方程式と非同次微分方程式について  
<a id="source-L93"></a>同次方程式はexp(λx)を代入して重ね合わせで終わり  

<a id="source-L95"></a>非同次微分方程式の場合は特殊解を１つ求めて、それを同次方程式の解に足し算すれば良い  

<a id="source-L97"></a>非同次方程式と同次方程式の解は結構異なる  

<a id="source-L99"></a>同次方程式のいつもの、２つの重みがバネで繋がれているときの解析の復習  

<a id="source-L101"></a>次はNこの物体がバネで繋がれているときの解析の復習  




<a id="source-L105"></a>

### 第4講

<a id="source-L106"></a>宿題は定数変化法でやればよかった  

<a id="source-L108"></a>バネのNこの錬成系の問題を行列を使って解こうとしている  
<a id="source-L109"></a>いつものやつ  

<a id="source-L111"></a>機械系数理工学の復習  



<a id="source-L114"></a>

### 第5講

<a id="source-L115"></a>泡の入った液体では伝達する速さが普通とは異なる  
<a id="source-L116"></a>というのも、mが液体、kが気体となる  

<a id="source-L118"></a>固有関数と固有ベクトルが離散と連続の  

<a id="source-L120"></a>固有ベクトルはいつも固有関数の線上にある  
<a id="source-L121"></a>これは面白い  

<a id="source-L123"></a>変数分離ほうで解けるのは、こういう風に表せるvが見つかるからである  

<a id="source-L125"></a>非線型では、一般解は線型の一般解と特殊解の重ね合わせで表せる  
<a id="source-L126"></a>どのようにして特殊解を見つけるのか？  
<a id="source-L127"></a>ここで活躍するのがGreen関数である  

<a id="source-L129"></a>H.W.  
<a id="source-L130"></a>decide a1 and a2  



<a id="source-L133"></a>

### 第6講

<a id="source-L134"></a>宿題は、もう１つa1とa2の式があればよかった  
<a id="source-L135"></a>これは普通に積分して条件を出して求められる  

<a id="source-L137"></a>グリーン関数はインパルス応答のようなものでこれをξに関して和をとることでuが求まる  

<a id="source-L139"></a>inhomogeneous partial differential equation  
<a id="source-L140"></a>xの境界の値が限られている時は境界の値によって固有値が困ったが、このように決まっていない時は新しいアプローチが必要になる  
<a id="source-L141"></a>今回はフーリエ変換による方法を紹介する  
<a id="source-L142"></a>どのようにしてGを決めるのか？  
<a id="source-L143"></a>あとで示す  

<a id="source-L145"></a>今回はフーリエ変換を使って解く  
<a id="source-L146"></a>フーリエ変換を使えば、Gを考えなくても良い  

<a id="source-L148"></a>0\~∞ならラプラス変換が良い  

<a id="source-L150"></a>limT(x,t)expがなぜ０になるのか  

<a id="source-L151"></a>

### 1 Weak Convergence


<a id="source-L153"></a>フーリエ変換は、微分がただの変数になるのでとても良い  
<a id="source-L154"></a>これは変数分離で解けそう  

<a id="source-L156"></a>同時方程式では定数だったが、非同次のときは定数変化ほうで解いてみるか  

<a id="source-L158"></a>非同次の境界条件を持つ同次方程式の解と同次の境界条件を持つ非同次方程式の重ね合わせでかける  

<a id="source-L160"></a>偏微分方程式のタイプに合わせていろいろなgreen関数が知られている  
<a id="source-L161"></a>これを覚えておけば秒で解が出せる  




<a id="source-L165"></a>

### 第7講

<a id="source-L166"></a>宿題には２種類のやり方がある  

<a id="source-L168"></a>まずは境界条件がない時のグリーン関数の解き方をやった  
<a id="source-L169"></a>今回は境界条件があるときのグリーン関数の解き方をやりますやります  

<a id="source-L171"></a>フーリエ変換はいろんな意味がある  
<a id="source-L172"></a>フーリエ解析を学んだ後だと複素積分を使う意義が感じられる  
<a id="source-L173"></a>というのも、フーリエ逆変換やラプラス逆変換に出てくるので  
<a id="source-L174"></a>だが、これらの計算は表などに頼れるので、フーリエ解析の方が学ぶ意味がありそう  

<a id="source-L176"></a>ベッセル関数は弦の振動に相当する  
<a id="source-L177"></a>丸い面の振動もベッセル関数  
<a id="source-L178"></a>JnとNnはsinとcosのようなもの  
<a id="source-L179"></a>直交する  




<a id="source-L183"></a>

### 第8講

<a id="source-L184"></a>境界条件がない時とある時でグリーン関数に変化がある  

<a id="source-L186"></a>境界条件がないGreen関数はFourier使えば良いが、境界条件があるときはフーリエ級数展開でok  

<a id="source-L188"></a>フーリエ級数展開とフーリエ変換の違いについて  

<a id="source-L190"></a>摂動法の基本について  




<a id="source-L194"></a>

### 第9講

<a id="source-L195"></a>ナビエストークス方程式から境界層が導かれる話  

<a id="source-L197"></a>オーダーで考察する  

<a id="source-L199"></a>逆に、厳密解から分けた答えを予想することもできる  

<a id="source-L201"></a>まあ要するに教科書よめ  




<a id="source-L205"></a>

### 第10講

<a id="source-L206"></a>復習と宿題の解説  

<a id="source-L208"></a>より高次の項の解法について説明する  





<a id="source-L213"></a>

### 第11講

<a id="source-L214"></a>高次の項については複雑なのでいろいろなやり方がある  

<a id="source-L216"></a>Umatch1は片方のものがめっちゃでかいので  
<a id="source-L217"></a>これは後で別のスライドを用意する  

<a id="source-L219"></a>ドットの意味が変わっているところがある  



<a id="source-L222"></a>

### 第12講

<a id="source-L223"></a>Why do we need to learn multiple time scale method when this method is much simpler?  
<a id="source-L224"></a>→  
<a id="source-L225"></a>given time dependent problem, we dont know how to solve that  



<a id="source-L229"></a>—————————————————————————————————————————  


<a id="source-L231"></a>

### 「機械系のための数学」


<a id="source-L233"></a>1章 ベクトル解析とテンソルの基礎  

<a id="source-L234"></a>

### 1.1 勾配・発散・回転

<a id="source-L235"></a>ベクトルで表記するときに、順番を変えて、微分演算子が基底ベクトルに作用していないことを明記できる  
<a id="source-L236"></a>勾配の演算はテンソルの階数を１つあげ、発散の演算はテンソルの階数を１つ下げる微分演算である  


<a id="source-L238"></a>

### 1.2 テンソルの添字演算1

<a id="source-L239"></a>テンソルはいくつかの方向と関連づけて定義される量  
<a id="source-L240"></a>アインシュタインの縮約規則  
<a id="source-L241"></a>ベクトルやテンソルそのものは座標変換に影響を受けない量だが、その成分は用いる基底によって異なるものとなる  
<a id="source-L242"></a>テンソルの不変量は３つある  
<a id="source-L243"></a>対角和と第二不変量と行列式  


<a id="source-L245"></a>

### 1.3 テンソルの添字演算2

<a id="source-L246"></a>ここでは、基底を省略  
<a id="source-L247"></a>基底としてデカルト座標系を選んだときは、基底ベクトルの空間微分がゼロベクトルになることを考慮に入れると、基底を省略し、添え字のみでテンソルの階数を表す方が便利  
<a id="source-L248"></a>内積、外積、勾配、発散、回転  
<a id="source-L249"></a>ベクトル恒等式  


<a id="source-L251"></a>

### 1.4 ベクトルの積分定理

<a id="source-L252"></a>ガウスの発散定理  
<a id="source-L253"></a>ストークスの定理  
<a id="source-L254"></a>グリーンの定理  
<a id="source-L255"></a>レイノルズの輸送定理  


<a id="source-L257"></a>

### 1.5 空間曲線・曲面と曲率

<a id="source-L258"></a>接線ベクトル  
<a id="source-L259"></a>フレネーー・セレーの公式  


<a id="source-L262"></a>2章 常微分方程式  

<a id="source-L263"></a>

### 2.1 微分方程式の分類

<a id="source-L264"></a>常微分と偏微分  
<a id="source-L265"></a>線形方程式と非線形方程式  
<a id="source-L266"></a>階数  
<a id="source-L267"></a>同次と非同次  
<a id="source-L268"></a>定係数と変形数  


<a id="source-L270"></a>

### 2.2 振動の方程式

<a id="source-L271"></a>5億回見たやつ  


<a id="source-L273"></a>

### 2.3 その他の常微分方程式

<a id="source-L274"></a>あるある  


<a id="source-L276"></a>

### 2.4 解の定性的理論の基礎

<a id="source-L277"></a>2でやった  


<a id="source-L280"></a>3章 固有値問題  

<a id="source-L281"></a>

### 3.1 行列の固有値・固有ベクトル

<a id="source-L282"></a>5億回見たやつ  


<a id="source-L284"></a>

### 3.2 行列の固有値問題から演算子の固有値問題へ

<a id="source-L285"></a>非連続と連続の比較  


<a id="source-L287"></a>

### 3.3 演算子の固有値・固有関数

<a id="source-L288"></a>スツリム・リウビル型微分方程式の固有値問題  


<a id="source-L291"></a>4章 偏微分方程式  

<a id="source-L292"></a>

### 4.1 機械工学で用いられる偏微分方程式

<a id="source-L293"></a>双曲型、放物型、楕円型に分けられる  
<a id="source-L294"></a>双曲型：振動や波の伝播、波動方程式  
<a id="source-L295"></a>放物型：熱伝導や流れのない系での物質の拡散、拡散方程式、熱伝導方程式  
<a id="source-L296"></a>楕円型：ポテンシャル量を支配する方程式、ポアソン方程式  


<a id="source-L298"></a>

### 4.2 双曲型方程式

<a id="source-L299"></a>変数分離  
<a id="source-L300"></a>スツリム・リウビル型  


<a id="source-L302"></a>

### 4.3 放物型方程式

<a id="source-L303"></a>変数分離  


<a id="source-L305"></a>

### 4.4 楕円型方程式

<a id="source-L306"></a>オイラー型  
<a id="source-L307"></a>スツリム・リウビル型  


<a id="source-L309"></a>

### 4.5 非線形方程

<a id="source-L310"></a>バーガース方程式  



<a id="source-L314"></a>5章 汎関数と超関数  

<a id="source-L315"></a>

### 5.1 汎関数

<a id="source-L316"></a>関数から数への対応  


<a id="source-L318"></a>

### 5.2 超関数とデルタ関数

<a id="source-L319"></a>超関数の微分など  


<a id="source-L321"></a>

### 5.3 デルタ関数の公式

<a id="source-L322"></a>いろいろな公式  


<a id="source-L324"></a>

### 5.4 クロネッカーのデルタとディラックのデルタ

<a id="source-L325"></a>いろいろ  



<a id="source-L329"></a>6章 フーリエ解析とグリーン関数  

<a id="source-L330"></a>

### 6.1 フーリエ級数

<a id="source-L331"></a>知ってた  


<a id="source-L333"></a>

### 6.2 フーリエ変換

<a id="source-L334"></a>知ってた  


<a id="source-L336"></a>

### 6.3 フーリエ変換の重要な関係式

<a id="source-L337"></a>覚えろ〜  


<a id="source-L339"></a>

### 6.4 フーリエ変換による常微分方程式の解法

<a id="source-L340"></a>非同次方程式の特解を求める手段としてフーリエ変換は有力  


<a id="source-L342"></a>

### 6.5 非同次スツルム・リウビル型微分方程式とグリーン関数

<a id="source-L343"></a>グリーン関数はすごい  


<a id="source-L345"></a>

### 6.6 フーリエ変換による偏微分方程式の解法

<a id="source-L346"></a>定数変化法  


<a id="source-L348"></a>

### 6.7 よく用いられる微分方程式とそのグリーン関数

<a id="source-L349"></a>グリーン関数がわかれば微分方程式は解けたも同然  


<a id="source-L352"></a>7章 変分法の基礎  

<a id="source-L353"></a>

### 7.1 汎関数微分と変分問題

<a id="source-L354"></a>やった  


<a id="source-L356"></a>

### 7.2 オイラー・ラグランジュの微分方程式

<a id="source-L357"></a>やった  


<a id="source-L359"></a>

### 7.3 拘束条件のある場合の変分法

<a id="source-L360"></a>やった  


<a id="source-L362"></a>

### 7.4 近似解の計算法

<a id="source-L363"></a>レイリーリッツの方法  
<a id="source-L364"></a>ガラーキンの方法  


<a id="source-L366"></a>

### 7.5 有限要素法

<a id="source-L367"></a>レイリーリッツの方法とガラーキンの方法は汎関数の停留問題に対する解を求める際にオイラーラグランジュ方程式をとかずに解を規定関数による級数展開で近似して直接計算する方法だった  
<a id="source-L368"></a>これは方程式や境界条件が比較的単純な問題に対しては有効だが、非線形や多次元問題はきつい  
<a id="source-L369"></a>有限要素法は、解析の対象となる領域を一度に扱うので半買う、多数の小領域に分割して取り扱う  
<a id="source-L370"></a>そして小領域ごとの簡単な近似式で解を構成しそれらを結合して全体の解を作る  



<a id="source-L374"></a>8章 摂動法の基礎  

<a id="source-L375"></a>

### 8.1 単純摂動展開

<a id="source-L376"></a>単純摂動法は解の形を微小パラメータを用いて冪級数の形で表し、εのべきごとに揃え、方程式と分離し、それぞれの方程式を解く  
<a id="source-L377"></a>εのより高次な項に注目するほど真の解に近づける  


<a id="source-L379"></a>

### 8.2 領域摂動法

<a id="source-L380"></a>領域摂動法とは、ある形状に対して解が与えられるとき、その形状からわずかにずれた形状に対しての近似解を求める方法である  
<a id="source-L381"></a>通常、ラプラス方程式やポアソン方程式などの境界値問題に対して、解析解が与えられる単純な形状からずれた場合の解を計算するのに用いられる  


<a id="source-L383"></a>

### 8.3 特異摂動法

<a id="source-L384"></a>特異摂動法は単純に小さいパラメータに関するべき級数の展開では解けない問題に対して適用する手法  
<a id="source-L385"></a>ここでは、境界層に関連する問題と時間方向に多重スケール性を持つ２つの異なるタイプの問題について説明する  

<a id="source-L387"></a>・境界層型  
<a id="source-L388"></a>接合漸近展開法という手法で近似解を求める必要がある  
<a id="source-L389"></a>数学的な意味で境界層が形成される  

<a id="source-L391"></a>・多重時間スケール型  
<a id="source-L392"></a>振り子の問題をより正確に取ることができる  


<a id="source-L394"></a>

### 8.4 くりこみ群の基礎

<a id="source-L395"></a>くりこみ群の手法には様々な手法があり、多くの場合が高度な数学的技法と結びついている  
<a id="source-L396"></a>相変化・相転移などの臨海現象の解析を始め、工学でしばしば問題となる多重スケール問題などで強力なツールになる  

<a id="source-L398"></a>与えられた式の中に同じ構造がまた見られる入れ子構造のようになっており、その特性を用いて式を整理する操作をくりこみという  





<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

グリーン関数は微分演算子だけで一意には決まらない。境界条件や初期条件を含めて $LG(x,\xi)=\delta(x-\xi)$ を定め、適切な条件下で外力への応答を積分で表す。定常境界値問題と時間発展の因果的応答を区別する。摂動法では小さい係数の項が全域で小さいとは限らず、境界層や長時間で近似が破れることがある。元の「なぜ別の方法を学ぶのか」は、近似の適用範囲を比較する問いとして残せる。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [常微分方程式](../../math/analysis/ordinary-differential-equations.md)
- [偏微分方程式](../../math/analysis/partial-differential-equations.md)
- [フーリエ変換とラプラス変換](../../math/analysis/fourier-and-laplace-transforms.md)
- [関数解析](../../math/analysis/functional-analysis.md)
- [解析力学](analytical-mechanics.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
