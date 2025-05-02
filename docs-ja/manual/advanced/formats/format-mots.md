---
title: 'MOTS'
linkTitle: 'MOTS'
weight: 4
description: 'MOTSフォーマットでのデータのエクスポートとインポート方法'
---

MOT（Multiple Object Tracking：複数物体追跡）シーケンスフォーマットは、主に歩行者追跡や車両追跡などのマルチオブジェクトトラッキングアルゴリズムの評価で広く使用されています。  
MOTシーケンスフォーマットは、本質的にビデオフレームと、時間経過に伴う物体の位置とIDを指定するアノテーションを含みます。

このバージョンは.png形式でエンコードされています。マスクに対応しています。

詳細については、以下を参照してください。

- [MOTS PNG仕様](https://www.vision.rwth-aachen.de/page/mots)
- [データセット例](https://github.com/cvat-ai/datumaro/tree/v0.3/tests/assets/mots_dataset)

## MOTS PNGエクスポート

画像および動画のエクスポートについて：

- 対応アノテーション：バウンディングボックス、マスク
- 属性：`visibility`（数値）、`ignored`（チェックボックス）
- トラック：対応

ダウンロードされるファイルは、以下の構造を持つ.zipアーカイブです。

```bash
taskname.zip/
└── <any_subset_name>/
    |   images/
    |   ├── image1.jpg
    |   └── image2.jpg
    └── instances/
        ├── labels.txt
        ├── image1.png
        └── image2.png

# labels.txt
cat
dog
person
...
```

- 対応アノテーション：矩形およびポリゴントラック

## MOTS PNGインポート

アップロードファイル：上記構造のzipアーカイブ

- 対応アノテーション：ポリゴントラック