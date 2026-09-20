---
title: "非平衡熱力学"
status: draft
tags: [scrapbox, thermal-statistical]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E9%9D%9E%E5%B9%B3%E8%A1%A1%E7%86%B1%E5%8A%9B%E5%AD%A6"
source_created: "2023-08-05T08:26:06Z"
source_updated: "2024-10-19T07:32:43Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 非平衡熱力学

ゆらぎ・学習・拡散モデル・最適輸送をつなぐ資料の収集。

原ページ作成：2023-08-05 ／ 最終更新：2024-10-19（UTC、取得時点）

[物理学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/nonequilibrium-thermodynamics.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E9%9D%9E%E5%B9%B3%E8%A1%A1%E7%86%B1%E5%8A%9B%E5%AD%A6)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 非平衡熱力学

<a id="source-L2"></a>[scrapboxまとめ(物理)](../learning-paths/original-physics-index.md)  
<a id="source-L3"></a>[熱力学](thermodynamics.md)  
<a id="source-L4"></a>[情報熱力学](information-thermodynamics.md)  
<a id="source-L5"></a>[非平衡開放系の物理](open-systems.md)  
<a id="source-L6"></a>[統計力学](statistical-mechanics.md)  
<a id="source-L7"></a>[熱&amp;伝熱工学](heat-transfer.md)  
<a id="source-L8"></a>[Diffusion Model](https://scrapbox.io/MistMavGamer/Diffusion%20Model)  
<a id="source-L9"></a>[最適輸送](../../math/optimization-computation/optimal-transport.md)  



> <a id="source-L13"></a>Workshop on Stochastic Thermodynamics - WOST IV | (smr 3837)  

<a id="source-L14"></a><https://indico.ictp.it/event/10171>  



> <a id="source-L18"></a>ゆらぐ系の熱力学  

<a id="source-L19"></a><https://www.amazon.co.jp/ゆらぐ系の熱力学-非平衡統計力学の発展-SGCライブラリ-齊藤-圭司/dp/4781915639>  



> <a id="source-L23"></a>量子エンタングルメントから創発する宇宙 (基本法則から読み解く物理学最前線)   

<a id="source-L24"></a><https://www.amazon.co.jp/量子エンタングルメントから創発する宇宙-基本法則から読み解く物理学最前線-須藤-彰三/dp/4320035437>  


> <a id="source-L27"></a>ゆらぎの定理@東京理科大学  

<a id="source-L28"></a>[https://www.youtube.com/watch?v=FDPqRyJbM5s](<https://www.youtube.com/watch?v=FDPqRyJbM5s>)  



> <a id="source-L32"></a>大規模複雑ネットワークの非平衡熱力学を切り開く―非対称イジング模型のエントロピー生成の厳密解導出に成功―  

<a id="source-L33"></a><https://www.kyoto-u.ac.jp/ja/research-news/2023-06-27>  



> <a id="source-L37"></a>深層学習の学習過程における相転移  

<a id="source-L38"></a><http://www-adsys.sys.i.kyoto-u.ac.jp/mohzeki/Presentation/Tokyo20150826.pdf>  



> <a id="source-L42"></a>生成モデルは世界をどのように理解しているのか  

<a id="source-L43"></a><https://hillbig.github.io/ISM_Symposium2023_generativemodel_okanohara.pdf>  



> <a id="source-L47"></a>拡散モデルとその周辺  

<a id="source-L48"></a><https://hillbig.github.io/WorkshopOT2023_diffusion_okanohara.pdf>  


> <a id="source-L51"></a>Deep Unsupervised Learning using Nonequilibrium Thermodynamics  

<a id="source-L52"></a><https://proceedings.mlr.press/v37/sohl-dickstein15.pdf>  


> <a id="source-L55"></a>非平 衡定 常系 の 熱 力学 と統計 力 学 に む けて  

<a id="source-L56"></a><https://www.jstage.jst.go.jp/article/butsuri/63/10/63_KJ00005047211/_pdf>  







<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

ゆらぎ、学習過程、拡散モデルを同じ入口から見ようとした資料の収集として残す。生成モデルの確率過程と実物の熱・粒子の輸送を同一視せず、時間反転やエントロピーの定義をそろえて対応を考える。原文にある[Sohl-Dicksteinらの論文](https://proceedings.mlr.press/v37/sohl-dickstein15.html)は接点を確認する一次資料。今回確認したのは論文ページの概要である。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [scrapboxまとめ(物理)](../learning-paths/original-physics-index.md)
- [熱力学](thermodynamics.md)
- [情報熱力学](information-thermodynamics.md)
- [非平衡開放系の物理](open-systems.md)
- [統計力学](statistical-mechanics.md)
- [熱&amp;伝熱工学](heat-transfer.md)
- [最適輸送](../../math/optimization-computation/optimal-transport.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
