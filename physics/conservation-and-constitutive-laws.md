---
title: "保存則だけで計算できるか — ばね、流体、電気回路をつなぐ"
status: draft
tags: [modeling, conservation-laws, continuum-mechanics, circuits]
created: 2026-09-20
updated: 2026-09-20
provenance: ai-authored-from-source-questions
---

# 保存則だけで計算できるか — ばね、流体、電気回路をつなぐ

[力学の元メモ](mechanics-waves/classical-mechanics.md#source-L471)には、保存則の式だけでは未知数が多く、応力や熱流の関係が必要だという記録がある。[電気の理論の地図](electromagnetism-matter/electrical-theory-map.md#source-L5)には「機械系と似ている？」という疑問が残っている。

この二つを出発点に、**収支の法則に、材料や素子の応答を表す関係を加えると、計算するモデルになる**ことを具体例で考える。以下の導出・例・実装は今回AIが補ったもので、当時の学習成果ではない。

## 質点とばねなら、何が足りないか

慣性系で、一定質量 $m$ の質点が水平な一直線上を動くとする。変位を $x$、外力を $f(t)$ とすると、運動量収支は

$$
m\ddot x=f(t)+F_{\mathrm{spring}}+F_{\mathrm{damper}}.
$$

これだけでは、右辺の二つの力がどう決まるかわからない。ここに、平衡位置からの変位に比例するばねと、速度に比例するダンパを仮定する。

$$
F_{\mathrm{spring}}=-kx,\qquad F_{\mathrm{damper}}=-c\dot x.
$$

$m>0,\ k>0,\ c\geq0$ を定数とすると、

$$
m\ddot x+c\dot x+kx=f(t)
$$

が得られる。$k$ はN/m、$c$ はN s/mで、各項は力（N）の次元になる。初期位置 $x(0)$ と初期速度 $\dot x(0)$ を指定すれば、この線形常微分方程式の初期値問題が定まる。

ばねが大きく変形したり、摩擦が速度に比例しなかったりすれば、構成関係を変える。運動量収支の考え方は残る。単振動・減衰振動の基礎は[Feynman I-23](https://www.feynmanlectures.caltech.edu/I_23.html)を参照。

## 散逸があると、保存則は破れるのか

上の式に $\dot x$ を掛けると、

$$
\frac{d}{dt}\left(\frac12m\dot x^2+\frac12kx^2\right)
=f(t)\dot x-c\dot x^2.
$$

左辺は質点とばねの力学的エネルギーの変化率、右辺は外力による入力とダンパへの散逸で、単位はW。無外力・無減衰なら力学的エネルギーは一定になる。無外力で減衰があれば、力学的エネルギーは減る。

これはエネルギー保存の破れではない。熱などを含めた系全体の収支と、今追跡している力学的エネルギーを区別する。どこまでをモデルの「系」に含めるかが大切になる。

## 電気回路にも同じ形が現れる

理想的な抵抗 $R$、インダクタンス $L$、容量 $C$ を直列につなぎ、印加電圧を $V(t)$、コンデンサーの電荷を $q$、電流を $i=\dot q$ とする。集中定数回路として扱える条件のもとで、電圧の収支は

$$
L\ddot q+R\dot q+\frac{q}{C}=V(t).
$$

機械系の $(m,c,k,x,f)$ に、回路の $(L,R,1/C,q,V)$ が対応する。等しい単位の量という意味ではなく、方程式の役割が対応している。蓄積するエネルギーも

$$
E_{\mathrm{circuit}}=\frac12Li^2+\frac{q^2}{2C},
\qquad
\frac{dE_{\mathrm{circuit}}}{dt}=Vi-Ri^2
$$

と書ける。$Li^2$ と $q^2/C$ はJ、$Vi$ と $Ri^2$ はWになる。この対応から、機械の振動で学んだ固有角周波数や減衰の考え方を回路へ持ち込める。[Feynman I-24 §24–3](https://www.feynmanlectures.caltech.edu/I_24.html)も機械系と電気回路の過渡応答を対応させている。

伝播遅延や電磁波の放射が無視できない場合などは、この単純な回路モデルの前提を見直す。

## 連続体でも、法則と材料の応答を分ける

流体では位置ごとに密度 $\rho$ と速度 $u$ を持つ。通常の非相対論的な連続体なら、

$$
\partial_t\rho+\nabla\cdot(\rho u)=0,
\qquad
\rho\frac{Du}{Dt}=\nabla\cdot\sigma+\rho b
$$

が質量と運動量の収支になる。$D/Dt=\partial_t+u\cdot\nabla$ は流体要素を追う物質微分、$\sigma$ は応力テンソル、$b$ は単位質量あたりの体積力。

まだ応力の決まり方が必要になる。一定密度・一定粘度の非圧縮Newton流体というモデルなら、

$$
\sigma=-pI+2\mu D,\qquad
D=\frac12\left(\nabla u+(\nabla u)^{\mathsf T}\right),
\qquad \nabla\cdot u=0
$$

を使い、非圧縮Navier–Stokes方程式へ進める。温度も未知なら、エネルギー収支、熱流の構成式、物性なども必要になる。[Feynman II-40](https://www.feynmanlectures.caltech.edu/II_40.html)と[II-41](https://www.feynmanlectures.caltech.edu/II_41.html)を参照。

元メモの「17未知数・5本の式」は、そのとき採用した変数の数え方に依存する。欠落した式を復元せず、ここでは別に仮定を宣言して説明した。構成式を加えた後も、境界条件、初期条件、解の存在、計算精度の問題は残る。

## ソフトウェアやAIへつなぐとき

実装では、状態変数、収支の式、構成関係、入力・初期条件を分けて持つと、どの仮定を変えたかを追いやすい。[有限要素法](continuum-simulation/finite-element-method.md)は空間の離散化、時間積分は時間方向の近似であり、材料モデルの妥当性とは別に確認する。

[PINNs](physics-ml/physics-informed-neural-networks.md#ai-notes)で方程式の残差を損失へ入れる場合も、その方程式がすでに何を仮定しているかを確認したい。「物理法則を入れた」だけでは、選んだ構成式や境界条件まで現実に合っているとは言えない。

[ばね・質点の実行例](../examples/oscillator_energy.py)では、無減衰の解析解と数値解を比較し、刻みを半分にすると誤差が減ること、減衰系で力学的エネルギーが減ることを確認する。

~~~sh
python3 examples/oscillator_energy.py
~~~

実行例では時間・変位を無次元化し、質量とばね定数を1に規格化している。無減衰・初期変位1・初期速度0の解析解は $x(t)=\cos t$。この検算は、指定したモデルと実装の確認である。実物との一致は、測定と別に照合する。

## 次に確かめたいこと

- 非Newton流体では、応力と変形速度の関係をどう変えるか。
- 保存則の残差が小さいことと、解の誤差が小さいことはどう関係するか。
- 熱設計やロボットのモデルで、何を省略すると予測が崩れるか。

[物理学の入口へ](README.md) · [元メモの移植記録](import-report.md)
