---
title: "量子情報"
status: draft
tags: [scrapbox, quantum]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E9%87%8F%E5%AD%90%E6%83%85%E5%A0%B1"
source_created: "2023-04-08T16:43:09Z"
source_updated: "2024-12-01T14:17:47Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 量子情報

量子情報・通信・計算の講義項目と、原理を整理するための資料。

原ページ作成：2023-04-08 ／ 最終更新：2024-12-01（UTC、取得時点）

[物理学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/quantum-information.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E9%87%8F%E5%AD%90%E6%83%85%E5%A0%B1)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 量子情報

<a id="source-L2"></a>[情報理論](../../math/information-discrete/information-theory.md)  
<a id="source-L3"></a>[量子力学](quantum-mechanics.md)  
<a id="source-L4"></a>[量子コンピュータ](quantum-computing.md)  


<a id="source-L7"></a>量子情報・量子計算の入門的講義を行う。近年、量子力学の原理を応用して従来不可能な情報処理や通信を実現する「量子情報処理」に注目が集まっている。その代表例は、盗聴を確実に検知できる量子暗号や、特定の計算を従来よりも高速に行う量子計算（量子コンピュータ）などである。本講義の前半では、様々な量子情報処理のベースとなる基礎概念や法則の理解を目的とする。後半では特に量子計算に焦点を当て、その構成要素やアルゴリズムについて学習する。  

<a id="source-L9"></a>第1部 量子情報理論  

> <a id="source-L10"></a>(1)量子情報技術の歴史と現状。量子論の公理とその表現方法1  
> <a id="source-L11"></a>(2)量子論の公理とその表現方法2  
> <a id="source-L12"></a>(3)量子論の公理とその表現方法3  
> <a id="source-L13"></a>(4)いくつかの応用例  
> <a id="source-L14"></a>(5)量子論の非実在性と限界  
> <a id="source-L15"></a>(6)量子鍵配送  

<a id="source-L17"></a>第2部 量子計算  

> <a id="source-L18"></a>(1) 量子計算の歴史と現状  
> <a id="source-L19"></a>(2) 量子回路モデル  
> <a id="source-L20"></a>(3) 測定型量子計算モデル  
> <a id="source-L21"></a>(4) 量子フーリエ変換とショアのアルゴリズム  
> <a id="source-L22"></a>(5) グローバーのアルゴリズム  
> <a id="source-L23"></a>(6) 量子誤り訂正符号  
> <a id="source-L24"></a>(7) 量子コンピュータの物理的実装  


> <a id="source-L27"></a>Quantum Computation and Quantum Information, Nielsen&amp;Chuang  

<a id="source-L28"></a>代表的教科書らしい  


> <a id="source-L31"></a>Quantum Information Theory, Wilde  

<a id="source-L32"></a>量子シャノン理論の比較的最近の結果がよくまとまっているらしい  


> <a id="source-L35"></a>Quantum Algorithm Zoo  

<a id="source-L36"></a><https://quantumalgorithmzoo.org/>  
<a id="source-L37"></a>計算的な量子アルゴリズム  


> <a id="source-L40"></a>Quantum protocol zoo  

<a id="source-L41"></a><https://wiki.veriqloud.fr/index.php?title=Clifford_Code_for_Quantum_Authentication>  


> <a id="source-L44"></a>”新版 量子光学と量子情報科学”  

<a id="source-L45"></a>連続量自由度(CV)を用いた量子光学の系について  


> <a id="source-L48"></a>Protocol Library  

<a id="source-L49"></a><https://wiki.veriqloud.fr/index.php?title=Protocol_Library>  


> <a id="source-L52"></a>量子技術高等教育拠点  

<a id="source-L53"></a><https://qacademy.jp/>  


> <a id="source-L56"></a>QEd(講義動画+サマースクール）  

<a id="source-L57"></a><https://www.sqei.c.u-tokyo.ac.jp/qed/>  


> <a id="source-L60"></a>量子コンピュータ授業  量子コンピュータの歴史  

<a id="source-L61"></a>[https://www.youtube.com/watch?v=wBilQWKd1yU](<https://www.youtube.com/watch?v=wBilQWKd1yU>)  




> <a id="source-L66"></a>20世紀前半  

<a id="source-L67"></a>古典的発想だと実験事実が理論で再現できない  
<a id="source-L68"></a>- 黒体輻射  
<a id="source-L69"></a>- 光電効果  

<a id="source-L71"></a>コペンハーゲン解釈：予想が確率的になるのを受け入れましょう  

<a id="source-L73"></a>量子力学の数学的基礎：john von neumann  

<a id="source-L75"></a>einstein-podolsky-rosen paradox：量子論はまともな理論が持ってほしい性質を持たない  

<a id="source-L77"></a>lmab shift：場の量子論、繰り込み  

<a id="source-L79"></a>bellの不等式：検証が2022年ノー別物理学賞、局所実在論で物理が記述できないことを実験で示す方法の提案  

<a id="source-L81"></a>bellの不等式の破れの検証実験：破れている！！  

<a id="source-L83"></a>量子力学の不可思議な性質を逆手にとった応用が提案されるようになってきた  
<a id="source-L84"></a>- 量子鍵配送  
<a id="source-L85"></a>- 素因数分解  

<a id="source-L87"></a>昔と今の違い  
<a id="source-L88"></a>- 測定理論が整備(POVM, CPTP map etc..)  
<a id="source-L89"></a>- 実験技術が進んで非古典的状態の生成、制御、観測ができるように  

<a id="source-L91"></a>性質を応用するには？  
<a id="source-L92"></a>- どのような原理に則っているのかの整理が必要  
<a id="source-L93"></a>- さまざまな類型になれていく  

<a id="source-L95"></a>量子計算  
<a id="source-L96"></a>- 量子アルゴリズム  
<a id="source-L97"></a>- 量子エラー訂正  
<a id="source-L98"></a>- 計算複雑性  
<a id="source-L99"></a>- 量子シミュレーター  
<a id="source-L100"></a>- 量子アニーリング  
<a id="source-L101"></a>- 評価手法  

<a id="source-L103"></a>量子通信  
<a id="source-L104"></a>- 量子shannon理論  
<a id="source-L105"></a>- 量子あんごう  
<a id="source-L106"></a>- 量子インターネット  

<a id="source-L108"></a>量子sensing metrology  
<a id="source-L109"></a>- 標準量子限界を超える測定  
<a id="source-L110"></a>- 量子系を使っていて感度がよければなんでも  

<a id="source-L112"></a>その他  
<a id="source-L113"></a>- 量子推定理論  
<a id="source-L114"></a>- リソース理論  
<a id="source-L115"></a>- 量子制御理論  
<a id="source-L116"></a>- 量子熱力学  
<a id="source-L117"></a>- hamiltonian engineering  
<a id="source-L118"></a>- 量子基礎論  
<a id="source-L119"></a>- 高エネルギー、物性応用  
<a id="source-L120"></a>- 量子情報幾何  



<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

情報の担体、操作、測定、通信相手のモデルを分ける。「盗聴を確実に検知」という講義紹介を実機の無条件の保証とは扱わない。量子鍵配送でもプロトコルの仮定、実装、有限の測定データ、認証を含めて評価する。講義項目と、引用された社会的・歴史的な説明は、根拠を確認する対象として残す。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [情報理論](../../math/information-discrete/information-theory.md)
- [量子力学](quantum-mechanics.md)
- [量子コンピュータ](quantum-computing.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
