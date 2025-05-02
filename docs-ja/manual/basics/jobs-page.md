---
title: 'ジョブページ'
linkTitle: 'ジョブページ'
weight: 4
---

ジョブページでは、ユーザー（たとえば、ワーカーロールを持つユーザー）が、タスクページへのアクセス権がなくても、自分に割り当てられたジョブを確認したり、進捗を追跡したり、ジョブリストを並べ替えたりフィルターを適用したりできます。

![](/images/image243_detrac.jpg)

ジョブページにはジョブのリストがタイル形式で表示され、各タイルが1つのジョブを表します。
各要素には以下が含まれます：
- ジョブID
- 次元　`2D` または `3D`
- プレビュー
- [ステージ][stage] と [状態][state]
- 要素にカーソルを合わせると表示される情報：
  - サイズ
  - 担当者
- タスク、プロジェクト、バグトラッカーへのナビゲーションメニュー

> ジョブを新しいタブで開くには、`Ctrl` を押しながらジョブをクリックしてください。

左上には検索バーがあり、担当者、ステージ、状態などでジョブを検索できます。
右上には[並べ替え][sorting]、[クイックフィルター][quick-filters]、およびフィルターがあります。

## フィルター

> フィルターを適用すると、[クイックフィルター][quick-filters]は無効になります。

フィルターはアノテーション用フィルターと同様に機能し、
[プロパティ](#supported-properties-for-jobs-list)、[演算子][operators]、値からルールを作成し、
ルールを[グループ][groups]にまとめることができます。詳細は[フィルターのセクション][create-filter]をご覧ください。
[日付と時刻の選択][data-and-time]についても参照してください。

すべてのフィルターをクリアするには「Clear filters」を押してください。

### ジョブリストでサポートされているプロパティ

| プロパティ         | サポートされる値                                  | 説明                                                         |
| ------------------ | ----------------------------------------------- | ------------------------------------------------------------ |
| `状態`             | すべての状態名                                   | ジョブの状態 <br>（ジョブ内のメニューで変更可能）           |
| `ステージ`         | すべてのステージ名                               | ジョブのステージ <br>（タスクページのドロップダウンリストで指定）|
| `次元`             | `2D` または `3D`                                | データ形式による <br>（[アノテーションタスクの作成][create-task]を参照）|
| `担当者`           | ユーザー名                                       | 担当者はそのジョブを担当しているユーザー <br>（タスクページで指定）|
| `最終更新日`       | 最終編集日時（または値の範囲）                   | 日付は `dd.MM.yyyy HH:mm` 形式で入力でき、<br>入力フィールドをクリックすると表示されるウィンドウからも選択可能 |
| `ID`               | ジョブIDまたはその範囲                            |                                                              |
| `タスクID`         | タスクIDまたはその範囲                            |                                                              |
| `プロジェクトID`   | プロジェクトIDまたはその範囲                      |                                                              |
| `タスク名`         | タスク名                                          | タスク作成時に設定 <br>（{{< ilink "/docs/manual/basics/task-details" "タスクページ" >}}で変更可能）|
| `プロジェクト名`   | プロジェクト名                                    | プロジェクト作成時に設定 <br>（{{< ilink "/docs/manual/advanced/projects" "プロジェクトセクション" >}}で変更可能）|

[state]: /docs/manual/basics/vocabulary/#state
[stage]: /docs/manual/basics/vocabulary/#stage
[create-task]: /docs/manual/basics/create_an_annotation_task
[create-filter]: /docs/manual/advanced/filter/#create-a-filter
[operators]: /docs/manual/advanced/filter/#supported-operators-for-properties
[groups]: /docs/manual/advanced/filter/#groups
[data-and-time]: /docs/manual/advanced/filter#date-and-time-selection
[sorting]: /docs/manual/advanced/filter/#sort-by
[quick-filters]: /docs/manual/advanced/filter/#quick-filters