---
title: "グラフ理論/離散数学"
status: draft
tags: [scrapbox, information-discrete]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E3%82%B0%E3%83%A9%E3%83%95%E7%90%86%E8%AB%96%2F%E9%9B%A2%E6%95%A3%E6%95%B0%E5%AD%A6"
source_created: "2023-01-21T17:15:15Z"
source_updated: "2024-12-23T12:59:15Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# グラフ理論/離散数学

組合せ構造から、最短路・最大流・マッチングなどを学ぶ記録。

原ページ作成：2023-01-21 ／ 最終更新：2024-12-23（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/graph-theory.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E3%82%B0%E3%83%A9%E3%83%95%E7%90%86%E8%AB%96%2F%E9%9B%A2%E6%95%A3%E6%95%B0%E5%AD%A6)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<details>
<summary>本文の見出しから探す</summary>

- [0. グラフ基礎](#source-L11)
- [1. 平面グラフ、双対平面グラフ](#source-L12)
- [2. 2部グラフ、Eulerグラフ、双対性](#source-L13)
- [3. ネットワーク、最大流問題、最大流最小カット定理](#source-L14)
- [4. 最大2部マッチング点被覆定理、Mengerの定理](#source-L15)
- [5. 線形計画法、単体法](#source-L16)
- [6. 双対定理、相補性定理](#source-L17)
- [7. 線形計画法と整数性、完全単模行列](#source-L18)
- [8. 最小費用流問題](#source-L19)
- [9. 理想グラフ](#source-L20)
- [10. 区間グラフ](#source-L21)
- [11. マトロイド、独立性、双対性](#source-L22)
- [12. 双対性、貪欲アルゴリズム](#source-L23)
- [13. グラフマイナー理論](#source-L24)
- [14. 離散数学まとめ](#source-L25)
- [第1講 グラフの基礎](#source-L28)
- [第2講 ネットワークフローの基礎](#source-L49)
- [第3講 ネットワークフローの基礎](#source-L61)
- [第4講 線形計画](#source-L67)
- [第5講 線形計画の双対性](#source-L90)
- [第6講 計算量理論](#source-L95)
- [第7講 最短路問題](#source-L111)
- [第8講 最小費用流](#source-L114)
- [第9講 Matroid](#source-L119)
- [第10講](#source-L147)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### グラフ理論/離散数学


<a id="source-L3"></a>\[競技プログラミングでよくあるアルゴリズム集\]  
<a id="source-L4"></a>\[知識グラフについて調べる\]  
<a id="source-L5"></a>[Graph Neural Network](graph-neural-networks.md)  
<a id="source-L6"></a>[ネットワーク分析](network-analysis.md)  


<a id="source-L9"></a>有限離散の組合せ構造の諸性質を解析し、組合せ最適化を効率よく行うアルゴリズムを講究する。  


<a id="source-L11"></a>

### 0. グラフ基礎


<a id="source-L12"></a>

### 1. 平面グラフ、双対平面グラフ


<a id="source-L13"></a>

### 2. 2部グラフ、Eulerグラフ、双対性


<a id="source-L14"></a>

### 3. ネットワーク、最大流問題、最大流最小カット定理


<a id="source-L15"></a>

### 4. 最大2部マッチング点被覆定理、Mengerの定理


<a id="source-L16"></a>

### 5. 線形計画法、単体法


<a id="source-L17"></a>

### 6. 双対定理、相補性定理


<a id="source-L18"></a>

### 7. 線形計画法と整数性、完全単模行列


<a id="source-L19"></a>

### 8. 最小費用流問題


<a id="source-L20"></a>

### 9. 理想グラフ


<a id="source-L21"></a>

### 10. 区間グラフ


<a id="source-L22"></a>

### 11. マトロイド、独立性、双対性


<a id="source-L23"></a>

### 12. 双対性、貪欲アルゴリズム


<a id="source-L24"></a>

### 13. グラフマイナー理論


<a id="source-L25"></a>

### 14. 離散数学まとめ




<a id="source-L28"></a>

### 第1講 グラフの基礎

<a id="source-L29"></a>vertex set:点集合  
<a id="source-L30"></a>Edge set:辺集合  
<a id="source-L31"></a>(U,v)でuからvへの枝を表す  
<a id="source-L32"></a>(U,u)で自己閉路を表す  
<a id="source-L33"></a>無限グラフになると色々おかしいことが起こるので有限グラフで考える  

<a id="source-L35"></a>枝は無向と有向を考える。  

<a id="source-L37"></a>単純：自己閉路、並列枝なし  
<a id="source-L38"></a>完全グラフ：どの2点の間にも枝がある→枝数はCで求められる  
<a id="source-L39"></a>Planer：平面上の交差なしで描ける  
<a id="source-L40"></a>削除：  
<a id="source-L41"></a>縮約：  
<a id="source-L42"></a>全域木：  
<a id="source-L43"></a>Eulerの定理：  
<a id="source-L44"></a>双対平面グラフ  





<a id="source-L49"></a>

### 第2講 ネットワークフローの基礎

<a id="source-L50"></a>ネットワーク：重み付き有向グラフ、有向グラフで、枝に実数値が割り当てられていて、特別な２点が存在する  
<a id="source-L51"></a>(A,b)は順序付きで、{a,b}は順序なしを表す  
<a id="source-L52"></a>今回は、自己閉路がなくて、平行辺がない単純な有向グラフを扱う  

<a id="source-L54"></a>フローの定義：容量保存かつ流量保存  

<a id="source-L56"></a>カットの定義：  

<a id="source-L58"></a>カット容量について調べることでフローについてわかることがある  



<a id="source-L61"></a>

### 第3講 ネットワークフローの基礎







<a id="source-L67"></a>

### 第4講 線形計画

<a id="source-L68"></a>線形計画問題  
<a id="source-L69"></a>・多変数の線形等式・線形不等式の制約のもと、その他変数の線形関数を最適化  
<a id="source-L70"></a>-様々な現実問題をモデル化できる  
<a id="source-L71"></a>-ネットワークフローの諸問題は特殊な場合（整数性）  
<a id="source-L72"></a>-かなり大規模問題も解ける(単体ほう、内点法)  

<a id="source-L74"></a>・単体法  
<a id="source-L75"></a>-基底解をpivotingで写って最適解を求める  
<a id="source-L76"></a>考え方  
<a id="source-L77"></a>最適解は凸多面体の端点に限って良い  
<a id="source-L78"></a>ある端点からスタートして、辺をたどって隣の端点でより良い端点に動く、これを繰り返しどの隣の端点より良い端点が最適解となる  
<a id="source-L79"></a>これを行列で表現する（標準形から基底形式へ）  
<a id="source-L80"></a>ー部分正方行列で正則な基底に着目  
<a id="source-L81"></a>-実行可能基底解：端点になっている  
<a id="source-L82"></a>-隣の端点に移動：pivoting(現基底から一変数入れ替え)  

<a id="source-L84"></a>単体法の基底形式での考え方  
<a id="source-L85"></a>・等式制約で注目している単位行列（基底）  





<a id="source-L90"></a>

### 第5講 線形計画の双対性






<a id="source-L95"></a>

### 第6講 計算量理論

<a id="source-L96"></a>アルゴリズムとは与えられたデータの中から欲しい情報を見つける手順  

<a id="source-L98"></a>計算不可能の時は停止性問題というプログラムが有限時間で終わるかを調べる問題になる  
<a id="source-L99"></a>計算可能の時は、  
<a id="source-L100"></a>NP困難：解の候補の大部分を調べることが必要、整数計画問題、Ising模型、コミュニティ発見  
<a id="source-L101"></a>NP完全：怪異の候補の大部分を調べることが必要かつ解の候補をある程度は調べなければいけない  
<a id="source-L102"></a>NP：解本候補をある程度は調べなければいけない、素因数分解、グラフ同型  
<a id="source-L103"></a>P：解の候補を部分だけ調べれば最適解が求まる、最短経路問題、線形計画問題、pagerank  

<a id="source-L105"></a>最近では計算機の高速化によって計算困難な問題でも取り扱い可能になり、一緒くたに計算困難とされていた問題の中にも困難さのグラデーションが存在することがわかった  
<a id="source-L106"></a>というのも、従来は一変数解析だったが、多変数解析になった  
<a id="source-L107"></a>指数時間は計算困難で、多項式時間は効率的である  




<a id="source-L111"></a>

### 第7講 最短路問題




<a id="source-L114"></a>

### 第8講 最小費用流

<a id="source-L115"></a>有向グラフの接続行列ではtotally moduler  
<a id="source-L116"></a>で整数性と関係している  



<a id="source-L119"></a>

### 第9講 Matroid

<a id="source-L120"></a>Sによる点誘導部分グラフ  
<a id="source-L121"></a>Induced subgraphがsubgraphの特殊な場合。  
<a id="source-L122"></a>点が中心のグラフ問題では誘導部分グラフを考えるのがセオリーである。  

<a id="source-L124"></a>補グラフ：全てを結ぶEdgeを加えたグラフ  

<a id="source-L126"></a>GのクリークはGの捕グラフの  

<a id="source-L128"></a>レジスターロケーションはグラフの彩色の問題となる  

<a id="source-L130"></a>３点について考えたときに完全グラフになっているのがクリーク  

<a id="source-L132"></a>双対性が壊れたとき、NP完全になる  

<a id="source-L134"></a>Duality-gapが0になるケースを考える  

<a id="source-L136"></a>Weak perfect graph theorem  

<a id="source-L138"></a>Strong perfect graph theorem  

<a id="source-L140"></a>PerfectGraphの有用な部分クラスとしてInterval Graphがある。  

<a id="source-L142"></a>実数のグラフ  





<a id="source-L147"></a>

### 第10講

<a id="source-L148"></a>無効グラフで閉路がないことがあ  



<a id="source-L152"></a>過去問用語  
<a id="source-L153"></a>単純、連結、外平面グラフ、２部グラフ、マッチング、最大流量最小カット定理、マトロイド、双対グラフ、双対マトロイド、基底形式、ピボッティング、双対性・相補性、退化、交差グラフ、区間グラフ、最大重み安定集合、単体法、クリーク、  

<a id="source-L155"></a>重み付きのMaxmam weightのstabke setを求めるのが出題  
<a id="source-L156"></a>単体法  
<a id="source-L157"></a>最小費用流の問題  
<a id="source-L158"></a>最短路問題  

<a id="source-L160"></a><http://www.hongo.wide.ad.jp/~jo2lxq/dm/>  

<a id="source-L162"></a>1問 平面グラフ、オイラーの公式、トポロジカルな公式、平面グラフのduality、Matroidのduality、平面グラフの場合の木分解、最大の重さを求める(?)  
<a id="source-L163"></a>2問 ネットワークフローについての線形計画問題、線形計画の単体法  
<a id="source-L164"></a>3問 最小費用流の問題  
<a id="source-L165"></a>4問 そこまでに見つかった最長路のを中間変数として定義して、前回やったアルゴリズムの重みがあるバージョンを出す  




> <a id="source-L170"></a>ランダムグラフ  

<a id="source-L171"></a><http://lealgorithm.blogspot.com/2017/06/blog-post_24.html>  




<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

モデル化するときは、有向か無向か、重みが何を表すか、多重辺や自己ループを許すかを明示する。「P＝候補の一部だけ調べればよい」という本文の説明は正式な定義ではない。計算量クラスは入力長と計算時間などで定める。次は小さなグラフで経路問題を作り、アルゴリズムの前提と結果を照合する。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [Graph Neural Network](graph-neural-networks.md)
- [ネットワーク分析](network-analysis.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
