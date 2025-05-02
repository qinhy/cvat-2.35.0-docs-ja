---
title: 'VGGFace2'
linkTitle: 'VGGFace2'
weight: 12
description: 'VGGFace2形式でのデータのエクスポートとインポート方法'
---

VGGFace2は主に顔認識タスク向けに設計されており、顔認識や認証などのタスク専用に設計されたディープラーニングモデルと共によく使用されます。

詳細については、以下を参照してください。

- [VGGFace2 Github](https://github.com/ox-vgg/vgg_face2)
- [データセット例](https://github.com/cvat-ai/datumaro/tree/v0.3/tests/assets/vgg_face2_dataset)

## VGGFace2のエクスポート

画像のエクスポートについて：

- サポートされているアノテーション：バウンディングボックス、ポイント（ランドマーク - 5点のグループ）
- 属性：非対応
- トラック：非対応

ダウンロードされるファイルは、以下のような構造の.zipアーカイブです。

```bash
taskname.zip/
├── labels.txt # 任意
├── <any_subset_name>/
|   ├── label0/
|   |   └── image1.jpg
|   └── label1/
|       └── image2.jpg
└── bb_landmark/
    ├── loose_bb_<any_subset_name>.csv
    └── loose_landmark_<any_subset_name>.csv
# labels.txt
# n000001 car
label0 <class0>
label1 <class1>
```

## VGGFace2のインポート

アップロードするファイル：上記の構造のzipアーカイブ

- サポートされているアノテーション：矩形、ポイント（ランドマーク - 5点のグループ）