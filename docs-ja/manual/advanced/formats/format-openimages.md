---
title: 'Open Images'
linkTitle: 'Open Images'
weight: 15
description: 'Open Imagesフォーマットでデータをエクスポートおよびインポートする方法'
---

Open Imagesフォーマットは、
物体検出、物体セグメンテーション、視覚的関係、
およびローカライズされたナラティブ注釈を含む
大規模かつ多様なデータセットに基づいています。

そのエクスポートデータフォーマットは、多くの物体検出およびセグメンテーションモデルと互換性があります。

詳細については、以下を参照してください：

- [Open Images サイト](https://storage.googleapis.com/openimages/web/index.html)
- [フォーマット仕様](https://storage.googleapis.com/openimages/web/download.html)
- [データセット例](https://github.com/cvat-ai/datumaro/tree/v0.3/tests/assets/open_images_dataset)

## Open Imagesのエクスポート

画像のエクスポートについて：

- サポートされるアノテーション：バウンディングボックス（検出）、
  タグ（分類）、ポリゴン（セグメンテーション）。

- サポートされる属性：
  - タグ：`score`はラベルとして`text`または`number`で定義する必要があります。
    信頼度は0から1の範囲です。
  - バウンディングボックス：<br>`score`はラベルとして`text`または`number`で定義する必要があります。
    信頼度は0から1の範囲です。<br> `occluded`はUIオプションと
    個別の属性の両方として。オブジェクトが他のオブジェクトによって隠されているかどうか。<br>`truncated`
    はラベルとして`checkbox`で定義する必要があります。オブジェクトが画像の境界を超えているかどうか。
    <br>`is_group_of`はラベルとして`checkbox`で定義する必要があります。オブジェクトが同じクラスのオブジェクトのグループを表しているかどうか。<br>`is_depiction`は
    ラベルとして`checkbox`で定義する必要があります。オブジェクトが実物ではなく（例えばイラストなどの）描写かどうか。<br>`is_inside`は
    ラベルとして`checkbox`で定義する必要があります。オブジェクトが内部から見られているかどうか。
  - マスク：
    <br>`box_id`はラベルとして`text`で定義する必要があります。
    マスクに関連付けられたバウンディングボックスの識別子。
    <br>`predicted_iou`はラベルとして`text`または`number`で定義する必要があります。
    正解データとの予測IoU値。
- トラック：未対応。

ダウンロードされるファイルは、以下の構造の.zipアーカイブです：

```
└─ taskname.zip/
    ├── annotations/
    │   ├── bbox_labels_600_hierarchy.json
    │   ├── class-descriptions.csv
    |   ├── images.meta  # 画像サイズ情報の追加ファイル
    │   ├── <subset_name>-image_ids_and_rotation.csv
    │   ├── <subset_name>-annotations-bbox.csv
    │   ├── <subset_name>-annotations-human-imagelabels.csv
    │   └── <subset_name>-annotations-object-segmentation.csv
    ├── images/
    │   ├── subset1/
    │   │   ├── <image_name101.jpg>
    │   │   ├── <image_name102.jpg>
    │   │   └── ...
    │   ├── subset2/
    │   │   ├── <image_name201.jpg>
    │   │   ├── <image_name202.jpg>
    │   │   └── ...
    |   ├── ...
    └── masks/
        ├── subset1/
        │   ├── <mask_name101.png>
        │   ├── <mask_name102.png>
        │   └── ...
        ├── subset2/
        │   ├── <mask_name201.png>
        │   ├── <mask_name202.png>
        │   └── ...
        ├── ...
```

## Open Imagesのインポート

アップロードするファイル：以下の構造のzipアーカイブ

```
└─ upload.zip/
    ├── annotations/
    │   ├── bbox_labels_600_hierarchy.json
    │   ├── class-descriptions.csv
    |   ├── images.meta  # オプション、画像サイズ情報のファイル
    │   ├── <subset_name>-image_ids_and_rotation.csv
    │   ├── <subset_name>-annotations-bbox.csv
    │   ├── <subset_name>-annotations-human-imagelabels.csv
    │   └── <subset_name>-annotations-object-segmentation.csv
    └── masks/
        ├── subset1/
        │   ├── <mask_name101.png>
        │   ├── <mask_name102.png>
        │   └── ...
        ├── subset2/
        │   ├── <mask_name201.png>
        │   ├── <mask_name202.png>
        │   └── ...
        ├── ...
```

`<subset_name>-image_ids_and_rotation.csv`内の画像IDは、
タスク内の画像名と一致している必要があります。