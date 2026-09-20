# Scrapboxの物理メモと補足資料

## 移植元

公開プロジェクト [MistMavGamer](https://scrapbox.io/MistMavGamer) の物理欄を起点に、2026-09-20に51ページの本文を取得しました。[物理の入口](../physics/README.md)から整形版、[原文一覧](../physics/sources/README.md)から取得時の本文へ戻れます。範囲・欠落・訂正は[移植記録](../physics/import-report.md)を参照してください。

元メモの参考文献、講義案内、SNS由来の文章は、取得時の出典と文脈を残すために保存しています。資料の収集は読了を意味せず、引用元が曖昧な文章の著者を推測で確定していません。

## 今回の補足で確認した資料

以下は今回AIが確認した資料で、本人が当時読んだ資料の一覧ではありません。閲覧日は2026-09-20です。参照した論点を記し、教材全体の読了とは区別しています。

- Feynman, Leighton, Sands, *The Feynman Lectures on Physics*, Caltech公開版。[I-23](https://www.feynmanlectures.caltech.edu/I_23.html)・[I-24](https://www.feynmanlectures.caltech.edu/I_24.html)：減衰振動と電気回路への対応。
- 同 [I-52 §52–3](https://www.feynmanlectures.caltech.edu/I_52.html)：対称性と保存則の対応。
- 同 [II-18 §18–1](https://www.feynmanlectures.caltech.edu/II_18.html)：Maxwell方程式、電荷保存、変位電流。
- 同 [II-31](https://www.feynmanlectures.caltech.edu/II_31.html)・[II-39](https://www.feynmanlectures.caltech.edu/II_39.html)：応力テンソル、弾性の記述。
- 同 [II-40](https://www.feynmanlectures.caltech.edu/II_40.html)・[II-41](https://www.feynmanlectures.caltech.edu/II_41.html)：流体の質量・運動量収支、非圧縮性、粘性。
- 同 [I-40](https://www.feynmanlectures.caltech.edu/I_40.html)・[I-43](https://www.feynmanlectures.caltech.edu/I_43.html)・[I-44](https://www.feynmanlectures.caltech.edu/I_44.html)：Boltzmann分布、熱伝導、可逆性とエントロピー。
- 同 [I-47](https://www.feynmanlectures.caltech.edu/I_47.html)：波動方程式。[III-1](https://www.feynmanlectures.caltech.edu/III_01.html)：確率振幅と干渉。
- 同 [I-17](https://www.feynmanlectures.caltech.edu/I_17.html)・[II-25](https://www.feynmanlectures.caltech.edu/II_25.html)：時空、四元ポテンシャル、電磁場テンソル。
- Max Planck Institute for Gravitational Physics, *Einstein Online*, [The elevator, the rocket, and gravity: the equivalence principle](https://www.einstein-online.info/en/spotlight/equivalence_principle/)：等価原理の局所性と潮汐効果。
- FEniCS Project, [Poisson equation](https://docs.fenicsproject.org/dolfinx/main/python/demos/demo_poisson.html)：境界条件を含む弱形式、一次三角形要素、線形系の解法。APIの実行確認ではなく説明と掲載コードを参照。
- Raissi, Perdikaris, Karniadakis, [Physics Informed Deep Learning](https://maziarraissi.github.io/PINNs/)：方程式残差と初期・境界条件を用いる損失の説明。
- Krishnapriyan et al. (2021), [Characterizing possible failure modes in physics-informed neural networks](https://arxiv.org/abs/2109.01050)：概要を確認。実験の再現はしていない。
- Sohl-Dickstein et al. (2015), [Deep Unsupervised Learning using Nonequilibrium Thermodynamics](https://proceedings.mlr.press/v37/sohl-dickstein15.html)：論文ページの概要を確認。非平衡熱力学と生成モデルの接点をたどる一次資料。

原文にある東京大学の量子計算ワークブックは入口を確認しましたが、各演習の実行やSDKの動作確認は行っていません。補足中の初等的な定義からの説明・計算はAIによる整理であり、特定の教材の文章を転記したものではありません。
