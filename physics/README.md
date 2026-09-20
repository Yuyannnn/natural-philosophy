# 物理学 / Physics

Scrapboxに残してきた物理と工学のメモを、当時の言葉と疑問を残しながら整理しています。現象を式にするだけでなく、その式が何を仮定し、どこまで使えるのかを考える場所です。

**51ページ・6,063行**を全文移植しました。各ページは「当時の本文」と「今回のAIによる補足・訂正」を分けています。講義の目次、資料の収集、短い未完のメモも、その時点の記録として残しました。

## まず読む

[保存則だけで計算できるか — ばね、流体、電気回路をつなぐ](conservation-and-constitutive-laws.md)

「保存則だけでは未知数が多い」「電気系は機械系と似ている？」という元メモの問いから、構成式・単位・初期条件をそろえ、ソフトウェアやAIのモデルへつなぐ説明ノートです。今回のAI補足として、[小さなPythonの検算](../examples/oscillator_energy.py)も添えました。

## 当時の疑問から読み直す

- [保存則だけで十分なのか](mechanics-waves/classical-mechanics.md#source-L471)：応力と熱流の形を決める必要性、非Newton流体への関心。
- [電気系は機械系と似ている？](electromagnetism-matter/electrical-theory-map.md#source-L5)：自分の専門から別の分野を見渡した問い。
- [統計力学で苦戦した記憶](thermal-statistical/statistical-mechanics.md#source-L11)：学部1年の授業から、もう一度ミクロとマクロの関係へ。
- [なぜ仕事を内圧で定義しないのか](thermal-statistical/thermodynamics.md#source-L75)：式の使い方より先に、外界とのやり取りと仮定を考える。
- [化学ポテンシャルがわからなかった](electromagnetism-matter/molecular-engineering.md#source-L122)：曖昧な直感を残し、定義と単位から読み直す。
- [量子計算は何と比べて速いのか](quantum/quantum-theory.md#source-L34)：理解の途上の疑問と、比較条件への関心。
- [手を動かしていてメモがなかった](thermal-statistical/stirling-engine-project.md#source-L3)：エンジン製作の題名、周辺の実習記録、手描き図を一緒に残す。
- [理解は遠くても、面白い](relativity-cosmology/string-theory.md#source-L10)：超弦理論への素朴な関心。

これは本文を根拠にした読み返し方の提案です。ページの更新日を学習日とみなしたり、引用文をすべて本人の発言とみなしたりしていません。

## 分野から読む

- [学びの経緯・入口](learning-paths/README.md)：元の物理索引、現代物理への問い、勉強法と資料集。
- [力学・振動・数理的な道具](mechanics-waves/README.md)：運動方程式、解析力学、振動・波動、グリーン関数と摂動。
- [連続体・流体・数値シミュレーション](continuum-simulation/README.md)：流体と材料、応力、有限要素法、CGでの実装。
- [熱・統計・非平衡](thermal-statistical/README.md)：状態量、熱機関、伝熱、統計力学、情報とゆらぎ。
- [電磁気・光・物質](electromagnetism-matter/README.md)：場と回路、光学、半導体、分子工学と化学への接点。
- [量子論・量子情報](quantum/README.md)：状態と測定、場の量子論、量子計算。
- [相対論・宇宙・原子核](relativity-cosmology/README.md)：時空、重力、宇宙論、核融合。気象の資料もここから案内。
- [物理と機械学習](physics-ml/README.md)：PINNs、対称性、物理による学習の理解、学習による物理の予測。

## 数学や実装へつなぐ

力学・振動からは[常微分方程式](../math/analysis/ordinary-differential-equations.md)、流体・伝熱からは[偏微分方程式](../math/analysis/partial-differential-equations.md)、応力や相対論からは[テンソル](../math/geometry/tensors.md)、対称性からは[群論](../math/algebra/group-theory.md)へ戻れます。

数学側にある[フーリエ変換とラプラス変換](../math/analysis/fourier-and-laplace-transforms.md)は共通のノートとして参照し、重複した原文を作りません。物性化学・分子工学は、[化学編](../chemistry/README.md)からも参照する境界領域のノートです。化学編の[平衡と速度](../chemistry/reaction-direction-and-rate.md)では、化学ポテンシャルから反応の向きへつなぎます。

## 原文・出典・確認した範囲

[原文テキスト](sources/README.md)には取得した全行を保存し、元ページの日時、原文とMarkdownの行の対応も記録しました。説明の不備を見つけた箇所は、原文を変更せず補足節で理由を示しています。

元データの埋め込み欠落記号は**64か所**あり、図・式の内容は復元できていません。取得できた画像2点は出典付きで保存しました。各資料・講義の全内容を検証したものではありません。詳しくは[移植記録](import-report.md)と[参考資料](../references/yuyannnn-scrapbox-physics.md)を参照してください。

[全体の入口へ](../README.md)
