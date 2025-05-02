---
title: 'COCO キーポイント'
linkTitle: 'COCO キーポイント'
weight: 5
description: 'COCO キーポイント形式でデータをエクスポート・インポートする方法'
---

COCO キーポイント形式は、人間の姿勢推定タスク向けに特化したフォーマットです。このタスクの目的は、画像内の人物の身体の関節（キーポイント）を特定し、位置を特定することです。

この特殊なフォーマットは、姿勢推定に特化した最新のさまざまなモデルで使用されています。

詳細については、以下をご覧ください：

- [COCO キーポイント サイト](https://cocodataset.org/#keypoints-2020)
- [フォーマット仕様](https://openvinotoolkit.github.io/datumaro/latest/docs/data-formats/formats/coco.html)
- [アーカイブの例](https://openvinotoolkit.github.io/datumaro/latest/docs/data-formats/formats/coco.html#import-coco-dataset)

## COCO キーポイントのエクスポート

画像のエクスポートについて：

- サポートされているアノテーション: スケルトン
- 属性:
  - `is_crowd`：チェックボックスまたは整数（0 または 1 の値）で指定できます。これはインスタンス（またはオブジェクト群）が `segmentation` フィールドに RLE エンコードされたマスクを含むべきことを示します。グループ内のすべてのシェイプは 1 つのマスクにまとめられ、最大のシェイプがオブジェクトグループ全体のプロパティを設定します。
  - `score`: この数値フィールドはアノテーションの `score` を表します。
  - 任意の属性: これらはアノテーションの `attributes` セクションに保存されます。
- トラック: 非対応

ダウンロードされるファイルは以下の構造を持つ .zip アーカイブです：

```
archive.zip/
├── images/
│
│   ├── <image_name1.ext>
│   ├── <image_name2.ext>
│   └── ...
├──<annotations>.xml
```

## COCO インポート

アップロードするファイル: 単一の展開された `*.json` または、[こちら](https://openvinotoolkit.github.io/datumaro/latest/docs/data-formats/formats/coco.html#import-coco-dataset)で説明されている構造（画像なし）の zip アーカイブ。

- サポートされているアノテーション: スケルトン

`person_keypoints`,

Datumaro による COCO タスクのサポートについては[こちら](https://openvinotoolkit.github.io/datumaro/latest/docs/data-formats/formats/coco.html#export-to-other-formats)で説明されています。
例えば、[Datumaro 経由の COCO キーポイントサポート](https://github.com/openvinotoolkit/cvat/issues/2910#issuecomment-726077582):

1. [Datumaro](https://github.com/openvinotoolkit/datumaro)をインストール
   `pip install datumaro`
2. タスクを `Datumaro` 形式でエクスポートし、解凍
3. Datumaro プロジェクトを `coco` / `coco_person_keypoints` 形式でエクスポート
   `datum export -f coco -p path/to/project [-- --save-images]`

この方法で、CVAT のポイントを単一キーポイントまたはキーポイントリスト（`visibility` COCO フラグなし）としてエクスポートできます。