---
title: "量子論"
status: draft
tags: [scrapbox, quantum]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E9%87%8F%E5%AD%90%E8%AB%96"
source_created: "2023-03-14T15:26:54Z"
source_updated: "2023-03-14T15:42:43Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 量子論

「何もわかっていない」という出発点と、量子計算の速さへの問い。

原ページ作成：2023-03-14 ／ 最終更新：2023-03-14（UTC、取得時点）

[物理学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/quantum-theory.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E9%87%8F%E5%AD%90%E8%AB%96)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

## 思考の手がかり

> 一丁前に羅列してますが、現状「自分は何もわかっていない」ということがわかっています

[本文の該当箇所へ](#source-L10)

> どうやって負の確率を用いて高速化しているのかはわからん

[本文の該当箇所へ](#source-L31)

> ちゃんと古典のベストと比較してるか？

[本文の該当箇所へ](#source-L34)

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 量子論


<a id="source-L3"></a>[量子力学](quantum-mechanics.md)  
<a id="source-L4"></a>[量子コンピュータ](quantum-computing.md)  
<a id="source-L5"></a>[量子アニーリング](quantum-annealing.md)  
<a id="source-L6"></a>[場の量子論](quantum-field-theory.md)  
<a id="source-L7"></a>[圏論的量子力学入門](../../math/algebra/categorical-quantum-mechanics.md)  
<a id="source-L8"></a>[scrapboxまとめ(物理)](../learning-paths/original-physics-index.md)  

<a id="source-L10"></a>一丁前に羅列してますが、現状「自分は何もわかっていない」ということがわかっています  


> <a id="source-L13"></a>量子計算と物理,  京都大学基礎物理学研究所 森前智行さん  

<a id="source-L14"></a>量子的重ね合わせ、複製不可能性、トンネル効果など謎の現象たくさん  

<a id="source-L16"></a>状態：ベクトル  
<a id="source-L17"></a>状態の時間発展：ユニタリ行列の作用  
<a id="source-L18"></a>物理量：エルミーと行列  

<a id="source-L20"></a>By definitionで量子論は日常言語で説明不可能、数式から"数学的意味"を感じ取ろう  

<a id="source-L22"></a>量子計算機は古典計算機で指数時間でシミュレート可能  

<a id="source-L24"></a>アルゴリズムの例  
<a id="source-L25"></a>- Shorの素因数分解アルゴリズム  
<a id="source-L26"></a>- Groverの検索アルゴリズム  

<a id="source-L28"></a>古典計算機：マルコフ連鎖  
<a id="source-L29"></a>量子計算機：負の確率を使ったマルコフ連鎖  

<a id="source-L31"></a>どうやって負の確率を用いて高速化しているのかはわからん  

<a id="source-L33"></a>古典でしらみつぶしにやるような場合、量子でも指数時間かかる  
<a id="source-L34"></a>ちゃんと古典のベストと比較してるか？  

<a id="source-L36"></a>重ね合わせで意味のある問題がいろいろ高速に解ける←証拠ない  

<a id="source-L38"></a>社会にすぐに役に立つ応用なんか全然先  


<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

[原文29行目](#source-L29)の「負の確率を使ったマルコフ連鎖」は注意が必要。通常の測定確率は非負で、干渉に使うのは複素数の確率振幅。二経路の振幅が $a,b$ なら確率は $|a+b|^2$ で、一般に $|a|^2+|b|^2$ とは異なる。負になる準確率の表現もあるが、この区別を飛ばさない。

「ちゃんと古典のベストと比較してるか？」は残す。計算量は問題・入力・誤差・利用できる操作を指定して比較し、重ね合わせだけで全問題が速くなるとはしない。確認資料：[Feynman III-1](https://www.feynmanlectures.caltech.edu/III_01.html)。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [量子力学](quantum-mechanics.md)
- [量子コンピュータ](quantum-computing.md)
- [量子アニーリング](quantum-annealing.md)
- [場の量子論](quantum-field-theory.md)
- [圏論的量子力学入門](../../math/algebra/categorical-quantum-mechanics.md)
- [scrapboxまとめ(物理)](../learning-paths/original-physics-index.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
