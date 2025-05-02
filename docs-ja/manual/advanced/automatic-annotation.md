---
title: '自動アノテーション'
linkTitle: '自動アノテーション'
weight: 16
description: 'タスクの自動アノテーション'
---

CVATの自動アノテーションは、事前学習済みモデルを使ってデータに自動的に事前アノテーションを付与できるツールです。

CVATは以下のソースからモデルを利用できます：

- [プリインストール済みモデル](#models)。
- [Hugging Face および Roboflow](#adding-models-from-hugging-face-and-roboflow) から統合したモデル。
- {{< ilink "/docs/manual/advanced/serverless-tutorial" "Nuclioでデプロイしたセルフホストモデル" >}}。

以下の表は利用可能なオプションについて説明しています：

|                                             | セルフホスト            | クラウド                                            |
| ------------------------------------------- | ---------------------- | ------------------------------------------------ |
| **価格**                                   | 無料                   | [価格表](https://www.cvat.ai/pricing/cloud) を参照 |
| **モデル**                                 | モデルを追加する必要あり | プリインストール済みモデルを利用可能                 |
| **Hugging Face & Roboflow <br>統合**       | 非対応                 | 対応                                               |

参照：

- [自動アノテーションの実行](#running-automatic-annotation)
- [ラベルのマッチング](#labels-matching)
- [モデル一覧](#models)
- [Hugging Face および Roboflow からのモデル追加](#adding-models-from-hugging-face-and-roboflow)

## 自動アノテーションの実行

自動アノテーションを開始するには、以下の手順を実行してください：

1. 上部メニューから **Tasks** をクリックします。
1. アノテーションしたいタスクを探し、**Action** > **Automatic annotation** をクリックします。

   ![](/images/image119_detrac.jpg)

1. 自動アノテーションのダイアログで、ドロップダウンリストから[モデル](#models)を選択します。
1. モデルとタスクの[ラベルをマッチング](#labels-matching)します。
1. （任意）マスクをポリゴンとして返したい場合は、**Return masks as polygons** のトグルをオンにします。
1. （任意）過去のアノテーションをすべて削除したい場合は、**Clean old annotations** のトグルをオンにします。
1. （任意）モデルの**閾値**を指定できます。指定しない場合は、モデル設定のデフォルト値が使用されます。

   ![](/images/running_automatic_annotation.png)

1. **Annotate** をクリックします。

CVATはプログレスバーでアノテーションの進捗を表示します。

![プログレスバー](/images/image121_detrac.jpg)

自動アノテーションは、いつでもキャンセルをクリックすることで停止できます。

## ラベルのマッチング

各モデルは特定のデータセットで学習されており、そのデータセットのラベルのみ対応しています。

例：

- DLモデルには `car` というラベルがある。
- あなたのタスク（またはプロジェクト）には `vehicle` というラベルがある。

アノテーションするには、これら2つのラベルをマッチさせて、
この場合 `car` = `vehicle` であることをCVATに伝える必要があります。

もしDLラベル一覧に存在しないラベルがある場合、
それらをマッチさせることはできません。

このため、対応しているDLモデルは特定のラベルにのみ利用可能です。

各モデルのラベル一覧を確認するには、[モデル一覧](#models)の論文や公式ドキュメントを参照してください。

## モデル一覧

自動アノテーションはプリインストール済みモデルと追加したモデルを利用します。

> セルフホスト型の場合は、
> まず
> {{< ilink "/docs/administration/advanced/installation_automatic_annotation" "自動アノテーションをインストール" >}}
> し、{{< ilink "/docs/manual/advanced/models" "モデルを追加" >}}する必要があります。

プリインストール済みモデル一覧：

<!--lint disable maximum-line-length-->

| モデル                     | 説明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 属性付き顔検出             | 3つのOpenVINOモデルが連携します：<br><br><li>[Face Detection 0205](https://docs.openvino.ai/2022.3/omz_models_model_face_detection_0205.html)：MobileNetV2をバックボーンにしたFCOSヘッドによる、屋内外の前向きカメラ映像対応の顔検出器。<li>[Emotions recognition retail 0003](https://docs.openvino.ai/2022.3/omz_models_model_emotions_recognition_retail_0003.html#emotions-recognition-retail-0003)：5つの感情（‘neutral’, ‘happy’, ‘sad’, ‘surprise’, ‘anger’）を認識する全結合畳み込みネットワーク。<li>[Age gender recognition retail 0013](https://docs.openvino.ai/2022.3/omz_models_model_age_gender_recognition_retail_0013.html)：年齢・性別同時認識の全結合畳み込みネットワーク。18～75歳の年齢認識が可能で、訓練セットに子供の顔は含まれていません。 |
| RetinaNet R101            | RetinaNetは、学習時のクラス不均衡に対応するためにフォーカルロス関数を利用するワンステージ物体検出モデルです。フォーカルロスはクロスエントロピーロスに調整項を加えることで難易度の高い負例に学習を集中させます。RetinaNetはバックボーンネットワークと2つのタスク固有サブネットワークから構成される単一統合ネットワークです。<br><br>詳細は：<li>[Site: RetinaNET](https://paperswithcode.com/lib/detectron2/retinanet) |
| テキスト検出               | PixelLinkアーキテクチャをベースにしたMobileNetV2（depth_multiplier=1.4）バックボーンの屋内外対応テキスト検出器。<br><br>詳細は：<li>[Site: OpenVINO Text detection 004](https://docs.openvino.ai/2022.3/omz_models_model_text_detection_0004.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| YOLO v3                   | YOLO v3はCOCOデータセットで事前学習された物体検出アーキテクチャとモデル群です。<br><br>詳細は：<li>[Site: YOLO v3](https://docs.openvino.ai/2022.3/omz_models_model_yolo_v3_tf.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| YOLO v7                   | YOLOv7は、速度・精度の両面で他の検出器を上回る先進的な物体検出モデルです。5～160FPSの範囲でフレーム処理可能で、V100 GPU上で30FPS以上のリアルタイム物体検出器中、最高精度56.8% AP（平均適合率）を実現しています。<br><br>詳細は：<li>[GitHub: YOLO v7](https://github.com/WongKinYiu/yolov7) <li>[Paper: YOLO v7](https://arxiv.org/pdf/2207.02696.pdf)                                                                                                                                                                                                                                                                                                                                                                                                    |

<!--lint enable maximum-line-length-->

## Hugging Face および Roboflow からのモデル追加

必要なモデルが見つからない場合は、[Hugging Face](https://huggingface.co/) または [Roboflow](https://roboflow.com/) からお好きなモデルを追加できます。

> **注意**：セルフホストCVATにはHugging FaceおよびRoboflowからモデルを追加できません。

<!--lint disable maximum-line-length-->

詳細は
[Hugging FaceおよびRoboflowモデル統合によるアノテーション効率化](https://www.cvat.ai/post/integrating-hugging-face-and-roboflow-models)
を参照してください。

以下のビデオでプロセスを説明しています：

<iframe width="560" height="315" src="https://www.youtube.com/embed/SbU3aB65W5s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<!--lint enable maximum-line-length-->