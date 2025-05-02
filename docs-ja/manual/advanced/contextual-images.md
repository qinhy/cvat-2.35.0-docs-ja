---
title: 'コンテキスト画像'
linkTitle: 'コンテキスト画像'
weight: 26
description: 'タスクのコンテキスト画像'
---

コンテキスト画像とは、主画像に関連するコンテキストや追加情報を提供するための補助的な画像です。

対象物についてのコンテキストを追加してアノテーションの精度を向上させるために使用します。

コンテキスト画像は2Dおよび3Dタスクで利用可能です。

参照：

- [フォルダ構成](#folder-structure)
- [データ形式](#data-format)
- [コンテキスト画像](#contextual-images)

## フォルダ構成

タスクにコンテキスト画像を追加するには、画像フォルダを整理する必要があります。

CVATにアーカイブをアップロードする前に、以下を行ってください：

1. アノテーション用画像が入ったフォルダ内に `related_images` フォルダを作成します。
2. `related_images` 内に、リンクしたい主画像と同じ名前のサブフォルダを作成します。
3. 手順2で作成したサブフォルダ内に、コンテキスト画像を配置します。
4. フォルダをアーカイブに追加します。
5. {{< ilink "/docs/manual/basics/create_an_annotation_task#create-a-task" "タスク作成" >}}。

## データ形式

2Dおよび3Dタスクのファイル構成例：

{{< tabpane >}}
{{< tab header="2Dタスク" >}}
  root_directory
    image_1_to_be_annotated.jpg
    image_2_to_be_annotated.jpg
    related_images/
      image_1_to_be_annotated_jpg/
        context_image_for_image_1.jpg
      image_2_to_be_annotated_jpg/
        context_image_for_image_2.jpg
     subdirectory_example/
        image_3_to_be_annotated.jpg
         related_images/
          image_3_to_be_annotated_jpg/
             context_image_for_image_3.jpg
{{< /tab >}}
{{< tab header="3Dオプション1" >}}
 root_directory
    pointcloud/
      image_1_to_be_annotated.pcd
      image_2_to_be_annotated.pcd
    related_images/
      image_1_to_be_annotated_pcd/
        context_image_for_image_1.jpg
      image_2_to_be_annotated_pcd/
        context_image_for_image_2.jpg
{{< /tab >}}
{{< tab header="3Dオプション2" >}}
 /any_directory
    pointcloud.pcd
    pointcloud.jpg
/any_other_directory
    /any_subdirectory
        pointcloud.pcd
        pointcloud.png
{{< /tab >}}
{{< tab header="3Dタスク KITTI形式" >}}
 /image_00
    /data
        /0000000000.png
        /0000000001.png
        /0000000002.png
        /0000000003.png
/image_01
    /data
        /0000000000.png
        /0000000001.png
        /0000000002.png
        /0000000003.png
/image_02
    /data
        /0000000000.png
        /0000000001.png
        /0000000002.png
        /0000000003.png
/image_N
    /data
        /0000000000.png
        /0000000001.png
        /0000000002.png
        /0000000003.png
/velodyne_points
    /data
        /0000000000.bin
        /0000000001.bin
        /0000000002.bin
        /0000000003.bin
{{< /tab >}}
{{< /tabpane >}}

- KITTIの場合：`image_00`、`image_01`、`image_02`、`image_N`
（ここで `N` は12以下の任意の数） はコンテキスト画像です。
- 3Dオプション3の場合：同名の.pcdファイルの近くに通常の画像ファイルが配置されていれば、それがコンテキスト画像と見なされます。

3Dデータ形式に関する一般的な情報については、
{{< ilink "/docs/manual/basics/create_an_annotation_task#data-formats-for-a-3d-task" "3Dデータ形式" >}} を参照してください。

## コンテキスト画像

コンテキスト画像の最大数は12枚です。

デフォルトでは主画像の右側に配置されます。

> **注意:** デフォルトでは、3枚のコンテキスト画像のみが表示されます。

![contex_images_1](/images/context_img_01.jpg)

コンテキスト画像をセットに追加すると、
画面上部に小さなツールバーが表示され、以下の要素が含まれます：

<!--lint disable maximum-line-length-->

| 要素                                         | 説明                                                                                                                                                                                                                  |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![contex_images_4](/images/context_img_04.jpg) | **ビューをフィット**。クリックするとレイアウトを元の状態に戻します。<p>レイアウト内で画像を拡大していた場合は元のサイズに戻ります。<p>画面上のコンテキスト画像数には影響しません。                  |
| ![contex_images_5](/images/context_img_05.jpg) | **新しい画像を追加**。クリックでレイアウトにコンテキスト画像を追加します。                                                                                                     |
| ![contex_images_6](/images/context_img_06.jpg) | **レイアウトの再読み込み**。クリックするとレイアウトをデフォルト表示に戻します。<p>この操作により表示されているコンテキスト画像数が3枚にリセットされることがあります。                           |

<!--lint enable maximum-line-length-->

各コンテキスト画像には以下の要素があります：

![contex_images_2](/images/context_img_02.jpg)

<!--lint disable maximum-line-length-->

| 要素 | 説明                                                                                                           |
| ---- | -------------------------------------------------------------------------------------------------------------- |
| 1    | **全画面**。クリックでコンテキスト画像を全画面表示します。<p>もう一度クリックするとウィンドウ表示に戻ります。    |
| 2    | **コンテキスト画像の移動**。長押しして他の場所にドラッグできます。<p>![contex_images_3](/images/context_img_03.gif) |
| 3    | **名前**。ユニークなコンテキスト画像名                                                                           |
| 4    | **コンテキスト画像の選択**。クリックで利用可能な全てのコンテキスト画像の横並びリストビューを開きます。<p>クリックで選択。 |
| 5    | **閉じる**。クリックでコンテキスト画像メニューから画像を削除します。                                             |
| 6    | **拡張**。長押しして画像を拡大します。                                                                         |

<!--lint enable maximum-line-length-->