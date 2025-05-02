---
title: 'Ultralytics YOLO'
linkTitle: 'Ultralytics YOLO'
weight: 7
description: 'Ultralytics YOLOフォーマットでのデータのエクスポートとインポート方法'
---

Ultralytics YOLOは、以下の4つのフォーマットからなるフォーマットファミリーです：
- [検出（Detection）](https://docs.ultralytics.com/datasets/detect/)
- [方向付きバウンディングボックス（Oriented bounding Box）](https://docs.ultralytics.com/datasets/obb/)
- [セグメンテーション（Segmentation）](https://docs.ultralytics.com/datasets/segment/)
- [ポーズ（Pose）](https://docs.ultralytics.com/datasets/pose/)

データセット例：
- [検出（Detection）](https://github.com/cvat-ai/datumaro/tree/develop/tests/assets/yolo_dataset/yolo_ultralytics_detection)
- [方向付きバウンディングボックス](https://github.com/cvat-ai/datumaro/tree/develop/tests/assets/yolo_dataset/yolo_ultralytics_oriented_boxes)
- [セグメンテーション](https://github.com/cvat-ai/datumaro/tree/develop/tests/assets/yolo_dataset/yolo_ultralytics_segmentation)
- [ポーズ](https://github.com/cvat-ai/datumaro/tree/develop/tests/assets/yolo_dataset/yolo_ultralytics_pose)

## Ultralytics YOLOエクスポート

画像のエクスポートについて：

- サポートされているアノテーション
  - 検出：バウンディングボックス
  - 方向付きバウンディングボックス：方向付きバウンディングボックス
  - セグメンテーション：ポリゴン、マスク
  - ポーズ：スケルトン
- 属性：未対応
- トラック：対応

ダウンロードされるファイルは、以下の構造を持つ.zipアーカイブです：

```bash
archive.zip/
   ├── data.yaml  # 設定ファイル
   ├── train.txt  # 訓練サブセット画像パスのリスト
   │
   ├── images/
   │   ├── train/  # 訓練サブセットの画像ディレクトリ
   │   │    ├── image1.jpg
   │   │    ├── image2.jpg
   │   │    ├── image3.jpg
   │   │    └── ...
   ├── labels/
   │   ├── train/  # 訓練サブセットのアノテーションディレクトリ
   │   │    ├── image1.txt
   │   │    ├── image2.txt
   │   │    ├── image3.txt
   │   │    └── ...

# train.txt:
images/<subset>/image1.jpg
images/<subset>/image2.jpg
...

# data.yaml:
path:  ./ # データセットルートディレクトリ
train: train.txt  # 訓練画像（'path'からの相対パス）

# Ultralytics YOLO Pose特有のフィールド
# 最初の数字はスケルトンのポイント数
# 異なるポイント数のスケルトンが複数ある場合は最大ポイント数
# 2つ目の数字はアノテーションtxtファイル内のポイント情報の形式を定義
kpt_shape: [17, 3]

# クラス
names:
  0: person
  1: bicycle
  2: car
  # ...

# <image_name>.txt:
# フォーマットによって内容が異なる

# Ultralytics YOLO 検出（Detection）:
# label_id - data.yamlのnamesフィールドのID
# cx, cy - バウンディングボックス中心の相対座標
# rw, rh - バウンディングボックスの相対サイズ
# label_id cx cy rw rh
1 0.3 0.8 0.1 0.3
2 0.7 0.2 0.3 0.1

# Ultralytics YOLO 方向付きバウンディングボックス:
# xn, yn - n番目のポイントの相対座標
# label_id x1 y1 x2 y2 x3 y3 x4 y4
1 0.3 0.8 0.1 0.3 0.4 0.5 0.7 0.5
2 0.7 0.2 0.3 0.1 0.4 0.5 0.5 0.6

# Ultralytics YOLO セグメンテーション:
# xn, yn - n番目のポイントの相対座標
# label_id x1 y1 x2 y2 x3 y3 ...
1 0.3 0.8 0.1 0.3 0.4 0.5
2 0.7 0.2 0.3 0.1 0.4 0.5 0.5 0.6 0.7 0.5

# Ultralytics YOLO ポーズ:
# cx, cy - バウンディングボックス中心の相対座標
# rw, rh - バウンディングボックスの相対サイズ
# xn, yn - n番目のポイントの相対座標
# vn - n番目のポイントの可視性。2-可視、1-部分的に可視、0-不可視
# kpt_shapeの2つ目の値が3の場合：
# label_id cx cy rw rh x1 y1 v1 x2 y2 v2 x3 y3 v3 ...
1 0.3 0.8 0.1 0.3 0.3 0.8 2 0.1 0.3 2 0.4 0.5 2 0.0 0.0 0 0.0 0.0 0
2 0.3 0.8 0.1 0.3 0.7 0.2 2 0.3 0.1 1 0.4 0.5 0 0.5 0.6 2 0.7 0.5 2

# kpt_shapeの2つ目の値が2の場合：
# label_id cx cy rw rh x1 y1 x2 y2 x3 y3 ...
1 0.3 0.8 0.1 0.3 0.3 0.8 0.1 0.3 0.4 0.5 0.0 0.0 0.0 0.0
2 0.3 0.8 0.1 0.3 0.7 0.2 0.3 0.1 0.4 0.5 0.5 0.6 0.7 0.5

# 異なるポイント数のスケルトンが複数ある場合は、
# 小さいスケルトンは座標0.0 0.0および可視性=0でパディングされることに注意
```

全ての座標は正規化されている必要があります。
x座標や幅は画像の幅で、y座標や高さは画像の高さで割ることで正規化できます。
> CVATではオブジェクトやその一部を画像外に配置することができ、
> この場合座標は[0, 1]範囲外になります。
> YOLOv8フレームワークはこのような座標を持つラベルを無視します。

各アノテーションファイル（拡張子`.txt`）は
対応する画像ファイル名と一致しています。

例：`frame_000001.txt` は
`frame_000001.jpg`画像のアノテーションとなります。

### トラック対応

Ultralytics YOLO Detection Trackフォーマットを使うことで、
検出タスクでトラックをエクスポート時に保存できます。
対応するアノテーションの末尾にトラックIDを書き込みます：
```bash
# label_id cx cy rw rh <オプショントラックID>
1 0.3 0.8 0.1 0.3 1
2 0.7 0.2 0.3 0.1
```

## インポート

アップロードするファイル：上記と同じ構造のzipアーカイブ。

他のUltralytics YOLO形式エクスポートツール（例：[roboflow](https://roboflow.com/formats/yolov8-pytorch-txt)）との互換性のために、
CVATはサブセットと"images"または"labels"のディレクトリ順序が逆の場合も対応しています。
つまり、`train/images/`、`images/train/`のどちらも有効です。
```bash
archive.zip/
   ├── train/
   │   ├── images/  # 訓練サブセットの画像ディレクトリ
   │   │    ├── image1.jpg
   │   │    ├── image2.jpg
   │   │    └── ...
   │   ├── labels/  # 訓練サブセットのアノテーションディレクトリ
   │   │    ├── image1.txt
   │   │    ├── image2.txt
   │   │    └── ...
```

### トラック対応

各Ultralytics YOLOフォーマットでトラッキングをサポートしています。
整数のトラックIDは任意で各アノテーションの末尾に追加できます（例：検出フォーマット）：
```bash
# label_id cx cy rw rh <オプショントラックID>
1 0.3 0.8 0.1 0.3 1
2 0.7 0.2 0.3 0.1
```