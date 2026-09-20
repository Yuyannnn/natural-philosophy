# Natural Philosophy

yuyannnnがこれまで学んできたことと、これから学び直すことをまとめる、個人の学習ノートです。数学・物理学・化学を軸に、現実の現象やソフトウェア、AIとのつながりを考えていきます。

## まず読む

- [線形写像と行列 — 基底を変えると、何が変わるのか](math/linear-maps-and-matrices.md)：定義から導出、具体例、Pythonでの検算まで。
- [微分形式に驚いたきっかけ](math/geometry/differential-forms.md#source-L3)：Maxwell方程式への驚きから、別の数学へ関心が広がった記録。
- [保存則だけで計算できるか](physics/conservation-and-constitutive-laws.md)：ばね、流体、電気回路から、モデルと実装の関係を考える。
- [反応はどちらへ進むか、どれだけ速いか](chemistry/reaction-direction-and-rate.md)：平衡・速度・物質収支をつなぐ。
- [数学の入口](math/README.md)・[物理学の入口](physics/README.md)・[化学の入口](chemistry/README.md)：分野別の索引と、当時の疑問から読み返す経路。

Scrapboxから数学と関連分野の**64ページ**、物理と関連分野の**51ページ**、化学・材料・生命科学の**12ページ**を全文移植しました。当時の言葉・疑問・感想は残し、今回AIが加えた説明は別の節に記しています。出典と[数学の原文](math/sources/README.md)・[物理の原文](physics/sources/README.md)・[化学の原文](chemistry/sources/README.md)をたどりながら、一つの問いを掘り下げるノートを育てていきます。

## 分野

- [数学 — Math](math/README.md)：線形代数、解析、幾何、確率・統計、数値計算など。
- [物理学 — Physics](physics/README.md)：力学、流体、熱・統計、電磁気、量子、相対論、機械学習との接点。
- [化学 — Chemistry](chemistry/README.md)：化学の基礎、材料・分子とAI、生命科学との接点。
- [分野のつながり — Connections](connections/README.md)：数学と自然科学・工学・ソフトウェアの接点を、これからまとめる場所。
- [参考文献 — References](references/README.md)：学びの出発点と、確認した範囲。

## 学び直しのきっかけ

書き手は工学系出身です。学生時代を終えてからは、まとまった時間を取ることが難しくなり、新しいことをじっくり学ぶのは半ば諦めていました。興味はあっても、わからないところを一つずつ調べ、その前提までさかのぼるには時間がかかります。

AIに、その場で疑問を聞いたり、説明をかみ砕いてもらったりできるようになったことで、学び直しに少し希望の光が差してきました。限られた時間でも、疑問を持ったところから少しずつ理解を進められる。その感覚をきっかけに、以前の学びを整理しながら、止まっていた勉強をゆっくり再開していこうと思っています。

このノートでは、AIとの対話を学びの足がかりにしつつ、教科書や資料を読み、計算や実装でも確かめながら、自分の言葉で理解を残していきます。

## 抽象と応用を行き来する

学んだ概念が、別の場所でどのように使われているのかにも関心があります。たとえば、数学には次のようなつながりがあります。

- **線形代数**：ベクトルや行列は、3Dグラフィックスの座標変換や、ニューラルネットワークの計算に現れます。
- **微分・微分方程式**：変化を記述する考え方は、物体の運動や化学反応の速度を表すモデルにつながります。微分は、機械学習で使われる勾配法の基礎でもあります。
- **グラフ理論**：点と辺で関係を表す考え方は、交通網の経路探索や、ソフトウェアの依存関係の解析に使われます。

こうしたつながりを入口に、「なぜ使えるのか」「どんな仮定のもとで成り立つのか」まで考えてみたいと思っています。工学で親しんだ応用の視点も大切にしながら、純粋に面白いと感じた問いにも寄り道して、ゆるく分野を広げていくつもりです。

定義や計算結果に加えて、考えた道筋や、まだわかっていない点も残します。理解が変われば、ノートも書き直していきます。

## 計算を動かす

[基底変換の実行例](examples/change_of_basis.py)は、ノートと同じ行列を使い、座標を変えても同じ線形写像を表すことを確認します。[ばねの実行例](examples/oscillator_energy.py)では、解析解との比較とエネルギー収支を確認します。どちらもPython 3.10以上の標準ライブラリだけで動きます。

```sh
python3 examples/change_of_basis.py
python3 examples/oscillator_energy.py
python3 scripts/import_scrapbox_math.py --check
python3 scripts/import_scrapbox_physics.py --check
python3 scripts/import_scrapbox_chemistry.py --check
```

後半3つのコマンドは、公開ファイルだけで原文・移植本文のチェックサム、行の対応、ローカルリンク、画像を検証します。同じ確認を[GitHub Actions](https://github.com/Yuyannnn/natural-philosophy/actions/workflows/check.yml)でも実行します。数理的な正しさは、各ノートで出典・導出・計算を確かめていきます。

## 書く・育てる

本文は日本語、ファイルはMarkdownを基本に、通常のリンクでノートをつなぎます。定義・仮定・直感・未解決の問いを区別し、理解が変わった経緯も残します。

```text
math/           数学のノート、原文、画像、分野別索引
physics/        物理のノート、原文、画像、分野別索引
chemistry/      化学・材料・生命科学のノート、原文、分野別索引
connections/    分野をつなぐノートの入口
references/     参考文献と読んだ範囲
examples/       ノートに対応する小さな実行例
scripts/        原文の移植と整合性の検証
templates/      ノートと参考文献のひな形
docs/           書き方、取り込み方、構成の背景
```

- ノートを追加する：[ひな形](templates/note.md) → [執筆ガイド](docs/writing.md)。
- 以前の学びを移す：[取り込みガイド](docs/importing.md)と移植記録（[数学](math/import-report.md)・[物理](physics/import-report.md)・[化学](chemistry/import-report.md)）。
- 誤りや改善を伝える：[修正の提案について](CONTRIBUTING.md)。
- AIと一緒に編集する：[編集規約](AGENTS.md)。
- 公開ノートの構成を考える：[参考にしたリポジトリ](docs/repository-design.md)。

私的な原文や下書きはローカルの `inbox/` に置き、Git管理対象から除外します。
