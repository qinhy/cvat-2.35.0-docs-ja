---
title: 'インストールガイド'
linkTitle: 'インストールガイド'
weight: 1
description: '異なるオペレーティングシステム向けのCVATインストールガイドです。'
---

<!--lint disable heading-style-->

# 簡単なインストールガイド

CVATを使用する前に、インストールする必要があります。以下のドキュメントには、最も一般的なオペレーティングシステム向けの手順が含まれています。お使いのシステムがこのドキュメントでカバーされていない場合でも、以下の手順を他のシステムに適用するのは比較的簡単なはずです。

プロキシサーバーを経由している場合は、以下の手順を修正する必要があるかもしれません。プロキシは高度なトピックであり、このガイドでは扱っていません。

中国からのアクセスについては、[中国ユーザー向けの情報源](#sources-for-users-from-china)セクションをお読みください。

## Ubuntu 22.04/20.04 (x86_64/amd64)

-   端末ウィンドウを開きます。Ubuntuで端末ウィンドウを開く方法がわからない場合は、[こちらの回答](https://askubuntu.com/questions/183775/how-do-i-open-a-terminal)をお読みください。

-   以下のコマンドを端末ウィンドウに入力して、DockerとDocker Composeをインストールします。詳細な手順は[こちら](https://docs.docker.com/install/linux/docker-ce/ubuntu/)で確認できます。

    ```shell
    sudo apt-get update
    sudo apt-get --no-install-recommends install -y \
      apt-transport-https \
      ca-certificates \
      curl \
      gnupg-agent \
      software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository \
      "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) \
      stable"
    sudo apt-get update
    sudo apt-get --no-install-recommends install -y \
      docker-ce docker-ce-cli containerd.io docker-compose-plugin
    ```

-   (オプション) Dockerコマンドの前に`sudo`を付けるのを避けるには、[インストール後の手順](https://docs.docker.com/install/linux/linux-postinstall/)を実行できます。これには、`docker`という名前のUnixグループを作成し、現在のユーザーをこのグループに追加することが含まれます。

    ```shell
    sudo groupadd docker
    sudo usermod -aG docker $USER
    ```

    ログアウトして再度ログイン（または再起動）し、グループメンバーシップが再評価されるようにします。その後、端末ウィンドウで`groups`コマンドを入力し、出力に`docker`グループが含まれているか確認できます。

-   Gitを使用して[GitHubリポジトリ](https://github.com/cvat-ai/cvat)から_CVAT_のソースコードをクローンします。

    以下のコマンドは最新のdevelopブランチをクローンします：

    ```shell
    git clone https://github.com/cvat-ai/cvat
    cd cvat
    ```

    リリースバージョンの一つをダウンロードしたい場合や、`wget`または`curl`ツールを使用したい場合は、[代替手段](#how-to-get-cvat-source-code)を参照してください。

-   ネットワーク経由または異なるシステムからCVATにアクセスするには、`CVAT_HOST`環境変数をエクスポートします。

    ```shell
    export CVAT_HOST=FQDNまたはあなたのIPアドレス
    ```

-   Dockerコンテナを実行します。最新のCVATおよびその他の必要なイメージ（postgres、redisなど）をダウンロードし、コンテナを開始するには時間がかかります。

    ```shell
    docker compose up -d
    ```

-   (オプション) `CVAT_VERSION`環境変数を使用して、インストールしたいCVATの特定のバージョン（例：`v2.1.0`、`dev`）を指定します。デフォルトの動作：developブランチには`dev`イメージが、リリースバージョンには対応するリリースイメージがプルされます。

    ```shell
    CVAT_VERSION=dev docker compose up -d
    ```

-   代替：未リリースの変更を含むイメージをローカルでビルドしたい場合は、[CVATイメージのプル/ビルド/更新方法](#how-to-pullbuildupdate-cvat-images)セクションを参照してください。

-   ユーザーを登録できますが、デフォルトではタスクのリストを表示する権限すらありません。したがって、スーパーユーザーを作成する必要があります。スーパーユーザーは管理パネルを使用して、ユーザーに適切なグループを割り当てることができます。以下のコマンドを使用してください：

    ```shell
    docker exec -it cvat_server bash -ic 'python3 ~/manage.py createsuperuser'
    ```

    管理者アカウントのユーザー名とパスワードを選択してください。詳細については、[Djangoドキュメント](https://docs.djangoproject.com/en/2.2/ref/django-admin/#createsuperuser)をお読みください。

-   Google ChromeはCVATがサポートする唯一のブラウザです。これもインストールする必要があります。以下のコマンドを端末ウィンドウに入力してください：

    ```shell
    curl https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
    sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
    sudo apt-get update
    sudo apt-get --no-install-recommends install -y google-chrome-stable
    ```

-   インストールされたGoogle Chromeブラウザを開き、[localhost:8080](http://localhost:8080)にアクセスします。ログインページでスーパーユーザーのログイン情報/パスワードを入力し、_Login_ボタンを押します。これで新しいアノテーションタスクを作成できるようになります。詳細については、{{< ilink "/docs/manual" "CVATマニュアル" >}}をお読みください。

## Windows 10

-   [こちらの公式ガイド](https://docs.microsoft.com/windows/wsl/install-win10)を参照してWSL2（Linux用Windowsサブシステム）をインストールします。WSL2にはWindows 10、バージョン2004以降が必要です。WSL2をインストールした後、選択したLinuxディストリビューションをインストールします。

-   [Docker Desktop for Windows](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe)をダウンロードしてインストールします。`Docker for Windows Installer`をダブルクリックしてインストーラーを実行します。詳細な手順は[こちら](https://docs.docker.com/docker-for-windows/install/)で確認できます。Docker WSL2バックエンドの公式ガイドは[こちら](https://docs.docker.com/docker-for-windows/wsl/)で確認できます。注意：Dockerには具体的にWSL2バックエンドを使用していることを確認してください。

-   Docker Desktopで、`Settings >> Resources >> WSL Integration`に移動し、選択したLinuxディストリビューションとの統合を有効にします。

-   [Git for Windows](https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-64-bit.exe)をダウンロードしてインストールします。パッケージをインストールする際は、すべてのオプションをデフォルトのままにしてください。パッケージに関する詳細情報は[こちら](https://gitforwindows.org)で確認できます。

-   [Google Chrome](https://www.google.com/chrome/)をダウンロードしてインストールします。これはCVATがサポートする唯一のブラウザです。

-   Windowsメニューに移動し、インストールしたLinuxディストリビューションを見つけて実行します。端末ウィンドウが表示されるはずです。

-   [GitHubリポジトリ](https://github.com/cvat-ai/cvat)から_CVAT_のソースコードをクローンします。

    以下のコマンドは最新のdevelopブランチをクローンします：

    ```shell
    git clone https://github.com/cvat-ai/cvat
    cd cvat
    ```

    リリースバージョンの一つをダウンロードしたい場合は、[代替手段](#how-to-get-cvat-source-code)を参照してください。

-   Dockerコンテナを実行します。最新のCVATリリースおよびその他の必要なイメージ（postgres、redisなど）をDockerHubからダウンロードし、コンテナを作成するには時間がかかります。

    ```shell
    docker compose up -d
    ```

-   (オプション) `CVAT_VERSION`環境変数を使用して、インストールしたいCVATの特定のバージョン（例：`v2.1.0`、`dev`）を指定します。デフォルトの動作：developブランチには`dev`イメージが、リリースバージョンには対応するリリースイメージがプルされます。

    ```shell
    CVAT_VERSION=dev docker compose up -d
    ```

-   代替：未リリースの変更を含むイメージをローカルでビルドしたい場合は、[CVATイメージのプル/ビルド/更新方法](#how-to-pullbuildupdate-cvat-images)セクションを参照してください。

-   ユーザーを登録できますが、デフォルトではタスクのリストを表示する権限すらありません。したがって、スーパーユーザーを作成する必要があります。スーパーユーザーは管理パネルを使用して、他のユーザーに適切なグループを割り当てることができます。以下のコマンドを使用してください：

    ```shell
    sudo docker exec -it cvat_server bash -ic 'python3 ~/manage.py createsuperuser'
    ```

    winptyがインストールされていない場合や上記のコマンドが機能しない場合は、以下を試すこともできます：

    ```shell
    # 最初にdockerイメージに入る
    docker exec -it cvat_server /bin/bash
    # 次に実行
    python3 ~/manage.py createsuperuser
    ```

    管理者アカウントのユーザー名とパスワードを選択してください。詳細については、[Djangoドキュメント](https://docs.djangoproject.com/en/2.2/ref/django-admin/#createsuperuser)をお読みください。

-   インストールされたGoogle Chromeブラウザを開き、[localhost:8080](http://localhost:8080)にアクセスします。ログインページでスーパーユーザーのログイン情報/パスワードを入力し、_Login_ボタンを押します。これで新しいアノテーションタスクを作成できるようになります。詳細については、{{< ilink "/docs/manual" "CVATマニュアル" >}}をお読みください。

## Mac OS Mojave

-   [Docker for Mac](https://download.docker.com/mac/stable/Docker.dmg)をダウンロードします。`Docker.dmg`をダブルクリックしてインストーラーを開き、Moby the whale（クジラのアイコン）をApplicationsフォルダにドラッグします。Applicationsフォルダ内の`Docker.app`をダブルクリックしてDockerを起動します。詳細な手順は[こちら](https://docs.docker.com/v17.12/docker-for-mac/install/#install-and-run-docker-for-mac)で確認できます。

-   MacにGitをインストールする方法はいくつかあります。最も簡単なのは、おそらくXcode Command Line Toolsをインストールすることです。Mavericks (10.9)以降では、初めてターミナルからgitを実行しようとすると、これを簡単に行うことができます。

    ```shell
    git --version
    ```

    まだインストールされていない場合は、インストールを促すプロンプトが表示されます。詳細な手順は[こちら](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)で確認できます。

-   [Google Chrome](https://www.google.com/chrome/)をダウンロードしてインストールします。これはCVATがサポートする唯一のブラウザです。

-   端末ウィンドウを開きます。ターミナルアプリはApplicationsフォルダ内のUtilitiesフォルダにあります。開くには、Applicationsフォルダを開き、Utilitiesを開いてターミナルをダブルクリックするか、Command - スペースバーを押してSpotlightを起動し、「Terminal」と入力して検索結果をダブルクリックします。

-   Gitを使用して[GitHubリポジトリ](https://github.com/cvat-ai/cvat)から_CVAT_のソースコードをクローンします。

    以下のコマンドは最新のdevelopブランチをクローンします：

    ```shell
    git clone https://github.com/cvat-ai/cvat
    cd cvat
    ```

    リリースバージョンの一つをダウンロードしたい場合や、`wget`または`curl`ツールを使用したい場合は、[代替手段](#how-to-get-cvat-source-code)を参照してください。

-   Dockerコンテナを実行します。最新のCVATリリースおよびその他の必要なイメージ（postgres、redisなど）をDockerHubからダウンロードし、コンテナを作成するには時間がかかります。

    ```shell
    docker compose up -d
    ```

-   (オプション) `CVAT_VERSION`環境変数を使用して、インストールしたいCVATの特定のバージョン（例：`v2.1.0`、`dev`）を指定します。デフォルトの動作：developブランチには`dev`イメージが、リリースバージョンには対応するリリースイメージがプルされます。

    ```shell
    CVAT_VERSION=dev docker compose up -d
    ```

-   代替：未リリースの変更を含むイメージをローカルでビルドしたい場合は、[CVATイメージのプル/ビルド/更新方法](#how-to-pullbuildupdate-cvat-images)セクションを参照してください。

-   ユーザーを登録できますが、デフォルトではタスクのリストを表示する権限すらありません。したがって、スーパーユーザーを作成する必要があります。スーパーユーザーは管理パネルを使用して、他のユーザーに適切なグループを割り当てることができます。以下のコマンドを使用してください：

    ```shell
    docker exec -it cvat_server bash -ic 'python3 ~/manage.py createsuperuser'
    ```

    管理者アカウントのユーザー名とパスワードを選択してください。詳細については、[Djangoドキュメント](https://docs.djangoproject.com/en/2.2/ref/django-admin/#createsuperuser)をお読みください。

-   インストールされたGoogle Chromeブラウザを開き、[localhost:8080](http://localhost:8080)にアクセスします。ログインページでスーパーユーザーのログイン情報/パスワードを入力し、_Login_ボタンを押します。これで新しいアノテーションタスクを作成できるようになります。詳細については、{{< ilink "/docs/manual" "CVATマニュアル" >}}をお読みください。

## 高度なトピック

### CVATソースコードの取得方法

#### Git (Linux, Mac, Windows)

1.  システムにGitがまだインストールされていない場合はインストールします。

    -   Ubuntu:

    ```shell
    sudo apt-get --no-install-recommends install -y git
    ```

    -   Windows:
        [https://git-scm.com/download/win](https://git-scm.com/download/win)の手順に従います。

2.  [GitHubリポジトリ](https://github.com/cvat-ai/cvat)から_CVAT_のソースコードをクローンします。

    以下のコマンドはデフォルトブランチ（develop）をクローンします：

    ```shell
    git clone https://github.com/cvat-ai/cvat
    cd cvat
    ```

    特定のタグ、例えばv2.1.0をクローンするには：

    ```shell
    git clone -b v2.1.0 https://github.com/cvat-ai/cvat
    cd cvat
    ```

#### Wget (Linux, Mac)

最新のdevelopブランチをダウンロードするには：

```shell
wget https://github.com/cvat-ai/cvat/archive/refs/heads/develop.zip
unzip develop.zip && mv cvat-develop cvat
cd cvat
```

特定のタグをダウンロードするには：

```shell
wget https://github.com/cvat-ai/cvat/archive/refs/tags/v1.7.0.zip
unzip v1.7.0.zip && mv cvat-1.7.0 cvat
cd cvat
```

#### Curl (Linux, Mac)

最新のdevelopブランチをダウンロードするには：

```shell
curl -LO https://github.com/cvat-ai/cvat/archive/refs/heads/develop.zip
unzip develop.zip && mv cvat-develop cvat
cd cvat
```

特定のタグをダウンロードするには：

```shell
curl -LO https://github.com/cvat-ai/cvat/archive/refs/tags/v1.7.0.zip
unzip v1.7.0.zip && mv cvat-1.7.0 cvat
cd cvat
```

### CVATヘルスチェックコマンド

以下のコマンドを使用すると、CVATコンテナが正常に動作しているかテストできます。

```shell
docker exec -t cvat_server python manage.py health_check
```

正常なCVATコンテナの期待される出力：

```shell
Cache backend: default   ... working
DatabaseBackend          ... working
DiskUsage                ... working
MemoryUsage              ... working
MigrationsHealthCheck    ... working
OPAHealthCheck           ... working
```

### プロキシの背後でCVATをデプロイする

プロキシの背後でCVATをデプロイし、自動アノテーションのための[サーバーレス関数](#semi-automatic-and-automatic-annotation)を使用しない場合は、エクスポートされた環境変数`http_proxy`、`https_proxy`、`no_proxy`でイメージをビルドするのに十分です。そうでない場合は、コンテナを起動するユーザーのホームディレクトリにある`~/.docker/config.json`ファイルを作成または編集し、次のようなJSONを追加してください：

```json
{
  "proxies": {
    "default": {
      "httpProxy": "http://proxy_server:port",
      "httpsProxy": "http://proxy_server:port",
      "noProxy": "*.test.example.com,.example2.com"
    }
  }
}
```

これらの環境変数は、任意のコンテナ内で自動的に設定されます。詳細については、[Dockerドキュメント](https://docs.docker.com/network/proxy/)を参照してください。

### Traefikダッシュボードの使用

docker-composeファイルをカスタマイズしていて予期しない問題が発生した場合、Traefikダッシュボードを使用すると、問題がTraefikの設定にあるのか、それとも他のサービスにあるのかを確認するのに非常に役立ちます。

`docker-compose.yml`から以下の行のコメントを解除することで、Traefikダッシュボードを有効にできます。

```yml
services:
  traefik:
    # Traefikダッシュボードを取得するにはコメントを解除
    #   - "--entryPoints.dashboard.address=:8090"
    #   - "--api.dashboard=true"
    # labels:
    #   - traefik.enable=true
    #   - traefik.http.routers.dashboard.entrypoints=dashboard
    #   - traefik.http.routers.dashboard.service=api@internal
    #   - traefik.http.routers.dashboard.rule=Host(`${CVAT_HOST:-localhost}`)
```

そして、`docker-compose.https.yml`を使用している場合は、これらの行もコメント解除します。

```yml
services:
  traefik:
    command:
      # Traefikダッシュボードを取得するにはコメントを解除
      # - "--entryPoints.dashboard.address=:8090"
      # - "--api.dashboard=true"
```

注意：この「安全でない」ダッシュボードは、本番環境（およびインスタンスが公開されている場合）では推奨されません。本番環境でダッシュボードを保持したい場合は、Traefikの[ドキュメント](https://doc.traefik.io/traefik/operations/dashboard/)を読んで適切に保護する方法を確認してください。

### 追加コンポーネント

#### 半自動および自動アノテーション

{{< ilink "/docs/administration/advanced/installation_automatic_annotation" "このガイド" >}}に従ってください。

### すべてのコンテナを停止する

以下のコマンドは、`up`によって作成されたコンテナとネットワークを停止し、削除します。

```shell
docker compose down
```

### 独自のドメインを使用する

localhost以外（別のドメイン）からCVATインスタンスにアクセスしたい場合は、`CVAT_HOST`環境変数を次のように指定する必要があります：

```shell
export CVAT_HOST=<YOUR_DOMAIN>
```

### 共有パス

タスクを作成する際に、データのアップロードに共有ストレージを使用できます。そのためには、共有ストレージをCVAT dockerコンテナにマウントする必要があります。この目的のための`docker-compose.override.yml`の例：

```yml
services:
  cvat_server:
    volumes:
      - cvat_share:/home/django/share:ro
  cvat_worker_import:
    volumes:
      - cvat_share:/home/django/share:ro
  cvat_worker_export:
    volumes:
      - cvat_share:/home/django/share:ro
  cvat_worker_annotation:
    volumes:
      - cvat_share:/home/django/share:ro
  cvat_worker_chunks:
    volumes:
      - cvat_share:/home/django/share:ro

volumes:
  cvat_share:
    driver_opts:
      type: none
      device: /mnt/share
      o: bind
```

共有デバイスパスを実際の共有パスに変更できます。

クラウドストレージをFUSEとして{{< ilink "/docs/administration/advanced/mounting_cloud_storages" "マウント" >}}し、後で共有として使用できます。

### メール検証

新しく登録されたユーザーに対してメール検証を有効にすることができます。Django allauthを設定してメール検証を有効にするには、[設定ファイル](https://github.com/cvat-ai/cvat/blob/develop/cvat/settings/base.py)でこれらのオプションを指定します（ACCOUNT_EMAIL_VERIFICATION = 'mandatory'）。ユーザーのメールアドレスが検証されるまでアクセスは拒否されます。

```python
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Django用のメールバックエンド設定
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
```

また、メールを送信するためにDjangoのメールバックエンドを設定する必要があります。これは使用しているメールサーバーに依存し、このチュートリアルではカバーされていません。詳細については、[Django SMTPバックエンド設定](https://docs.djangoproject.com/en/3.1/topics/email/#django.core.mail.backends.smtp.EmailBackend)を参照してください。

### ScalewayパブリッククラウドにCVATをデプロイする

[このチュートリアル](https://blog.scaleway.com/smart-data-annotation-for-your-computer-vision-projects-cvat-on-scaleway/)に従って、ScalewayクラウドインスタンスにCVATをインストールし、マウントされたオブジェクトストレージバケット内のデータを使用してリモートアクセスを設定します。

### HTTPSを使用した安全なCVATインスタンスのデプロイ

Traefikを使用すると、Let's EncryptからドメインのTLS証明書を自動的に取得でき、ウェブサイトへのアクセスにHTTPSプロトコルを使用できるようになります。

これを有効にするには、まず`CVAT_HOST`（ウェブサイトのドメイン）と`ACME_EMAIL`（Let's Encryptの連絡先メールアドレス）環境変数を設定します：

```shell
export CVAT_HOST=<YOUR_DOMAIN>
export ACME_EMAIL=<YOUR_EMAIL>
```

次に、`docker-compose.https.yml`ファイルを使用して、ベースの`docker-compose.yml`ファイルをオーバーライドします：

```shell
docker compose -f docker-compose.yml -f docker-compose.https.yml up -d
```

> ファイアウォールでは、ポート80と443が任意の場所からのインバウンド接続に対して開いている必要があります。

すると、CVATインスタンスはあなたのドメインのポート443（HTTPS）と80（HTTP、443にリダイレクト）で利用可能になります。

### 外部データベースを使用したCVATのデプロイ

デフォルトでは、`docker compose up`はPostgreSQLデータベースサーバーを起動し、CVATのデータを保存するために使用されます。代わりに独自のPostgreSQLインスタンスを使用したい場合は、次のようにします。CVATは`docker-compose.yml`で使用されているPostgreSQLと同じメジャーバージョンのみをサポートすることに注意してください。

まず、データベース接続設定を持つ環境変数を定義します：

```shell
export CVAT_POSTGRES_HOST=<PostgreSQLホスト名> # 必須
export CVAT_POSTGRES_PORT=<PostgreSQLポート> # デフォルトは5432
export CVAT_POSTGRES_DBNAME=<PostgreSQLデータベース名> # デフォルトは "cvat"
export CVAT_POSTGRES_USER=<PostgreSQLロール名> # デフォルトは "root"
export CVAT_POSTGRES_PASSWORD=<PostgreSQLロールのパスワード> # 必須
```

次に、`docker-compose.external_db.yml`ファイルを`docker compose up`コマンドに追加します：

```shell
docker compose -f docker-compose.yml -f docker-compose.external_db.yml up -d
```

### CVATイメージのプル/ビルド/更新方法

-   **CVATバージョンが2.1.0以下の場合**、compose設定は常に最新のイメージタグを指しているため、dockerを使用してイメージをプルする必要があります。例：

    ```shell
    docker pull cvat/server:v1.7.0
    docker tag cvat/server:v1.7.0 openvino/cvat_server:latest

    docker pull cvat/ui:v1.7.0
    docker tag cvat/ui:v1.7.0 openvino/cvat_ui:latest
    ```

    **CVATバージョンがv2.1.0より大きい場合**、`CVAT_VERSION`環境変数を使用して、DockerHubから特定のバージョンのビルド済みイメージをプルすることができます（例：`dev`）：

    ```shell
    CVAT_VERSION=dev docker compose pull
    ```

-   イメージを自分でビルドするには、`docker-compose.dev.yml` compose設定ファイルを`docker compose`コマンドに含めます。これは、ソースコードに変更を加えたCVATをビルドする場合に便利です。
    ```shell
    docker compose -f docker-compose.yml -f docker-compose.dev.yml build
    ```
-   ローカルイメージを`latest`または`dev`タグに更新するには、以下を実行します：
    ```shell
    CVAT_VERSION=dev docker compose pull
    ```
    または
    ```shell
    CVAT_VERSION=latest docker compose pull
    ```

## トラブルシューティング

### 中国ユーザー向けの情報源

中国にお住まいの場合、インストールには以下の情報源を上書きする必要があります。

-   `apt update`を使用するために：

    [Ubuntuミラーリングヘルプ](https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/)

    コンパイル済みパッケージ：

    ```shell
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse
    ```

    またはソースパッケージ：

    ```shell
    deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
    deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
    deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
    deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse
    ```

-   [Dockerミラーステーション](https://www.daocloud.io/mirror)

    `daemon.json`ファイルにレジストリミラーを追加します：

    ```json
    {
      "registry-mirrors": [
        "http://f1361db2.m.daocloud.io",
        "https://docker.mirrors.ustc.edu.cn",
        "https://hub-mirror.c.163.com",
        "https://mirror.ccs.tencentyun.com"
      ]
    }
    ```

-   `pip`を使用するために：

    [PyPIミラーリングヘルプ](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

    ```shell
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
    ```

-   `npm`を使用するために：

    [npmミラーリングヘルプ](https://npmmirror.com/)

    ```shell
    npm config set registry https://registry.npm.taobao.org/
    ```

-   `git`の代わりに[`gitee`](https://gitee.com/)を使用：

    [gitee.com上のCVATリポジトリ](https://gitee.com/monkeycc/cvat)

-   高速化ソース`docker.com`を置き換えるために実行：

    ```shell
    curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository \
      "deb [arch=amd64] https://mirrors.aliyun.com/docker-ce/linux/ubuntu \
      $(lsb_release -cs) stable"
    ```
    *(Note: Replaced download.docker.com with a common Chinese mirror, aliyun. Adjust if needed.)*

-   高速化ソース`google.com`を置き換えるために実行：
    *(Note: A direct replacement for google.com GPG key might be tricky or depend on local network setup. Often, package managers configured with Chinese mirrors handle this implicitly. If direct access to dl-ssl.google.com is blocked, users might need to find an alternative way to get the key or rely on mirrors that cache it. The original command is kept here for reference, but users in China might need to adapt.)*
    ```shell
    curl https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
    ```

### 証明書が原因でHTTPSが機能しない

SSL接続に問題がある場合、原因を特定するには、次のコマンドを実行してtraefikからログを取得する必要があります：

```shell
docker logs traefik
```

ログは問題を見つけるのに役立ちます。

エラーがファイアウォールに関連している場合：

-   ポート80と443を任意の場所からのインバウンド接続に対して開きます。
-   `acme.json`を削除します。場所はおそらく次のようになります：`/var/lib/docker/volumes/cvat_cvat_letsencrypt/_data/acme.json`。

`acme.json`が削除された後、すべてのcvat dockerコンテナを停止します：

```shell
docker compose -f docker-compose.yml -f docker-compose.https.yml down
```

変数が（あなたの値で）設定されていることを確認します：

```shell
export CVAT_HOST=<YOUR_DOMAIN>
export ACME_EMAIL=<YOUR_EMAIL>
```

そしてdockerを再起動します：

```shell
docker compose -f docker-compose.yml -f docker-compose.https.yml up -d
```