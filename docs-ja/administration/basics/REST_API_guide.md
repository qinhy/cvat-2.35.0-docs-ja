---
title: 'REST APIガイド'
linkTitle: 'REST API'
weight: 12
description: 'REST APIとのやり取り方法およびSwaggerドキュメントの取得方法についての説明。'
---

Swaggerドキュメントへアクセスするには認証が必要です。

Django REST APIの自動生成されたSwaggerドキュメントは
`<cvat_origin>/api/swagger`（デフォルト：`localhost:8080/api/swagger`）で利用できます。

Swaggerドキュメントは許可されたホスト上で表示されます。docker-compose.ymlファイルの環境変数を、
cvatをホストしているマシンのIPまたはドメイン名に更新してください。
例：`ALLOWED_HOSTS: 'localhost, 127.0.0.1'`

サーバー上に保存されたリソースへリクエストを送信すると、サーバーは要求された情報で応答します。
データの転送にはHTTPプロトコルが使用されます。
リクエストは以下のグループに分けられます：

- `auth` - ユーザー認証クエリ
- `comments` - 課題へのコメントの投稿/削除リクエスト
- `issues` - 問題コメントの更新、削除、閲覧
- `jobs` - ジョブ管理リクエスト
- `lambda` - ラムダ関数操作リクエスト
- `projects` - プロジェクト管理クエリ
- `reviews` - ジョブのレビュー追加・削除
- `server` - サーバー情報リクエスト
- `tasks` - タスク管理リクエスト
- `users` - ユーザー管理クエリ

また、`Models`も含まれます。
Models - データ型は[schema object](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.3.md#schemaObject)を使って記述されています。

各グループには、`GET`、`POST`、`PATCH`、`DELETE`などの異なるHTTPメソッドに関連するクエリが含まれます。
異なるメソッドは異なる色で強調表示されます。各項目には名前と説明があります。
要素をクリックすると、名前・説明・設定入力欄、またはjson値の例を含むフォームが開きます。

詳細については[swagger specification](https://swagger.io/docs/specification/about/)をお読みください。

リクエスト送信を試すには、`Try it now`をクリックし、`Execute`を入力してください。
[`Curl`](https://curl.se/)、`Request URL`、`Server response`の形式でレスポンスが得られます。