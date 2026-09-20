---
title: "確率過程"
status: draft
tags: [scrapbox, probability-statistics]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E7%A2%BA%E7%8E%87%E9%81%8E%E7%A8%8B"
source_created: "2023-01-21T18:34:10Z"
source_updated: "2025-08-01T03:36:19Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# 確率過程

時間とともに変化する不確実性を、マルチンゲールなどで捉える記録。

原ページ作成：2023-01-21 ／ 最終更新：2025-08-01（UTC、取得時点）

[数学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/stochastic-processes.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E7%A2%BA%E7%8E%87%E9%81%8E%E7%A8%8B)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

<details>
<summary>本文の見出しから探す</summary>

- [「数理手法3」](#source-L14)
- [第1講 集合と写像](#source-L32)
- [第2講 離散型確率空間の基礎](#source-L37)
- [第3講 部分加法族の性質や可測の定義](#source-L43)
- [第4講 離散的確率空間のマルチンゲール理論](#source-L46)
- [第5講](#source-L49)
- [第6講](#source-L55)
- [第7講](#source-L60)
- [第8講](#source-L65)
- [第9講](#source-L69)
- [第10講](#source-L72)
- [「数理手法Ⅵ」](#source-L130)
- [「ブラックショールズ方程式への道」](#source-L168)

</details>

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### 確率過程

<a id="source-L2"></a>[確率](probability.md)  
<a id="source-L3"></a>\[機械学習によく出てくる確率統計的な知識\]  
<a id="source-L4"></a>[確率ロボティクス](https://scrapbox.io/MistMavGamer/%E7%A2%BA%E7%8E%87%E3%83%AD%E3%83%9C%E3%83%86%E3%82%A3%E3%82%AF%E3%82%B9)  
<a id="source-L5"></a>[Poker](https://scrapbox.io/MistMavGamer/Poker)  
<a id="source-L6"></a>[金融マーケット攻略ゲーム](https://scrapbox.io/MistMavGamer/%E9%87%91%E8%9E%8D%E3%83%9E%E3%83%BC%E3%82%B1%E3%83%83%E3%83%88%E6%94%BB%E7%95%A5%E3%82%B2%E3%83%BC%E3%83%A0)  
<a id="source-L7"></a>[集合と位相](../foundations/sets-and-topology.md)  
<a id="source-L8"></a>[統計的機械学習](statistical-machine-learning.md)  


<a id="source-L11"></a>確率過程論  
<a id="source-L12"></a>Stochastic process  


<a id="source-L14"></a>

### 「数理手法3」


<a id="source-L16"></a><https://ocw.u-tokyo.ac.jp/course_11395/>  

<a id="source-L18"></a>時間とともに変化する不確実な現象を記述し理解するには、確率過程論が重要な道具として用いられる。この講義では離散時間の確率過程論、特にマルチンゲール理論に関しての講義を行う。この講義では、測度論や積分論等の数学の専門的知識は前提とせず、とくに前半では確率空間が有限集合である場合を取り扱う。  

<a id="source-L20"></a>１．基礎的準備：集合と写像  
<a id="source-L21"></a>２．離散型確率空間の基礎  
<a id="source-L22"></a>３．離散型確率空間のマルチンゲール理論  
<a id="source-L23"></a>４．一般の確率空間  
<a id="source-L24"></a>５．積分の定義と収束定理  
<a id="source-L25"></a>６．一般のマルチンゲール理論  







<a id="source-L32"></a>

### 第1講 集合と写像

<a id="source-L33"></a>独立を仮定できないような現象にマルチンゲール理論が使われる。  
<a id="source-L34"></a>冪集合：Aの部分集合全体の集合族  



<a id="source-L37"></a>

### 第2講 離散型確率空間の基礎

<a id="source-L38"></a>写像として確率の定義  
<a id="source-L39"></a>根元集合、根元集合の冪集合、冪集合からの写像を合わせて確率空間という。  
<a id="source-L40"></a>確率変数とは根元事象からの写像を表す。  



<a id="source-L43"></a>

### 第3講 部分加法族の性質や可測の定義




<a id="source-L46"></a>

### 第4講 離散的確率空間のマルチンゲール理論




<a id="source-L49"></a>

### 第5講

<a id="source-L50"></a>条件付き期待値の性質  
<a id="source-L51"></a>フィルとレーション  
<a id="source-L52"></a>マルチンゲールの定義  



<a id="source-L55"></a>

### 第6講

<a id="source-L56"></a>マルチンゲール変換  
<a id="source-L57"></a>任意停止定理  



<a id="source-L60"></a>

### 第7講

<a id="source-L61"></a>確率過程  
<a id="source-L62"></a>一般の確率空間の基礎  



<a id="source-L65"></a>

### 第8講

<a id="source-L66"></a>測度と積分  



<a id="source-L69"></a>

### 第9講

<a id="source-L70"></a>可積分性やLebesque積分  


<a id="source-L72"></a>

### 第10講

<a id="source-L73"></a>誘拐収束定理など  





<a id="source-L79"></a>———————————メモ------------------  

<a id="source-L81"></a>確率論において、マルチンゲールとは確率過程の性質の１つである、過去の情報に制限して計算した期待値と未来の期待値が同一になる性質である。この性質は公平な賭け事を行なっている時の持ち金の変異に現れるものだと考えられており、マルチンゲールという名前も賭けにおける戦略から取られたものである。数学的には情報は情報増大系で与えられ、未来における期待値はこの情報による条件付期待値となる。  

<a id="source-L83"></a>マルチンゲールの定義は、Ft可測、可積分、条件付期待値の条件である。  
<a id="source-L84"></a>戦略を変更することをマルチンゲール変換といい、実行可能な戦略によるマルチンゲール変換によって得られる確率過程もマルチンゲールになることが知られている。  

<a id="source-L86"></a>停止時刻：停止時刻はかけをやめる時刻を数学的に定式化したものである。  

<a id="source-L88"></a>任意抽出定理：  


<a id="source-L91"></a>動画版授業  

<a id="source-L93"></a>1講 はじめに  
<a id="source-L94"></a>測度論がむずいので確率論になる前につまづいてしまうことがある  
<a id="source-L95"></a>この講義では、測度論を誤魔化す  
<a id="source-L96"></a>確率論のアイデアを中心にする  

<a id="source-L98"></a>数学の世界では、確率過程論の重要なエッセンスがマルチンゲールの理論に入っている  
<a id="source-L99"></a>マルチンゲールは人工的なもの  



<a id="source-L103"></a>2講 確率論の基礎1  

<a id="source-L105"></a>3講 確率論の基礎2  

<a id="source-L107"></a>4講 条件付き期待値  

<a id="source-L109"></a>5講 マルチンゲール理論1  

<a id="source-L111"></a>6講 マルチンゲール理論2  

<a id="source-L113"></a>7講 マルチンゲール理論3  

<a id="source-L115"></a>8講 マルチンゲール理論4・測度論からの準備1  

<a id="source-L117"></a>9講 測度論からの準備2  

<a id="source-L119"></a>10講 測度論的確率論  

<a id="source-L121"></a>11講 応用1  

<a id="source-L123"></a>12講 応用2  

<a id="source-L125"></a>13講 試験問題  


<a id="source-L128"></a>—————————————————————————————————————————————————————————————————  


<a id="source-L130"></a>

### 「数理手法Ⅵ」


<a id="source-L132"></a><https://ocw.u-tokyo.ac.jp/course_11403/>  

<a id="source-L134"></a>1講 測度論からの準備  
<a id="source-L135"></a>確立微分方程式の入門  
<a id="source-L136"></a>積分論などはあまり厳密にやることはない  

<a id="source-L138"></a>最初の難関はブラウン運動  

<a id="source-L140"></a>2講 測度論的確率論  

<a id="source-L142"></a>3講 ブラウン運動1  

<a id="source-L144"></a>4講 ブラウン運動2  

<a id="source-L146"></a>5講 ブラウン運動3  

<a id="source-L148"></a>6講 連続マルチンゲール  

<a id="source-L150"></a>7講 確率積分1  

<a id="source-L152"></a>8講 確率積分2  

<a id="source-L154"></a>9講 確率積分3  

<a id="source-L156"></a>10講 伊藤の公式1  

<a id="source-L158"></a>11講 伊藤の公式2  

<a id="source-L160"></a>12講 伊藤の公式の応用  

<a id="source-L162"></a>13講 確率微分方程式の拡張  



<a id="source-L166"></a>——————————————————————————————————————————————  


<a id="source-L168"></a>

### 「ブラックショールズ方程式への道」


<a id="source-L170"></a><https://www.youtube.com/watch?v=NE1W0wJH8q8>  

<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

確率過程 $(X_t)$ だけでなく、時刻 $t$ までの情報を表す族 $(\mathcal F_t)$ も記すと、マルチンゲールの意味が明確になる。離散時間では、適合性と可積分性のもとで $\mathbb E[X_{t+1}\mid\mathcal F_t]=X_t$ が条件。これは各時刻の値が独立という意味ではない。元メモの「独立を仮定できない現象」への関心につながる区別になる。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [確率](probability.md)
- [集合と位相](../foundations/sets-and-topology.md)
- [統計的機械学習](statistical-machine-learning.md)

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
