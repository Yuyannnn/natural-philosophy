---
title: "量子コンピュータ"
status: draft
tags: [scrapbox, quantum]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E9%87%8F%E5%AD%90%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF"
source_created: "2023-04-06T00:01:39Z"
source_updated: "2025-10-09T14:53:01Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 量子コンピュータ

状態の操作と測定、計算速度の比較条件を気に留めた講義メモ。

原ページ作成：2023-04-06 ／ 最終更新：2025-10-09（UTC、取得時点）

[物理学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/quantum-computing.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E9%87%8F%E5%AD%90%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

## 思考の手がかり

> 量子コンピュータが早いというのはマーケティング、いろんな但し書きがある

[本文の該当箇所へ](#source-L83)

<details>
<summary>本文の見出しから探す</summary>

- [第1回 概要・実習準備・Python入門](#source-L44)
- [第2回 量子コンピュータに触れる](#source-L48)
- [1. 量子力学的な物体を用意](#source-L55)
- [2. 物体を操作して状態を変化](#source-L56)
- [3. 物体の情報を測定](#source-L57)
- [4. 答えを読み取る or 観測量の期待値を得る](#source-L58)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 量子コンピュータ

<a id="source-L2"></a>[量子力学](quantum-mechanics.md)  
<a id="source-L3"></a>[量子論](quantum-theory.md)  
<a id="source-L4"></a>[量子アニーリング](quantum-annealing.md)  
<a id="source-L5"></a>[場の量子論](quantum-field-theory.md)  


> <a id="source-L8"></a>量子コンピューティングワークブック  

<a id="source-L9"></a><https://utokyo-icepp.github.io/qc-workbook/welcome.html>  

> <a id="source-L11"></a>IBM HP  

<a id="source-L12"></a><https://www.ibm.com/jp-ja?utm_content=SRCWW&p1=Search&p4=43700052529967079&p5=e&gclid=Cj0KCQjwuLShBhC_ARIsAFod4fIgj5mwmYW9xbZBoXuFPE95KTTKFRy4im6fH-AbjV7CokkkN3GT_sIaAmhFEALw_wcB&gclsrc=aw.ds>  


> <a id="source-L15"></a>IBM Quantum  


> <a id="source-L18"></a>Qiskit  


> <a id="source-L21"></a>Qiskit TextBook  

<a id="source-L22"></a><https://qiskit.org/learn/>  



<a id="source-L26"></a>• 実習の準備とPython入門  
<a id="source-L27"></a>・IBMQは本当に量子コンピュータか？を確認   
<a id="source-L28"></a>・量子プログラムで計算をする  
<a id="source-L29"></a>・量子ダイナミクスシミュレーション  
<a id="source-L30"></a>・ショアのアルゴリズム  
<a id="source-L31"></a>・グローバーのアルゴリズム  
<a id="source-L32"></a>・変分法と変分量子固有値ソルバー  
<a id="source-L33"></a>・量子・古典ハイブリッド機械学習  
<a id="source-L34"></a>・演習：ToffoliゲートとShorコード  
<a id="source-L35"></a>・演習：量子化学VQE  
<a id="source-L36"></a>・演習：シミュレーテッド分岐マシン  
<a id="source-L37"></a>・超伝導量子コンピュータの仕組み  
<a id="source-L38"></a>・超電導以外の方式  






<a id="source-L44"></a>

### 第1回 概要・実習準備・Python入門





<a id="source-L48"></a>

### 第2回 量子コンピュータに触れる


<a id="source-L50"></a>量子コンピュータ、コンピュータより演算ユニット  
<a id="source-L51"></a>中心は特別な量子系  
<a id="source-L52"></a>どんな量子系でも良い  

<a id="source-L54"></a>量子計算の流れ  

<a id="source-L55"></a>

### 1. 量子力学的な物体を用意


<a id="source-L56"></a>

### 2. 物体を操作して状態を変化


<a id="source-L57"></a>

### 3. 物体の情報を測定


<a id="source-L58"></a>

### 4. 答えを読み取る or 観測量の期待値を得る


<a id="source-L60"></a>物体を操作するのが量子アルゴリズム  

<a id="source-L62"></a>量子ビットは量子情報の入れ物の最小単位  

<a id="source-L64"></a>量子レジスタは量子ビットを複数並べたもの  

<a id="source-L66"></a>量子ゲートは量子レジスタに対する操作  
<a id="source-L67"></a>パターンの決まった操作を組み合わせて望みの状態を作る  
<a id="source-L68"></a>少数の基本ゲートですべての操作を表現可能  

<a id="source-L70"></a>量子回路  
<a id="source-L71"></a>量子レジスタにゲートをかけていったもの  

<a id="source-L73"></a>測定  
<a id="source-L74"></a>初期状態の量子レジスタにゲートをかけていく  
<a id="source-L75"></a>測定 = 終状態から情報を読み出す方法  

<a id="source-L77"></a>量子コンピュータの測定と、量子力学の測定は意味が違う  
<a id="source-L78"></a>量子コンピュータの測定は単に計算基底それぞれにかかっている係数の絶対値二乗を知ることに対応する  
<a id="source-L79"></a>直接教えてくれるわけではなくて、何回も測定して、ヒストグラムにして確率を得る  

<a id="source-L81"></a>変換というのはsplitしているというよりは二次元平面上で回しているイメージ  

<a id="source-L83"></a>量子コンピュータが早いというのはマーケティング、いろんな但し書きがある  
<a id="source-L84"></a>早いアルゴリズムを探している  
<a id="source-L85"></a>早いアルゴリズムが見つけられたら、指数関数的に速くなる  

<a id="source-L87"></a>Sが2を超えていたら量子コンピュータ  





> <a id="source-L93"></a>デジタルアニーラ  

<a id="source-L94"></a><https://www.fujitsu.com/jp/digitalannealer/>  


<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

[原文77行目](#source-L77)の測定は量子力学と違う原理ではなく、計算基底で測定する代表例として読む。同じ準備を繰り返して標本を集め、確率を推定する。「Sが2を超えれば量子コンピュータ」も、CHSH相関の検証と汎用的に計算できる装置の要件を区別する。元の[東京大学のワークブック](https://utokyo-icepp.github.io/qc-workbook/welcome.html)に戻り、実験設定を確認する。今回はSDKやサービスの実行環境更新までは行っていない。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [量子力学](quantum-mechanics.md)
- [量子論](quantum-theory.md)
- [量子アニーリング](quantum-annealing.md)
- [場の量子論](quantum-field-theory.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
