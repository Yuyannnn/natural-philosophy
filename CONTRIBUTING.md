# 修正の提案について

誤りの指摘や、理解を深める資料の紹介を歓迎します。IssueまたはPull Requestに、対象のノート・該当箇所・修正の理由を記してください。数式や定義の訂正には、前提条件と根拠となる資料の章・節、または計算を添えると確認しやすくなります。

## 過去の記録を修正するとき

移植ノートの「当時の本文」と `math/sources/`・`physics/sources/`・`chemistry/sources/` は、疑問や誤解も含む当時の記録です。内容上の訂正や新しい理解は別の節に追記し、原文を上書きしません。変換処理そのものの不具合は、原文との差分を示して修正します。

本人の経験や学習順序を推測で書き足さず、AIによる説明はその旨を明記します。詳しくは[執筆ガイド](docs/writing.md)と[取り込みガイド](docs/importing.md)を参照してください。

## 変更後の確認

Python 3.10以上で、リポジトリのルートから実行できます。追加パッケージやネット接続は不要です。

```sh
python3 scripts/import_scrapbox_math.py --check
python3 scripts/import_scrapbox_physics.py --check
python3 scripts/import_scrapbox_chemistry.py --check
python3 -m unittest discover -s tests
python3 examples/change_of_basis.py
python3 examples/oscillator_energy.py
```

新しいノートには出典と関連リンクを添え、分野の索引にも追加してください。`status: reviewed` は内容と出典を人が確認した場合だけ使います。

継続的な更新は[壁打ちと更新の手順](docs/learning-workflow.md)を参照してください。説明は既存ノートで育て、[次に考える問い](learning/README.md)には再開場所を短く残します。
