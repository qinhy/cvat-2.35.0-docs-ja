---
title: 'プロジェクトページ'
linkTitle: 'プロジェクトページ'
weight: 1
description: 'CVATでのプロジェクトの作成とエクスポート。'
---

## プロジェクトページ

このページでは、新しいプロジェクトの作成、バックアップからのプロジェクト作成、作成済みプロジェクトの一覧表示ができます。

左上には検索バーがあり、プロジェクト名や担当者などでプロジェクトを検索できます。
右上には[並び替え][sorting]、[クイックフィルター][quick-filters]、およびフィルターがあります。

## フィルター

> フィルターを適用すると[クイックフィルター][quick-filters]は無効になります。

フィルターはアノテーション用のフィルターと同様に動作します。
[プロパティ](#supported-properties-for-projects-list)、[演算子][operators]、値からルールを作成し、[グループ][groups]としてルールをまとめることができます。
詳細は[フィルターセクション][create-filter]を参照してください。
[日付と時刻の選択][data-and-time]について詳しくはこちら。

すべてのフィルターをクリアするには「Clear filters」を押してください。

### プロジェクト一覧でサポートされているプロパティ

| プロパティ       | サポートされている値                  | 説明                                                                                       |
| -------------- | ------------------------------------ | ---------------------------------------------------------------------------------------- |
| `Assignee`     | ユーザー名                            | 担当者はプロジェクト・タスク・ジョブに取り組んでいるユーザーです。<br>(タスクページで指定)     |
| `Owner`        | ユーザー名                            | プロジェクト・タスク・ジョブの所有者                                                      |
| `Last updated` | 最終更新日時（または範囲）             | 日付は `dd.MM.yyyy HH:mm` 形式で入力するか、入力欄をクリックして表示されるウィンドウで選択可 |
| `ID`           | ジョブIDの番号または範囲               |                                                                                          |
| `Name`         | 名前                                  | タスクページではタスク名、<br>プロジェクトページではプロジェクト名                             |

## プロジェクトの作成

CVATでは、同じタイプのタスクを含むプロジェクトを作成できます。
プロジェクトに関連するすべてのタスクは、ラベルリストを継承します。

プロジェクトを作成するには、トップメニューの「Projects」をクリックしてプロジェクトセクションに移動します。
プロジェクトページでは、プロジェクト一覧の表示、検索の利用、
「+」ボタンをクリックして「Create New Project」を選択することで新しいプロジェクトを作成できます。

![](/images/image190.jpg)

> プロジェクトは作成時に選択した組織内で作成されます。
> {{< ilink "/docs/manual/advanced/organization" "組織" >}}について詳しくはこちら。

プロジェクト名、ラベルリスト（このプロジェクトで作成されるタスクに使用）、
必要に応じてスケルトンを変更できます。
詳細設定では、課題へのリンクやソース・ターゲットストレージも指定できます。
{{< ilink "/docs/manual/basics/create_an_annotation_task#labels" "ラベルリストの作成" >}}、
{{< ilink "/docs/manual/advanced/skeletons" "スケルトンの作成" >}}、
{{< ilink "/docs/manual/basics/attach-cloud-storage" "クラウドストレージの添付" >}}について詳しくはこちら。

プロジェクトを保存して開くには「Submit & Open」ボタンをクリックします。
また、連続して複数のプロジェクトを作成したい場合は「Submit & Continue」ボタンをクリックします。

![](/images/image191.jpg)

作成後、プロジェクトはプロジェクトページに表示されます。プロジェクトを開くには、そのプロジェクトをクリックしてください。

![](/images/image192_mapillary_vistas.jpg)

ここで以下の操作が可能です:

1. プロジェクトタイトルの変更
1. 「Actions」メニューを開く。「Actions」メニュー内の各ボタンは特定の機能を担当します。
   - `Export dataset`/`Import dataset`：特定のフォーマットでアノテーションやアノテーション＋画像のダウンロード／アップロード。
     詳細は{{< ilink "/docs/manual/advanced/import-datasets" "データセットのエクスポート／インポート" >}}セクション参照。
   - `Backup project`：プロジェクトのバックアップ作成。詳細は{{< ilink "/docs/manual/advanced/backup" "バックアップ" >}}セクション参照。
   - `Delete`：プロジェクトと関連タスクをすべて削除。
1. イシュートラッカーの変更または、指定されていればイシュートラッカーを開く。
1. ラベルやスケルトンの変更。
   「Raw」モードまたは「Constructor」モードで新しいラベルや既存ラベルへの属性追加が可能です。
   ラベルごとに色の変更もできます。
   「Setup skeleton」をクリックすると、このプロジェクト用のスケルトンを作成できます。

1. 「Assigned to」―プロジェクトを担当者に割り当てる際に使用します。
   担当者名を入力し、ドロップダウンリストから該当者を選択してください。
1. 「Tasks」―特定プロジェクトのすべてのタスクの一覧で、タスクの検索・並び替え・フィルターが可能です。
   {{< ilink "/docs/manual/advanced/search" "検索について詳しくはこちら" >}}。
   {{< ilink "/docs/manual/advanced/filter#sort-and-filter-projects-tasks-and-jobs"
     "並び替え・フィルターについて詳しくはこちら" >}}
プロジェクト内のタスクでサブセットを選択することも可能です。利用可能な選択肢（`Train`、`Test`、`Validation`）や独自のサブセットを設定できます。

[create-filter]: /docs/manual/advanced/filter/#create-a-filter
[operators]: /docs/manual/advanced/filter/#supported-operators-for-properties
[groups]: /docs/manual/advanced/filter/#groups
[data-and-time]: /docs/manual/advanced/filter#date-and-time-selection
[sorting]: /docs/manual/advanced/filter/#sort-by
[quick-filters]: /docs/manual/advanced/filter/#quick-filters