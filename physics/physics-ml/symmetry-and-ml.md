---
title: "対称性と機械学習"
status: draft
tags: [scrapbox, physics-ml]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E5%AF%BE%E7%A7%B0%E6%80%A7%E3%81%A8%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92"
source_created: "2025-10-04T08:26:25Z"
source_updated: "2025-10-04T10:22:29Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 対称性と機械学習

群・表現・同変な関数をニューラルネットワークへつなぐ読書項目。

原ページ作成：2025-10-04 ／ 最終更新：2025-10-04（UTC、取得時点）

[物理学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/symmetry-and-ml.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E5%AF%BE%E7%A7%B0%E6%80%A7%E3%81%A8%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<details>
<summary>本文の見出しから探す</summary>

- [1 対称性と機械学習への誘い](#source-L16)
- [2 群・表現論](#source-L17)
- [3 対称性を備えた関数](#source-L18)
- [4 対称性を備えたニューラルネットワーク](#source-L19)
- [5 リー郡に同変な関数の設計](#source-L20)
- [6 クリフォード代数にもとづく対称性](#source-L21)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 対称性と機械学習

<a id="source-L2"></a>[物理学と機械学習](physics-and-ml.md)  
<a id="source-L3"></a>[言語モデルの物理学](physics-of-language-models.md)  
<a id="source-L4"></a>[モデルの内部構造解析](https://scrapbox.io/MistMavGamer/%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E5%86%85%E9%83%A8%E6%A7%8B%E9%80%A0%E8%A7%A3%E6%9E%90)  
<a id="source-L5"></a>[深層学習の原理](https://scrapbox.io/MistMavGamer/%E6%B7%B1%E5%B1%A4%E5%AD%A6%E7%BF%92%E3%81%AE%E5%8E%9F%E7%90%86)  
<a id="source-L6"></a>[Lie代数](../../math/algebra/lie-algebras.md)  
<a id="source-L7"></a>[代数の基礎](../../math/algebra/algebra-foundations.md)  
<a id="source-L8"></a>[群論](../../math/algebra/group-theory.md)  
<a id="source-L9"></a>[多様体](../../math/geometry/manifolds.md)  
<a id="source-L10"></a>[帰納バイアス](https://scrapbox.io/MistMavGamer/%E5%B8%B0%E7%B4%8D%E3%83%90%E3%82%A4%E3%82%A2%E3%82%B9)  
<a id="source-L11"></a>[表現論](../../math/algebra/representation-theory.md)  



> <a id="source-L15"></a>対称性と機械学習  

<a id="source-L16"></a>

### 1 対称性と機械学習への誘い


<a id="source-L17"></a>

### 2 群・表現論


<a id="source-L18"></a>

### 3 対称性を備えた関数


<a id="source-L19"></a>

### 4 対称性を備えたニューラルネットワーク


<a id="source-L20"></a>

### 5 リー郡に同変な関数の設計


<a id="source-L21"></a>

### 6 クリフォード代数にもとづく対称性




<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

不変性と同変性を分ける。入力・出力の変換を $\rho_{\mathrm{in}}(g),\rho_{\mathrm{out}}(g)$ とすると、同変性は $f(\rho_{\mathrm{in}}(g)x)=\rho_{\mathrm{out}}(g)f(x)$。出力側が恒等のとき不変性になる。回転すると力ベクトルも回転するモデルと、同じエネルギーを出すモデルでは要件が異なる。元の目次を[群論](../../math/algebra/group-theory.md)・[表現論](../../math/algebra/representation-theory.md)へつなげられる。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [物理学と機械学習](physics-and-ml.md)
- [言語モデルの物理学](physics-of-language-models.md)
- [Lie代数](../../math/algebra/lie-algebras.md)
- [代数の基礎](../../math/algebra/algebra-foundations.md)
- [群論](../../math/algebra/group-theory.md)
- [多様体](../../math/geometry/manifolds.md)
- [表現論](../../math/algebra/representation-theory.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
