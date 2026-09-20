# 数学メモの全文移植記録

取得・移植日：2026-09-20。対象：公開Scrapboxプロジェクト `MistMavGamer`。

## 対象範囲

公開ページ一覧1,352件を確認し、AI生成の俯瞰マップの数学欄にある全45ページと、数学索引・関連リンク・ページ一覧から選んだ19ページを移植しました。計64ページ、16,697行（タイトル・空行を含む）です。選定したページの取得失敗はありません。

全ページの一覧は[数学の入口](README.md)から各分野へ、原文ファイルの一覧は[Sources](sources/README.md)からたどれます。対象は数学とその近接領域であり、プロジェクト内の全1,352ページを移したわけではありません。元の分野マップ・全体俯瞰マップは数学の背景を残すため、他分野の項目も含めて全文を保持しました。

## 残したもの

- 当時の本文、ページ内の順序、感想、疑問、未完の見出し、資料へのリンク。
- 原ページの作成・最終更新日時と、APIに含まれる行単位の作成・更新日時。
- 整形前の原文テキストと、原文行から移植本文への対応。
- 元ページにURLが残っていた画像11点。画像の出典リンクも保持。

日時は原ページの編集の記録であり、本人が学習した日時や感想を書いた当初の日付を必ず表すものではありません。取得できたのは現時点のページであり、過去の全改訂履歴・削除済みの文章は含みません。

## 整形とAI補足

本文の語句を勝手に書き換えず、Scrapboxの見出し・リンク・字下げをMarkdownへ整形しました。字下げは引用段落の深さで表現し、原文の表は表として残しました。数式の角括弧をページリンクと誤認しないようにし、元ページ一覧で確認できないリンク名は文字として保持しました。詳細な原表記は対応する原文テキストで確認できます。

64ページすべてに、その内容に合わせた「AIによる補足・訂正」を別の節で追加しました。定義の不足、条件、反例、応用へ進むための問いを補っています。補足が当時の本人の理解や感想に混ざらないよう、冒頭の案内もAIが加えたものと明示しています。

主な訂正・区別は次のとおりです。

- [線形代数](linear-algebra/linear-algebra.md#ai-notes)：ベクトルと座標表示、一般線形群と正方行列全体、相似類と剰余群。
- [群論](algebra/group-theory.md#ai-notes)：結合法則と交換法則。
- [Lie代数](algebra/lie-algebras.md#ai-notes)：括弧の双線形性と、局所的な線形化の意味。
- [集合と位相](foundations/sets-and-topology.md#ai-notes)：Cauchy列の収束と完備性。
- [数理最適化](optimization-computation/mathematical-optimization.md#ai-notes)：停留点と最適解、制約の条件。
- [数値解析](optimization-computation/numerical-analysis.md#ai-notes)：条件数の定義と、問題の条件・算法の安定性の区別。
- [計算量理論](information-discrete/computational-complexity.md#ai-notes)：NPの定義と、P対NPの未解決性。
- [MLにおける幾何学的手法](geometry/geometric-methods-in-ml.md#ai-notes)：双曲空間への関心を残しつつ、埋め込みの保証を一般化しすぎない。

これらは重要な箇所への補足です。本文全体の全定理・証明・出典の検証が済んだとは扱わず、ノートの状態は `draft` としています。

## 元データにある欠落

8ページに、埋め込み内容のない U+FFFC（オブジェクト置換文字）が計171か所あります。元データが既にこの状態のため、図・数式・添付のどれだったかを特定できません。削除済み内容を推測で作らず、整形版の各箇所に欠落表示を入れました。

また、[幾何学の基礎of基礎](geometry/geometry-foundations.md)には、画像を削除したため疎になっている旨が原文で明示されています。記号が残っていない削除もあり得るため、171はすべての欠落の総数を保証する数字ではありません。

### 常微分方程式：5か所

[L408](analysis/ordinary-differential-equations.md#source-L408), [L411](analysis/ordinary-differential-equations.md#source-L411), [L414](analysis/ordinary-differential-equations.md#source-L414), [L415](analysis/ordinary-differential-equations.md#source-L415), [L416](analysis/ordinary-differential-equations.md#source-L416)

### フーリエ変換とラプラス変換：26か所

[L203](analysis/fourier-and-laplace-transforms.md#source-L203), [L207](analysis/fourier-and-laplace-transforms.md#source-L207), [L211](analysis/fourier-and-laplace-transforms.md#source-L211), [L212](analysis/fourier-and-laplace-transforms.md#source-L212), [L217](analysis/fourier-and-laplace-transforms.md#source-L217), [L219](analysis/fourier-and-laplace-transforms.md#source-L219), [L237](analysis/fourier-and-laplace-transforms.md#source-L237), [L239](analysis/fourier-and-laplace-transforms.md#source-L239), [L241](analysis/fourier-and-laplace-transforms.md#source-L241), [L242](analysis/fourier-and-laplace-transforms.md#source-L242), [L255](analysis/fourier-and-laplace-transforms.md#source-L255), [L257](analysis/fourier-and-laplace-transforms.md#source-L257), [L258](analysis/fourier-and-laplace-transforms.md#source-L258), [L259](analysis/fourier-and-laplace-transforms.md#source-L259), [L260](analysis/fourier-and-laplace-transforms.md#source-L260), [L289](analysis/fourier-and-laplace-transforms.md#source-L289), [L291](analysis/fourier-and-laplace-transforms.md#source-L291), [L300](analysis/fourier-and-laplace-transforms.md#source-L300), [L312](analysis/fourier-and-laplace-transforms.md#source-L312), [L314](analysis/fourier-and-laplace-transforms.md#source-L314), [L316](analysis/fourier-and-laplace-transforms.md#source-L316), [L325](analysis/fourier-and-laplace-transforms.md#source-L325), [L327](analysis/fourier-and-laplace-transforms.md#source-L327), [L329](analysis/fourier-and-laplace-transforms.md#source-L329), [L331](analysis/fourier-and-laplace-transforms.md#source-L331), [L338](analysis/fourier-and-laplace-transforms.md#source-L338)

### 群論：14か所

[L25](algebra/group-theory.md#source-L25), [L30](algebra/group-theory.md#source-L30), [L46](algebra/group-theory.md#source-L46), [L56](algebra/group-theory.md#source-L56), [L61](algebra/group-theory.md#source-L61), [L73](algebra/group-theory.md#source-L73), [L100](algebra/group-theory.md#source-L100), [L108](algebra/group-theory.md#source-L108), [L110](algebra/group-theory.md#source-L110), [L161](algebra/group-theory.md#source-L161), [L179](algebra/group-theory.md#source-L179), [L191](algebra/group-theory.md#source-L191), [L203](algebra/group-theory.md#source-L203), [L215](algebra/group-theory.md#source-L215)

### ガロア理論：1か所

[L35](algebra/galois-theory.md#source-L35)

### 代数の基礎：64か所

[L153](algebra/algebra-foundations.md#source-L153), [L241](algebra/algebra-foundations.md#source-L241), [L244](algebra/algebra-foundations.md#source-L244), [L247](algebra/algebra-foundations.md#source-L247), [L250](algebra/algebra-foundations.md#source-L250), [L253](algebra/algebra-foundations.md#source-L253), [L258](algebra/algebra-foundations.md#source-L258), [L261](algebra/algebra-foundations.md#source-L261), [L264](algebra/algebra-foundations.md#source-L264), [L266](algebra/algebra-foundations.md#source-L266), [L269](algebra/algebra-foundations.md#source-L269), [L279](algebra/algebra-foundations.md#source-L279), [L282](algebra/algebra-foundations.md#source-L282), [L285](algebra/algebra-foundations.md#source-L285), [L288](algebra/algebra-foundations.md#source-L288), [L291](algebra/algebra-foundations.md#source-L291), [L295](algebra/algebra-foundations.md#source-L295), [L305](algebra/algebra-foundations.md#source-L305), [L308](algebra/algebra-foundations.md#source-L308), [L310](algebra/algebra-foundations.md#source-L310), [L314](algebra/algebra-foundations.md#source-L314), [L320](algebra/algebra-foundations.md#source-L320), [L323](algebra/algebra-foundations.md#source-L323), [L326](algebra/algebra-foundations.md#source-L326), [L329](algebra/algebra-foundations.md#source-L329), [L332](algebra/algebra-foundations.md#source-L332), [L335](algebra/algebra-foundations.md#source-L335), [L341](algebra/algebra-foundations.md#source-L341), [L344](algebra/algebra-foundations.md#source-L344), [L347](algebra/algebra-foundations.md#source-L347), [L350](algebra/algebra-foundations.md#source-L350), [L353](algebra/algebra-foundations.md#source-L353), [L356](algebra/algebra-foundations.md#source-L356), [L359](algebra/algebra-foundations.md#source-L359), [L362](algebra/algebra-foundations.md#source-L362), [L371](algebra/algebra-foundations.md#source-L371), [L374](algebra/algebra-foundations.md#source-L374), [L378](algebra/algebra-foundations.md#source-L378), [L380](algebra/algebra-foundations.md#source-L380), [L386](algebra/algebra-foundations.md#source-L386), [L389](algebra/algebra-foundations.md#source-L389), [L392](algebra/algebra-foundations.md#source-L392), [L395](algebra/algebra-foundations.md#source-L395), [L398](algebra/algebra-foundations.md#source-L398), [L401](algebra/algebra-foundations.md#source-L401), [L403](algebra/algebra-foundations.md#source-L403), [L404](algebra/algebra-foundations.md#source-L404), [L412](algebra/algebra-foundations.md#source-L412), [L415](algebra/algebra-foundations.md#source-L415), [L418](algebra/algebra-foundations.md#source-L418), [L421](algebra/algebra-foundations.md#source-L421), [L427](algebra/algebra-foundations.md#source-L427), [L430](algebra/algebra-foundations.md#source-L430), [L433](algebra/algebra-foundations.md#source-L433), [L436](algebra/algebra-foundations.md#source-L436), [L439](algebra/algebra-foundations.md#source-L439), [L442](algebra/algebra-foundations.md#source-L442), [L445](algebra/algebra-foundations.md#source-L445), [L453](algebra/algebra-foundations.md#source-L453), [L456](algebra/algebra-foundations.md#source-L456), [L459](algebra/algebra-foundations.md#source-L459), [L462](algebra/algebra-foundations.md#source-L462), [L465](algebra/algebra-foundations.md#source-L465), [L468](algebra/algebra-foundations.md#source-L468)

### 確率：3か所

[L367](probability-statistics/probability.md#source-L367), [L372](probability-statistics/probability.md#source-L372), [L559](probability-statistics/probability.md#source-L559)

### 統計学：47か所

[L59](probability-statistics/statistics.md#source-L59), [L148](probability-statistics/statistics.md#source-L148), [L151](probability-statistics/statistics.md#source-L151), [L152](probability-statistics/statistics.md#source-L152), [L153](probability-statistics/statistics.md#source-L153), [L156](probability-statistics/statistics.md#source-L156), [L157](probability-statistics/statistics.md#source-L157), [L158](probability-statistics/statistics.md#source-L158), [L159](probability-statistics/statistics.md#source-L159), [L160](probability-statistics/statistics.md#source-L160), [L163](probability-statistics/statistics.md#source-L163), [L164](probability-statistics/statistics.md#source-L164), [L165](probability-statistics/statistics.md#source-L165), [L166](probability-statistics/statistics.md#source-L166), [L170](probability-statistics/statistics.md#source-L170), [L171](probability-statistics/statistics.md#source-L171), [L172](probability-statistics/statistics.md#source-L172), [L173](probability-statistics/statistics.md#source-L173), [L177](probability-statistics/statistics.md#source-L177), [L178](probability-statistics/statistics.md#source-L178), [L179](probability-statistics/statistics.md#source-L179), [L180](probability-statistics/statistics.md#source-L180), [L183](probability-statistics/statistics.md#source-L183), [L184](probability-statistics/statistics.md#source-L184), [L185](probability-statistics/statistics.md#source-L185), [L186](probability-statistics/statistics.md#source-L186), [L189](probability-statistics/statistics.md#source-L189), [L190](probability-statistics/statistics.md#source-L190), [L191](probability-statistics/statistics.md#source-L191), [L192](probability-statistics/statistics.md#source-L192), [L195](probability-statistics/statistics.md#source-L195), [L196](probability-statistics/statistics.md#source-L196), [L197](probability-statistics/statistics.md#source-L197), [L198](probability-statistics/statistics.md#source-L198), [L201](probability-statistics/statistics.md#source-L201), [L202](probability-statistics/statistics.md#source-L202), [L203](probability-statistics/statistics.md#source-L203), [L204](probability-statistics/statistics.md#source-L204), [L207](probability-statistics/statistics.md#source-L207), [L208](probability-statistics/statistics.md#source-L208), [L211](probability-statistics/statistics.md#source-L211), [L212](probability-statistics/statistics.md#source-L212), [L213](probability-statistics/statistics.md#source-L213), [L216](probability-statistics/statistics.md#source-L216), [L217](probability-statistics/statistics.md#source-L217), [L218](probability-statistics/statistics.md#source-L218), [L254](probability-statistics/statistics.md#source-L254)

### 統計的機械学習：11か所

[L322](probability-statistics/statistical-machine-learning.md#source-L322), [L607](probability-statistics/statistical-machine-learning.md#source-L607), [L649](probability-statistics/statistical-machine-learning.md#source-L649), [L774](probability-statistics/statistical-machine-learning.md#source-L774), [L906](probability-statistics/statistical-machine-learning.md#source-L906), [L988](probability-statistics/statistical-machine-learning.md#source-L988), [L1078](probability-statistics/statistical-machine-learning.md#source-L1078), [L1208](probability-statistics/statistical-machine-learning.md#source-L1208), [L1282](probability-statistics/statistical-machine-learning.md#source-L1282), [L1305](probability-statistics/statistical-machine-learning.md#source-L1305), [L1332](probability-statistics/statistical-machine-learning.md#source-L1332)

## 未移植の参照先

物理・ロボティクス・ソフトウェアなど、対象64ページの外へ出るリンクは元の公開ページへのリンクとして残しています。リンク先の論文・本・動画は、ページ本文とは別の資料であり、全文をダウンロードして複製していません。

元のリンク名が取得したページ一覧と一致しない場合も、勝手なリンク先や内容を作っていません。以下は該当ラベルの記録です。不在・削除と断定するものではなく、別名や表記差の可能性もあります。

<details>
<summary>一覧と一致しないリンク名</summary>

- AGI社会論研究会
- AISI
- AIに関する法的規制
- Domain Adaptation
- Figma
- Illustrator
- In-Context Learning
- J-SOX
- LoRA
- M&Aについてのメモ
- Progressive Web Apps
- PythonではじめるKaggleスタートブック
- Restaurant Tech
- SEO
- Simulation
- Unreal
- Vision Transformer
- Y Combinator
- e-sports
- eKYC技術
- コンピューターグラフィクス
- スパコン・高性能プログラミング・FEM・CAE
- デリバティブ
- ノーコードでHP作成Studio
- バリュープロポジション
- パワー半導体
- プログラマが独立するときに注意すべきこと
- メカトロニクス
- リスキリング
- リバースエンジニアリング
- ワンピースに学ぶ組織
- 何で制御すべき？回転行列?二重四元数?
- 俯瞰経営塾
- 実践コンピュータアーキテクチャ
- 建築
- 必修魔術論
- 恐れのない組織
- 政治とマスメディア
- 株式投資入門
- 機械学習によく出てくる確率統計的な知識
- 機構学
- 深層強化学習の汎用に向けて
- 現代国際ビジネス法
- 知識グラフについて調べる
- 確率的プログラミング言語
- 競技プログラミングでよくあるアルゴリズム集
- 経営学
- 総務
- 螺旋本
- 語彙力向上

</details>

## 検証

原文テキスト64件は、取得したAPI本文の全行との完全一致を確認しました。全16,697行の対応表、ローカルリンク2,568件、画像11点のチェックサムも照合済みです。Markdownの解析で、意図しないコードブロックや欠落箇所のアンカー消失がないことを確認し、数式中のアスタリスクなどが誤って斜体に変わる箇所も修正しました。

```sh
python3 scripts/import_scrapbox_math.py --check
```

このコマンドは公開ファイルだけで原文・移植本文のチェックサム、全行の対応・ローカルリンク・画像を再照合できます。ローカルの `inbox/` に取得時のAPI応答がある場合は、原文と再変換した本文の一致も追加確認します。移植後に本人が追記した内容を再生成で上書きしないため、生成スクリプトは手編集を検出すると停止します。

[数学の入口へ](README.md)
