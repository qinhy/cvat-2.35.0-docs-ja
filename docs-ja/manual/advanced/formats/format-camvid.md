---
title: 'CamVid'
linkTitle: 'CamVid'
weight: 10
description: 'CamVid形式でのデータのエクスポートおよびインポート方法'
---

CamVid（Cambridge-driving Labeled Video Database）形式は、主にセマンティックセグメンテーションタスクの分野で使用されます。特に自動運転やその他のビジョンベースのロボティクスアプリケーションのモデルの学習および評価に有用です。

詳細については、以下を参照してください：

- [CamVid仕様](http://mi.eng.cam.ac.uk/research/projects/VideoRec/CamVid/)
- [データセット例](https://github.com/cvat-ai/datumaro/tree/v0.3/tests/assets/camvid_dataset)

## CamVidエクスポート

画像および動画のエクスポートについて：

- サポートされているアノテーション：バウンディングボックス、ポリゴン
- 属性：サポートされていません
- トラック：サポートされていません

ダウンロードされるファイルは、以下の構造を持つ.zipアーカイブです：

```bash
taskname.zip/
├── label_colors.txt # オプション、CamVid以外のラベルに必要
├── <any_subset_name>/
|   ├── image1.png
|   └── image2.png
├── <any_subset_name>annot/
|   ├── image1.png
|   └── image2.png
└── <any_subset_name>.txt

# label_colors.txt（カラーバリュータイプあり）
# ラベルの色を手動で設定したい場合、label_colors.txtを以下のように記述します：
# color (RGB) label
0 0 0 Void
64 128 64 Animal
192 0 128 Archway
0 128 192 Bicyclist
0 128 64 Bridge

# label_colors.txt（カラーバリュータイプなし）
# ラベルの色を手動で設定しない場合、自動的に色が設定されます：
# label
Void
Animal
Archway
Bicyclist
Bridge
```

CamVidデータセットのマスクは、通常**.png**形式の画像で、1チャネルまたは3チャネルのいずれかです。

この画像では、各ピクセルに特定のラベルに対応する色が割り当てられています。

デフォルトでは、色 `(0, 0, 0)`、つまり「黒」が背景を表すために使用されます。

## CamVidインポート

画像のインポートについて：

- アップロードファイル：上記構造の_.zip_アーカイブ
- サポートされているアノテーション：ポリゴン