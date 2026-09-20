---
title: "Lie代数"
status: draft
tags: [scrapbox, algebra]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/Lie%E4%BB%A3%E6%95%B0"
source_created: "2024-11-02T09:28:43Z"
source_updated: "2025-06-02T11:01:43Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# Lie代数

連続的な対称性と工学への応用に関する、過去のAI回答も含む記録。

原ページ作成：2024-11-02 ／ 最終更新：2025-06-02（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/lie-algebras.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/Lie%E4%BB%A3%E6%95%B0)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### Lie代数

<a id="source-L2"></a>[表現論](representation-theory.md)  
<a id="source-L3"></a>[線形代数](../linear-algebra/linear-algebra.md)  
<a id="source-L4"></a>[線形数理要論](../linear-algebra/linear-mathematics.md)  
<a id="source-L5"></a>[代数の基礎](algebra-foundations.md)  
<a id="source-L6"></a>[二重四元数によるロボット制御](https://scrapbox.io/MistMavGamer/%E4%BA%8C%E9%87%8D%E5%9B%9B%E5%85%83%E6%95%B0%E3%81%AB%E3%82%88%E3%82%8B%E3%83%AD%E3%83%9C%E3%83%83%E3%83%88%E5%88%B6%E5%BE%A1)  


> <a id="source-L9"></a>Lie群とLie代数  

<a id="source-L10"></a><https://www2.yukawa.kyoto-u.ac.jp/~hideo.kodama/monographs/LieGroup_v20210406.pdf>  



> <a id="source-L14"></a>Claude先生  

<a id="source-L16"></a>lie代数について説明させていただきます。  
<a id="source-L17"></a>Lie(リー)代数は、19世紀末にノルウェーの数学者Sophus Lie(ソフス・リー)により導入された数学的構造で、連続変換群(Lie群)の局所的な性質を調べるための強力なツールです。  
<a id="source-L18"></a>主な特徴と利点を説明します：  

<a id="source-L20"></a>数学的構造  


<a id="source-L23"></a>Lie代数は、ベクトル空間に「リー括弧」という二項演算が定義された代数系です  
<a id="source-L24"></a>リー括弧は以下の性質を満たします：  

<a id="source-L26"></a>反対称性: \[X,Y\] = -\[Y,X\]  
<a id="source-L27"></a>ヤコビ恒等式: \[X,\[Y,Z\]\] + \[Y,\[Z,X\]\] + \[Z,\[X,Y\]\] = 0  




<a id="source-L32"></a>主な利点  

<a id="source-L34"></a>(a) 連続から離散への橋渡し  

<a id="source-L36"></a>Lie群(連続的な対称性を表す群)の局所的な性質をより扱いやすい線形の形で研究できます  
<a id="source-L37"></a>複雑なLie群の構造を、より単純なLie代数で理解できます  

<a id="source-L39"></a>(b) 物理学への応用  

<a id="source-L41"></a>量子力学での対称性の研究  
<a id="source-L42"></a>素粒子物理学での基本粒子の分類  
<a id="source-L43"></a>場の理論での保存則の導出  

<a id="source-L45"></a>(c) 工学への応用  

<a id="source-L47"></a>ロボット工学での姿勢制御  
<a id="source-L48"></a>コンピュータビジョンでの3次元運動の解析  
<a id="source-L49"></a>制御理論での非線形システムの解析  


<a id="source-L52"></a>具体例  

<a id="source-L54"></a>簡単な例として、3次元回転群SO(3)に対応するLie代数so(3)を考えてみましょう：  

<a id="source-L56"></a>SO(3)は3次元空間の回転を表す3×3の直交行列からなる群です  
<a id="source-L57"></a>そのLie代数so(3)は3×3の歪対称行列からなり、より扱いやすい構造となっています  


<a id="source-L60"></a>なぜ嬉しいのか  

<a id="source-L62"></a>(1) 計算の簡略化  

<a id="source-L64"></a>非線形なLie群の計算を、線形なLie代数での計算に帰着できます  
<a id="source-L65"></a>指数写像を通じて、Lie代数での計算結果をLie群に戻すことができます  

<a id="source-L67"></a>(2) 統一的な理論  

<a id="source-L69"></a>様々な種類の連続変換群を、統一的な観点から研究できます  
<a id="source-L70"></a>対称性の分類や解析が体系的に行えます  

<a id="source-L72"></a>(3) 応用範囲の広さ  

<a id="source-L74"></a>純粋数学から物理学、工学まで幅広い分野で活用されています  
<a id="source-L75"></a>特に現代の素粒子理論では必須のツールとなっています  




> <a id="source-L80"></a>CV・CG・ロボティクスのためのリー群・リー代数入門  

<a id="source-L81"></a><https://speakerdeck.com/spatial_ai_network/lie-group>  

<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

原文中の「Claude先生」以下は、当時のAI回答としての来歴を保つ。定義には括弧の**双線形性**も必要。実数・複素数上では反対称性とJacobi恒等式を併せて課す。行列Lie代数の例は $[X,Y]=XY-YX$。「連続から離散への橋渡し」という見出しは不正確で、ここでは連続的な群の局所構造を線形な空間で調べることが中心。Lie代数だけで群の大域的構造がすべて決まるとも限らない。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [表現論](representation-theory.md)
- [線形代数](../linear-algebra/linear-algebra.md)
- [線形数理要論](../linear-algebra/linear-mathematics.md)
- [代数の基礎](algebra-foundations.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
