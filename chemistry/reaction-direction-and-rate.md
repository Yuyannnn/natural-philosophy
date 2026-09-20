---
title: "反応はどちらへ進むか、どれだけ速いか — 平衡と速度を分ける"
status: draft
tags: [chemistry, thermodynamics, kinetics, differential-equations]
created: 2026-09-20
updated: 2026-09-20
provenance: ai-authored-companion-to-imported-notes
---

# 反応はどちらへ進むか、どれだけ速いか — 平衡と速度を分ける

反応の向き・到達する組成と、そこへ近づく速さは別の問いです。前者には熱力学、後者には反応速度論が必要になります。

このノートは、[高校化学の速度・平衡](foundations/high-school-chemistry.md#source-L201)と、[分子工学の化学ポテンシャルへの疑問](../physics/electromagnetism-matter/molecular-engineering.md#source-L122)を起点に、今回AIが書いた補足です。本人が当時ここまで導出していたという記録ではありません。

## まず原子数と電荷を合わせる

例えば水素と酸素から水ができる総括反応式は、

$$
2\mathrm{H_2(g)}+\mathrm{O_2(g)}\longrightarrow2\mathrm{H_2O(l)}
$$

です。両辺の水素原子は4個、酸素原子は2個、総電荷は0。係数は物質量の変化の比を決めますが、この反応が一度に3分子の衝突で起こるという意味ではありません。総括反応式から速度式を決めることもできません。[OpenStax Chemistry 2e §12.3](https://openstax.org/books/chemistry-2e/pages/12-3-rate-laws)

## 化学ポテンシャルを反応の向きへつなぐ

一定温度 $T$・圧力 $p$ の閉じた系を考え、仕事は体積変化に伴うものだけとします。各成分の物質量を $n_i$、Gibbsエネルギーを $G$ とすると、

$$
\mu_i=\left(\frac{\partial G}{\partial n_i}\right)_{T,p,n_{j\ne i}}
$$

が化学ポテンシャルで、単位は $\mathrm{J\,mol^{-1}}$。元のメモにある「押し込めようとする力」は直感的な表現であり、単位がNの力とは異なります。

生成物の係数を正、反応物を負に取った $\nu_i$ と、反応進行度 $\xi$（mol）を使うと $dn_i=\nu_i\,d\xi$。したがって、

$$
dG=\sum_i\mu_i\,dn_i
=\left(\sum_i\nu_i\mu_i\right)d\xi
=\Delta_rG\,d\xi.
$$

この条件のもとで、$\Delta_rG<0$ なら正方向への微小な進行で $G$ が減り、平衡では $\Delta_rG=0$ になります。組成による変化を含めると、

$$
\Delta_rG=\Delta_rG^\circ+RT\ln Q,\qquad
\Delta_rG^\circ=-RT\ln K
$$

です。$Q$ はその時点の反応商、$K$ は平衡時の値で、いずれも標準状態に対する無次元の活量から作ります。標準状態は特定の温度を自動的に意味しません。[§16.4 Free Energy](https://openstax.org/books/chemistry-2e/pages/16-4-free-energy)

この式から「進む向き」はわかっても「何秒かかるか」はわかりません。元メモの発熱・エントロピーに関する直感を、組成と条件を含む判定へ進めた形です。

## 同じ平衡でも、近づく時間は違う

ここからは説明用に、同一分子式・同一電荷を持つ2種類の異性体 $A,B$ の単純なモデルを考えます。実在物質の測定値ではありません。閉じた容器、一定温度・体積、理想希薄溶液、正逆とも一次反応、他の反応なしと仮定します。

$$
A \mathrel{\mathop{\rightleftharpoons}^{k_f}_{k_r}} B,\qquad
\frac{dc_B}{dt}=k_fc_A-k_rc_B,\qquad
c_A+c_B=c_{\mathrm{tot}}.
$$

濃度の単位は $\mathrm{mol\,L^{-1}}$、両速度定数は $\mathrm{s^{-1}}$。物質収支を代入すると、

$$
\frac{dc_B}{dt}=k_fc_{\mathrm{tot}}-(k_f+k_r)c_B.
$$

右辺を0と置いた平衡濃度と、この微分方程式の解は、

$$
c_{B,\mathrm{eq}}=\frac{k_f}{k_f+k_r}c_{\mathrm{tot}},\qquad
c_B(t)=c_{B,\mathrm{eq}}+
\left(c_B(0)-c_{B,\mathrm{eq}}\right)e^{-(k_f+k_r)t}.
$$

同じ濃度標準を用いるこのモデルでは、平衡比は $K=c_{B,\mathrm{eq}}/c_{A,\mathrm{eq}}=k_f/k_r$、緩和時間は $\tau=1/(k_f+k_r)$ です。一般の多段階反応へ、そのまま拡張する式ではありません。

例えば $c_{\mathrm{tot}}=1.0\ \mathrm{mmol\,L^{-1}}$、$k_f=0.20\ \mathrm{s^{-1}}$、$k_r=0.10\ \mathrm{s^{-1}}$ と置くと、$K=2$、$c_{B,\mathrm{eq}}=2/3\ \mathrm{mmol\,L^{-1}}$、$\tau\approx3.33\ \mathrm{s}$。両方の速度定数を10倍にすると、平衡比は同じまま緩和時間が約0.333秒になります。

解を微分すれば元の方程式を満たし、$t=0$ で初期値、$t\to\infty$ で平衡値に戻ることも確認できます。可逆な速度過程と平衡の関係は[§13.1 Chemical Equilibria](https://openstax.org/books/chemistry-2e/pages/13-1-chemical-equilibria)を参照してください。

## ソフトウェアやAIで何を予測するのか

今回のモデルでは、同じ $K$ に対して速度定数の組は無数にあります。平衡組成のデータだけでは、時間変化を一意に推定できないということです。

反応のデータを扱うときは、最終組成を予測するのか、観測時刻での濃度を予測するのかを先に決めます。装置が大きくなると、混合や伝熱も観測結果に関わります。[Process Informatics](materials-informatics/process-informatics.md)のスケールアップへの関心は、ここにつながります。

生体でも、濃度が一定であることと平衡は同じではありません。流入・流出が反応による増減を打ち消す定常状態なら、上の閉じた系の収支式に流れの項を足す必要があります。[生命科学の元メモ](life-sciences/life-sciences.md)と[開放系](../physics/thermal-statistical/open-systems.md)へ戻る入口です。

[化学の入口へ](README.md) · [高校化学の補足・訂正](foundations/high-school-chemistry.md#ai-notes)
