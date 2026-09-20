---
title: "線形写像と行列 — 基底を変えると、何が変わるのか"
status: draft
tags: [linear-algebra, coordinates, machine-learning]
created: 2026-09-20
updated: 2026-09-20
---

# 線形写像と行列 — 基底を変えると、何が変わるのか

行列の成分だけを眺めると、異なる行列は異なる操作に見える。しかし、同じ線形写像でも、座標を決める基底によって表現する行列は変わる。

[移植した「線形代数」の全文](linear-algebra/linear-algebra.md)にあった、計算と概念を分け、「行列を写像として眺める」という視点を出発点に整理する。以下の導出、数値例、応用への説明は今回補ったもの。

## 線形写像を座標で表す

ここでは実数上の有限次元ベクトル空間を扱う。写像 $T:V\to W$ が線形であるとは、任意の $u,v\in V$ と実数 $a,b$ に対し、

$$
T(au+bv)=aT(u)+bT(v)
$$

が成り立つことをいう。

$V$ の基底を $\mathcal B=(b_1,\ldots,b_n)$、$W$ の基底を $\mathcal C=(c_1,\ldots,c_m)$ とする。基底は、各ベクトルを一意な係数の組で表すためのもの。その係数を並べた列ベクトルを $[v]_{\mathcal B}$ と書く。

$T$ の表現行列 $A$ は、各 $T(b_j)$ の $\mathcal C$ に関する座標を第 $j$ 列に並べたもので、

$$
[T(v)]_{\mathcal C}=A[v]_{\mathcal B}
$$

を満たす。ベクトル $v$ と座標の列 $[v]_{\mathcal B}$、写像 $T$ とその表現行列 $A$ を区別するのがポイントになる。座標と表現行列については、[TU Delftの教材 §4.3.2–4.3.3](https://interactivetextbooks.tudelft.nl/linear-algebra/Chapter4/ChangeOfBasis.html)を参照。

## 基底を変えると行列はどう変わるか

ここからは $T:\mathbb R^n\to\mathbb R^n$ とし、$A$ を標準基底での表現行列とする。別の基底のベクトルを標準座標で列に並べた行列を $P$ とする。基底なので $P$ は可逆である。

新しい基底での入力座標を $z$ とすれば、標準座標は $x=Pz$。$T$ を作用させた結果は $Ax=APz$ なので、これを新しい座標へ戻すと $P^{-1}APz$ になる。したがって、新しい表現行列は

$$
A'=P^{-1}AP
$$

となる。同じ空間の入力側・出力側で同じ基底変更をしている、という条件がある。一般の $V\to W$ で両側の基底を別々に変える場合とは区別する。[TU Delftの教材 §4.3.4–4.3.5](https://interactivetextbooks.tudelft.nl/linear-algebra/Chapter4/ChangeOfBasis.html)

## 小さな計算例

標準座標で

$$
A=\begin{pmatrix}2&1\\1&2\end{pmatrix},\qquad
b_1=\begin{pmatrix}1\\1\end{pmatrix},\quad
b_2=\begin{pmatrix}1\\-1\end{pmatrix}
$$

とする。計算すると $Ab_1=3b_1$、$Ab_2=b_2$ なので、基底 $(b_1,b_2)$ では

$$
P=\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad
P^{-1}AP=\begin{pmatrix}3&0\\0&1\end{pmatrix}
$$

になる。この基底で見ると、変換は一方の成分を3倍し、もう一方を保つ操作だと読める。

たとえば $x=(2,0)^{\mathsf T}$ の新しい座標は $z=(1,1)^{\mathsf T}$。変換後は $z'=(3,1)^{\mathsf T}$ となり、標準座標に戻すと $Pz'=(4,2)^{\mathsf T}=Ax$ になる。

この計算は[Pythonの実行例](../examples/change_of_basis.py)でも確かめられる。標準ライブラリの `Fraction` で有理数を正確に扱い、$AP=PA'$ と、二つの座標系を通る計算結果の一致を検証する。

```sh
python3 examples/change_of_basis.py
```

## 現実の計算とのつながり

**座標を扱うソフトウェア**では、同じベクトルでも、どの基底で成分を表すかによって値が違う。行列の形だけでなく、入力と出力がどの座標系に属するかをそろえる必要がある。位置を扱い、座標系の原点も異なる場合には、さらに平行移動が必要になる。

**機械学習**では、入力の重み付き和にバイアスを加える $y=Wx+b$ という形が現れる。$b\ne0$ なら $x=0$ をゼロへ写さないため、これは厳密には線形写像ではなくアフィン写像である。[Dive into Deep Learning §3.1.1.1](https://d2l.ai/chapter_linear-regression/linear-regression.html)でも、この区別が説明されている。

今回の整理から考えたいのは、数値配列としての行列を実装するときにも、「何を、どの座標で表しているか」を追えるようにすること。

## 元メモから明確にした点

元メモには、基底によらず固有ベクトルや固有空間が同じ、という趣旨の記述がある。これは、抽象的な写像の固有ベクトル・固有空間と、それらの座標表示を区別して読む必要がある。

$Av=\lambda v$ なら、$A'=P^{-1}AP$ に対し $A'(P^{-1}v)=\lambda(P^{-1}v)$。固有値は同じでも、対応する固有ベクトルの座標は $P^{-1}v$ へ変わる。上の例では、標準座標の $(1,1)^{\mathsf T}$ が新しい座標の $(1,0)^{\mathsf T}$ に対応する。

また、一つの固有値に対応する方向が一つとは限らない。単位行列なら、すべての非零ベクトルが固有値1の固有ベクトルになる。

## 次の問い

- この例のように対角化できるのは、どんな条件のときか。
- 基底の選び方は、計算機上の丸め誤差にどう影響するか。

このノートは有限次元での座標表示に範囲を絞った整理中の文章であり、元ページ全体の検証や移植ではない。

## 出典・関連ノート

- [Scrapboxの数学メモ](../references/yuyannnn-scrapbox-math.md)：原文の所在と、取得・確認した範囲。
- TU Delft, *Linear algebra*, [§4.3 Change of basis](https://interactivetextbooks.tudelft.nl/linear-algebra/Chapter4/ChangeOfBasis.html)：座標、表現行列、基底変更。2026-09-20閲覧。
- *Dive into Deep Learning*, [§3.1.1.1 Linear Model](https://d2l.ai/chapter_linear-regression/linear-regression.html)：線形回帰の式とアフィン写像の区別。2026-09-20閲覧。
- [数学の入口](README.md)：数値解析や幾何など、次にたどるメモ。
