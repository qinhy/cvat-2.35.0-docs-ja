---
title: 'アップグレードガイド'
linkTitle: 'アップグレードガイド'
weight: 60
description: 'docker compose でデプロイされた CVAT のアップグレード手順'
---

<!--lint disable heading-style-->

## アップグレードガイド

注意: CVAT をバージョン 2.2.0 から 2.3.0 へアップデートする場合、PostgreSQL のベースイメージのメジャーバージョンアップに伴い、データベースデータに対して追加の手動操作が必要です。詳細は[こちら](#how-to-upgrade-postgresql-database-base-image)をご覧ください。

CVAT をアップグレードするには、以下の手順に従ってください。

- アップデート前に必ずすべての CVAT データをバックアップしてください。{{< ilink "/docs/administration/advanced/backup_guide" "バックアップガイド" >}}に従い、すべての CVAT ボリュームをバックアップしてください。

- 以前にクローンした CVAT ディレクトリに移動し、すべての CVAT コンテナを停止します:
  ```shell
  docker compose down
  ```
  もし
  {{< ilink "/docs/administration/basics/installation#additional-components" "追加コンポーネント" >}}
  を含めている場合は、使用しているすべての compose 設定ファイルを含めてください。例:
  ```shell
  docker compose -f docker-compose.yml -f components/serverless/docker-compose.serverless.yml down
  ```

- CVAT のソースコードを任意の方法で更新します。git でクローンするか、GitHub から zip ファイルをダウンロードしてください。
  Docker Compose の設定ファイルだけではなく、ソースコード全体をダウンロードする必要がある点に注意してください。
  詳細は
  {{< ilink "/docs/administration/basics/installation#how-to-get-cvat-source-code" "インストールガイド" >}}
  を確認してください。

- 設定を確認します:
  バージョンごとにインストールプロセスが変更されており、
  一部の環境変数をエクスポートする必要がある場合があります。
  例:
  {{< ilink "/docs/administration/basics/installation#use-your-own-domain" "CVAT_HOST" >}}。

- ローカルの CVAT イメージを更新します。
  新しい CVAT イメージをプルまたはビルドしてください。詳細は
  {{< ilink "/docs/administration/basics/installation#how-to-pullbuildupdate-cvat-images"
    "CVAT イメージの取得/ビルド/更新方法" >}}
  をご覧ください。

- CVAT を起動します:
  ```shell
  docker compose up -d
  ```
  CVAT の起動時に、最新のスキーマに従って DB がアップグレードされます。
  データ量が多い場合、時間がかかることがあります。
  マイグレーションが完了するまで中断せずにお待ちください。
  起動プロセスは下記コマンドで監視できます:
  ```shell
  docker logs cvat_server -f
  ```

## v2.26.0 以降の CVAT のアップグレード

バージョン 2.26.0 で、CVAT のエクスポートキャッシュの保存場所が変更されました。
古いキャッシュをクリーンアップするには、CVAT のデプロイ方法に応じて以下のコマンドを実行してください:

<!--lint disable no-undefined-references-->

{{< tabpane lang="shell" >}}
  {{< tab header="Docker" >}}
  docker exec -it cvat_server python manage.py cleanuplegacyexportcache
  {{< /tab >}}
  {{< tab header="Kubernetes" >}}
  cvat_backend_pod=$(kubectl get pods -l component=server -o 'jsonpath={.items[0].metadata.name}')
  kubectl exec -it ${cvat_backend_pod} -- python manage.py cleanuplegacyexportcache
  {{< /tab >}}
  {{< tab header="Development" >}}
  python manage.py cleanuplegacyexportcache
  {{< /tab >}}
{{< /tabpane >}}

<!--lint enable no-undefined-references-->

## v2.2.0 から v2.3.0 への CVAT のアップグレード方法

v2.2.0 から v2.3.0 へ CVAT をアップグレードする手順です。
CVAT v2.2.0 が稼働していると仮定します。
```shell
docker exec -it cvat_db pg_dumpall > cvat.db.dump
cd cvat
docker compose down
docker volume rm cvat_cvat_db
export CVAT_VERSION="v2.3.0"
cd ..
mv cvat cvat_220
wget https://github.com/cvat-ai/cvat/archive/refs/tags/${CVAT_VERSION}.zip
unzip ${CVAT_VERSION}.zip && mv cvat-${CVAT_VERSION:1} cvat
unset CVAT_VERSION
cd cvat
export CVAT_HOST=cvat.example.com
export ACME_EMAIL=example@example.com
docker compose pull
docker compose up -d cvat_db
docker exec -i cvat_db psql -q -d postgres < ../cvat.db.dump
docker compose -f docker-compose.yml -f docker-compose.dev.yml -f docker-compose.https.yml up -d
```

## v1.7.0 から v2.2.0 への CVAT のアップグレード方法

v1.7.0 から v2.2.0 へ CVAT をアップグレードする手順です。
CVAT v1.7.0 が稼働していると仮定します。
```shell
export CVAT_VERSION="v2.2.0"
cd cvat
docker compose down
cd ..
mv cvat cvat_170
wget https://github.com/cvat-ai/cvat/archive/refs/tags/${CVAT_VERSION}.zip
unzip ${CVAT_VERSION}.zip && mv cvat-${CVAT_VERSION:1} cvat
cd cvat
docker pull cvat/server:${CVAT_VERSION}
docker tag cvat/server:${CVAT_VERSION} openvino/cvat_server:latest
docker pull cvat/ui:${CVAT_VERSION}
docker tag cvat/ui:${CVAT_VERSION} openvino/cvat_ui:latest
docker compose up -d
```

## PostgreSQL データベースベースイメージのアップグレード方法

1. アップデート前に必ずすべての CVAT データをバックアップしてください。{{< ilink "/docs/administration/advanced/backup_guide" "バックアップガイド" >}}に従い、CVAT データベースボリュームをバックアップしてください。

1. これまで使用していた CVAT バージョンを通常通り起動します。

1. `pg_dumpall` ツールで現在のデータベースをバックアップします:
   ```shell
   docker exec -it cvat_db pg_dumpall > cvat.db.dump
   ```

1. CVAT を停止します:
   ```shell
   docker compose down
   ```

1. 現在の PostgreSQL のボリュームを削除します。必ずバックアップがあることを確認してください:
   ```shell
   docker volume rm cvat_cvat_db
   ```

1. CVAT のソースコードを任意の方法で更新します。git でクローンするか、GitHub から zip ファイルをダウンロードしてください。
   詳細は
   {{< ilink "/docs/administration/basics/installation#how-to-get-cvat-source-code" "インストールガイド" >}}
   をご覧ください。

1. データベースコンテナのみを起動します:
   ```shell
   docker compose up -d cvat_db
   ```

1. PostgreSQL のダンプを新しい DB コンテナにインポートします:
   ```shell
   docker exec -i cvat_db psql -q -d postgres < cvat.db.dump
   ```

1. CVAT を起動します:
   ```shell
   docker compose up -d
   ```