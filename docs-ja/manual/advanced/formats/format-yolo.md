---
title: 'YOLO'
linkTitle: 'YOLO'
weight: 7
description: 'YOLOフォーマットでのデータのエクスポートとインポート方法'
---

YOLO（You Only Look Onceの略）は、主にリアルタイム物体検出タスクで広く利用されている有名なフレームワークです。
その効率性と高速性から、多くの用途で理想的な選択肢となっています。
YOLOには独自のデータフォーマットがありますが、
このフォーマットは他の物体検出モデルにも合わせて調整することが可能です。

詳細については、以下を参照してください：

- [YOLO仕様](https://pjreddie.com/darknet/yolo/)
- [フォーマット仕様](https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects)
- [データセット例](https://github.com/cvat-ai/datumaro/tree/v0.3/tests/assets/yolo_dataset)

## YOLOエクスポート

画像のエクスポートについて：

- サポートされているアノテーション: バウンディングボックス
- 属性: サポートされていません
- トラック: サポートされていません

ダウンロードされるファイルは、以下の構造を持つ.zipアーカイブです：

```bash
archive.zip/
├── obj.data
├── obj.names
├── obj_<subset>_data
│   ├── image1.txt
│   └── image2.txt
└── train.txt # サブセット画像パスのリスト

# 有効なサブセットは: train, valid のみ
# train.txtおよびvalid.txt:
obj_<subset>_data/image1.jpg
obj_<subset>_data/image2.jpg

# obj.data:
classes = 3 # 任意
names = obj.names
train = train.txt
valid = valid.txt # 任意
backup = backup/ # 任意

# obj.names:
cat
dog
airplane

# image_name.txt:
# label_id - obj.namesのid
# cx, cy - バウンディングボックス中心の相対座標
# rw, rh - バウンディングボックスの相対サイズ
# label_id cx cy rw rh
1 0.3 0.8 0.1 0.3
2 0.7 0.2 0.3 0.1
```

各アノテーションファイル（.txt拡張子）は、
対応する画像ファイルに合わせて名付けられています。

例えば、`frame_000001.txt`は
`frame_000001.jpg`画像のアノテーションとなります。

`.txt`ファイルの構造は以下の通りです：
各行はラベルとバウンディングボックスを
`label_id cx cy w h`という形式で記述します。
`obj.names`ファイルには、ラベル名の順序付きリストが含まれます。

## YOLOインポート

アップロードするファイルは、上記と同じ構造のzipアーカイブです。
CVATフレーム（画像名）とアノテーションファイル名が一致する必要があります。方法は2つあります：

1. 画像名とアノテーション`*.txt`ファイル名が完全一致する場合
   （画像または画像アーカイブからタスクを作成した場合）。

1. フレーム番号で一致させる場合（CVATが名前で一致できない場合）。ファイル名は次の形式である必要があります：`<number>.jpg`。
   これは、動画からタスクを作成した場合に使用します。

## YOLOフォーマットデータセット（例：VOCから）からタスクを作成する方法

1. 公式の[ガイド](https://pjreddie.com/darknet/yolo/)（Training YOLO on VOCセクション参照）に従い、
   YOLOフォーマットのアノテーションファイルを準備します。

1. トレイン画像をzip化します

   ```bash
   zip images.zip -j -@ < train.txt
   ```

1. 次のラベルでCVATタスクを作成します：

   ```bash
   aeroplane bicycle bird boat bottle bus car cat chair cow diningtable dog
   horse motorbike person pottedplant sheep sofa train tvmonitor
   ```

   画像としてimages.zipを選択します。images.zipのサイズが500MBを超える場合が多いため、`share`機能の利用を推奨します。
   詳細は{{< ilink "/docs/manual/basics/create_an_annotation_task" "アノテーションタスクの作成" >}}ガイドを参照してください。

1. 次の内容で`obj.names`を作成します：

   ```bash
   aeroplane
   bicycle
   bird
   boat
   bottle
   bus
   car
   cat
   chair
   cow
   diningtable
   dog
   horse
   motorbike
   person
   pottedplant
   sheep
   sofa
   train
   tvmonitor
   ```

1. すべてのラベルファイルをまとめてzip化します（trainサブセットに対応するラベルファイルのみ追加）：

   ```bash
   cat train.txt | while read p; do echo ${p%/*/*}/labels/${${p##*/}%%.*}.txt; done | zip labels.zip -j -@ obj.names
   ```

1. `アノテーションのアップロード`ボタンをクリックし、`YOLO 1.1`を選択して、前のステップで作成したラベルのzipファイルを選択します。