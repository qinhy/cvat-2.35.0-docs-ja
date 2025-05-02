---
title: 'フィルター'
linkTitle: 'フィルター'
weight: 24
description: 'CVATのフィルター機能の使い方ガイド。'
---

この機能を使用する理由はいくつかあります：

1. フィルターを使用すると、フィルター条件に一致しないオブジェクトが非表示になります。
1. 興味のあるオブジェクトが存在するフレーム間を素早く移動できます。
   この目的には `左矢印` / `右矢印` キーを使用するか、
   UIボタンを右クリックして `フィルターで切り替え` を選択してカスタマイズできます。
   フィルターに対応するオブジェクトがない場合は、
   アノテーション済みオブジェクトが含まれる前/次のフレームへ移動します。

フィルターを適用するには、上部パネルのボタンをクリックします。

![](/images/image059.jpg)

## フィルターの作成

フィルター入力用のウィンドウが開きます。ここには `ルール追加` と `グループ追加` の2つのボタンがあります。

![](/images/image202.jpg)

### ルール

`ルール追加` ボタンはオブジェクト表示のためのルールを追加します。ルールでは以下のプロパティが使用できます：

![](/images/image204.jpg)

### アノテーションのサポートプロパティ

| プロパティ   | サポート値                                       | 説明                                 |
| ------------ | ------------------------------------------------ | ------------------------------------ |
| `Label`      | タスク内のすべてのラベル名                       | ラベル名                             |
| `Type`       | shape, track, tag                                | オブジェクトの種類                   |
| `Shape`      | すべてのシェイプタイプ                           | シェイプの種類                       |
| `Occluded`   | true または false                                | オクルード（{{< ilink "/docs/manual/advanced/shape-mode-advanced" "詳細はこちら" >}}）|
| `Width`      | px数またはフィールド                             | シェイプの幅                         |
| `Height`     | px数またはフィールド                             | シェイプの高さ                       |
| `ServerID`   | 数値またはフィールド                             | サーバー上のオブジェクトID <br>（アクションメニューからオブジェクトへのリンクを形成して確認可能）|
| `ObjectID`   | 数値またはフィールド                             | クライアント内のオブジェクトID <br>（オブジェクトサイドバーに表示）|
| `Attributes` | 類似タイプまたは特定属性値を持つ<br>他のフィールドを含む | ラベルで指定された任意のフィールド   |

- {{< ilink "/docs/manual/advanced/projects#supported-properties-for-projects-list"
    "プロジェクトリストのサポートプロパティ" >}}

- {{< ilink "/docs/manual/basics/tasks-page#supported-properties-for-tasks-list"
    "タスクリストのサポートプロパティ" >}}

- {{< ilink "/docs/manual/basics/jobs-page#supported-properties-for-jobs-list"
    "ジョブリストのサポートプロパティ" >}}

- {{< ilink "/docs/manual/basics/cloud-storages#supported-properties-for-cloud-storages-list"
    "クラウドストレージリストのサポートプロパティ" >}}

### プロパティで使用可能な演算子

`==` - 等しい; `!=` - 等しくない; `>` - より大きい; `>=` - 以上; `<` - より小さい; `<=` - 以下;

`Any in`; `Not in` - この演算子は1つのルールで複数の値を設定できます。

![](/images/image203.jpg)

`Is empty`; `is not empty` – これらの演算子は値の入力が不要です。

`Between`; `Not between` – 2つの値の範囲を選択できます。

`Like` - この演算子は、プロパティが値を含む必要があることを示します。

`Starts with`; `Ends with` - 始まりまたは終わりでフィルタリングします。

一部のプロパティは、選択可能な2種類の値をサポートしています：

![](/images/image205.jpg)

複数のルールを追加できます。ルール追加ボタンをクリックし、別のルールを設定してください。
新しいルールを設定した後、それらをどの演算子（`And` または `Or`）で接続するか選択できます。

![](/images/image206.jpg)

以降に追加されるルールは選択した演算子で結合されます。
`送信` をクリックしてフィルターを適用するか、複数の演算子でルールを結合したい場合はグループを使用してください。

### グループ

グループを追加するには、`グループ追加` ボタンをクリックします。グループ内ではルールやグループを作成できます。

![](/images/image207.jpg)

グループ内に複数のルールがある場合、それらは `And` または `Or` 演算子で結合できます。
ルールグループはグループ外の個別ルールと同様に動作し、
グループ外の演算子で結合されます。
グループ内でさらにグループを作成するには、グループ内のグループ追加ボタンをクリックします。

ルールやグループは移動できます。ルールまたはグループを移動するには、該当ボタンでドラッグしてください。
ルールやグループを削除するには、`削除` ボタンをクリックします。

![](/images/image208.jpg)

`Not` ボタンを有効にすると、グループに一致しないオブジェクトが除外されます。
`送信` をクリックしてフィルターを適用します。
`キャンセル` ボタンはフィルターを取り消します。`フィルタークリア` ボタンはフィルターを削除します。

適用されたフィルターは自動的に `最近使用` リストに表示されます。リストの最大数は10です。

---

## リストの並べ替えとフィルター

{{< ilink "/docs/manual/advanced/projects#projects-page" "プロジェクト" >}}ページのタスクリストや、
{{< ilink "/docs/manual/basics/tasks-page" "タスク" >}}, {{< ilink "/docs/manual/basics/jobs-page" "ジョブ" >}},
{{< ilink "/docs/manual/basics/cloud-storages" "クラウドストレージ" >}} ページで並べ替えやフィルターが利用できます。

> 適用されたフィルターや並べ替え条件はブラウザのURLに表示されるため、
> フィルターや並べ替えを適用したページを共有できます。

### 並べ替え基準

次のパラメーターで並べ替えが可能です：
- ジョブリスト：ID、担当者、更新日、[stage][stage]、[state][state]、タスクID、プロジェクトID、タスク名、プロジェクト名
- タスクリストおよびプロジェクトページ内タスクリスト：ID、オーナー、ステータス、担当者、更新日、[subset][subset]、[mode][mode]、[dimension][dimension]、プロジェクトID、名前、プロジェクト名
- プロジェクトリスト：ID、担当者、オーナー、ステータス、名前、更新日
- クラウドストレージリスト：ID、プロバイダータイプ、更新日、表示名、[resource][resource]、[credentials][credentials]、オーナー、説明

並べ替えを適用するには、パラメーターを横線上部のエリアへドラッグします。
横線下のパラメーターは適用されません。
パラメーターを移動することで優先順位を変更でき、
上部のパラメーターから順に並べ替えが行われます。

`並べ替えボタン` を押すと `昇順`/`降順` を切り替えられます。

### クイックフィルター

クイックフィルターにはよく使われるものが含まれます：
- `Assigned to me` - あなたに割り当てられたプロジェクト、タスク、ジョブのみ表示
- `Owned by me` - あなたが所有するプロジェクトまたはタスクのみ表示
- `Not completed` - 完了以外のステータスのプロジェクト、タスク、ジョブのみ表示
- `AWS storages` - AWSクラウドストレージのみ表示
- `Azure storages` - Azureクラウドストレージのみ表示
- `Google cloud storages` - Googleクラウドストレージのみ表示

#### 日付と時刻の選択

`最終更新` ルール作成時、選択ウィンドウで日付と時刻を選択できます。

![](/images/image244_detrac.jpg)

矢印や年・月をクリックして年や月を選択できます。
カレンダーで日付をクリックして日を選択し、
スクロールリストで時間（時・分）を選択できます。
`現在` ボタンで現在の日時を選択することも可能です。
適用するには `OK` をクリックしてください。

[state]: /docs/manual/basics/vocabulary/#state
[stage]: /docs/manual/basics/vocabulary/#stage
[subset]: /docs/manual/basics/vocabulary/#subset
[resource]: /docs/manual/basics/vocabulary/#resource
[credentials]: /docs/manual/basics/vocabulary/#credentials
[mode]: /docs/manual/basics/vocabulary/#mode
[dimension]: /docs/manual/basics/vocabulary/#dimension
