# 物理メモの移植記録

## 対象と範囲

2026-09-20取得。[Scrapboxの俯瞰マップ](../math/learning-paths/original-ai-overview.md)の物理欄45リンクを起点にしました。そのうち「フーリエ変換とラプラス変換」は数学編に移植済みなので参照でつなぎ、残る44ページを物理編へ移しました。さらに以下の7ページを関連メモとして追加しています。

- 光学：波動・センサーとの接点。
- 半導体：物質とAI計算機の接点。
- 電気の理論の地図：電磁気学からのリンクと、機械系との類似への疑問。
- 物理ベースアニメーション(CG)：数学・運動方程式・実装の接点。
- 有限要素法：流体と材料のモデルを数値計算へつなぐ。
- 言語モデルの物理学：対称性と機械学習からの関連リンク。
- スターリングエンジンを0から作る備忘録：熱力学からつながる製作・実習の記録。

計51ページ、6,063行を保存しました。物理欄のリンクは45件すべて、このリポジトリ内でたどれます。プロジェクト全1,352ページのうち、あらゆる物理関連ページを網羅したという意味ではありません。ロボット・制御・電子回路など、今回対象に含めずカタログに存在するページは元の公開Scrapboxへリンクしています。取得時カタログで対応先を確認できなかったラベル（Simulation、Breakdowns、パワー半導体、メカトロニクス、分子動力学シミュレーション、競技プログラミングでよくあるアルゴリズム集、設計者に必要なメカトロニクスの基礎知識）は文字として残し、manifestにも記録しています。

## 意図と本文を残す方法

- 各ページの原文をそのままテキストで保存し、別にMarkdownへ整形した。
- 本文の順序・字下げ・空白・疑問・感想・未完の箇所を保持した。字下げは引用の深さで表示する。
- 元のページ日時と、行ID・行の日時・本文位置の対応をmanifestに記録した。日時は学習順序の証明には使わない。
- 本人の疑問が明確な部分は「思考の手がかり」として抜き出し、元の位置へリンクした。
- 講義案内、書籍の項目、SNSの引用、過去のAI回答などを、本人の独自の発言や理解として一括で扱わない。
- 51ページすべてに、今回AIが追加した導入・訂正・次の問いを別の節で置いた。

「原子核物理」はタイトルのみ、「簡易版流体力学シミュレーション」はABMAC法への短いメモだけでした。完成した説明や実装履歴を補作していません。スターリングエンジンのページには「メモがなかった」という文章と寸法入りの手描き図があります。図は保存しましたが、製作過程や完成状況を断定していません。

## 主な補足・訂正

本文を改変せず、各ページの補足節に記しました。

- [解析力学](mechanics-waves/analytical-mechanics.md#ai-notes)：循環座標で保存されるのは共役運動量。正準方程式の符号と作用の停留条件。
- [電磁気学](electromagnetism-matter/electromagnetism.md#ai-notes)：磁荷を導入しないMaxwell方程式、伝導電流と電磁波、静電平衡。
- [材料力学](continuum-simulation/mechanics-of-materials.md#ai-notes)：ヤング率の比と単位、線形弾性のひずみエネルギー。
- [Navier–Stokes方程式](continuum-simulation/navier-stokes.md#ai-notes)：応力ベクトルとテンソル、質量と運動量の収支、構成式。
- [流体力学](continuum-simulation/fluid-mechanics.md#ai-notes)：渦なしと循環、非粘性とポテンシャル流れ、相似則の適用条件。
- [有限要素法](continuum-simulation/finite-element-method.md#ai-notes)：逆行列を作る説明の限界、弱形式と一次三角形要素。
- [熱力学](thermal-statistical/thermodynamics.md#ai-notes)：状態量と熱、準静的過程と可逆過程。
- [量子論](quantum/quantum-theory.md#ai-notes)：負の確率という比喩と複素確率振幅の違い。
- [場の量子論](quantum/quantum-field-theory.md#ai-notes)：多体系、電磁相互作用、四元ポテンシャルと電磁場テンソル。
- [一般相対論](relativity-cosmology/general-relativity.md#ai-notes)：局所座標と計量、曲率、測地線を最短とする説明の限界。
- [PINNs](physics-ml/physics-informed-neural-networks.md#ai-notes)：点での残差と全域での精度、保存則の保証の違い。

これらは今回見つけた箇所の補足です。長い本文全体の全主張・引用元を校閲済みという意味ではありません。未同定の資料やリンク先の動画・本の全内容も未確認のまま残しています。

## 欠落と画像

元データにはU+FFFC（埋め込み欠落記号）が64か所あり、内容を推測で復元していません。位置は以下と本文中で確認できます。

### 力学・機械力学 — 20か所

[L459](mechanics-waves/classical-mechanics.md#source-L459)、[L460](mechanics-waves/classical-mechanics.md#source-L460)、[L461](mechanics-waves/classical-mechanics.md#source-L461)、[L478](mechanics-waves/classical-mechanics.md#source-L478)、[L480](mechanics-waves/classical-mechanics.md#source-L480)、[L481](mechanics-waves/classical-mechanics.md#source-L481)、[L482](mechanics-waves/classical-mechanics.md#source-L482)、[L483](mechanics-waves/classical-mechanics.md#source-L483)、[L484](mechanics-waves/classical-mechanics.md#source-L484)、[L485](mechanics-waves/classical-mechanics.md#source-L485)、[L486](mechanics-waves/classical-mechanics.md#source-L486)、[L487](mechanics-waves/classical-mechanics.md#source-L487)、[L488](mechanics-waves/classical-mechanics.md#source-L488)、[L489](mechanics-waves/classical-mechanics.md#source-L489)、[L490](mechanics-waves/classical-mechanics.md#source-L490)、[L491](mechanics-waves/classical-mechanics.md#source-L491)、[L492](mechanics-waves/classical-mechanics.md#source-L492)、[L493](mechanics-waves/classical-mechanics.md#source-L493)、[L494](mechanics-waves/classical-mechanics.md#source-L494)、[L495](mechanics-waves/classical-mechanics.md#source-L495)

### 熱&伝熱工学 — 44か所

[L72](thermal-statistical/heat-transfer.md#source-L72)、[L259](thermal-statistical/heat-transfer.md#source-L259)、[L262](thermal-statistical/heat-transfer.md#source-L262)、[L272](thermal-statistical/heat-transfer.md#source-L272)、[L303](thermal-statistical/heat-transfer.md#source-L303)、[L307](thermal-statistical/heat-transfer.md#source-L307)、[L310](thermal-statistical/heat-transfer.md#source-L310)、[L312](thermal-statistical/heat-transfer.md#source-L312)、[L317](thermal-statistical/heat-transfer.md#source-L317)、[L318](thermal-statistical/heat-transfer.md#source-L318)、[L320](thermal-statistical/heat-transfer.md#source-L320)、[L324](thermal-statistical/heat-transfer.md#source-L324)、[L327](thermal-statistical/heat-transfer.md#source-L327)、[L334](thermal-statistical/heat-transfer.md#source-L334)、[L367](thermal-statistical/heat-transfer.md#source-L367)、[L381](thermal-statistical/heat-transfer.md#source-L381)、[L396](thermal-statistical/heat-transfer.md#source-L396)、[L400](thermal-statistical/heat-transfer.md#source-L400)、[L408](thermal-statistical/heat-transfer.md#source-L408)、[L420](thermal-statistical/heat-transfer.md#source-L420)、[L421](thermal-statistical/heat-transfer.md#source-L421)、[L429](thermal-statistical/heat-transfer.md#source-L429)、[L431](thermal-statistical/heat-transfer.md#source-L431)、[L435](thermal-statistical/heat-transfer.md#source-L435)、[L443](thermal-statistical/heat-transfer.md#source-L443)、[L447](thermal-statistical/heat-transfer.md#source-L447)、[L448](thermal-statistical/heat-transfer.md#source-L448)、[L449](thermal-statistical/heat-transfer.md#source-L449)、[L450](thermal-statistical/heat-transfer.md#source-L450)、[L456](thermal-statistical/heat-transfer.md#source-L456)、[L457](thermal-statistical/heat-transfer.md#source-L457)、[L458](thermal-statistical/heat-transfer.md#source-L458)、[L459](thermal-statistical/heat-transfer.md#source-L459)、[L460](thermal-statistical/heat-transfer.md#source-L460)、[L480](thermal-statistical/heat-transfer.md#source-L480)、[L484](thermal-statistical/heat-transfer.md#source-L484)、[L488](thermal-statistical/heat-transfer.md#source-L488)、[L499](thermal-statistical/heat-transfer.md#source-L499)、[L509](thermal-statistical/heat-transfer.md#source-L509)、[L531](thermal-statistical/heat-transfer.md#source-L531)、[L532](thermal-statistical/heat-transfer.md#source-L532)、[L547](thermal-statistical/heat-transfer.md#source-L547)、[L582](thermal-statistical/heat-transfer.md#source-L582)、[L583](thermal-statistical/heat-transfer.md#source-L583)

取得できた画像は「電気の理論の地図」と「スターリングエンジンを0から作る備忘録」の2点。元URLと画像のチェックサムをmanifestに保存しました。画像にある文字や寸法を、新しい設計仕様として転記したものではありません。

## 検証

~~~sh
python3 scripts/import_scrapbox_physics.py --check
python3 examples/oscillator_energy.py
~~~

公開ファイルだけで原文と移植本文のチェックサム、6,063行の対応、ローカルリンク、画像を確認できます。取得時のAPI応答がローカルにあれば原文と再変換した本文との一致も追加確認します。GitHub Actionsでも公開ファイルの検証と計算例を実行します。

公開ファイルだけの作業コピーでも数学・物理の検証と両計算例が通ることを確認しました。意図的な原文・本文・画像の破損を検出し、本人の追記がある場合に再生成が停止することも確認しています。Markdown解析では意図しないコードブロックがないことと、欠落箇所のアンカーが残ることを確認しました。

移植先・説明・補足は[scripts/physics_import_content.py](../scripts/physics_import_content.py)で管理します。再生成にはローカルの取得データが必要で、手編集がある場合は上書きせず停止します。元ページの全改訂履歴や削除された内容を取得したものではありません。

[物理学の入口へ](README.md) · [原文一覧](sources/README.md)
