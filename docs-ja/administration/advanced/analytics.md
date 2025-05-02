---
title: 'CVAT アナリティクスとモニタリング'
linkTitle: 'CVAT アナリティクスとモニタリング'
weight: 20
description: 'アナリティクスおよびモニタリングの導入とカスタマイズ手順。'
---

CVAT アナリティクスツール群は、ユーザーの行動やシステムパフォーマンスの追跡、およびアプリケーション内の潜在的な問題の特定を目的としています。

また、Grafana を使ってユーザーアクティビティを可視化したり、
ジョブごとにユーザーの作業時間を集計することも可能です。

収集されたログは、効率的なデバッグのために追加でフィルタリングできます。

アナリティクスを活用することで、システムの最適化や
ユーザー満足度の向上につながる貴重なインサイトを得られます。

CVAT アナリティクスはトップメニューから利用できます。

スーパーユーザーおよび管理者権限を持つユーザーはアナリティクスにアクセスできます。
アナリティクスへのアクセス権は、管理ページでユーザー編集時に
「アナリティクスへのアクセス権」チェックボックスを有効にすることでも付与できます。

![CVAT Analytics](/images/analytics_menu.jpg)

> 注: CVAT アナリティクスおよびモニタリングはオンプレミス・ソリューションのみで利用可能です。

参照:

- [ハイレベルアーキテクチャ](#high-level-architecture)
- [CVAT アナリティクス](#cvat-analytics)
  - [ポート設定](#ports-settings)
  - [イベントログ構造](#events-log-structure)
  - [サポートされているイベントの種類](#types-of-supported-events)
  - [作業時間の計算](#working-time-calculation)
  - [トラッキング用リクエスト`id`](#request-id-for-tracking)
  - [`/api/events` エンドポイントからCSVでイベントデータ取得](#fetching-event-data-as-csv-from-the-apievents-endpoint)
- [ダッシュボード](#dashboards)
  - [ダッシュボード: 全イベント](#dashboard-all-events)
  - [ダッシュボード: 管理](#dashboard-management)
  - [ダッシュボード: モニタリング](#dashboard-monitoring)
  - [ダッシュボード設定](#dashboards-setup)
- [利用例](#example-of-use)

## ハイレベルアーキテクチャ

CVAT アナリティクスは Vector、ClickHouse、Grafana を基盤としています。

![CVAT Analytics](/images/analytic_architecture.jpg)

## CVAT アナリティクス

CVAT とそのアナリティクスモジュールはローカルでセットアップ可能で、
セルフホスト型の場合はアナリティクスがデフォルトで有効になっています。

> CVAT の詳細なインストール手順は
> {{< ilink "/docs/administration/basics/installation" "インストールガイド" >}}
> または [CVATコース](https://www.youtube.com/playlist?list=PL0to7Ng4PuuYQT4eXlHb_oIlq_RPeuasN)
> のインストール動画を参照してください。

アナリティクス関連の機能は、以下のコマンドで
CVAT コンテナを起動すると有効になります。

```shell
docker compose up -d
```

### ポート設定

開発環境でアナリティクスにアクセスできない場合は、
{{< ilink "/docs/contributing/development-environment#cvat-analytics-ports" "アナリティクスポート" >}} を参照してください。

### イベントログ構造

[リレーショナルデータベース](https://github.com/cvat-ai/cvat/blob/develop/components/analytics/clickhouse/init.sh)
のスキーマは以下のフィールドを持ちます。

<!--lint disable maximum-line-length-->

| フィールド      | 説明                                                                                                   |
| -------------- | ------------------------------------------------------------------------------------------------------ |
| scope          | イベントのスコープ（例：`zoomin:image`、`add:annotations`、`delete:image`、`update:assignee`など）      |
| obj_name       | オブジェクト名またはNone（例：task、job、cloudstorage、model、organizationなど）                        |
| obj_id         | DB上のオブジェクト識別子またはNone                                                                     |
| obj_val        | イベントの値（例：フレーム番号、追加アノテーション数など）またはNone                                    |
| source         | ログイベントの発生元（例：server, ui）                                                                 |
| timestamp      | ローカルイベント時刻（通常UIとサーバーで異なります）                                                    |
| count          | 行で発生した回数                                                                                       |
| duration       | 所要時間（durationのないイベントは0）                                                                  |
| project_id     | プロジェクトIDまたはNone                                                                               |
| task_id        | タスクIDまたはNone                                                                                     |
| job_id         | ジョブIDまたはNone                                                                                     |
| user_id        | ユーザーIDまたはNone                                                                                   |
| user_name      | ユーザー名またはNone                                                                                   |
| user_email     | ユーザーEメールまたはNone                                                                              |
| org_id         | 組織IDまたはNone                                                                                       |
| org_slug       | 組織スラッグまたはNone                                                                                 |
| payload        | JSONペイロードまたはNone。追加フィールドはJSON blobに追加可能。                                         |

<!--lint enable maximum-line-length-->

### サポートされているイベントの種類

サポートされているイベントにより、Grafanaで表示される情報の範囲が変わります。

![Supported Events](/images/supported_events.jpg)

<!--lint disable maximum-line-length-->

サーバーイベント:

- `create:project`, `update:project`, `delete:project`

- `create:task`, `update:task`, `delete:task`

- `create:job`, `update:job`, `delete:job`

- `create:organization`, `update:organization`, `delete:organization`

- `create:user`, `update:user`, `delete:user`

- `create:cloudstorage`, `update:cloudstorage`, `delete:cloudstorage`

- `create:issue`, `update:issue`, `delete:issue`

- `create:comment`, `update:comment`, `delete:comment`

- `create:annotations`, `update:annotations`, `delete:annotations`

- `create:label`, `update:label`, `delete:label`

- `export:dataset`, `import:dataset`

- `call:function`

- `create:membership`, `update:membership`, `delete:membership`

- `create:webhook`, `update:webhook`, `delete:webhook`

- `create:invitation`, `delete:invitation`

クライアントイベント:

- `load:cvat`

- `load:job`, `save:job`

- `send:exception`

- `draw:object`, `paste:object`, `copy:object`, `propagate:object`, `drag:object`, `resize:object`, `delete:object`, `merge:objects`, `split:objects`, `group:objects`, `slice:object`,
`join:objects`

- `change:frame`

- `zoom:image`, `fit:image`, `rotate:image`

- `action:undo`, `action:redo`

- `run:annotations_action`

- `click:element`

- `debug:info`

<!--lint enable maximum-line-length-->

### 作業時間の計算

CVATがユーザーの作業時間をどのように扱うかの概要は以下の通りです。

- ユーザーインターフェイスは、ユーザーがインターフェイスとやり取りした際にイベントを収集します
  （キャンバスのリサイズ、オブジェクトの描画、ボタンのクリックなど）。
  単一イベントの構造は[こちら](#events-log-structure)で説明しています。

- UIはこれらのイベントをまとめてサーバーへ送信します。
  現在、イベント送信のトリガーは以下です。
  - 定期タイマー（約90秒ごと）
  - アノテーションビューで「保存」ボタンをクリック
  - アノテーションビューを開く
  - アノテーションビューを閉じる時（タブやブラウザ終了時は除く）
  - **ログアウト**ボタンをクリック

- イベントがサーバーに到達すると、イベントのタイムスタンプに基づき作業時間を計算します。

- 各イベントの作業時間は以下の合計で算出されます。
  - 前回イベント終了時刻から今回イベント開始時刻までの差が100秒以内であればその差分
  - `change:frame`タイプのイベントはイベントのduration

- 計算後、サーバーはペイロードに時間値を含む`send:working_time`イベントを生成します。
  これらのイベントは、発生元のクライアントイベント次第で、特定のジョブやタスク、プロジェクトに紐付かない場合もあります。

- CVATはイベントをDBに保存し、後にこれらイベントをもとにアナリティクスメトリクスを算出します。

### トラッキング用リクエスト`id`

各APIリクエストのレスポンスには
`X-Request-Id`というヘッダーが含まれています。
例: `X-Request-Id: 6a2b7102-c4b9-4d57-8754-5658132ba37d`

この識別子は、そのリクエストに起因するすべてのサーバーイベントにも記録されます。

例えばタスク作成操作を行った際、
**Task**オブジェクト以外にもラベルやアトリビュート等の
関連エンティティがサーバーで生成されます。

この操作に関連するすべてのイベントのpayloadフィールドには同じ`request_id`が記録されます。

### `/api/events` エンドポイントからCSVでイベントデータ取得

<!--lint disable maximum-line-length-->

`/api/events` エンドポイントでは、
`org_id`, `project_id`, `task_id`, `job_id`, `user_id`
などのフィルターパラメータを使って
イベントデータを取得できます。

詳細は [Swagger API Documentation](https://app.cvat.ai/api/swagger/#/events/events_list)
を参照してください。

例えば特定ジョブに関連するすべてのイベントを取得するには、
以下の `curl` コマンドを使用します。

```bash
curl --user 'user:pass' https://app.cvat.ai/api/events?job_id=123
```

レスポンスでクエリーIDが返されます。

```json
{ "query_id": "150cac1f-09f1-4d73-b6a5-5f47aa5d0031" }
```

この処理には時間がかかる場合があるため、
リクエストに`query_id`パラメータを追加して
ステータスを確認できます。

```bash
curl -I --user 'user:pass' https://app.cvat.ai/api/events?job_id=123&query_id=150cac1f-09f1-4d73-b6a5-5f47aa5d0031
```

正常に作成されると、サーバーは `201 Created` ステータスを返します。

```
HTTP/2 201
allow: GET, POST, HEAD, OPTIONS
date: Tue, 16 May 2023 13:38:42 GMT
referrer-policy: same-origin
server: Apache
vary: Accept,Origin,Cookie
x-content-type-options: nosniff
x-frame-options: DENY
x-request-id: 4631f5fa-a4f0-42a8-b77b-7426fc298a85
```

CSVファイルをダウンロードするには、
リクエストに`action=download`クエリパラメータを追加してください。

```bash
curl --user 'user:pass' https://app.cvat.ai/api/events?job_id=123&query_id=150cac1f-09f1-4d73-b6a5-5f47aa5d0031&action=download > /tmp/events.csv
```

これにより、ローカルマシンの `/tmp/events.csv`
にファイルがダウンロード・保存されます。

<!--lint enable maximum-line-length-->

## ダッシュボード

デフォルトで、CVAT には3つのダッシュボードが用意されています。

アクセスするには、**General** をクリックすると、利用可能な
ダッシュボード一覧ページに移動します。

![List of dashboards](/images/dashboard_00.jpg)

<!--lint disable maximum-line-length-->

| ダッシュボード      | 説明                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------ |
| **全イベント**     | すべてのイベントログ、タイムスタンプ、発生元を表示するダッシュボード                 |
| **管理**           | ユーザーの作業時間やアクティビティ情報等、ユーザーアクティビティに関するダッシュボード |
| **モニタリング**   | サーバーログやエラーを含むダッシュボード                                             |

<!--lint enable maximum-line-length-->

### ダッシュボード: 全イベント

このダッシュボードでは、すべてのイベントとタイムスタンプ、発生元を表示します。

![Dashboard: All Events](/images/dashboard_01.jpg)

<!--lint disable maximum-line-length-->

| 要素                    | 説明                                                                                                              |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **フィルター**         | ドロップダウンリストや検索フィールドとして利用可能。矢印をクリックで有効化。                                        |
| **全体アクティビティ** | 指定フィルターでの全体アクティビティのグラフ。                                                                    |
| **Scope**              | ユーザーアクティビティ。[サポートされているイベントの種類](#types-of-supported-events)参照。                        |
| **obj_name**           | **Scope**に関連するオブジェクトやアイテム。                                                                      |
| **obj_id**             | オブジェクトID。空の場合あり。                                                                                    |
| **source**             | イベントの発生元。`client` または `server`。                                                                     |
| **timestamp**          | イベント発生時刻。                                                                                                |
| **count**              | すべてのイベント共通フィールド。有効な場合はnull以外。例：アノテーション保存数など。                               |
| **duration**           | ミリ秒単位の所要時間。                                                                                            |
| **project_id**         | プロジェクトID。                                                                                                  |
| **project_id**         | プロジェクトID。                                                                                                  |
| **task_id**            | タスクID。                                                                                                        |
| **job_id**             | ジョブID。                                                                                                        |

<!--lint enable maximum-line-length-->

ダッシュボード下部には、ブラウザやOSの統計フィールドが2つ表示されます。

カラム名をクリックするとフィルターが有効になります。

値を確認したい場合は、上にカーソルを合わせて目のアイコンをクリックしてください。

### ダッシュボード: 管理

このダッシュボードではユーザーアクティビティを表示します。

![Dashboard: Management](/images/dashboard_02.jpg)

<!--lint disable maximum-line-length-->

| 要素                      | 説明                                                                                                                   |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| **フィルター**           | ドロップダウンリストや検索フィールドとして利用可能。矢印をクリックで有効化。                                            |
| **ユーザーアクティビティ**| ユーザーがアクティブだった日時を示すグラフ。下のユーザーIDクリックでそのユーザーのグラフ表示。                         |
| **全体アクティビティ**   | すべてのユーザーの共通アクティビティのグラフ。                                                                        |
| **User**                 | ユーザーID。                                                                                                           |
| **Project**              | プロジェクトID。空の場合あり。                                                                                         |
| **Task**                 | タスクID。空の場合あり。                                                                                               |
| **Job**                  | ジョブID。空の場合あり。                                                                                               |
| **Working time(h)**      | タスクにかけた時間（時間単位）。                                                                                       |
| **Activity**             | 各ユーザーのイベント数。                                                                                               |

<!--lint enable maximum-line-length-->

カラム名をクリックするとフィルターが有効になります。

値を確認したい場合は、上にカーソルを合わせて目のアイコンをクリックしてください。

### ダッシュボード: モニタリング

このダッシュボードはサーバーログの表示、エラー対応、ユーザーアクティビティも表示します。

![Dashboard: Monitoring](/images/dashboard_03.jpg)

<!--lint disable maximum-line-length-->

| 要素                        | 説明                                                                                                                                                                                |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **フィルター**             | ドロップダウンリストや検索フィールドとして利用可能。矢印をクリックで有効化。                                                                                                         |
| **Active users (now)**     | インスタンス上のアクティブユーザー数。                                                                                                         |
| **Overall activity**       | アクティブユーザー数のグラフ。                                                                                                                 |
| **Exceptions**             | インスタンスで発生したエラー数のグラフ。                                                                                                       |
| **timestamp**              | エラー発生時刻。                                                                                                                              |
| **user_id**                | ユーザーID。                                                                                                                                  |
| **user_name**              | ユーザーニックネーム。                                                                                                                        |
| **project_id**             | プロジェクトID。空の場合あり。                                                                                                                |
| **task_id**                | タスクID。空の場合あり。                                                                                                                      |
| **job_id**                 | ジョブID。空の場合あり。                                                                                                                      |
| **error**                  | エラー内容の説明                                                                                                                              |
| **stack**                  | エラー内容の説明                                                                                                                              |
| **payload**                | エラー内容の説明                                                                                                                              |
| **stack**                  | スタックトレース。実行時のアクティブなスタックフレームのレポート。デバッグ目的で問題発生箇所特定に利用。                                     |
| **payload**                | イベントに関連するJSONオブジェクト全体。失敗したAPIリクエストで作成されたイベントに関する情報を含みます。                                      |

<!--lint enable maximum-line-length-->

カラム名をクリックするとフィルターが有効になります。

値を確認したい場合は、上にカーソルを合わせて目のアイコンをクリックしてください。

### ダッシュボード設定

ダッシュボードは調整可能です。これを行うには、
グラフまたはテーブル名をクリックし、ドロップダウンメニューから**Edit**を選択します。

エディターでクエリーを調整してください。

![Dashboard: look and feel](/images/dashboard_04.jpg)

クエリー例:

```sql
SELECT
    time,
    uniqExact(user_id) Users
FROM
(
    SELECT
      user_id,
      toStartOfInterval(timestamp, INTERVAL 15 minute) as time
    FROM cvat.events
    WHERE
      user_id IS NOT NULL
    GROUP BY
      user_id,
      time
    ORDER BY time ASC WITH FILL STEP toIntervalMinute(15)
)
GROUP BY time
ORDER BY time
```

> **注意**: デフォルトでは変更した設定は保存されず、
> コンテナを再起動するとデフォルトパラメータにリセットされます。

設定を保存するには、下記手順を実施してください。

1. **設定の更新**: まずクエリーを編集し、希望する変更を加えます。

2. **変更の適用**: 変更を加えたら、**Apply**ボタンをクリックして反映させます。

   ![Apply changes](/images/apply.jpg)

3. **設定の保存**: 適用後、ダッシュボード上部の**Save**ボタンをクリックして保存します。

   ![Apply changes](/images/save_results.jpg)

4. **設定ファイルの差し替え**: 保存後、`components/analytics/grafana/dashboards`
   にある既存のGrafanaダッシュボード設定ファイルを新しいJSONファイルで置き換えます。

   ![Apply changes](/images/save_json.jpg)

5. **Grafanaサービスの再起動**: すべての変更を反映させるには
   Grafanaサービスを再起動してください。Docker Compose を使っている場合は
   `docker compose restart cvat_grafana` を実行します。

詳細は
[Grafana Dashboards](https://grafana.com/docs/grafana/latest/dashboards/)
も参照してください。

## 利用例

この動画では、デフォルトで利用可能なCVATアナリティクス機能をデモしています。

<!--lint disable maximum-line-length-->

<iframe width="560" height="315" src="https://www.youtube.com/embed/-1kiLPidXpI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<!--lint enable maximum-line-length-->