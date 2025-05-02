---
title: 'Cityscapes（シティスケープス）'
linkTitle: 'Cityscapes'
weight: 16
description: 'Cityscapesフォーマットでのデータのエクスポートおよびインポート方法'
---

Cityscapesフォーマットは、コンピュータビジョン分野で広く使用されている標準フォーマットであり、
特に都市のシーンにおけるセマンティックおよびインスタンスセグメンテーションのタスクで用いられます。
このデータセット形式は通常、
都市風景の高解像度画像と詳細なピクセル単位のアノテーションで構成されています。

各ピクセルには「道路」「歩行者」「車両」などのカテゴリラベルが付与されており、
都市環境を理解するための機械学習モデルの学習や検証にとって
非常に価値のあるリソースです。自動運転車、
ロボティクス、スマートシティ分野で研究者や専門家が
よく利用する選択肢となっています。

詳細については、以下を参照ください：

- [Cityscapes公式サイト](https://www.cityscapes-dataset.com/login/)
- [Cityscapesフォーマット仕様](https://github.com/mcordts/cityscapesScripts#the-cityscapes-dataset)
- [Cityscapesデータセット例](https://github.com/cvat-ai/datumaro/tree/v0.3/tests/assets/cityscapes_dataset)

# Cityscapes エクスポート

画像のエクスポートについて：

- サポートされるアノテーション：ポリゴン（セグメンテーション）、バウンディングボックス
- 属性:
  - `is_crowd` ブール値。ラベルに対して`checkbox`として定義されている必要があります。
    アノテーションラベルが異なるインスタンスを区別できるかどうかを指定します。
    Falseの場合、アノテーションのidフィールドがインスタンスIDをエンコードします。
- トラック：非対応

ダウンロードされるファイルは、以下の構造を持つ.zipアーカイブです：

```
.
├── label_color.txt
├── gtFine
│   ├── <subset_name>
│   │   └── <city_name>
│   │       ├── image_0_gtFine_instanceIds.png
│   │       ├── image_0_gtFine_color.png
│   │       ├── image_0_gtFine_labelIds.png
│   │       ├── image_1_gtFine_instanceIds.png
│   │       ├── image_1_gtFine_color.png
│   │       ├── image_1_gtFine_labelIds.png
│   │       ├── ...
└── imgsFine  # 画像の保存を選択した場合
    └── leftImg8bit
        ├── <subset_name>
        │   └── <city_name>
        │       ├── image_0_leftImg8bit.png
        │       ├── image_1_leftImg8bit.png
        │       ├── ...
```

- `label_color.txt` 各ラベルの色を記述したファイル

```
# label_color.txt 例
# r g b label_name
0 0 0 background
0 255 0 tree
...
```

- `*_gtFine_color.png` 各クラスラベルが色でエンコードされた画像
- `*_gtFine_labelIds.png` 各クラスラベルがインデックスでエンコードされた画像
- `*_gtFine_instanceIds.png` クラスおよびインスタンスラベルが
  インスタンスIDでエンコードされた画像。ピクセル値はクラスと個々のインスタンスを表します：
  各IDを1000で割った整数部分がクラスID、余りがインスタンスIDとなります。
  アノテーションが複数インスタンスを示す場合、ピクセル値はそのクラスの通常のIDになります。

# Cityscapes アノテーションのインポート

アップロードするファイル：以下の構造を持つzipアーカイブ

```
.
├── label_color.txt # 任意
└── gtFine
    └── <city_name>
        ├── image_0_gtFine_instanceIds.png
        ├── image_1_gtFine_instanceIds.png
        ├── ...
```

# Cityscapesデータセットでタスクを作成

必要なラベルでタスクを作成するか、
元のデータセットのラベルと色を利用することもできます。
Cityscapesフォーマットで作業する場合、背景用に黒色のラベルが
必要となります。

元のCityscapesカラーマップ：

```JSON
[
    {"name": "unlabeled", "color": "#000000", "attributes": []},
    {"name": "egovehicle", "color": "#000000", "attributes": []},
    {"name": "rectificationborder", "color": "#000000", "attributes": []},
    {"name": "outofroi", "color": "#000000", "attributes": []},
    {"name": "static", "color": "#000000", "attributes": []},
    {"name": "dynamic", "color": "#6f4a00", "attributes": []},
    {"name": "ground", "color": "#510051", "attributes": []},
    {"name": "road", "color": "#804080", "attributes": []},
    {"name": "sidewalk", "color": "#f423e8", "attributes": []},
    {"name": "parking", "color": "#faaaa0", "attributes": []},
    {"name": "railtrack", "color": "#e6968c", "attributes": []},
    {"name": "building", "color": "#464646", "attributes": []},
    {"name": "wall", "color": "#66669c", "attributes": []},
    {"name": "fence", "color": "#be9999", "attributes": []},
    {"name": "guardrail", "color": "#b4a5b4", "attributes": []},
    {"name": "bridge", "color": "#966464", "attributes": []},
    {"name": "tunnel", "color": "#96785a", "attributes": []},
    {"name": "pole", "color": "#999999", "attributes": []},
    {"name": "polegroup", "color": "#999999", "attributes": []},
    {"name": "trafficlight", "color": "#faaa1e", "attributes": []},
    {"name": "trafficsign", "color": "#dcdc00", "attributes": []},
    {"name": "vegetation", "color": "#6b8e23", "attributes": []},
    {"name": "terrain", "color": "#98fb98", "attributes": []},
    {"name": "sky", "color": "#4682b4", "attributes": []},
    {"name": "person", "color": "#dc143c", "attributes": []},
    {"name": "rider", "color": "#ff0000", "attributes": []},
    {"name": "car", "color": "#00008e", "attributes": []},
    {"name": "truck", "color": "#000046", "attributes": []},
    {"name": "bus", "color": "#003c64", "attributes": []},
    {"name": "caravan", "color": "#00005a", "attributes": []},
    {"name": "trailer", "color": "#00006e", "attributes": []},
    {"name": "train", "color": "#005064", "attributes": []},
    {"name": "motorcycle", "color": "#0000e6", "attributes": []},
    {"name": "bicycle", "color": "#770b20", "attributes": []},
    {"name": "licenseplate", "color": "#00000e", "attributes": []}
]

```

</details>

タスク作成時に画像をアップロードしてください：

```
images.zip/
    ├── image_0.jpg
    ├── image_1.jpg
    ├── ...

```

タスク作成後、前述のセクションで説明した通りに
Cityscapesアノテーションをアップロードしてください。