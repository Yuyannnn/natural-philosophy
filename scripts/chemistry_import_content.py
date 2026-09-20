"""Chemistry source selection and explicitly separate editorial supplements."""
GROUPS = {
    'foundations': '化学の基礎',
    'materials-informatics': '材料・分子とAI',
    'life-sciences': '生命科学との接点',
}
PAGES = {
    '高校化学': {'group': 'foundations', 'slug': 'high-school-chemistry', 'description': '電子とモルを軸に、理論・無機・有機を読み直す長い学習メモ。'},
    '材料工学': {'group': 'materials-informatics', 'slug': 'materials-engineering', 'description': '材料の成分・組織・製造プロセスと、強度や機能の関係。'},
    'ケモインフォマティクス': {'group': 'materials-informatics', 'slug': 'cheminformatics', 'description': '分子の記述子、SMILES、機械学習、構造式画像認識の資料。'},
    'マテリアルズインフォマティクス': {'group': 'materials-informatics', 'slug': 'materials-informatics', 'description': '材料探索・生成AI・データ共有への資料と、生命科学への関連リンク。'},
    'AI for Materials': {'group': 'materials-informatics', 'slug': 'ai-for-materials', 'description': '材料・分子・プロセス・実験自動化をつなぐ短いリンクメモ。'},
    'Process Informatics': {'group': 'materials-informatics', 'slug': 'process-informatics', 'description': '反応系のスケールアップと製造条件の最適化への資料。'},
    'AIロボット駆動科学': {'group': 'materials-informatics', 'slug': 'automated-experimental-science', 'description': '研究活動の自動化、実験ロボット、AI for Scienceに関する資料。'},
    '生命科学': {'group': 'life-sciences', 'slug': 'life-sciences', 'description': '以前の講義を見返した感想と、代謝・自由エネルギー・数理モデルの入口。'},
    '生物学': {'group': 'life-sciences', 'slug': 'biology', 'description': '生物学の読書マップ、学生の活動、細胞画像解析と顕微鏡制御へのリンク。'},
    'バイオインフォマティクス': {'group': 'life-sciences', 'slug': 'bioinformatics', 'description': '配列・グラフ・確率的アルゴリズムから、単一細胞解析や予測モデルへ。'},
    '創薬AI': {'group': 'life-sciences', 'slug': 'ai-drug-discovery', 'description': '分子生成、タンパク質構造予測、高分子や創薬研究の資料。'},
    'バイオサイバネティクス': {'group': 'life-sciences', 'slug': 'biocybernetics', 'description': '生命現象の制御と工学をつなぐ短い紹介メモ。'},
}
# Only clearly personal remarks are highlighted; study summaries may quote teachers.
SIGNALS = {'生命科学': ['授業一回も出ずに一夜漬け']}
SUPPLEMENTS = {}
SUPPLEMENTS['高校化学'] = r"""### このメモの読み方

[冒頭](#source-L4)と[無機化学の導入](#source-L351)には、暗記を減らすために電子の性質から考えるという学習方針が書かれています。教材由来の説明と本人の言葉の境界は不明ですが、この考え方を読み返す手がかりとして残します。「最終目標」は当時の受験学習の目標で、化学全体の到達点とは区別します。

長い本文は、[電子・結合](#source-L23)、[気体・溶液](#source-L97)、[熱化学](#source-L161)、[速度・平衡](#source-L201)、[酸塩基](#source-L227)、[酸化還元・電池](#source-L283)、[無機](#source-L343)、[有機・構造決定](#source-L427)、[芳香族](#source-L613)から読めます。

### 電子の直感に条件を付ける

- [L31](#source-L31)の「2個ずつセット」は、軌道の収容数と占有順序を混同しやすい表現です。1軌道は逆向きスピンで最大2電子。同じエネルギーの軌道は、まず別々に同じ向きのスピンで占有します（Hund則）。[OpenStax Chemistry 2e §6.4](https://openstax.org/books/chemistry-2e/pages/6-4-electronic-structure-of-atoms-electron-configurations)
- [L42](#source-L42)の平均値による電気陰性度はMullikenの考え方です。結合エネルギーに基づくPauling尺度の数値とそのまま混ぜません。[IUPAC Gold Book: electronegativity](https://goldbook.iupac.org/terms/view/E01990)。[L74](#source-L74)の「クーロン力による結合は不可能」も不適切で、共有結合でも電子と原子核の静電相互作用が働きます。[§7.2](https://openstax.org/books/chemistry-2e/pages/7-2-covalent-bonding)
- [L76](#source-L76)の水溶性から毒性・臭い・酸塩基性を一括で判断する説明は成立しません。溶けやすさと酸塩基平衡は別の性質で、例えばショ糖の水溶液が強酸や強塩基になるわけではありません。[L66–71](#source-L66)の融点・密度に関する比例関係も、普遍的な計算式には使えません。

### 熱力学と速度を分ける

[L220](#source-L220)の「発熱とエントロピー増大が同方向なら平衡にはならない」は訂正が必要です。一定温度・圧力で、反応の向きはその組成での反応Gibbsエネルギー $\Delta_rG$ を使って判断します。平衡では $\Delta_rG=0$、標準反応量とは $\Delta_rG^\circ=-RT\ln K$ で結ばれます。大きい有限の $K$ は「平衡が存在しない」ことを意味しません。[§16.4](https://openstax.org/books/chemistry-2e/pages/16-4-free-energy)

[L203](#source-L203)の速度式には化学種でないScrapboxリンクが混入しています。元の記号は特定できないため復元せず、一般形として $v=k[A]^m[B]^n$ を別に示します。次数は通常実験で決め、総括反応式の係数からは決まりません。[§12.3](https://openstax.org/books/chemistry-2e/pages/12-3-rate-laws)。詳しくは[反応の向きと速さ](../reaction-direction-and-rate.md)へ。

### 酸塩基・沈殿・電極反応

- [L242](#source-L242)：pHの厳密な定義は水素イオンの無次元の活量によります（[IUPAC Gold Book](https://goldbook.iupac.org/terms/view/P04524)）。希薄水溶液では $-\log_{10}([H^+]/c^\circ)$ で近似し、$c^\circ=1\ \mathrm{mol\,L^{-1}}$。極めて薄い酸では水の自己解離も含めます。[§14.2](https://openstax.org/books/chemistry-2e/pages/14-2-ph-and-poh)
- [L245](#source-L245)、[L270–271](#source-L270)：滴定の当量関係と、平衡後の電離度は別です。緩衝液でも「いつも近似できる」とは限りません。十分な弱酸・共役塩基が共存するかを確認し、物質収支・電荷収支と平衡式から判断します。[§14.6](https://openstax.org/books/chemistry-2e/pages/14-6-buffers)
- [L316](#source-L316)、[L367](#source-L367)：金属の酸化されやすさから塩の沈殿を判断できません。沈殿はイオン積と溶解度積を比較します。例えば $\mathrm{CaCO_3(s)\rightleftharpoons Ca^{2+}(aq)+CO_3^{2-}(aq)}$ は、酸化数の変化を伴わない溶解平衡です。[§15.1](https://openstax.org/books/chemistry-2e/pages/15-1-precipitation-and-dissolution)
- [L375](#source-L375)：4配位には正四面体だけでなく平面正方形もあります。配位数だけで構造は一意に決まりません。[§19.2](https://openstax.org/books/chemistry-2e/pages/19-2-coordination-chemistry-of-transition-metals)
- [L327](#source-L327)：正極で必ず陰イオンが生まれるわけではありません。例えば銅イオンの還元では $\mathrm{Cu^{2+}(aq)+2e^-\to Cu(s)}$。電子は外部回路を、イオンは電解質中を移動し、電荷収支を保ちます。[§17.2](https://openstax.org/books/chemistry-2e/pages/17-2-galvanic-cells)

### 有機化学の分類・機構

- [L479](#source-L479)：ジアステレオマーは「鏡像異性体の一種」ではなく、互いに鏡像関係にない立体異性体です。不斉中心が $n$ 個なら $2^n$ は上限で、分子内の対称性などによって少なくなります。[Organic Chemistry §5.6](https://openstax.org/books/organic-chemistry/pages/5-6-diastereomers)
- [L531](#source-L531)：ヒドロホウ素化を「BH2+が先に付加」とは説明しません。B–H結合が協奏的に付加する機構で、単純なカルボカチオン経由の段階的反応と区別します。[§8.5](https://openstax.org/books/organic-chemistry/pages/8-5-hydration-of-alkenes-addition-of-h2o-by-hydroboration)
- [L628](#source-L628)、[L630](#source-L630)、[L635](#source-L635)のベンゼンの通常のハロゲン化・スルホン化・ニトロ化は、芳香族求電子置換で説明します。ラジカル反応と一括しません。結合の組み替えをすべて酸化還元とする[L434](#source-L434)の見方も分けて考えます。[第16章まとめ](https://openstax.org/books/organic-chemistry/pages/16-summary)
- [L608–610](#source-L608)：アミドをエステルと同じ条件で一般に合成できるとはいえません。カルボン酸とアミンはまず塩を作りやすく、アミド形成には活性化などの条件を考えます。小さいアミドには水溶性のものもあります。[§21.7](https://openstax.org/books/organic-chemistry/pages/21-7-chemistry-of-amides)

### まだ確認が必要な記述

[L280](#source-L280)の「最新の研究」は出典未同定です。[L319](#source-L319)の不動態、[L401](#source-L401)の濃硫酸、[L502–517](#source-L502)の安定性・反応分類、[L537–543](#source-L537)の酸化とアルキン反応、[L555](#source-L555)の炭素数による脱水の制限、[L581](#source-L581)のギ酸、[L588](#source-L588)の脱水、[L596–600](#source-L596)の触媒・収率にも、条件の欠落や誤りが疑われます。今回すべてを確定・訂正したものではありません。個別の実験条件や手順の根拠にする前に、対応する教材・原資料との照合が残ります。"""
SUPPLEMENTS['材料工学'] = r"""### 成分から製造履歴までを一緒に考える

[L85–86](#source-L85)の「成分 * 組織」「成分 * 製造プロセス」は、実数を掛け合わせる法則としてではなく、性質が複数の要因に依存するという見取り図として読むと有用です。同じ組成でも、熱処理・加工・組織の違いが特性に関わります。[MIT OCW 3.032の講義概要](https://ocw.mit.edu/courses/3-032-mechanical-behavior-of-materials-fall-2007/)も、原子・分子機構から巨視的な力学特性までを結んでいます。

[L57](#source-L57)の「CFRPはベスト」は当時の短い評価です。設計では荷重方向、剛性、破壊、温度、加工性、費用を含めて目的を定める必要があります。[材料力学](../../physics/continuum-simulation/mechanics-of-materials.md)で構造としての応答を、[マテリアルズインフォマティクス](materials-informatics.md)で特性を予測する入力の選び方を考えるとつながります。

今回の補足からの問い：同一組成の試料を異なる熱処理で作った場合、機械学習の入力にどの履歴を残すべきでしょうか。"""
SUPPLEMENTS['ケモインフォマティクス'] = r"""### 分子をデータとして表現する

元の本文は、入門書・記述子・機械学習・構造式画像認識の資料を集めたものです。すべてを実装済み・読了とは扱いません。

分子式が同じでも結合のつながりが異なることがあります。例えばエタノールとジメチルエーテルはともに $\mathrm{C_2H_6O}$ ですが、SMILESではそれぞれ CCO と COC と書けます。原子と結合をグラフとして扱うと、この違いを保持できます。SMILESの読み込み、記述子、フィンガープリントの基本操作は[RDKit公式 Getting Started](https://www.rdkit.org/docs/GettingStartedInPython.html)で確認できます。

構造を読む処理、特徴量へ変換する処理、物性を予測する処理を分けて考えます。文字列が異なっても同一分子を表す場合があるため、文字列の完全一致だけで同一性を判断しません。立体化学や電荷もデータに残す必要があります。

原文の[L36](#source-L36)にはURLと未完の文が連結しています。正しいリンク先や意図を推測して本文を書き換えていません。次に整理するなら、[高校化学の異性体](../foundations/high-school-chemistry.md#source-L477)から、グラフによる表現で何が残り、何が省かれるかを確かめる経路が考えられます。"""
SUPPLEMENTS['マテリアルズインフォマティクス'] = r"""### 予測・生成・実験を分ける

[原文のMatterGen紹介](#source-L14)は、既存候補の性質を予測するだけでなく、狙う性質を条件として無機材料の結晶構造を生成する研究への入口です。[Microsoft Researchの原紹介](https://www.microsoft.com/en-us/research/blog/mattergen-a-new-paradigm-of-materials-design-with-generative-ai/)の説明を確認しました。生成した候補と、合成・測定で確認した材料の区別は残します。

[材料工学](materials-engineering.md)の成分・組織・製造プロセスという見方から、化学式だけを入力にするモデルにどの情報が欠けるかを考えられます。これは今回追加した読み方です。

[L43](#source-L43)のCellOracleは、材料特性の予測器ではなく、遺伝子制御ネットワークを用いて摂動の影響を計算する生命科学のツールです。[公式説明](https://morris-lab.github.io/CellOracle.documentation/)に基づき、元の配置は保ちながら[バイオインフォマティクス](../life-sciences/bioinformatics.md)へつなぎます。原文の資料間の近さを、分野や機能が同じという意味に置き換えません。"""
SUPPLEMENTS['AI for Materials'] = """### 交差点として残す

本文は関連ページとNIMSの人材公募へのリンクを集めた短いメモです。採用情報を学習済みの理論として膨らませず、[分子表現](cheminformatics.md)・[材料探索](materials-informatics.md)・[製造プロセス](process-informatics.md)・[実験自動化](automated-experimental-science.md)を行き来する入口にします。

今回の整理では、各資料を「入力は何か」「何を予測・生成するか」「何を実測して確かめるか」で読むことを提案します。この分類はAIによる整理であり、元ページにその方針が明記されていたわけではありません。公募の現在の募集状況は確認していません。"""
SUPPLEMENTS['Process Informatics'] = """### 分子の反応を装置の規模へつなぐ

原文の[スケールアップの論文](https://www.nature.com/articles/s41467-025-63982-2)は、ナフサの流動接触分解を対象に、機構モデルと深層転移学習を組み合わせる研究です。AbstractとIntroductionを確認しました。反応器の規模が変わると、流れ・伝熱などの輸送現象や観測データの種類も変わることが出発点です。実験室の予測精度だけで、より大きな装置でも同じように使えるとは限りません。

[流体力学](../../physics/continuum-simulation/fluid-mechanics.md)と[熱・伝熱](../../physics/thermal-statistical/heat-transfer.md)が、反応そのもののモデルに加わる接点です。論文のモデルや実験を今回再現したわけではありません。

今回追加する読み方：分子組成、温度、滞留時間、装置形状のうち、モデルの入力に入るものと、測定していないものを分けて読む。"""
SUPPLEMENTS['AIロボット駆動科学'] = """### 紹介文の声と本人の記録を分ける

[L11–19](#source-L11)は、直前にリンクされた2023年のシンポジウムの紹介・主催者の署名を含みます。「我々」や社会的インパクトへの見通しを、本人の発言や参加実績として扱いません。後半は研究自動化に関する資料の収集です。

今回の整理では、実験候補の提案、装置への指示、測定、解析、次の候補の選択という流れで読むことを提案します。化学のデータには、分子構造だけでなく、試料・装置・条件・単位・失敗した結果を対応させる視点が必要になります。これは今回追加した設計上の観点で、原文に実験装置を運用した記録があるという意味ではありません。

材料の候補探索は[マテリアルズインフォマティクス](materials-informatics.md)、装置規模と反応条件は[Process Informatics](process-informatics.md)へ。"""
SUPPLEMENTS['生命科学'] = r"""### 「今見返すと面白そう」を出発点にする

[L3](#source-L3)の感想は本人の学び直しへの入口として残します。一方、講義概要や回ごとの予定が載っていることと、それらをすべて学習・理解したことは分けます。[L41](#source-L41)の高分子の説明は未完です。

今回の補足として、生体分子の構造は[物性化学](../../physics/electromagnetism-matter/physical-chemistry.md)、代謝の駆動力は[熱力学](../../physics/thermal-statistical/thermodynamics.md)、変化の時間尺度は[反応の向きと速さ](../reaction-direction-and-rate.md)から読み直せます。代謝には物質を合成・分解する反応があり、エネルギーの授受と結び付いています。[OpenStax Biology 2e §6.1](https://openstax.org/books/biology-2e/pages/6-1-energy-and-metabolism)

生体内の濃度が一定に見えるときも、物質の流入・流出や反応が続いていれば、熱力学的平衡とは限りません。「変わらない量は何か」と「流れ続けているものは何か」を分けると、[開放系](../../physics/thermal-statistical/open-systems.md)や制御への関心につながります。"""
SUPPLEMENTS['生物学'] = """### 資料の役割を分ける

本文には読書マップの画像、学生の活動、単一細胞解析、細胞画像の領域分割、顕微鏡制御など、種類の異なる入口があります。[Cellposeの公式ページ](https://www.cellpose.org/)では細胞などの画像の領域分割が対象です。画像から細胞の位置・形を取り出す処理と、細胞の分子状態を解析する処理は分けて考えます。

[L10](#source-L10)の画像は多数の生物学書をつなぐ読書マップでした。作者・利用条件が元ページから特定できないため、元URLへのリンクを保持し、画像ファイルの再配布はしていません。掲載された本を本人が読了したという扱いにもしていません。

化学からは[生命科学](life-sciences.md)で物質と代謝を、計算からは[バイオインフォマティクス](bioinformatics.md)でデータとアルゴリズムをたどれます。"""
SUPPLEMENTS['バイオインフォマティクス'] = """### アルゴリズムの目次と新しい研究資料をつなぐ

[L25–47](#source-L25)はアルゴリズムの章立てで、実装や読了の記録とは限りません。全探索、動的計画法、グラフ、隠れMarkovモデルという異なる方法が集まっています。今回の読み方として、入力が配列なのか、分子グラフなのか、細胞ごとの測定値なのかを先に区別すると、各手法の役割を追いやすくなります。

原文のscvi-toolsは、[公式ページ](https://scvi-tools.org/)によれば単一細胞オミクスを確率モデルで解析するためのライブラリです。分子の構造を特徴量にする[ケモインフォマティクス](../materials-informatics/cheminformatics.md)とは、観測単位も予測対象も異なります。

細胞の摂動を予測した結果は、実験で得られた結果と区別して記録します。[マテリアルズインフォマティクスに置かれていたCellOracle](../materials-informatics/materials-informatics.md#source-L43)も、こちらから参照できるようにしました。"""
SUPPLEMENTS['創薬AI'] = """### 構造予測から何がわかるか

原文は分子生成やタンパク質構造予測に関する資料の集積です。[L14–28](#source-L14)にはSNSリンクに続く紹介文があり、その期待や評価を本人自身の研究成果とは扱いません。

AlphaFold 3は複合体を含む構造を予測しますが、分子の時間変化をそのまま計算するモデルではありません。構造上の衝突や立体化学の誤りも起こり得ることが[EMBL-EBIの公式教材](https://www.ebi.ac.uk/training/online/courses/alphafold/alphafold-3-and-alphafold-server/introducing-alphafold-3/what-alphafold-3-struggles-with/)で説明されています。構造予測の信頼度と、結合の強さや細胞での働きの測定結果は分けて読みます。

[L7](#source-L7)の「分子動力学シミュレーション」は取得時カタログでページを確認できなかったため、未解決のラベルとして保持しました。[分子工学](../../physics/electromagnetism-matter/molecular-engineering.md)への経路は既存ノートで補います。今回、個別候補の有効性や臨床的な評価は検証していません。"""
SUPPLEMENTS['バイオサイバネティクス'] = """### 工学から生命現象を読み直す入口

原文は、生物の制御機構を扱う分野の紹介と、生命科学・ファジィ制御へのリンクです。紹介文の出典はページ内では特定できず、本人の専門や経験を示す文章とは扱いません。

今回の整理では「何を一定に保つか」「何を観測するか」「どこへ働きかけるか」という問いを、生命科学と工学の接点として提案します。[生命科学](life-sciences.md)の恒常性への記述と合わせて読む入口です。個々の生理現象をこの短いメモだけでモデル化できるという意味ではありません。"""
