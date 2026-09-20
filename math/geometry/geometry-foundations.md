---
title: "幾何学の基礎of基礎"
status: draft
tags: [scrapbox, geometry]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E5%B9%BE%E4%BD%95%E5%AD%A6%E3%81%AE%E5%9F%BA%E7%A4%8Eof%E5%9F%BA%E7%A4%8E"
source_created: "2023-01-21T18:32:58Z"
source_updated: "2023-01-22T07:05:58Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 幾何学の基礎of基礎

変換で変わらない性質に注目し、トポロジーとテンソルを学ぶ授業メモ。

原ページ作成：2023-01-21 ／ 最終更新：2023-01-22（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/geometry-foundations.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E5%B9%BE%E4%BD%95%E5%AD%A6%E3%81%AE%E5%9F%BA%E7%A4%8Eof%E5%9F%BA%E7%A4%8E)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

## 思考の手がかり

> すかすかなのはノートの画像を消しているからです。。(コピペではるとバグる + 流石にノートまで貼ったら著作権的に大丈夫かな・・って心配)

[本文の該当箇所へ](#source-L5)

<details>
<summary>本文の見出しから探す</summary>

- [1 トポロジー ](#source-L9)
- [1.1 位相空間 ](#source-L10)
- [1.2 ホモトピー ](#source-L11)
- [1.3 複体 ](#source-L12)
- [1.4 ホモロジー ](#source-L13)
- [2 テンソル ](#source-L15)
- [2.1 ベクトル空間の要素としてのテンソル ](#source-L16)
- [2.2 共変テンソル空間 ](#source-L17)
- [2.3 対称テンソルと交代テンソル ](#source-L18)
- [2.4 テンソル密度と擬テンソル](#source-L19)
- [第1講](#source-L23)
- [第2講](#source-L36)
- [第3講](#source-L53)
- [第4講](#source-L64)
- [第5講](#source-L75)
- [第6講](#source-L86)
- [第7講](#source-L107)
- [第8講](#source-L118)
- [第9講](#source-L129)
- [第10講](#source-L159)
- [第11講](#source-L163)
- [第12講](#source-L195)
- [1.位相空間：「近さ」が備わった空間概念](#source-L204)
- [2.位相幾何：連続変形に対する普遍性](#source-L205)
- [3.テンソル：座標変換に対する普遍性](#source-L208)
- [第1章 位相空間](#source-L210)
- [1.1 距離空間](#source-L211)
- [1.2 位相空間](#source-L215)
- [1.3 連結性](#source-L218)
- [1.4 コンパクト性](#source-L220)
- [第2章 位相幾何](#source-L223)
- [2.1 ホモトピー](#source-L224)
- [2.2 基本群](#source-L228)
- [2.3 被覆空間](#source-L230)
- [2.4 ホモロジー](#source-L232)
- [2.5 ホモロジーの計算1](#source-L236)
- [2.6 ホモロジーの計算2](#source-L239)
- [第3章 テンソル](#source-L241)
- [3.1 テンソルの定義](#source-L242)
- [3.2 テンソル解析1](#source-L243)
- [3.3 テンソル解析2](#source-L244)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 幾何学の基礎of基礎


> <a id="source-L3"></a>幾何数理工学授業めも  

> <a id="source-L5"></a>すかすかなのはノートの画像を消しているからです。。(コピペではるとバグる + 流石にノートまで貼ったら著作権的に大丈夫かな・・って心配)  

<a id="source-L7"></a>幾何学とは，「図形の変形方法が与えられたとき，その変形で変わらない性質を調べる学問」であるといわれる．本講義では，この考え方をさらに一般化して，「一定の変換群で不変な性質を調べる数学的手法」を学ぶことを目的として，「トポロジー」と「テンソル」の基礎的事項を学ぶ．トポロジーでは，位相同型写像とよばれる変換で不変な性質に注目する．テンソルでは，座標変換で不変な性質に注目する．いずれも，一見手のつけようのない複雑な対象の本質を体系的にとらえるアイディアを学ぶことに主眼を置く．  


<a id="source-L9"></a>

### 1 トポロジー 


<a id="source-L10"></a>

### 1.1 位相空間 


<a id="source-L11"></a>

### 1.2 ホモトピー 


<a id="source-L12"></a>

### 1.3 複体 


<a id="source-L13"></a>

### 1.4 ホモロジー 



<a id="source-L15"></a>

### 2 テンソル 


<a id="source-L16"></a>

### 2.1 ベクトル空間の要素としてのテンソル 


<a id="source-L17"></a>

### 2.2 共変テンソル空間 


<a id="source-L18"></a>

### 2.3 対称テンソルと交代テンソル 


<a id="source-L19"></a>

### 2.4 テンソル密度と擬テンソル





<a id="source-L23"></a>

### 第1講



<a id="source-L26"></a>距離空間  

<a id="source-L28"></a>境界点、境界、触点、開集合、閉集合  

<a id="source-L30"></a>近傍  

<a id="source-L32"></a>開集合系  




<a id="source-L36"></a>

### 第2講

<a id="source-L37"></a>位相と位相空間  

<a id="source-L39"></a>連続写像  

<a id="source-L41"></a>同相  

<a id="source-L43"></a>相対位相  

<a id="source-L45"></a>直積位相  

<a id="source-L47"></a>商位相  






<a id="source-L53"></a>

### 第3講


<a id="source-L55"></a>Pasty Lemma  

<a id="source-L57"></a>位相空間の例  

<a id="source-L59"></a>連結性  





<a id="source-L64"></a>

### 第4講


<a id="source-L66"></a>弧状連結性  

<a id="source-L68"></a>コンパクト性  







<a id="source-L75"></a>

### 第5講


<a id="source-L77"></a>ルベーグ数の補題  

<a id="source-L79"></a>ハイネ・ボレルの被覆定理  

<a id="source-L81"></a>ホモトピー  





<a id="source-L86"></a>

### 第6講




<a id="source-L90"></a>ホモトピー同値  

<a id="source-L92"></a>ホモトピー類＝同値類  

<a id="source-L94"></a>変形レトラクション  

<a id="source-L96"></a>可縮な空間  

<a id="source-L98"></a>群、基本群  


<a id="source-L101"></a>準同型、同型  

<a id="source-L103"></a>パス、ループ  




<a id="source-L107"></a>

### 第7講


<a id="source-L109"></a>基点の取り替え  

<a id="source-L111"></a>単連結  

<a id="source-L113"></a>同相写像  





<a id="source-L118"></a>

### 第8講


<a id="source-L120"></a>被覆空間、被覆写像  

<a id="source-L122"></a>リフト  

<a id="source-L124"></a>射影平面の基本群、トーラスの基本群  





<a id="source-L129"></a>

### 第9講


<a id="source-L131"></a>基本群は二次元の穴が検出できる  
<a id="source-L132"></a>ホモロジー群は高次元の穴が検出できる、可換で計算も楽  

<a id="source-L134"></a>単体  

<a id="source-L136"></a>n次元単体  

<a id="source-L138"></a>向きつけられた単体は頂点の順番が指定されている、つまり面にも向きが誘導される  

<a id="source-L140"></a>特異ホモロジー  

<a id="source-L142"></a>特異n単体は向きつけられたn単体からXへの連続写像  

<a id="source-L144"></a>特異nチェインは特異n単体たちの有限な形式的整数結合  

<a id="source-L146"></a>Cnは特異nチェインの集合（アーベル群になる）  


<a id="source-L149"></a>ホモロジー群  
<a id="source-L150"></a>Ker∂n / Im∂n  


<a id="source-L153"></a>位相不変性：ホモトピー不変性  






<a id="source-L159"></a>

### 第10講





<a id="source-L163"></a>

### 第11講

<a id="source-L164"></a>テンソルの定義  

<a id="source-L166"></a>物理現象のモデリング  
<a id="source-L167"></a>多様体論への準備  

<a id="source-L169"></a>Kが環の時はVをK加群という  

<a id="source-L171"></a>基底は存在する←ツォルンの補題を使う  

<a id="source-L173"></a>Vがn次元↔︎n個の元からなる基底が存在  

<a id="source-L175"></a>フーリエ変換での基底は上の意味での基底ではない（代数基底、ハメル基底）  

<a id="source-L177"></a>双対空間  
<a id="source-L178"></a>V:n次元たてベクトル空間  
<a id="source-L179"></a>V\*:n次元横ベクトル空間  

<a id="source-L181"></a>双対基底  

<a id="source-L183"></a>無限次元ベクトル空間ではV = V\*\*とはならない  

<a id="source-L185"></a>ベクトルはインデックスが1つの数の組  
<a id="source-L186"></a>行列はインデックスが２つの数の組  
<a id="source-L187"></a>テンソルはインデックスがkつの数の組  

<a id="source-L189"></a>双線型写像は要するに二次形式のようなもの  

<a id="source-L191"></a>テンソル積は色々な定義があり、それぞれの難しさがある  




<a id="source-L195"></a>

### 第12講







<a id="source-L202"></a>ーーーーーーーーー講義資料ーーーーーーーーー  
<a id="source-L203"></a>本講義の内容  

<a id="source-L204"></a>

### 1.位相空間：「近さ」が備わった空間概念


<a id="source-L205"></a>

### 2.位相幾何：連続変形に対する普遍性

<a id="source-L206"></a>—基本群  
<a id="source-L207"></a>—ホモロジー  

<a id="source-L208"></a>

### 3.テンソル：座標変換に対する普遍性



<a id="source-L210"></a>

### 第1章 位相空間


<a id="source-L211"></a>

### 1.1 距離空間

<a id="source-L212"></a>D1\~D3の条件を満たすとき、dをX上の距離函数という  
<a id="source-L213"></a>(X,d)を距離空間と呼ぶ  


<a id="source-L215"></a>

### 1.2 位相空間

<a id="source-L216"></a>Xに「位相（topology）」を入れて空間にする。「位相」を入れるとは、Xの開集合族を指定することである。  


<a id="source-L218"></a>

### 1.3 連結性



<a id="source-L220"></a>

### 1.4 コンパクト性




<a id="source-L223"></a>

### 第2章 位相幾何


<a id="source-L224"></a>

### 2.1 ホモトピー

<a id="source-L225"></a>２つの空間が同じ形をしているとはどういうことか？  
<a id="source-L226"></a>⇨位相空間X,Yが位相同型=連続全単射のfの存在  


<a id="source-L228"></a>

### 2.2 基本群



<a id="source-L230"></a>

### 2.3 被覆空間



<a id="source-L232"></a>

### 2.4 ホモロジー

<a id="source-L233"></a>基本群：「２次元の穴」を検出できる、非可換、計算は一般に難しい  
<a id="source-L234"></a>ホモロジー群：「高次元の穴」を検出できる、可換、計算が比較的容易  


<a id="source-L236"></a>

### 2.5 ホモロジーの計算1




<a id="source-L239"></a>

### 2.6 ホモロジーの計算2



<a id="source-L241"></a>

### 第3章 テンソル


<a id="source-L242"></a>

### 3.1 テンソルの定義


<a id="source-L243"></a>

### 3.2 テンソル解析1


<a id="source-L244"></a>

### 3.3 テンソル解析2




<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

原文には、ノート画像を削除したため内容が疎になっている旨が明記されている。その空白を、本人が書いた説明として補完しない。本文の基本群についての「2次元の穴」という表現も、そのまま一般的な定義にはできない。基本群は基点付きループとそのホモトピーを扱う。穴の次元という直感を使うなら、円周と球面などの具体例で意味を確かめる。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [同じ分野のノート](README.md)：幾何・テンソル。

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
