---
title: "振動波動論"
status: draft
tags: [scrapbox, mechanics-waves]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E6%8C%AF%E5%8B%95%E6%B3%A2%E5%8B%95%E8%AB%96"
source_created: "2023-01-18T11:04:20Z"
source_updated: "2025-06-29T10:45:55Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 振動波動論

単振動から連成振動・波動方程式・場の理論へ進む講義項目。

原ページ作成：2023-01-18 ／ 最終更新：2025-06-29（UTC、取得時点）

[物理学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/oscillations-and-waves.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E6%8C%AF%E5%8B%95%E6%B3%A2%E5%8B%95%E8%AB%96)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<details>
<summary>本文の見出しから探す</summary>

- [1. 序論](#source-L23)
- [2. 1自由度系の振動 ](#source-L25)
- [3. 連成振動 ](#source-L32)
- [4. 1次元の波動 ](#source-L37)
- [5. フーリエ級数，変換の方法　](#source-L45)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 振動波動論

<a id="source-L2"></a>[ネットワーク](https://scrapbox.io/MistMavGamer/%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF)  
<a id="source-L3"></a>[情報通信工学](https://scrapbox.io/MistMavGamer/%E6%83%85%E5%A0%B1%E9%80%9A%E4%BF%A1%E5%B7%A5%E5%AD%A6)  
<a id="source-L4"></a>[フーリエ変換とラプラス変換](../../math/analysis/fourier-and-laplace-transforms.md)  
<a id="source-L5"></a>[関数解析](../../math/analysis/functional-analysis.md)  
<a id="source-L6"></a>[複素解析](../../math/analysis/complex-analysis.md)  
<a id="source-L7"></a>[常微分方程式](../../math/analysis/ordinary-differential-equations.md)  
<a id="source-L8"></a>[偏微分方程式](../../math/analysis/partial-differential-equations.md)  
<a id="source-L9"></a>[スペクトル分析](https://scrapbox.io/MistMavGamer/%E3%82%B9%E3%83%9A%E3%82%AF%E3%83%88%E3%83%AB%E5%88%86%E6%9E%90)  



<a id="source-L13"></a>力学を物質点に用いて、連続体にする  

<a id="source-L15"></a>音や光は我々が生存してゆく上で決定的に重要な情報を担い，音楽，美しい景色，絵画，写真と生活に喜びを与えてくれる．  
<a id="source-L16"></a>音と光は共に波動現象の典型例であるが，我々の知的興味を引き付ける振動・波動現象は身近なところに数多く存在する．  
<a id="source-L17"></a>たとえば，ブランコはどうして漕げるのだろうかとか，海の波はどうして波打ち際で砕けるのだろうかなど．  
<a id="source-L18"></a>また，建造物や製品の設計においても，振動・波動の影響は欠かせない．  
<a id="source-L19"></a>このように我々の日常と密接に関わっている振動・波動現象を，物理学の基本法則により根本的に理解することがこの講義の目的である．  
<a id="source-L20"></a>その内容は古典的な場の理論の初歩を含み，引き続き量子力学，場の量子論を学ぶ者にとっては必須なものでもある．  
<a id="source-L21"></a>主な項目は以下の通りであるが，実際の内容や順序は教員によって多少の違いがあり、特に＊印のついた項目は省略される場合がある．  


<a id="source-L23"></a>

### 1. 序論



<a id="source-L25"></a>

### 2. 1自由度系の振動 

> <a id="source-L26"></a>・単振動  
> <a id="source-L27"></a>・減衰振動  
> <a id="source-L28"></a>・強制振動，共鳴，Q値  
> <a id="source-L29"></a>＊パラメーター励振  
> <a id="source-L30"></a>＊簡単な非線形振動  


<a id="source-L32"></a>

### 3. 連成振動 

> <a id="source-L33"></a>・2自由度系　  
> <a id="source-L34"></a>・基準振動，うなり  
> <a id="source-L35"></a>・N自由度系  


<a id="source-L37"></a>

### 4. 1次元の波動 

> <a id="source-L38"></a>・弦，弾性体，気柱　  
> <a id="source-L39"></a>・縦波と横波　  
> <a id="source-L40"></a>・波動方程式　  
> <a id="source-L41"></a>・反射と透過  
> <a id="source-L42"></a>＊波のエネルギー  
> <a id="source-L43"></a>＊インピーダンス  


<a id="source-L45"></a>

### 5. フーリエ級数，変換の方法　

> <a id="source-L46"></a>・考え方，基本事項，線形性　  
> <a id="source-L47"></a>・波束　  
> <a id="source-L48"></a>・位相速度と群速度   
> <a id="source-L49"></a>＊不確定性関係  

<a id="source-L51"></a>＊6. 2，3次元の波　  

> <a id="source-L52"></a>＊波動方程式　  
> <a id="source-L53"></a>＊平面波   
> <a id="source-L54"></a>＊球面波　  
> <a id="source-L55"></a>＊水の表面波   
> <a id="source-L56"></a>＊反射と屈折  
> <a id="source-L57"></a>＊干渉，回折  



<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

離散的な質点系と連続体をつなぐときは、何を連続極限にするかを明示したい。小振幅の一様な弦なら、張力 $T$、線密度 $\mu$ に対して波の速さは $c=\sqrt{T/\mu}$。$T$ はN、$\mu$ はkg/mなので、$c$ はm/sになる。線形近似のもとで重ね合わせやモード分解が使える。確認資料：[Feynman I-47](https://www.feynmanlectures.caltech.edu/I_47.html)。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [フーリエ変換とラプラス変換](../../math/analysis/fourier-and-laplace-transforms.md)
- [関数解析](../../math/analysis/functional-analysis.md)
- [複素解析](../../math/analysis/complex-analysis.md)
- [常微分方程式](../../math/analysis/ordinary-differential-equations.md)
- [偏微分方程式](../../math/analysis/partial-differential-equations.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
