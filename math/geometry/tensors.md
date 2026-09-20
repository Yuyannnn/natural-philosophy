---
title: "テンソルと奮闘"
status: draft
tags: [scrapbox, geometry]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E3%83%86%E3%83%B3%E3%82%BD%E3%83%AB%E3%81%A8%E5%A5%AE%E9%97%98"
source_created: "2023-01-18T11:28:14Z"
source_updated: "2025-09-14T05:32:37Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# テンソルと奮闘

直感的な説明だけでは納得しきれない、という疑問を含む記録。

原ページ作成：2023-01-18 ／ 最終更新：2025-09-14（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/tensors.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E3%83%86%E3%83%B3%E3%82%BD%E3%83%AB%E3%81%A8%E5%A5%AE%E9%97%98)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

## 思考の手がかり

> でもこの動画は数学的にごまかしすぎてまだよくわからないなあ

[本文の該当箇所へ](#source-L28)

<details>
<summary>本文の見出しから探す</summary>

- [物理の鍵しっぽ](#source-L21)
- [「テンソル積-Wikipedia-」](#source-L41)
- [1 定義](#source-L50)
- [1.1 基底を用いた定義](#source-L51)
- [1.2 商としての定義](#source-L53)
- [1.3 記法について](#source-L55)
- [「20分でわかるテンソルの本質」](#source-L68)
- [1 断面の取り方によって応力は変化する](#source-L70)
- [2 応力テンソルの紹介](#source-L76)
- [3 応力テンソルっぽい公式t = T・nの求め方](#source-L86)
- [「Youtube先生シリーズ」](#source-L99)
- [第1講 自然基底](#source-L101)
- [第2講 双対基底](#source-L115)
- [第3講 ベクトルの座標変換則](#source-L125)
- [第4講 テンソル完全掌握](#source-L129)
- [第5講 テンソルの座標変換則](#source-L163)
- [「ざっくりテンソル積を理解しよう」](#source-L180)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### テンソルと奮闘

<a id="source-L2"></a>[微分形式](differential-forms.md)  
<a id="source-L3"></a>[微分積分学](../analysis/calculus.md)  
<a id="source-L4"></a>[材料力学](https://scrapbox.io/MistMavGamer/%E6%9D%90%E6%96%99%E5%8A%9B%E5%AD%A6)  
<a id="source-L5"></a>[多様体](manifolds.md)  
<a id="source-L6"></a>[微分幾何学とトポロジー](differential-geometry-and-topology.md)  
<a id="source-L7"></a>[代数の基礎](../algebra/algebra-foundations.md)  
<a id="source-L8"></a>[線形代数](../linear-algebra/linear-algebra.md)  
<a id="source-L9"></a>[Lie代数](../algebra/lie-algebras.md)  


> <a id="source-L12"></a>テンソル  

<a id="source-L13"></a>物理現象は座標系によらないので基底ベクトルを省略した表記は厳密性を欠く  

<a id="source-L15"></a>連続体の力学ではベクトル値ベクトル関数が重要な役割を果たす。これは物理的には矢印ベクトルの一次変換であり、数学的にはテンソルで表現される。  
<a id="source-L16"></a>マトリックスに基底が導入されたようなもの  
<a id="source-L17"></a>テンソルの基底を生成するために２つのベクトルからテンソルを生成するテンソル積という演算を導入する  
<a id="source-L18"></a>なお力学におけるベクトルとテンソルの定義は線形代数やベクトル解析における定義と若干異なっている  



<a id="source-L21"></a>

### 物理の鍵しっぽ

<a id="source-L22"></a><http://hooktail.sub.jp/vectoranalysis/TensorConcept/>  


<a id="source-L25"></a><https://www.youtube.com/watch?v=_w2Vq0qEdkY>  
<a id="source-L26"></a>テンソルの気持ちが分かったかも知れん！！  
<a id="source-L27"></a>基底が導入ってそういうことだったんかな  
<a id="source-L28"></a>でもこの動画は数学的にごまかしすぎてまだよくわからないなあ  


<a id="source-L31"></a><https://www.youtube.com/watch?v=nNdq76Lrgac>  
<a id="source-L32"></a>テンソルについてとても良い  

<a id="source-L34"></a><https://qiita.com/n_kats_/items/c6a2312c80f6f4277809>  
<a id="source-L35"></a>qiita  



<a id="source-L39"></a>————————————————————————————————————————————————————————  


<a id="source-L41"></a>

### 「テンソル積-Wikipedia-」


<a id="source-L43"></a>数学におけるテンソル積は線形代数学で多重線形性を扱うための線型化を担う概念で、きちのベクトル空間・加群など様々な対象から新たな対象を作り出す操作の1つである  
<a id="source-L44"></a>そのようないずれの対象に関しても、テンソル積は最も自由な双線型乗法である  

<a id="source-L46"></a>共通の体K上の２つのベクトル空間V, Wのテンソル積は再びベクトル空間をなす  
<a id="source-L47"></a>ベクトル空間のテンソル積を繰り返して得られるテンソル空間は物理的なテンソルを数学的に定式化する  
<a id="source-L48"></a>テンソル空間に様々の積を入れて様々な多重線形代数・クリフォード代数が定式化されるが、その基本となる演算がテンソル積である  


<a id="source-L50"></a>

### 1 定義


<a id="source-L51"></a>

### 1.1 基底を用いた定義



<a id="source-L53"></a>

### 1.2 商としての定義



<a id="source-L55"></a>

### 1.3 記法について


<a id="source-L57"></a>普遍性  

<a id="source-L59"></a>線型写像のテンソル積  

<a id="source-L61"></a>双対空間との関係  


<a id="source-L64"></a>——————————————————————————————————————————————————————  

> <a id="source-L66"></a><https://www.youtube.com/watch?v=nNdq76Lrgac>  


<a id="source-L68"></a>

### 「20分でわかるテンソルの本質」



<a id="source-L70"></a>

### 1 断面の取り方によって応力は変化する


<a id="source-L72"></a>ポイント  
<a id="source-L73"></a>あとでどんな断面を指定されてもその面における応力がわかるようにしておく  
<a id="source-L74"></a>そうすることで、ある位置における応力を理解したことになる  


<a id="source-L76"></a>

### 2 応力テンソルの紹介


<a id="source-L78"></a>１個目の添字で断面を、二個目の添字で向きを指定している  

<a id="source-L80"></a>座標が大きい側の面をしてしてくれている  
<a id="source-L81"></a>他の面は釣り合いから求まる  
<a id="source-L82"></a>他の面が来てもこの組み合わせで求められる  
<a id="source-L83"></a>これを二次元の応力変換公式になっている  



<a id="source-L86"></a>

### 3 応力テンソルっぽい公式t = T・nの求め方


<a id="source-L88"></a>tが応力である  


<a id="source-L91"></a>4 2次元の応力変換公式  

<a id="source-L93"></a>ポイント 単位法線ベクトルと内積をとって垂直応力を抜き出す  



<a id="source-L97"></a>————————————————————————————————————————  


<a id="source-L99"></a>

### 「Youtube先生シリーズ」



<a id="source-L101"></a>

### 第1講 自然基底


<a id="source-L103"></a>まず、座標系を設定する  
<a id="source-L104"></a>これが局所座標系と言われ、それに分類されるやつが自然基底や双対基底がある  

<a id="source-L106"></a>曲がった規定ではユークリッド空間のように全てのベクトルが表せるとは限らない  

<a id="source-L108"></a>自然基底とは、位置ベクトルをそれぞれのパラメーターで偏微分したもの  
<a id="source-L109"></a>自然基底はパラメーター曲線の一部というか、接ベクトルになっている  

<a id="source-L111"></a>θによるパラメータ曲線を見るなら、θ以外は固定しておく  




<a id="source-L115"></a>

### 第2講 双対基底


<a id="source-L117"></a>自然基底同士の内積は正規直交規定ではない  

<a id="source-L119"></a>斜交座標では内積で成分が取り出せない  

<a id="source-L121"></a>ペアになる基底との内積が正規直交基底のような性質を満たすようにやっていくぞい  




<a id="source-L125"></a>

### 第3講 ベクトルの座標変換則





<a id="source-L129"></a>

### 第4講 テンソル完全掌握


<a id="source-L131"></a>「テンソルの定義とその変換則に隠された秘密」  

<a id="source-L133"></a><https://www.youtube.com/watch?v=nDKBJl3uxEw>  

<a id="source-L135"></a>Point  
<a id="source-L136"></a>・テンソルはベクトルの一次変換を表すものである  
<a id="source-L137"></a>・ベクトルは座標変換に対し、不変である  

<a id="source-L139"></a>この２つがわかれば、テンソルが座標変換に対して不変であり、テンソルの座標変換公式がわかる  

<a id="source-L141"></a>・応力テンソル(nからfへの一次変換)  

<a id="source-L143"></a>・慣性テンソル(ωからLへの一次変換)  

<a id="source-L145"></a>・電磁テンソル（vからfへの一次変換）  

<a id="source-L147"></a>この３つでテンソルに対する理解を深める  
<a id="source-L148"></a>断面を指定して、その断面に対して力を求める  
<a id="source-L149"></a>基底を選んで、ベクトルとベクトルの間を結んでいる行列にあたる部分  

<a id="source-L151"></a>しかし、多次元の配列として表現されていたら全てテンソルというわけではなく、テンソル自身は特定の座標系によらないで定まる対象である  
<a id="source-L152"></a>これがテンソルっぽい  
<a id="source-L153"></a>この要請をもとに得られるのが、それぞれの座標変換公式である  

<a id="source-L155"></a>まず、ベクトルは座標変換によって不変である  
<a id="source-L156"></a>テンソルは単体として存在するのではなく、ベクトルとセットで方程式の形で与えらえれる  
<a id="source-L157"></a>ベクトルが不変なら、その間をとりもっているテンソルの不変じゃないとおかしい！  
<a id="source-L158"></a>なので、fが不変に保たれるような成分の変換をする  
<a id="source-L159"></a>大学一年のときにやった表現行列や！！！  




<a id="source-L163"></a>

### 第5講 テンソルの座標変換則


<a id="source-L165"></a>テンソルは一次変換を表すものだった  

<a id="source-L167"></a>基底をとったときの成分同士を繋いでくれるものが表現行列だった  

<a id="source-L169"></a>テンソルはベクトル同士の関係なので、基底をとって行列に落とし込まないと表現できひん  

<a id="source-L171"></a>座標変換行列は新しい基底を古い基底で成分表示することで得られる  

<a id="source-L173"></a>ここまでは線形代数でやった  


<a id="source-L176"></a>一般相対論やリーマン幾何学だと、自然規定をとるのでそれの座標変換則がPという行列にきいてくる  

<a id="source-L178"></a>————————————————————————————————  


<a id="source-L180"></a>

### 「ざっくりテンソル積を理解しよう」


<a id="source-L182"></a><https://www.youtube.com/watch?v=gEvMfXe3osU>  



<a id="source-L186"></a>—————————————————————————————————  
<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

本文の「数学的にごまかしすぎてまだよくわからない」という疑問は重要な再開点。多次元配列としてのテンソル、ベクトル空間のテンソル積、座標変換に対する変換則を持つ幾何的対象を区別して整理する。まずベクトルと双対ベクトルを分け、基底を変えたときの成分を計算する例を作ると、直感を定義に結びつけられる。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [微分形式](differential-forms.md)
- [微分積分学](../analysis/calculus.md)
- [多様体](manifolds.md)
- [微分幾何学とトポロジー](differential-geometry-and-topology.md)
- [代数の基礎](../algebra/algebra-foundations.md)
- [線形代数](../linear-algebra/linear-algebra.md)
- [Lie代数](../algebra/lie-algebras.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
