---
title: "物理ベースアニメーション(CG)"
status: draft
tags: [scrapbox, continuum-simulation]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E7%89%A9%E7%90%86%E3%83%99%E3%83%BC%E3%82%B9%E3%82%A2%E3%83%8B%E3%83%A1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%28CG%29"
source_created: "2023-01-16T07:18:27Z"
source_updated: "2023-04-10T03:00:48Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 物理ベースアニメーション(CG)

CGの動きを、運動方程式と時間積分の実装につなげる講義メモ。

原ページ作成：2023-01-16 ／ 最終更新：2023-04-10（UTC、取得時点）

[物理学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/physics-based-animation.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E7%89%A9%E7%90%86%E3%83%99%E3%83%BC%E3%82%B9%E3%82%A2%E3%83%8B%E3%83%A1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%28CG%29)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<details>
<summary>本文の見出しから探す</summary>

- [第1講](#source-L18)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 物理ベースアニメーション(CG)


> <a id="source-L3"></a>github  

<a id="source-L4"></a><https://github.com/PBA-2023S/pba>  


<a id="source-L7"></a>コンピュータ・グラフィックス（CG）は，映画やゲームやVRなど様々な場所で用いられている．本講義ではCGの中でもとりわけ，物理シミュレーションを用いた動きの生成について取り扱う.　具体的には剛体や弾性体や流体のアニメーションを題材にして、その背後にある，線形代数、ベクトル解析、偏微分方程式，汎関数原理、最適化法，数値計算法などの応用数学について学ぶことを狙いとする．本講義は単に仕組みを座学で学ぶだけでなく，C++を用いたプログラミング課題を通じて，研究用途の実践的なプログラミングする能力を養う．  

<a id="source-L9"></a>講義項目：  
<a id="source-L10"></a>バネ・質点モデル  
<a id="source-L11"></a>剛体のシミュレーション  
<a id="source-L12"></a>弾性体のシミュレーション  
<a id="source-L13"></a>布や髪のシミュレーション  
<a id="source-L14"></a>空間ハッシュを用いた衝突判定  
<a id="source-L15"></a>連立一時方程式の解法  



<a id="source-L18"></a>

### 第1講


<a id="source-L20"></a>Video Games  
<a id="source-L21"></a>CG Animation  
<a id="source-L22"></a>Science, Training and Education  
<a id="source-L23"></a>CAD  
<a id="source-L24"></a>V Tuber  
<a id="source-L25"></a>E-Commerce  

<a id="source-L27"></a>Physics-based Animation vs Scientific/Engineering Sim  

> <a id="source-L29"></a>CG Research  

<a id="source-L30"></a>Applied Mathematics &amp; Domain Knowledge  
<a id="source-L31"></a>Computational Fabrication  
<a id="source-L32"></a>Image Processing  
<a id="source-L33"></a>Rendering  
<a id="source-L34"></a>Geometry Processing  
<a id="source-L35"></a>Geometry Capture  
<a id="source-L36"></a>Physics-based Animation  
<a id="source-L37"></a>Character Animation  
<a id="source-L38"></a>Computational Fabrication  


> <a id="source-L41"></a>Spatial Discretization  

<a id="source-L43"></a>・Physics-based Simulation  
<a id="source-L44"></a>- Data Structure  
<a id="source-L45"></a>- Algorithm(Equation of Motion + Time Integration)  


<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

元の講義メモにある「運動方程式＋時間積分」を再開の軸にできる。見た目が自然に動くこと、離散化した式を正しく解けること、実測を再現できることは別の確認になる。質点とばねで解析解・数値解・エネルギーを比較し、剛体や弾性体へ広げたい。課題の完了は本文から確認できない。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [同じ分野のノート](README.md)：連続体・流体・数値シミュレーション。

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
