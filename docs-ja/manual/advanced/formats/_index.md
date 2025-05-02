---
title: 'CVATからアノテーションとデータをエクスポートする'
linkTitle: 'CVATからアノテーションとデータをエクスポートする'
weight: 20
description: 'CVATがサポートするデータエクスポートフォーマット一覧。'
---

CVATでは、さまざまなフォーマットでデータをエクスポートすることができます。
エクスポートフォーマットの選択は、アノテーションの種類や
データセットの今後の用途によって異なります。

参照:

- [データエクスポートフォーマット](#data-export-formats)
- [CVATでのデータセットエクスポート](#exporting-dataset-in-cvat)
  - [タスクからのデータセットエクスポート](#exporting-dataset-from-task)
  - [ジョブからのデータセットエクスポート](#exporting-dataset-from-job)
- [データエクスポートのビデオチュートリアル](#data-export-video-tutorial)

## データエクスポートフォーマット

以下の表は、CVATで利用可能なデータエクスポートフォーマットを示しています。

<!--lint disable maximum-line-length-->

| フォーマット                                                                                                                 | 種類           | コンピュータビジョンタスク                                      | モデル                                                                                                                                                                                 | シェイプ                                                                                      | 属性                 | ビデオトラック   |
|-----------------------------------------------------------------------------------------------------------------------------|---------------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------------------|------------------|
| [CamVid 1.0](format-camvid)                                                                                                | .txt <br>.png | セマンティック<br>セグメンテーション                           | U-Net, SegNet, DeepLab, <br>PSPNet, FCN, Mask R-CNN, <br>ICNet, ERFNet, HRNet, <br>V-Net など                                                                                          | ポリゴン                                                                                      | 未対応               | 未対応           |
| [Cityscapes 1.0](format-cityscapes)                                                                                        | .txt<br>.png  | セマンティック<br>セグメンテーション                           | U-Net, SegNet, DeepLab, <br>PSPNet, FCN, ERFNet, <br>ICNet, Mask R-CNN, HRNet, <br>ENet など                                                                                           | ポリゴン                                                                                      | 特定属性             | 未対応           |
| [COCO 1.0](format-coco)                                                                                                    | JSON          | 検出、セマンティック<br>セグメンテーション                      | YOLO (You Only Look Once), <br>Faster R-CNN, Mask R-CNN, SSD (Single Shot MultiBox Detector), <br> RetinaNet, EfficientDet, UNet, <br>DeepLabv3+, CenterNet, Cascade R-CNN など         | バウンディングボックス、ポリゴン                                                             | 特定属性             | 未対応           |
| [COCO Keypoints 1.0](coco-keypoints)                                                                                       | .xml          | キーポイント                                                   | OpenPose, PoseNet, AlphaPose, <br> SPM (Single Person Model), <br>Mask R-CNN with Keypoint Detection など                                         | スケルトン                                                                                   | 特定属性             | 未対応           |
| {{< ilink "/docs/manual/advanced/formats/format-cvat#cvat-for-image-export" "CVAT for images 1.1" >}}                      | .xml          | 2Dのいかなるもの（ビデオトラッキング除く）                      | フォーマットをデコードできる任意のモデル                                                                                                         | バウンディングボックス、ポリゴン、<br>ポリライン、ポイント、キューボイド、<br>スケルトン、楕円、マスク、タグ | すべての属性         | 未対応           |
| {{< ilink "/docs/manual/advanced/formats/format-cvat#cvat-for-videos-export" "CVAT for video 1.1" >}}                      | .xml          | 2Dのいかなるもの（分類除く）                                    | フォーマットをデコードできる任意のモデル                                                                                                         | バウンディングボックス、ポリゴン、<br>ポリライン、ポイント、キューボイド、<br>スケルトン、楕円、マスク      | すべての属性         | 対応              |
| [Datumaro 1.0](format-datumaro)                                                                                            | JSON          | いかなるもの                                                    | フォーマットをデコードできる任意のモデル。<br>[Datumaro](https://github.com/openvinotoolkit/datumaro) フレームワークの主要フォーマット              | バウンディングボックス、ポリゴン、<br>ポリライン、ポイント、キューボイド、<br>スケルトン、楕円、マスク、タグ | すべての属性         | 対応              |
| [ICDAR](format-icdar)<br> ICDAR Recognition 1.0,<br>ICDAR Detection 1.0,<br>ICDAR Segmentation 1.0<br>を含む                | .txt          | 文字認識、<br>文字検出、<br>文字セグメンテーション              | EAST: Efficient and Accurate <br>Scene Text Detector, CRNN, Mask TextSpotter, TextSnake など                                                    | タグ、バウンディングボックス、ポリゴン                                                      | 特定属性             | 未対応           |
| [ImageNet 1.0](format-imagenet)                                                                                            | .jpg <br>.txt | セマンティックセグメンテーション、<br>分類、<br>検出            | VGG (VGG16, VGG19), Inception, YOLO, Faster R-CNN , U-Net など                                                                                   | タグ                                                                                          | 属性なし             | 未対応           |
| [KITTI 1.0](format-kitti)                                                                                                  | .txt <br>.png | セマンティックセグメンテーション、検出、3D                      | PointPillars, SECOND, AVOD, YOLO, DeepSORT, PWC-Net, ORB-SLAM など                                                                               | バウンディングボックス、ポリゴン                                                             | 特定属性             | 未対応           |
| [LabelMe 3.0](format-labelme)                                                                                              | .xml          | 互換性、<br>セマンティックセグメンテーション                    | U-Net, Mask R-CNN, Fast R-CNN,<br> Faster R-CNN, DeepLab, YOLO など                                                                              | バウンディングボックス、ポリゴン                                                             | 対応（ポリゴン）      | 未対応           |
| [LFW 1.0](format-lfw)                                                                                                      | .txt          | 照合、<br>顔認識                                               | OpenFace, VGGFace & VGGFace2, <br>FaceNet, ArcFace など                                                                                          | タグ、スケルトン                                                                               | 特定属性             | 未対応           |
| [Market-1501 1.0](format-market1501)                                                                                       | .txt          | 再識別                                                         | Triplet Loss Networks, <br>Deep ReID models など                                                                                                | バウンディングボックス                                                                       | 特定属性             | 未対応           |
| [MOT 1.0](format-mot)                                                                                                      | .txt          | ビデオトラッキング、<br>検出                                   | SORT, MOT-Net, IOU Tracker など                                                                                                                 | バウンディングボックス                                                                       | 特定属性             | 対応              |
| [MOTS PNG 1.0](format-mots)                                                                                                | .png<br>.txt  | ビデオトラッキング、<br>検出                                   | SORT, MOT-Net, IOU Tracker など                                                                                                                 | バウンディングボックス、マスク                                                               | 特定属性             | 対応              |
| [Open Images 1.0](format-openimages)                                                                                       | .csv          | 検出、<br>分類、<br>セマンティックセグメンテーション            | Faster R-CNN, YOLO, U-Net, <br>CornerNet など                                                                                                   | バウンディングボックス、タグ、ポリゴン                                                       | 特定属性             | 未対応           |
| [PASCAL VOC 1.0](format-voc)                                                                                               | .xml          | 分類、検出                                                     | Faster R-CNN, SSD, YOLO, <br>AlexNet など                                                                                                       | バウンディングボックス、タグ、ポリゴン                                                       | 特定属性             | 未対応           |
| [Segmentation Mask 1.0](format-smask)                                                                                      | .txt          | セマンティックセグメンテーション                                | Faster R-CNN, SSD, YOLO, <br>AlexNet など                                                                                                       | ポリゴン                                                                                      | 属性なし             | 未対応           |
| [VGGFace2 1.0](format-vggface2)                                                                                            | .csv          | 顔認識                                                         | VGGFace, ResNet, Inception など                                                                                                                 | バウンディングボックス、ポイント                                                             | 属性なし             | 未対応           |
| [WIDER Face 1.0](format-widerface)                                                                                         | .txt          | 検出                                                           | SSD (Single Shot MultiBox Detector), Faster R-CNN, YOLO など                                                                                    | バウンディングボックス、タグ                                                                 | 特定属性             | 未対応           |
| [YOLO 1.0](format-yolo)                                                                                                    | .txt          | 検出                                                           | YOLOv1, YOLOv2 (YOLO9000), <br>YOLOv3, YOLOv4 など                                                                                              | バウンディングボックス                                                                       | 属性なし             | 未対応           |
| [Ultralytics YOLO Detection 1.0](format-yolo-ultralytics)                                                                  | .txt          | 検出                                                           | YOLOv8                                                                                                                                                                               | バウンディングボックス                                                                       | 属性なし             | 対応              |
| [Ultralytics YOLO Segmentation 1.0](format-yolo-ultralytics)                                                               | .txt          | インスタンスセグメンテーション                                 | YOLOv8                                                                                                                                                                               | ポリゴン、マスク                                                                             | 属性なし             | 対応              |
| [Ultralytics YOLO Pose 1.0](format-yolo-ultralytics)                                                                       | .txt          | キーポイント                                                   | YOLOv8                                                                                                                                                                               | スケルトン                                                                                   | 属性なし             | 対応              |
| [Ultralytics YOLO Oriented Bounding Boxes 1.0](format-yolo-ultralytics)                                                    | .txt          | 検出                                                           | YOLOv8                                                                                                                                                                               | バウンディングボックス                                                                       | 属性なし             | 対応              |
| [Ultralytics YOLO Classification 1.0](format-yolo-ultralytics-classification)                                              | .jpg          | 分類                                                           | YOLOv8                                                                                                                                                                               | タグ                                                                                          | 属性なし             | 未対応           |


<!--lint enable maximum-line-length-->

## CVATでのデータセットエクスポート

### タスクからのデータセットエクスポート

タスクからデータセットをエクスポートするには、以下の手順に従います。

1. タスクを開きます。
2. **アクション** > **タスクデータセットのエクスポート** を選択します。
3. 利用可能なオプションから希望するフォーマットを選択します。

4. （オプション）エクスポートに画像を含めたい場合は
   **画像を保存** スイッチを有効にします。

   > **注意**: **画像を保存** オプションは **有料機能** です。

   ![画像を保存オプション](/images/export_job_as_dataset_dialog.png)

5. 作成される `.zip` アーカイブの名前を入力します。

6. **OK** をクリックしてエクスポートを開始します。

### ジョブからのデータセットエクスポート

ジョブからデータセットをエクスポートするには、以下の手順に従います。

1. **メニュー** > **ジョブデータセットのエクスポート** に移動します。

   ![データセットをエクスポート](/images/export_job_as_dataset_menu.png)

2. 利用可能なオプションから希望するフォーマットを選択します。

3. （オプション）エクスポートに画像を含めたい場合は
   **画像を保存** スイッチを有効にします。

   > **注意**: **画像を保存** オプションは **有料機能** です。

   ![画像を保存オプション](/images/export_job_as_dataset_dialog.png)

4. 作成される `.zip` アーカイブの名前を入力します。

5. **OK** をクリックしてエクスポートを開始します。

## データエクスポートのビデオチュートリアル

手順の詳細については、以下のチュートリアルをご覧ください。

<!--lint disable maximum-line-length-->

<iframe width="560" height="315" src="https://www.youtube.com/embed/gzjVpVV9orE?si=2tiBIqts8nk_byTH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<!--lint enable maximum-line-length-->