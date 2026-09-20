# 化学メモの移植記録

## 対象と選び方

2026-09-20取得。公開Scrapbox MistMavGamerの取得時カタログ（1,352ページ）を、化学・分子・材料・創薬・生命科学などの語と英語名で検索し、候補本文と関連リンクを確認しました。[俯瞰マップ](../math/learning-paths/original-ai-overview.md)の機械工学・物理・生命科学に分散した話題も参照しています。

新たに全文保存したのは**12ページ・1,239行**です。

- 化学の基礎：高校化学。
- 材料・分子とAI：材料工学、ケモインフォマティクス、マテリアルズインフォマティクス、AI for Materials、Process Informatics、AIロボット駆動科学。
- 生命科学との接点：生命科学、生物学、バイオインフォマティクス、創薬AI、バイオサイバネティクス。

物性化学・分子工学・熱力学・半導体・材料力学は物理編の既存ノートを参照し、原文を複製していません。本文を確認した候補のうち、Design Informaticsは機械設計・CADへのリンク、Process Intelligenceは業務プロセスへのリンクが中心だったため、今回の化学編には含めていません。生物学的安全保障や一般的なAI駆動研究まで関連リンクを無制限に広げてはいません。

全プロジェクト内のすべての化学的言及を網羅したという意味ではありません。対象ページが指す外部の本・論文・Web記事の全文取得でもありません。

## 思考と来歴の保存

原文テキストには空行や未完の文を含む全行を保存しました。Markdownでは段落の字下げやScrapboxリンクを整形し、原文の行へ戻れるアンカーと行対応を付けています。ページ・行の更新日は取得時の情報であり、学習した日時や順序の証明には使いません。過去の全改訂履歴は未取得です。

「生命科学」の授業を見返した感想は、本人の記録として明示しました。一方、高校化学の学習方針は教材由来か本人の表現か未同定です。講義案内、書籍の章立て、SNSの紹介文、シンポジウム主催者の挨拶を本人の独自の発言や参加・読了記録に置き換えていません。短い資料リストは、当時集めていた入口として残しました。

12ページすべてに、導入・訂正・新しい読み方のいずれかを「AIによる補足・訂正」として追加しました。[反応の向きと速さ](reaction-direction-and-rate.md)も今回AIが作成した説明ノートです。すべてstatusはdraftで、人による確認済みとはしていません。

## 補足した主な点

原文の語句は訂正せず、以下を別の節に記しています。

- [高校化学](foundations/high-school-chemistry.md#ai-notes)：電子配置、電気陰性度の尺度、共有結合、水溶性からの過度な一般化、反応速度と平衡、pHと活量、緩衝液の近似、沈殿と酸化還元の区別、4配位錯体、電極反応、ジアステレオマー、ヒドロホウ素化、芳香族求電子置換、アミド。
- [材料工学](materials-informatics/materials-engineering.md#ai-notes)：成分・組織・製造プロセスを数式の積とみなさず、材料選択の条件として読む。
- [ケモインフォマティクス](materials-informatics/cheminformatics.md#ai-notes)：同じ分子式と同じ構造の違い、SMILESと分子グラフ。
- [マテリアルズインフォマティクス](materials-informatics/materials-informatics.md#ai-notes)：材料の予測・生成・実験の区別、CellOracleの生命科学への位置付け。
- [Process Informatics](materials-informatics/process-informatics.md#ai-notes)：反応器の規模と輸送現象、モデル・データの違い。
- [創薬AI](life-sciences/ai-drug-discovery.md#ai-notes)：構造予測と分子の動力学・測定結果の区別。
- [生命科学](life-sciences/life-sciences.md#ai-notes)：代謝と自由エネルギー、平衡と定常状態の違い。

確認に使った資料は各補足の近くと[参考資料](../references/yuyannnn-scrapbox-chemistry.md)に記しました。高校化学には個別の反応条件や機構の未確認箇所がまだあり、末尾に該当行を挙げています。すべての主張・教材・論文を校閲済みではありません。

## 残した欠落・曖昧さ

- 取得した12ページにはU+FFFCの埋め込み欠落記号はありません。画像を含む全内容の完全保存を保証するものではありません。
- 生物学[L10](life-sciences/biology.md#source-L10)の画像は、実際に表示して読書マップであることを確認しました。作者・利用条件は未同定のため、元URLへのリンクを残し、画像のコピーは公開していません。外部画像が将来消えると、リポジトリだけでは復元できません。
- 高校化学[L203](foundations/high-school-chemistry.md#source-L203)の速度式に「スパコン・高性能プログラミング・FEM・CAE」というリンクラベルが混入しています。意図した化学種は復元せず、原文と補足の一般式を分けました。
- 創薬AI[L7](life-sciences/ai-drug-discovery.md#source-L7)の「分子動力学シミュレーション」は取得時カタログに見つかりませんでした。上記の混入ラベルとともにmanifestの未解決リンク欄に記録しています。
- ケモインフォマティクス[L36](materials-informatics/cheminformatics.md#source-L36)のURLと文の連結、生命科学[L41](life-sciences/life-sciences.md#source-L41)の書きかけ、原文の誤字や改ページ文字も保存しています。

## 検証方法

~~~sh
python3 scripts/import_scrapbox_chemistry.py --check
~~~

公開ファイルだけで、原文・移植本文のチェックサム、1,239行の対応、ローカルリンクを確認できます。ローカルに取得時のAPI応答があれば、原文・再変換した本文との一致も追加確認します。数学・物理と同じ変換器を利用し、本人の手編集を検出した場合は再生成を停止します。

公開ファイルのみの一時コピーでも数学・物理・化学の検証が通ることを確認しました。化学の原文・移植本文を意図的に壊すと検出され、本人の追記があると再生成が停止することも確認しています。Markdown解析で意図しないコードブロックがないこと、説明ノートの数値例で初期値・物質収支・微分方程式への代入が整合することを確認しました。

再生成にはinbox/scrapbox/2026-09-20/chemistry-full/の取得データが必要です。対象と補足は[scripts/chemistry_import_content.py](../scripts/chemistry_import_content.py)、入口は[scripts/import_scrapbox_chemistry.py](../scripts/import_scrapbox_chemistry.py)です。GitHub Actionsにも化学の検証を追加しました。

[化学の入口へ](README.md) · [原文一覧](sources/README.md)
