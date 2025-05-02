---
title: 'Webhook（ウェブフック）'
linkTitle: 'Webhook'
description: 'CVAT Webhook: 設定と利用方法'
weight: 80
---

Webhook（ウェブフック）は、特定のイベントによってトリガーされるユーザー定義のHTTPコールバックです。
Webhookをトリガーするイベントが発生すると、CVATはWebhookに設定されたURLへHTTPリクエストを送信します。
リクエストには、イベントに関する情報が含まれたペイロードが付与されます。

CVATでは、様々なイベント（タスク、ジョブなどの作成・削除・変更など）によってWebhookをトリガーできます。
これにより、CVAT内で行われた変更に自動で反応するプロセスを簡単に構築できます。

例えば、ジョブの担当者が変更された時や、ジョブ／タスクのステータスが更新された時（ジョブが完了しレビュー待ちになった時、レビュー済みになった時など）にアラートを受け取るWebhookを設定できます。
新しいタスクの作成時にも通知を発生させることが可能です。

これらの機能により、CVATワークフロー内の進捗や変更を即座に把握できます。

CVATでは、プロジェクトまたは組織単位でWebhookを作成できます。
CVATのGUIまたは直接APIコールを利用できます。

参照：

- [Webhookの作成](#create-webhook)
  - [プロジェクト向け](#for-project)
  - [組織向け](#for-organization)
  - [Webhookフォーム](#webhooks-forms)
  - [イベント一覧](#list-of-events)
- [ペイロード](#payloads)
  - [作成イベント](#create-event)
  - [更新イベント](#update-event)
  - [削除イベント](#delete-event)
- [Webhookシークレット](#webhook-secret)
- [Ping Webhook](#ping-webhook)
- [APIコールによるWebhook](#webhooks-with-api-calls)
- [セットアップと利用例](#example-of-setup-and-use)

## Webhookの作成

### プロジェクト向け

**プロジェクト**用のWebhookを作成するには、以下の手順で行います。

1. {{< ilink "/docs/manual/advanced/projects" "プロジェクトを作成" >}} します。
2. **Projects**ページで該当プロジェクトのウィジェットをクリックします。
3. 画面右上の**Actions** > **Setup Webhooks**をクリックします。
4. 右上の**+**をクリックします。

   ![Create Project Webhook](/images/create_project_webhook.gif)

5. **[Webhookの設定](#webhooks-forms)**フォームに必要事項を入力し、**Submit**をクリックします。

### 組織向け

**組織**用のWebhookを作成するには、以下の手順で行います。

1. {{< ilink "/docs/manual/advanced/organization" "組織を作成" >}}
2. **Organization** > **Settings** > **Actions** > **Setup Webhooks**へ移動します。
3. 右上の**+**をクリックします。

  ![](/images/create_organization_webhook.gif)

4. **[Webhookの設定](#webhooks-forms)**フォームに必要事項を入力し、**Submit**をクリックします。

### Webhookフォーム

**Webhookの設定**フォームは以下のようになります。

![Create Project And Org Webhook Forms ](/images/webhook_form_project_org.jpg)

フォームには以下のフィールドがあります。

<!--lint disable maximum-line-length-->

| フィールド                | 説明                                                                                                                                                       |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Target URL                | イベントデータを送信する先のURLです。                                                                                                                      |
| Description               | Webhookの目的を簡単に説明します。                                                                                                                          |
| Project                   | 利用可能なプロジェクトから選択できるドロップダウンリストです。                                                                                             |
| Content type              | WebhookリクエストのHTTP Content-Typeフィールドで、ペイロードのデータ型を定義します。                                                                         |
| Secret                    | Webhookの発信元を検証するための一意なキーです。CVATからのリクエストであることを確認できます。<br>詳細は[Webhookシークレット](#webhook-secret)を参照してください。|
| Enable SSL                | [SSL検証](https://ja.wikipedia.org/wiki/公開鍵証明書)を有効または無効にするチェックボックスです。                                                           |
| Active                    | 特定のWebhookペイロードの配信を停止したい場合はこのチェックを外します。                                                                                      |
| Send everything           | すべてのイベントタイプをWebhookで送信する場合はチェックします。                                                                                              |
| Specify individual events | 特定のイベントタイプのみ送信する場合に選択します。<br>イベントタイプの詳細は[利用可能なイベント一覧](#list-of-available-events)を参照してください。              |

<!--lint enable maximum-line-length-->

### イベント一覧

Webhookアラートで利用可能なイベントは以下の通りです。

<!--lint disable maximum-line-length-->

| リソース      | 作成  | 更新  | 削除  | 説明                                                                                   |
| ------------- | ----- | ----- | ----- | -------------------------------------------------------------------------------------- |
| Organization  |       | ✅    |       | 組織の変更に関するアラート。                                                           |
| Membership    |       | ✅    | ✅    | 組織へのメンバー追加・削除時のアラート。                                               |
| Invitation    | ✅    |       | ✅    | 組織への招待発行・取消時のアラート。                                                   |
| Project       | ✅    | ✅    | ✅    | プロジェクト内での各種操作に関するアラート。                                            |
| Task          | ✅    | ✅    | ✅    | タスクに関する操作（ステータス変更、割り当て等）のアラート。                           |
| Job           |       | ✅    |       | ジョブの更新に関するアラート。                                                         |
| Issue         | ✅    | ✅    | ✅    | イシューに関するあらゆる操作のアラート。                                               |
| Comment       | ✅    | ✅    | ✅    | コメントの作成・削除・変更などに関するアラート。                                        |

<!--lint enable maximum-line-length-->

## ペイロード

### 作成イベント

`create:<resource>`イベントのWebhookペイロードオブジェクト：

<!--lint disable maximum-line-length-->

| キー           | 型        | 説明                                                                                                                                |
| -------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `event`        | `string`  | Webhookをトリガーしたイベントを`create:<resource>`形式で示します。                                                                  |
| `<resource>`   | `object`  | 作成されたリソースの完全な情報。個々のリソースの詳細は[Swagger](#webhooks-with-api-calls)ドキュメントを参照してください。            |
| `webhook_id`   | `integer` | ペイロードを送信したWebhookの識別子。                                                                                                |
| `sender`       | `object`  | Webhookをトリガーしたユーザー情報。                                                                                                |

<!--lint enable maximum-line-length-->

`create:task`イベントのペイロード例：

{{< scroll-code lang="json" >}}
{
 "event": "create:task",
    "task": {
        "url": "<http://localhost:8080/api/tasks/15>",
        "id": 15,
        "name": "task",
        "project_id": 7,
        "mode": "",
        "owner": {
            "url": "<http://localhost:8080/api/users/1>",
            "id": 1,
            "username": "admin1",
            "first_name": "Admin",
            "last_name": "First"
        },
        "assignee": null,
        "bug_tracker": "",
        "created_date": "2022-10-04T08:05:50.419259Z",
        "updated_date": "2022-10-04T08:05:50.422917Z",
        "overlap": null,
        "segment_size": 0,
        "status": "annotation",
        "labels": [
            {
                "id": 28,
                "name": "label_0",
                "color": "#bde94a",
                "attributes": [],
                "type": "any",
                "sublabels": [],
                "has_parent": false
            }
        ],
        "segments": [],
        "dimension": "2d",
        "subset": "",
        "organization": null,
        "target_storage": {
            "id": 14,
            "location": "local",
            "cloud_storage_id": null
        },
        "source_storage": {
            "id": 13,
            "location": "local",
            "cloud_storage_id": null
        }
    },
    "webhook_id": 7,
    "sender": {
        "url": "<http://localhost:8080/api/users/1>",
        "id": 1,
        "username": "admin1",
        "first_name": "Admin",
        "last_name": "First"
    }
}
{{< /scroll-code >}}

### 更新イベント

`update:<resource>`イベントのWebhookペイロードオブジェクト：

<!--lint disable maximum-line-length-->

| キー              | 型        | 説明                                                                                           |
| ----------------- | --------- | ---------------------------------------------------------------------------------------------- |
| `event`           | `string`  | Webhookをトリガーしたイベントを`update:<resource>`形式で示します。                              |
| `<resource>`      | `object`  | 更新後のリソースの完全な情報。詳細はSwaggerドキュメント参照。                                  |
| `before_update`   | `object`  | 更新された`<resource>`のキーとその旧値を含みます。                                              |
| `webhook_id`      | `integer` | ペイロードを送信したWebhookの識別子。                                                           |
| `sender`          | `object`  | Webhookをトリガーしたユーザー情報。                                                            |

<!--lint enable maximum-line-length-->

`update:<resource>`イベントの例：

{{< scroll-code lang="json" >}}
{
    "event": "update:task",
    "task": {
        "url": "<http://localhost:8080/api/tasks/15>",
        "id": 15,
        "name": "new task name",
        "project_id": 7,
        "mode": "annotation",
        "owner": {
            "url": "<http://localhost:8080/api/users/1>",
            "id": 1,
            "username": "admin1",
            "first_name": "Admin",
            "last_name": "First"
        },
        "assignee": null,
        "bug_tracker": "",
        "created_date": "2022-10-04T08:05:50.419259Z",
        "updated_date": "2022-10-04T11:04:51.451681Z",
        "overlap": 0,
        "segment_size": 1,
        "status": "annotation",
        "labels": [
            {
                "id": 28,
                "name": "label_0",
                "color": "#bde94a",
                "attributes": [],
                "type": "any",
                "sublabels": [],
                "has_parent": false
            }
        ],
        "segments": [
            {
                "start_frame": 0,
                "stop_frame": 0,
                "jobs": [
                    {
                        "url": "<http://localhost:8080/api/jobs/19>",
                        "id": 19,
                        "assignee": null,
                        "status": "annotation",
                        "stage": "annotation",
                        "state": "new"
                    }
                ]
            }
        ],
        "data_chunk_size": 14,
        "data_compressed_chunk_type": "imageset",
        "data_original_chunk_type": "imageset",
        "size": 1,
        "image_quality": 70,
        "data": 14,
        "dimension": "2d",
        "subset": "",
        "organization": null,
        "target_storage": {
            "id": 14,
            "location": "local",
            "cloud_storage_id": null
        },
        "source_storage": {
            "id": 13,
            "location": "local",
            "cloud_storage_id": null
        }
    },
    "before_update": {
        "name": "task"
    },
    "webhook_id": 7,
    "sender": {
        "url": "<http://localhost:8080/api/users/1>",
        "id": 1,
        "username": "admin1",
        "first_name": "Admin",
        "last_name": "First"
    }
}
{{< /scroll-code >}}

### 削除イベント

`delete:<resource>`イベントのWebhookペイロードオブジェクト：

<!--lint disable maximum-line-length-->

| キー           | 型        | 説明                                                                                           |
| -------------- | --------- | ---------------------------------------------------------------------------------------------- |
| `event`        | `string`  | Webhookをトリガーしたイベントを`delete:<resource>`形式で示します。                              |
| `<resource>`   | `object`  | 削除されたリソースの完全な情報。詳細はSwaggerドキュメント参照。                                |
| `webhook_id`   | `integer` | ペイロードを送信したWebhookの識別子。                                                           |
| `sender`       | `object`  | Webhookをトリガーしたユーザー情報。                                                            |

<!--lint enable maximum-line-length-->

`delete:task`イベントのペイロード例：

{{< scroll-code lang="json" >}}
{
    "event": "delete:task",
    "task": {
        "url": "<http://localhost:8080/api/tasks/15>",
        "id": 15,
        "name": "task",
        "project_id": 7,
        "mode": "",
        "owner": {
            "url": "<http://localhost:8080/api/users/1>",
            "id": 1,
            "username": "admin1",
            "first_name": "Admin",
            "last_name": "First"
        },
        "assignee": null,
        "bug_tracker": "",
        "created_date": "2022-10-04T08:05:50.419259Z",
        "updated_date": "2022-10-04T08:05:50.422917Z",
        "overlap": null,
        "segment_size": 0,
        "status": "annotation",
        "labels": [
            {
                "id": 28,
                "name": "label_0",
                "color": "#bde94a",
                "attributes": [],
                "type": "any",
                "sublabels": [],
                "has_parent": false
            }
        ],
        "segments": [],
        "dimension": "2d",
        "subset": "",
        "organization": null,
        "target_storage": {
            "id": 14,
            "location": "local",
            "cloud_storage_id": null
        },
        "source_storage": {
            "id": 13,
            "location": "local",
            "cloud_storage_id": null
        }
    },
    "webhook_id": 7,
    "sender": {
        "url": "<http://localhost:8080/api/users/1>",
        "id": 1,
        "username": "admin1",
        "first_name": "Admin",
        "last_name": "First"
    }
}
{{< /scroll-code >}}

## Webhookシークレット

WebhookリクエストがCVATから送信されたものであることを検証するため、Webhook作成時に`secret`（シークレット）を設定してください。

Webhookに`secret`が設定されている場合、CVATはリクエストヘッダーに`X-Signature-256`を含めて送信します。

CVATはSHA256ハッシュ関数を利用してWebhookのリクエストボディをエンコードし、その結果のハッシュ値をヘッダーに格納します。

Webhookの受信側では、受信した`X-Signature-256`の値と期待値を比較することでリクエスト元を検証できます。

例えば、空のボディかつ`secret = mykey`の場合のヘッダー値は以下の通りです。

```
X-Signature-256: e1b24265bf2e0b20c81837993b4f1415f7b68c503114d100a40601eca6a2745f
```

Webhook受信サービスで署名を検証する例：

```python
# webhook_receiver.py

import hmac
from hashlib import sha256
from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    signature = (
        "sha256="
        + hmac.new("mykey".encode("utf-8"), request.data, digestmod=sha256).hexdigest()
    )

    if hmac.compare_digest(request.headers["X-Signature-256"], signature):
        return app.response_class(status=200)

    raise app.response_class(status=500, response="Signatures didn't match!")
```

## Ping Webhook

Webhookの設定が正しく行われているか、CVATがターゲットURLに接続できるかを確認するには、**Ping** Webhook機能を利用します。

![Ping Webhook ](/images/ping_webhook.jpg)

1. ユーザーインターフェースで**Ping**ボタンをクリック（またはAPIで`POST /webhooks/{id}/ping`リクエストを送信）。
2. CVATが指定ターゲットURLにWebhookアラート（Webhook情報の基本情報）を送信します。

Ping Webhookペイロード：

<!--lint disable maximum-line-length-->

| キー        | 型        | 説明                                                                                   |
| ----------- | --------- | -------------------------------------------------------------------------------------- |
| `event`     | `string`  | 値は常に`ping`です。                                                                   |
| `webhook`   | `object`  | Webhookの完全な情報。各フィールドの詳細はSwaggerドキュメント参照。                      |
| `sender`    | `object`  | Webhookの`ping`を発信したユーザー情報。                                                 |

<!--lint enable maximum-line-length-->

`ping`イベントのペイロード例：

{{< scroll-code lang="json" >}}
{
   "event": "ping",
    "webhook": {
        "id": 7,
        "url": "<http://localhost:8080/api/webhooks/7>",
        "target_url": "<https://example.com>",
        "description": "",
        "type": "project",
        "content_type": "application/json",
        "is_active": true,
        "enable_ssl": true,
        "created_date": "2022-10-04T08:05:23.007381Z",
        "updated_date": "2022-10-04T08:05:23.007395Z",
        "owner": {
            "url": "<http://localhost:8080/api/users/1>",
            "id": 1,
            "username": "admin1",
            "first_name": "Admin",
            "last_name": "First"
        },
        "project": 7,
        "organization": null,
        "events": [
            "create:comment",
            "create:issue",
            "create:task",
            "delete:comment",
            "delete:issue",
            "delete:task",
            "update:comment",
            "update:issue",
            "update:job",
            "update:project",
            "update:task"
        ],
        "last_status": 200,
        "last_delivery_date": "2022-10-04T11:04:52.538638Z"
    },
    "sender": {
        "url": "<http://localhost:8080/api/users/1>",
        "id": 1,
        "username": "admin1",
        "first_name": "Admin",
        "last_name": "First"
    }
}
{{< /scroll-code >}}

## APIコールによるWebhook

APIコールでWebhookを作成する方法は、
[Swaggerドキュメント](https://app.cvat.ai/api/docs)を参照してください。

サンプルについては、
[REST APIテスト](https://github.com/cvat-ai/cvat/blob/develop/tests/python/rest_api/test_webhooks.py)も参照ください。

## セットアップと利用例

このビデオは、ZapierとGmailを使ってプロジェクト用のメールアラートを設定する方法を紹介しています。

<!--lint disable maximum-line-length-->

<iframe width="560" height="315" src="https://www.youtube.com/embed/x87CsGsd-3I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<!--lint enable maximum-line-length-->