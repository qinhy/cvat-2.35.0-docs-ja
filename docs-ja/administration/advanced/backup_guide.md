---
title: 'バックアップガイド'
linkTitle: 'バックアップガイド'
weight: 50
description: 'Dockerを使ったCVATデータのバックアップ手順。'
---

<!--lint disable heading-style-->

## CVATデータボリュームについて

Dockerボリュームは、すべてのCVATデータを保存するために使用されます：

- `cvat_db`: PostgreSQLデータベースファイル。ユーザー、タスク、プロジェクト、アノテーションなどの情報を保存します。
  `cvat_db`コンテナ内の`/var/lib/postgresql/data`パスにマウントされます。

- `cvat_data`: アップロードおよび準備されたメディアデータを保存します。
  `cvat`コンテナ内の`/home/django/data`パスにマウントされます。

- `cvat_keys`: [Djangoシークレットキー](https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-SECRET_KEY)を保存します。
  `cvat`コンテナ内の`/home/django/keys`パスにマウントされます。

- `cvat_logs`: supervisordサービスによって管理されるCVATバックエンドプロセスのログを保存します。
  `cvat`コンテナ内の`/home/django/logs`パスにマウントされます。

- `cvat_events_db`: このボリュームはClickhouseデータベースファイルを保存するために使われます。
  `cvat_clickhouse`コンテナ内の`/var/lib/clickhouse`パスにマウントされます。

## すべてのCVATデータをバックアップする方法

バックアップ前にすべてのCVATコンテナを停止してください：

```shell
docker compose stop
```

`docker compose`コマンドで使用したすべてのcompose設定ファイルを`-f`パラメータで追加するのを忘れないでください。

データのバックアップ：

```shell
mkdir backup
docker run --rm --name temp_backup --volumes-from cvat_db -v $(pwd)/backup:/backup ubuntu tar -czvf /backup/cvat_db.tar.gz /var/lib/postgresql/data
docker run --rm --name temp_backup --volumes-from cvat_server -v $(pwd)/backup:/backup ubuntu tar -czvf /backup/cvat_data.tar.gz /home/django/data
docker run --rm --name temp_backup --volumes-from cvat_clickhouse -v $(pwd)/backup:/backup ubuntu tar -czvf /backup/cvat_events_db.tar.gz /var/lib/clickhouse
```

バックアップアーカイブが作成されたことを確認してください。`ls backup`コマンドの出力は次のようになります：

```shell
ls backup
cvat_data.tar.gz  cvat_db.tar.gz  cvat_events_db.tar.gz
```

## バックアップからCVATを復元する方法

**警告: DBを復元する際は必ず同じCVATバージョンを使用してください。
そうしないと、CVATのリリース間でDBの構造が変更されているため、正常に動作しません。
CVATは後からアップグレードできます。その際、内部的にデータ移行が適切に行われます。**

注意: CVATコンテナが存在している必要があります（ない場合は
{{< ilink "/docs/administration/basics/installation#quick-installation-guide" "インストールガイド" >}}に従ってください）。
すべてのCVATコンテナを停止してください：

```shell
docker compose stop
```

データの復元：

```shell
cd <path_to_backup_folder>
docker run --rm --name temp_backup --volumes-from cvat_db -v $(pwd):/backup ubuntu bash -c "cd /var/lib/postgresql/data && tar -xvf /backup/cvat_db.tar.gz --strip 4"
docker run --rm --name temp_backup --volumes-from cvat_server -v $(pwd):/backup ubuntu bash -c "cd /home/django/data && tar -xvf /backup/cvat_data.tar.gz --strip 3"
docker run --rm --name temp_backup --volumes-from cvat_clickhouse -v $(pwd):/backup ubuntu bash -c "cd /var/lib/clickhouse && tar -xvf /backup/cvat_events_db.tar.gz --strip 3"
```

その後、通常通りCVATを起動してください：

```shell
docker compose up -d
```

## 追加リソース

[Dockerによるボリュームバックアップのガイド](https://docs.docker.com/storage/volumes/#backup-restore-or-migrate-data-volumes)