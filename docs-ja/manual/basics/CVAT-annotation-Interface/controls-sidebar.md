---
title: 'コントロールサイドバー'
linkTitle: 'コントロールサイドバー'
weight: 2
description: '画像内のナビゲーション、アノテーションツール、およびラベルの統合・分割・グループ化などの追加オプションを提供します。'
---

## ナビゲーション

**ナビゲーションブロック** - 画像の移動や回転のためのツールが含まれています。
|アイコン |説明 |
|-- |-- |
|![](/images/image148.jpg)|`カーソル`（`Esc`）- 基本的なアノテーション編集ツール。|
|![](/images/image149.jpg)|`画像の移動` - 編集せずに画像内を移動するためのツール。|
|![](/images/image102.jpg)|`回転` - 現在のフレームを時計回り（`Ctrl+R`）と反時計回り（`Ctrl+Shift+R`）で回転する2つのボタン。<br/>設定で`すべての画像を回転`を有効にすると、ジョブ内のすべての画像を回転できます。|

---

## ズーム

**ズームブロック** - 画像のズームツールが含まれています。
|アイコン |説明 |
|-- |-- |
|![](/images/image151.jpg)|`画像をフィット` - ワークスペースのサイズに画像を合わせます。<br/>ショートカット：画像をダブルクリック|
|![](/images/image166.jpg)|`関心領域の選択` - 選択した領域にズームインします。<br/>このツールを使用して、フレームの特定部分に素早くズームインできます。|

---

## シェイプ

**シェイプブロック** - シェイプ作成用のすべてのツールが含まれています。
|アイコン |説明 |セクションへのリンク |
|-- |-- |-- |
|![](/images/image189.jpg)|`AIツール`|{{< ilink "/docs/manual/advanced/ai-tools" "AIツール" >}}|
|![](/images/image201.jpg)|`OpenCV`|{{< ilink "/docs/manual/advanced/ai-tools" "OpenCV" >}}|
|![](/images/image167.jpg)|`矩形`|{{< ilink "/docs/manual/basics/shape-mode-basics" "シェイプモード" >}}; {{< ilink "/docs/manual/basics/track-mode-basics" "トラックモード" >}};<br/> {{< ilink "/docs/manual/advanced/annotation-with-rectangles" "4点による描画" >}}|
|![](/images/image168.jpg)|`ポリゴン`|{{< ilink "/docs/manual/advanced/annotation-with-polygons" "ポリゴンによるアノテーション" >}}; {{< ilink "/docs/manual/advanced/annotation-with-polygons/track-mode-with-polygons" "ポリゴントラックモード" >}}|
|![](/images/image169.jpg)|`ポリライン`|{{< ilink "/docs/manual/advanced/annotation-with-polylines" "ポリラインによるアノテーション" >}}|
|![](/images/image170.jpg)|`ポイント`|{{< ilink "/docs/manual/advanced/annotation-with-points" "ポイントによるアノテーション" >}}|
|![](/images/image241.jpg)|`楕円`|{{< ilink "/docs/manual/advanced/annotation-with-ellipses" "楕円によるアノテーション" >}}|
|![](/images/image176.jpg)|`キューボイド`|{{< ilink "/docs/manual/advanced/annotation-with-cuboids" "キューボイドによるアノテーション" >}}|
|![](/images/brushing_tools_icon.png)|`ブラッシングツール`|{{< ilink "/docs/manual/advanced/annotation-with-brush-tool" "ブラッシングによるアノテーション" >}}|
|![](/images/image171.jpg)|`タグ`|{{< ilink "/docs/manual/advanced/annotation-with-tags" "タグによるアノテーション" >}}|
|![](/images/image195.jpg)|`課題を作成`|{{< ilink "/docs/manual/advanced/analytics-and-monitoring/manual-qa" "レビュー" >}}（レビュー モードでのみ利用可能）|

---

## 編集

**編集ブロック** - トラックやシェイプの編集ツールが含まれています。
|アイコン |説明 |セクションへのリンク |
|-- |-- |-- |
|![](/images/image172.jpg)|`シェイプの統合`（`M`）- シェイプ統合モードの開始/終了。|{{< ilink "/docs/manual/basics/track-mode-basics" "トラックモード（基本）" >}}|
|![](/images/image173.jpg)|`シェイプのグループ化`（`G`）- シェイプグループ化モードの開始/終了。|{{< ilink "/docs/manual/advanced/shape-grouping" "シェイプのグループ化" >}}|
|![](/images/image174.jpg)|`分割` - トラックを分割します。 |{{< ilink "/docs/manual/advanced/track-mode-advanced" "トラックモード（詳細）" >}}|
|![](/images/image174.jpg)|`分割` - トラックを分割します。 |{{< ilink "/docs/manual/advanced/track-mode-advanced" "トラックモード（詳細）" >}}|
|![](/images/join-masks-icon.jpg)|複数のラベルを1つに結合します |{{< ilink "/docs/manual/advanced/slice-and-join#joining-cvat-labels" "**マスク結合ツール**" >}}|
|![](/images/slicing-tool-icon.jpg)|1つのラベルを複数に分割します。|{{< ilink "/docs/manual/advanced/slice-and-join#slicing-cvat-labels" "**マスク/ポリゴン分割**" >}}|

---

## 画像の移動

ユーザーインターフェースモードの切り替え。

![](/images/image145.jpg)

1. 下の矢印を使って次/前のフレームに移動します。
   スクロールバーのスライダーを使ってフレームをスクロールします。
   ほとんどのボタンにショートカットキーがあります。
   ショートカットのヒントが欲しい場合は、UI要素の上にマウスポインタを置いてください。

1. 画像をナビゲートするには、コントロールサイドバーのボタンを使用してください。
   もう一つの方法として、アノテートされていない領域内で左クリックを押しながら画像を移動/シフトできます。
   `マウスホイール`が押されている場合は、すべてのアノテートオブジェクトが無視されます。それ以外の場合は、
   ハイライトされたバウンディングボックスが画像の代わりに移動されます。

   ![](/images/image136.jpg)

1. サイドバーコントロールのボタンを使用して、関心領域にズームできます。
   `画像をフィット`ボタンを使用して、画像をワークスペースに合わせてください。
   また、マウスホイールでも画像を拡大縮小できます
   （画像は現在のカーソル位置を基準にズームされます）。

   ![](/images/image137.jpg)