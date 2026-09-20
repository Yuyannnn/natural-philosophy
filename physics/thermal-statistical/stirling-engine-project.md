---
title: "スターリングエンジンを0から作る備忘録"
status: draft
tags: [scrapbox, thermal-statistical]
created: 2026-09-20
updated: 2026-09-20
source: "https://scrapbox.io/MistMavGamer/%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%AA%E3%83%B3%E3%82%B0%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%B3%E3%82%920%E3%81%8B%E3%82%89%E4%BD%9C%E3%82%8B%E5%82%99%E5%BF%98%E9%8C%B2"
source_created: "2023-01-20T03:05:35Z"
source_updated: "2023-02-12T06:46:36Z"
imported: 2026-09-20
provenance: imported-with-separate-ai-notes
---

# スターリングエンジンを0から作る備忘録

手を動かしていて製作メモが残らなかった、という言葉と周辺の実習記録。

原ページ作成：2023-01-20 ／ 最終更新：2023-02-12（UTC、取得時点）

[物理学の入口](../README.md) · [当時の本文](#original) · [AIによる補足](#ai-notes) · [原文テキスト](../sources/stirling-engine-project.txt) · [Scrapbox](https://scrapbox.io/MistMavGamer/%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%AA%E3%83%B3%E3%82%B0%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%B3%E3%82%920%E3%81%8B%E3%82%89%E4%BD%9C%E3%82%8B%E5%82%99%E5%BF%98%E9%8C%B2)

本文は当時の言葉・並び・疑問を残した移植です。講義・読書由来の記述や過去のAI回答も含み、すべてを本人の独自の考察や確認済みの事実とは扱いません。冒頭の案内と末尾の補足は今回AIが追加しました。

## 思考の手がかり

> と思ったが、こればかりはずっと手を動かしていたので、メモがなかった・・

[本文の該当箇所へ](#source-L3)

<a id="original"></a>

## 当時の本文

原文の字下げは引用段落の深さで表しています。順序はページ内の並びであり、学習した日時順を保証するものではありません。

<!-- BEGIN IMPORTED BODY: preserve historical wording -->
<a id="source-L1"></a>

### スターリングエンジンを0から作る備忘録


> <a id="source-L3"></a>と思ったが、こればかりはずっと手を動かしていたので、メモがなかった・・  

<a id="source-L5"></a>物体周りの流れ  
<a id="source-L6"></a>揚力と抗力は積分によって求める  
<a id="source-L7"></a>翼を囲む空間について運動量保存を考えても揚力はわかる  
<a id="source-L8"></a>揚力係数、抗力係数、モーメント係数、レイノルズ数など  


<a id="source-L11"></a>電子回路1(デジタル回路)  
<a id="source-L12"></a>ブレッドボードは小型の電子部品を用いた電子回路の施策にとても便利に作られています。  
<a id="source-L13"></a>ステッピングモータはパルス信号で一定角度ずつ高精度に回転するモータである。  


<a id="source-L16"></a>電子回路2(アナログ回路)  
<a id="source-L17"></a>連続的な信号であるアナログ信号を取り扱う回路をアナログ回路という。本演習では、メカトロニクスにおける自動制御機構に採用されているサーボ機構を設計・製作する。  
<a id="source-L18"></a>反転増幅器、積分・微分演算増幅器、演算増幅器、  
<a id="source-L19"></a>てすたの使い方、  


<a id="source-L22"></a>感温結晶を用いた温度の可視化計測  


<a id="source-L25"></a>Easy-σによる応力解析  
<a id="source-L26"></a>有限要素法では、同じ線の問題をメッシュの領域に分割し、変形を近似的にとく。  


<a id="source-L29"></a>ガスエンジンの性能  


<a id="source-L32"></a>計算機演習  

<a id="source-L34"></a>・バトルシップ  
<a id="source-L35"></a>コマンド  
<a id="source-L36"></a>cp main.c main2.c:main.cをmain2.cにコピー  
<a id="source-L37"></a>cp main main2 -r:mainというディレクトリをmain2というディレクトリにコピー  
<a id="source-L38"></a>less main.c:main.cの中身を見る  
<a id="source-L39"></a>Grep “”int” \*.c    
<a id="source-L40"></a>リバースエンジニアリング  
<a id="source-L41"></a>C言語コンパイルの流れ:プリプロセス→コンパイル→アセンブル→リンク  
<a id="source-L42"></a>ファイルの流れ:ソースファイル→アセンブラソースファイル→オブジェクトファイル→バイナリファイル  
<a id="source-L43"></a>プリプロセス:マクロの展開や#includeなどの直接的な処理が行われる、.iファイルができる  
<a id="source-L44"></a>（狭義の）コンパイル:プリプロセスが終わったらコンパイルでアセンブラに変換される  
<a id="source-L45"></a>デバッグオプションをつけるとファイルの大きさが膨れあがる、.sファイルができる  
<a id="source-L46"></a>アセンブル:狭義のコンパイルで得たファイルをアセンブルしてバイナリのオブジェクトファイルを生成する  
<a id="source-L47"></a>Objdumpやreadelfコマンドで詳細を確認できる、.oファイルができる  
<a id="source-L48"></a>リンク:必要なライブラリとの結合を行なって実行可能な形式のファイルを生成する処理  
<a id="source-L49"></a>Lddで依存ライブラリを確認できる、実行可能ファイルができる  


<a id="source-L52"></a>・MATLAB  
<a id="source-L53"></a>MatrixLaboratryの略で、行列計算などを行うためのプログラミング言語と実行環境である。  
<a id="source-L54"></a>Help コマンドで、コマンドの説明が表示される  
<a id="source-L55"></a>Edit \~.mでソースファイルを作成し、\~とコマンドプロンプトに入力すれば実行できる  
<a id="source-L56"></a>グラフの作成  
<a id="source-L57"></a>データの読み書き  
<a id="source-L58"></a>変数の定義  
<a id="source-L59"></a>関数の定義  
<a id="source-L60"></a>システム解析  


<a id="source-L63"></a>・MultiProgramming  
<a id="source-L64"></a>ロボット制御プログラムはアクチュエータを制御すると同時にセンサ情報も処理する必要があるので並列計算が必要になる。並列計算を容易に実現するOpenMPというライブラリがある。  
<a id="source-L65"></a>プロセスは別のメモリ空間が割り当てられているが、スレッドは同じメモリ空間を共有している。  
<a id="source-L66"></a>C言語では&lt;pthread.h&gt;をインクルードする。  
<a id="source-L67"></a>threadの同期にはpthread\_join  
<a id="source-L68"></a>スレッドによるデータの共有は簡単で、グローバル変数を用いれば良い  
<a id="source-L69"></a>一度に１つのスレッドしか共有データを操作できないようにする必要があり、コードのある部分で１つのスレっdpが他のすべてのスレッドを排除するので相互排除と呼ばれている。一度に１つのスレッドしか実行できないコード部分はクリティカルセクションと呼ばれる  
<a id="source-L70"></a>また、マルチスレッドはグローバル変数とスタティック変数に注意を払う必要がある。  
<a id="source-L71"></a>OpenMPは共有メモリ型計算機における並列処理をサポートするAPIである。  

<a id="source-L73"></a>プロセス間では、メモリ空間が異なるので単純に情報のやり取りをすることができない。マルチスレッドの場合、同一プロセス内での処理となるのでメモリ空間が共有されており、グローバル変数で情報の共有が可能であったが、プロセスの間では不可能なので、共有メモリを用いて情報共有を行う。  
<a id="source-L74"></a>Shmgetシステムコール：プロセスの共有メモリを作る  
<a id="source-L75"></a>Shmatシステムコール：共有メモリセグメントへの読み書きを許可する  
<a id="source-L76"></a>Shmdtシステムコール：共有メモリセグメントを取り外す  
<a id="source-L77"></a>Shmmctlシステムコール：共有メモリセグメントに関する情報の調査及び変更  

<a id="source-L79"></a>マルチプロセスでもレースコンディションが生じるため同期を行う必要があり、ここではセマフォを用いてプロセスの同期を取る。  
<a id="source-L80"></a>Semgetシステムコール：セマフォを作成  
<a id="source-L81"></a>Semctlシステムコール：セマフォを初期化  
<a id="source-L82"></a>Semopシステムコール：排他制御を行う  


<a id="source-L85"></a>・映像  
<a id="source-L86"></a>OpenGLは3Dグラフィクスのためのプログラムインタフェースである。  
<a id="source-L87"></a>OpenGLはハードウェアに依存しなインタフェースとして設計され散るので、コールバック関数等の機能はない。  
<a id="source-L88"></a>OpenGLはレンダリングパイプラインという一連の処理によって行われる。  
<a id="source-L89"></a>glClear:画面をクリア  
<a id="source-L90"></a>glFlush():バッファリングされている描画コマンドをすべてサーバに送る  
<a id="source-L91"></a>glutInit:GLUTの初期化を行う  
<a id="source-L92"></a>glutInitWindowsPosition,glutInitWindowSize:ウィンドウの開く位置や大きさを指定  
<a id="source-L93"></a>glutInitDisplayMode:ウィンドウ表示モードの初期化  
<a id="source-L94"></a>glutCreateWindow：OpenGLノウィンドウを初期化して開く  
<a id="source-L95"></a>glutPostRedisplay：カレントウィンドウの再描画が必要であるということをマーキングする  
<a id="source-L96"></a>glutMainLoop：イベント処理の無限ループに入る  

<a id="source-L98"></a>図形の描画  
<a id="source-L99"></a>OpenGLでは点・線分・ポリゴンという幾何学的プリミティブ群から必要なモデルを構築する必要がある。  

<a id="source-L101"></a>glut関数  
<a id="source-L102"></a>Glutライブラリには複数の幾何学シェープを生成するためのルーチンがいくつか用意されている。  

<a id="source-L104"></a>イベント処理  
<a id="source-L105"></a>入力イベントを処理するにはウィンドウを作成した後、メインループに入る前に次のルーチンを使用してコールバック関数を登録することが必要である。  
<a id="source-L106"></a>glutDisplayfunc：ウィンドウの内容を再描画する必要がある場合に呼び出す関数を指定する。  
<a id="source-L107"></a>glutReshapeFunc：ウィンドウをサイズ変更、または移動した時呼び出す関数を指定する。  
<a id="source-L108"></a>glutKeyboardFunc：ASCII文字を生成するキーを押した時に呼び出す関数funcを指定する。  
<a id="source-L109"></a>glutMousefunc：マウスボタンを押したり離したりした時に呼び出す関数funcを指定する  
<a id="source-L110"></a>glutMotionfunc：最低１つのマウスボタンを押している間にウィンドウ内でマウスポインタが移動した時に呼び出す関数を指定する  
<a id="source-L111"></a>glutPostRedisplay：現在のウィンドウを再描画が必要なものとしてマークする。  
<a id="source-L112"></a>GlutIdleFunc：他に未処理のイベントがない場合に実行する関数funcを指定する。  
<a id="source-L113"></a>アニメーション：OpenGLで動画を作成したい時は一秒間に何回も視点やモデルの１Dなどを変えてビュがしたものを切り替えることによって実現する  

<a id="source-L115"></a>コンセプトスケッチ  
<a id="source-L116"></a>描きやすい線の位置を見つけろ  
<a id="source-L117"></a>立方体は基本なので上手くかけるようになれ  
<a id="source-L118"></a>一点透視図、２点透視図、三点透視図を理解せよ  

<a id="source-L120"></a>マーカースケッチ  
<a id="source-L121"></a>短時間で頭の中のものを表現するためのもの  
<a id="source-L122"></a>同じ基本を理解しておけば共通言語になる  
<a id="source-L123"></a>物体を表現するための要素  
<a id="source-L124"></a>形、光源、影、素材、表面、色彩、表面の反射率、周りの環境  
<a id="source-L125"></a>基本的には形と影を書けば良い  
<a id="source-L126"></a>なぜマーカーかというと、スピード、色の安定、カラーバリエーションなどの展開である  
<a id="source-L127"></a>影はグラデーションで塗り分ける  
<a id="source-L128"></a>薄い方から塗る  

<a id="source-L130"></a>スケッチの三段階  
<a id="source-L131"></a>アイデアスケッチ  
<a id="source-L132"></a>テクニカルスケッチ  
<a id="source-L133"></a>プレゼンテーションスケッチ  

<a id="source-L135"></a>![元メモの画像](../assets/scrapbox/63e88b47371ae9001bf07546.png) ([画像の出典](<https://scrapbox.io/files/63e88b47371ae9001bf07546.png>))  



<!-- END IMPORTED BODY -->

<a id="ai-notes"></a>

## AIによる補足・訂正（2026-09-20）

「ずっと手を動かしていたので、メモがなかった」をそのまま残す。寸法の書き込みがある手描き図1点も保存した。ただし、図だけから製作手順・性能・完成状況を断定しない。後続の回路・熱計測・プログラミング・描画・スケッチの実習記録も、題名に合わないとして切り捨てない。追記するなら当時の記憶と新しく調べた理論を日付付きで分ける。

この補足は今回の整理で追加した導入・確認の観点です。元の本文全体の証明や出典を校閲済みという意味ではありません。

## つながる移植ノート

- [同じ分野のノート](README.md)：熱・統計・非平衡。

原文の来歴・欠落の一覧は[移植記録](../import-report.md)を参照してください。
