---
title: 'ICDAR13/15'
linkTitle: 'ICDAR13/15'
weight: 14
description: 'ICDAR13/15フォーマットでデータをエクスポートおよびインポートする方法'
---

ICDAR 13/15フォーマットは、主に文字検出・認識タスクやOCR（光学文字認識）で使用されます。

これらのフォーマットは、専門的な文字検出・認識モデルと組み合わせて利用されることが一般的です。

詳細については、以下を参照してください。

- [ICDAR13/15](https://rrc.cvc.uab.es/?ch=2)
- [データセット例](https://github.com/cvat-ai/datumaro/tree/v0.3/tests/assets/icdar_dataset)

## ICDAR13/15 エクスポート

画像のエクスポートについて：

- **ICDAR Recognition 1.0**（文字認識）:
  - サポートされているアノテーション: タグ `icdar`
  - 属性: `caption`
- **ICDAR Detection 1.0**（文字検出）:
  - サポートされているアノテーション: バウンディングボックス、ポリゴン（コンストラクタでラベル`icdar`を追加）
  - 属性: `text`
- **ICDAR Segmentation 1.0**（文字セグメンテーション）:
  - サポートされているアノテーション: バウンディングボックス、ポリゴン（コンストラクタでラベル`icdar`を追加）
  - 属性: `index`, `text`, `color`, `center`
- トラック: 未対応

ダウンロードされるファイルは、以下の構造を持つ.zipアーカイブです。

```bash
# 文字認識タスク
taskname.zip/
└── word_recognition/
    └── <any_subset_name>/
        ├── images
        |   ├── word1.png
        |   └── word2.png
        └── gt.txt
# 文字位置特定タスク
taskname.zip/
└── text_localization/
    └── <any_subset_name>/
        ├── images
        |   ├── img_1.png
        |   └── img_2.png
        ├── gt_img_1.txt
        └── gt_img_1.txt
# 文字セグメンテーションタスク
taskname.zip/
└── text_localization/
    └── <any_subset_name>/
        ├── images
        |   ├── 1.png
        |   └── 2.png
        ├── 1_GT.bmp
        ├── 1_GT.txt
        ├── 2_GT.bmp
        └── 2_GT.txt
```

## ICDAR13/15 インポート

アップロードファイル：上記構造のzipアーカイブ

**文字認識タスク**：

- サポートされているアノテーション: 属性`caption`を持つラベル`icdar`

**文字位置特定タスク**：

- サポートされているアノテーション: 属性`text`を持つラベル`icdar`の矩形またはポリゴン

**文字セグメンテーションタスク**：

- サポートされているアノテーション: 属性`index`, `text`, `color`, `center`を持つラベル`icdar`の矩形またはポリゴン