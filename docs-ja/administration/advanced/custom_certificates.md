---
title: 'カスタム証明書'
linkTitle: 'カスタム証明書'
description: 'CVATでカスタム証明書を使用する'
weight: 100
---

CVATは、SSL証明書の管理にリバースプロキシとしてtraefikを使用しています。
デフォルトでは、traefikはLet's Encryptを使用してSSL証明書を生成します。
しかし、Let's Encryptの代わりに独自の証明書を使用することもできます。

参照：

- [カスタム証明書のセットアップ](#カスタム証明書のセットアップ)
- [証明書ディレクトリの作成](#証明書ディレクトリの作成)
- [Traefik設定の変更](#traefik設定の変更)
- [CVATの起動](#cvatの起動)


## カスタム証明書のセットアップ

### 証明書ディレクトリの作成

プロジェクトのルートに`certs`ディレクトリを作成します：

```bash
mkdir -p ./certs

```

証明書を`./certs`ディレクトリに移動します：

```bash
mv /path/to/cert.pem ./certs/cert.pem
mv /path/to/key.pem ./certs/key.pem
```

### Traefik設定の変更

プロジェクトディレクトリのルートに、以下の内容で`tls.yml`を作成します：

```yaml
tls:
  stores:
    default:
      defaultCertificate:
        certFile: /certs/cert.pem
        keyFile: /certs/key.pem
```

`docker-compose.https.yml`ファイルを編集し、traefikサービスの設定を以下のように変更します：

```yaml
  traefik:
    environment:
      TRAEFIK_ENTRYPOINTS_web_ADDRESS: :80
      TRAEFIK_ENTRYPOINTS_web_HTTP_REDIRECTIONS_ENTRYPOINT_TO: websecure
      TRAEFIK_ENTRYPOINTS_web_HTTP_REDIRECTIONS_ENTRYPOINT_SCHEME: https
      TRAEFIK_ENTRYPOINTS_websecure_ADDRESS: :443
      # Let's Encryptを無効化
      # TRAEFIK_CERTIFICATESRESOLVERS_lets-encrypt_ACME_EMAIL: "${ACME_EMAIL:?Please set the ACME_EMAIL env variable}"
      # TRAEFIK_CERTIFICATESRESOLVERS_lets-encrypt_ACME_TLSCHALLENGE: "true"
      # TRAEFIK_CERTIFICATESRESOLVERS_lets-encrypt_ACME_STORAGE: /letsencrypt/acme.json
    ports:
      - 80:80
      - 443:443
    # 証明書のボリュームとtls.ymlルールを追加
    volumes:
      - ./certs:/certs
      - ./tls.yml:/etc/traefik/rules/tls.yml
```

### CVATの起動

以下のコマンドでCVATを起動します：

```bash
docker compose -f docker-compose.yml -f docker-compose.https.yml up -d
```