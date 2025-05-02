---
title: 'KITTI'
linkTitle: 'KITTI'
weight: 17
description: 'KITTIフォーマットでのデータのエクスポートとインポート方法'
---

KITTIフォーマットは、自動運転に関連した幅広いコンピュータビジョンタスクで広く使用されており、3D物体検出、マルチオブジェクトトラッキング、シーンフロー推定などが含まれますが、これらに限定されません。自動車シーンに特化しているため、KITTIフォーマットは通常、これらのタスク向けに設計または適応されたモデルとともに使用されます。

詳細については、以下を参照してください。

- [KITTIサイト](http://www.cvlibs.net/datasets/kitti/)
- [KITTI検出用フォーマット仕様](https://s3.eu-central-1.amazonaws.com/avg-kitti/devkit_object.zip)
- [KITTIセグメンテーション用フォーマット仕様](https://s3.eu-central-1.amazonaws.com/avg-kitti/devkit_semantics.zip)
- [データセット例](https://github.com/cvat-ai/datumaro/tree/v0.3/tests/assets/kitti_dataset)

## KITTIアノテーションのエクスポート

画像のエクスポートについて：

- サポートされているアノテーション：バウンディングボックス（検出）、ポリゴン（セグメンテーション）。
- サポートされている属性：
  - `occluded`（UIオプションおよび個別属性の両方で利用可能）
    バウンディングボックス内の物体の大部分が他の物体によって遮られていることを示します。
  - `truncated`（バウンディングボックスにのみ適用可能）
    ラベル用に`チェックボックス`として表現される必要があります。
    バウンディングボックスが物体全体を含んでおらず、一部が切り取られていることを示唆します。
  - `is_crowd`（ポリゴンにのみ有効）。ラベル用に`チェックボックス`で示される必要があります。
    アノテーションが同じ物体クラスの複数のインスタンスを含んでいることを示します。
- トラック：サポートされていません。

ダウンロードされるファイルは、以下の構造を持つ.zipアーカイブです。

```
└─ annotations.zip/
    ├── label_colors.txt # r g b ラベル名のペア一覧
    ├── labels.txt # ラベル一覧
    └── default/
        ├── label_2/ # 左カラーカメラのラベルファイル
        │   ├── <image_name_1>.txt
        │   ├── <image_name_2>.txt
        │   └── ...
        ├── instance/ # インスタンスセグメンテーションマスク
        │   ├── <image_name_1>.png
        │   ├── <image_name_2>.png
        │   └── ...
        ├── semantic/ # セマンティックセグメンテーションマスク（ラベルはIDでエンコード）
        │   ├── <image_name_1>.png
        │   ├── <image_name_2>.png
        │   └── ...
        └── semantic_rgb/ # セマンティックセグメンテーションマスク（ラベルは色でエンコード）
            ├── <image_name_1>.png
            ├── <image_name_2>.png
            └── ...
```

## KITTIアノテーションのインポート

KITTIアノテーションは2通りの方法でアップロードできます：
検出タスク用の矩形、および
セグメンテーションタスク用のマスクです。

検出タスクの場合、アップロードするアーカイブは以下の構造である必要があります。

```
└─ annotations.zip/
    ├── labels.txt # 任意、オリジナル以外の検出ラベル用のラベル一覧
    └── <subset_name>/
        ├── label_2/ # 左カラーカメラのラベルファイル
        │   ├── <image_name_1>.txt
        │   ├── <image_name_2>.txt
        │   └── ...
```

セグメンテーションタスクの場合、アップロードするアーカイブは以下の構造である必要があります。

```
└─ annotations.zip/
    ├── label_colors.txt # 任意、オリジナル以外のセグメンテーションラベル用のカラーマップ
    └── <subset_name>/
        ├── instance/ # インスタンスセグメンテーションマスク
        │   ├── <image_name_1>.png
        │   ├── <image_name_2>.png
        │   └── ...
        ├── semantic/ # 任意、セマンティックセグメンテーションマスク（ラベルはIDでエンコード）
        │   ├── <image_name_1>.png
        │   ├── <image_name_2>.png
        │   └── ...
        └── semantic_rgb/ # 任意、セマンティックセグメンテーションマスク（ラベルは色でエンコード）
            ├── <image_name_1>.png
            ├── <image_name_2>.png
            └── ...
```

すべてのアノテーションファイルおよびマスクは、
オリジナルのフォーマット仕様で説明されている構造である必要があります。