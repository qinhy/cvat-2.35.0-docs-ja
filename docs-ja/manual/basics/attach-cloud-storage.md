---
title: 'クラウドストレージの接続'
linkTitle: 'クラウドストレージの接続'
weight: 23
description: 'UIを使用してクラウドストレージを接続する方法'
---

CVATでは、**AWS S3**、**Azure Blob Storage**、**Google Cloud Storage**のストレージを利用して、タスク用の画像データセットのインポートおよびエクスポートが可能です。

参照：

- [AWS S3](#aws-s3)
  - [バケットの作成](#create-a-bucket)
  - [データのアップロード](#upload-data)
  - [アクセス権限](#access-permissions)
    - [認証付きアクセス](#authenticated-access)
    - [匿名アクセス](#anonymous-access)
  - [AWS S3ストレージの接続](#attach-aws-s3-storage)
  - [AWS S3マニフェストファイル](#aws-s3-manifest-file)
  - [ビデオチュートリアル：CVATにAWS S3をクラウドストレージとして追加](#video-tutorial-add-aws-s3-as-cloud-storage-in-cvat)
- [Google Cloud Storage](#google-cloud-storage)
  - [バケットの作成](#create-a-bucket-1)
  - [データのアップロード](#upload-data-1)
  - [アクセス権限](#access-permissions-1)
    - [認証付きアクセス](#authenticated-access-1)
    - [匿名アクセス](#anonymous-access-1)
  - [Google Cloud Storageの接続](#attach-google-cloud-storage)
  - [ビデオチュートリアル：CVATにGoogle Cloud Storageをクラウドストレージとして追加](#video-tutorial-add-google-cloud-storage-as-cloud-storage-in-cvat)
- [Microsoft Azure Blob Storage](#microsoft-azure-blob-storage)
  - [バケットの作成](#create-a-bucket-2)
  - [コンテナの作成](#create-a-container)
  - [データのアップロード](#upload-data-2)
  - [SASトークンと接続文字列](#sas-token-and-connection-string)
  - [個人利用](#personal-use)
  - [Azure Blob Storageの接続](#attach-azure-blob-storage)
  - [ビデオチュートリアル：CVATにMicrosoft Azure Blob Storageをクラウドストレージとして追加](#video-tutorial-add-microsoft-azure-blob-storage-as-cloud-storage-in-cvat)
- [データセットの準備](#prepare-the-dataset)

## AWS S3

### バケットの作成

バケットを作成するには、以下の手順を行ってください：

1. [AWSアカウント](https://portal.aws.amazon.com/billing/signup#/start)を作成します。
2. [AWS-S3コンソール](https://s3.console.aws.amazon.com/s3/home)にアクセスし、**Create bucket**をクリックします。

   ![](/images/aws-s3_tutorial_1.jpg)

3. バケットの名前とリージョンを指定します。他のバケットの設定をコピーしたい場合は、**Choose bucket**ボタンをクリックしてください。
4. **Block all public access**を有効にします。アクセスには**access key ID**と**secret access key**を使用します。
5. **Create bucket**をクリックします。

新しいバケットがバケット一覧に表示されます。

### データのアップロード

> **注意**: マニフェストファイルは任意です。

アノテーション用データと`manifest.jsonl`ファイルをアップロードする必要があります。

1. データを準備します。
   詳細は[データセットの準備](#prepare-the-dataset)をご参照ください。
2. バケットを開き、**Upload**をクリックします。

   ![](/images/aws-s3_tutorial_5.jpg)

3. マニフェストファイルと画像フォルダをページ上にドラッグし、**Upload**をクリックします。

![](/images/aws-s3_tutorial_1.gif)

### アクセス権限

#### 認証付きアクセス

アクセス権限を追加するには、以下の手順を行ってください：

1. [IAM](https://console.aws.amazon.com/iamv2/home#/users)にアクセスし、**Add users**をクリックします。
2. **User name**を設定し、**Access key - programmatic access**を有効にします。

   ![](/images/aws-s3_tutorial_2.jpg)

3. **Next: Permissions**をクリックします。
4. **Create group**をクリックし、グループ名を入力します。
5. 検索を使用して、以下を選択します：

   - 読み取り専用アクセス：**AmazonS3ReadOnlyAccess**
   - フルアクセス：**AmazonS3FullAccess**

   ![](/images/aws-s3_tutorial_3.jpg)

6. （任意）ユーザーにタグを追加し、次のページへ進みます。
7. **Access key ID**と**Secret access key**を保存します。

![](/images/aws-s3_tutorial_4.jpg)

詳細は[Creating an IAM user in your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)をご覧ください。

#### 匿名アクセス

バケットへのパブリックアクセスの設定方法については、
[Configuring block public access settings for your S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/configuring-block-public-access-bucket.html)を参照してください。

### AWS S3ストレージの接続

ストレージを接続するには、以下の手順を行ってください：

1. CVATにログインし、別タブでバケットページを開きます。
2. CVATのトップメニューで**Cloud storages**を選択し、開いたページで**+**をクリックします。

以下の項目を入力してください：

<!--lint disable maximum-line-length-->

| CVAT                    | AWS S3                                                                                                                                                                                                                                              |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Display name**        | ストレージの表示名（任意の名称）。                                                                                                                                                                                                                 |
| **Description**         | （任意）ストレージの説明を追加。                                                                                                                                                                                                                   |
| **Provider**            | ドロップダウンから**AWS S3**を選択。                                                                                                                                                                                                               |
| **Bucket name**         | [バケット名](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket)。                                                                                                                                                                 |
| **Authentication type** | バケット設定による：<br><li>**Key id and secret access key pair**：[IAM](https://console.aws.amazon.com/iamv2/home?#/users)で取得可能。<br><li>**Anonymous access**：匿名アクセス用。バケットのパブリックアクセスが有効である必要があります。 |
| **Region**              | （任意）リストからリージョンを選択、または新規追加。詳細は[**利用可能なリージョン**](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions)を参照。     |
| **Prefix**              | （任意）バケット内容をフィルタするプレフィックス。デフォルトプレフィックスを設定すると、CVATで特定フォルダのデータのみ使用されます。クラウドデータでタスク作成時に表示されるファイルに影響します。                 |
| **Manifests**           | （任意）**+ Add manifest**をクリックし、拡張子付きファイル名を入力。例：`manifest.jsonl`。                                                                                                                |

<!--lint enable maximum-line-length-->

全ての項目を入力したら、**Submit**をクリックしてください。

### AWS S3マニフェストファイル

> **注意**: マニフェストファイルは任意です。

マニフェストファイルを準備するには、以下の手順を行ってください：

1. [**AWS CLI**](https://aws.amazon.com/cli/)にアクセスし、
   [マニフェストファイル準備用スクリプト](https://github.com/cvat-ai/cvat/tree/develop/utils/dataset_manifest)を実行します。
2. [**aws-shell マニュアル**](https://github.com/awslabs/aws-shell)の手順に従ってインストールしてください。
   <br>`aws configure`コマンドで認証情報を設定できます。
   <br>`Access Key ID`と`Secret Access Key`、リージョンを入力してください。

```bash
aws configure
Access Key ID: <your Access Key ID>
Secret Access Key: <your Secret Access Key>
```

3. バケットの内容をPC上のフォルダにコピーします：

```bash
aws s3 cp <s3://bucket-name> <yourfolder> --recursive
```

4. ファイルをコピーしたら、以下のコマンドでマニフェストファイルを作成します。
   {{< ilink "/docs/manual/advanced/dataset_manifest" "マニフェストファイル準備セクション" >}}参照：

```bash
python <cvat repository>/utils/dataset_manifest/create.py --output-dir <yourfolder> <yourfolder>
```

5. マニフェストファイルが作成できたら、aws s3バケットにアップロードします：

- ユーザー作成時に読み書き権限を付与した場合、以下を実行：

```bash
aws s3 cp <yourfolder>/manifest.jsonl <s3://bucket-name>
```

- 読み取り専用権限の場合は、ブラウザーからアップロードページでマニフェストファイルをドラッグ＆ドロップし、アップロードをクリックしてください。

![](/images/aws-s3_tutorial_5.jpg)

### ビデオチュートリアル：CVATにAWS S3をクラウドストレージとして追加

<!--lint disable maximum-line-length-->

<iframe width="560" height="315" src="https://www.youtube.com/embed/y6fgZ4X87Lc?si=5EewLS4XA7birS25" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<!--lint enable maximum-line-length-->

## Google Cloud Storage

### バケットの作成

バケットを作成するには、以下の手順を行ってください：

1. [Googleアカウント](https://support.google.com/accounts/answer/27441?hl=ja)を作成し、ログインします。
2. [Google Cloud](https://cloud.google.com/)ページで**Start Free**をクリックし、必要事項を入力して利用規約に同意します。
   > **注意:** Googleは支払い情報の追加を要求します。2の手順にはクレジットカードが必要です。
3. 以下のパラメータで[バケットを作成](https://cloud.google.com/storage/docs/creating-buckets)します：
   - **Name your bucket**：一意な名前
   - **Choose where to store your data**：最寄りのロケーションを指定
   - **Choose a storage class for your data**：`Set a default class` > `Standard`
   - **Choose how to control access to objects**：`Enforce public access prevention on this bucket` > `Uniform`（デフォルト）
   - **How to protect data**：`None`

![GB](/images/google_bucket.png)

バケットページに遷移します。

### データのアップロード

> **注意**: マニフェストファイルは任意です。

アノテーション用データと`manifest.jsonl`ファイルをアップロードする必要があります。

1. データを準備します。
   詳細は[データセットの準備](#prepare-the-dataset)をご参照ください。
2. バケットを開き、トップメニューから
   **Upload files**または**Upload folder**
   （ファイルの構成によって選択）をクリックします。

### アクセス権限

Google Cloud Storageにアクセスするには、[cloud resource manager page](https://console.cloud.google.com/cloud-resource-manager)から**Project ID**を取得してください。

![](/images/google_cloud_storage_tutorial5.jpg)

アクセス種類に応じて下記の手順に従ってください。

#### 認証付きアクセス

認証付きアクセスには、サービスアカウントとキーファイルの作成が必要です。

サービスアカウントの作成方法：

1. Google Cloud Platformで、**IAM & Admin** > **Service Accounts**にアクセスし、**+Create Service Account**をクリックします。
2. アカウント名を入力し、**Create And Continue**をクリックします。
3. ロールを選択（例：**Basic** > **Viewer**）し、**Continue**をクリックします。
4. （任意）サービスアカウントへの権限を付与します。
5. **Done**をクリックします。

![](/images/google_cloud_storage_tutorial2.jpg)

キーファイルの作成方法：

1. **IAM & Admin** > **Service Accounts** > アカウント名をクリック > **Keys**を選択します。
2. **Add key**をクリックし、**Create new key** > **JSON**を選択します。
3. **Create**をクリックすると、キーファイルが自動でダウンロードされます。

![](/images/google_cloud_storage_tutorial3.jpg)

キーに関する詳細は
[キー作成について詳しくはこちら](https://cloud.google.com/docs/authentication/getting-started)を参照してください。

#### 匿名アクセス

匿名アクセスを設定するには：

1. バケットを開き、**Permissions**タブに移動します。
2. **+ Grant access**をクリックして新しいプリンシパルを追加します。
3. **New principals**欄に`allUsers`を入力し、
   ロールは`Cloud Storage Legacy` > `Storage Legacy Bucket Reader`を選択します。
4. **Save**をクリックします。

![](/images/google_cloud_storage_tutorial4.jpg)

これでGoogle Cloud StorageバケットをCVATに接続できます。

### Google Cloud Storageの接続

ストレージを接続するには、以下の手順を行ってください：

1. CVATにログインし、別タブで[バケット](https://console.cloud.google.com/storage/browser)ページを開きます。
2. CVATのトップメニューで**Cloud storages**を選択し、開いたページで**+**をクリックします。

以下の項目を入力してください：

<!--lint disable maximum-line-length-->

| CVAT                    | Google Cloud Storage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Display name**        | ストレージの表示名（任意の名称）。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Description**         | （任意）ストレージの説明を追加。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Provider**            | ドロップダウンから**Google Cloud Storage**を選択。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Bucket name**         | バケット名。[ストレージブラウザページ](https://console.cloud.google.com/storage/browser)で確認可能。                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Authentication type** | バケット設定による：<br><li>**認証付きアクセス**：**Key file**項目をクリックし、キーファイルをPCからアップロード。<br> **高度な設定**：セルフホストの場合、キーファイル未指定時は環境変数`GOOGLE_APPLICATION_CREDENTIALS`が使用されます。詳細は[クライアントライブラリを使用したCloudサービス認証](https://cloud.google.com/docs/authentication/client-libraries#setting_the_environment_variable)参照。<br><li> **匿名アクセス**：匿名アクセス用。バケットのパブリックアクセスが有効である必要があります。 |
| **Prefix**              | （任意）バケットデータをフィルタするプレフィックス。デフォルトプレフィックスを設定すると、CVATで特定フォルダのデータのみ使用されます。クラウドデータでタスク作成時に表示されるファイルに影響します。                                                                                                                                                                                                                                                                                                                                                                         |
| **Project ID**          | [Project ID](#authenticated-access)。<br>詳細は[プロジェクトページ](https://cloud.google.com/resource-manager/docs/creating-managing-projects)および[cloud resource manager page](https://console.cloud.google.com/cloud-resource-manager)参照。<br>**注意：**プロジェクト名とプロジェクトIDは異なります。                                                                                                                                                                                                                                                                                |
| **Location**            | （任意）リストからリージョンを選択、または新規追加。詳細は[**利用可能なロケーション**](https://cloud.google.com/storage/docs/locations#available-locations)を参照。                                                                                                                                                                                                                                                                                                                                                                                                |
| **Manifests**           | （任意）**+ Add manifest**をクリックし、拡張子付きファイル名を入力。例：`manifest.jsonl`。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

<!--lint enable maximum-line-length-->

全ての項目を入力したら、**Submit**をクリックしてください。

### ビデオチュートリアル：CVATにGoogle Cloud Storageをクラウドストレージとして追加

<!--lint disable maximum-line-length-->

<iframe width="560" height="315" src="https://www.youtube.com/embed/pl2KZqJouvI?si=58sziJGbHHc-Mcom" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<!--lint enable maximum-line-length-->

## Microsoft Azure Blob Storage

### バケットの作成

バケットを作成するには、以下の手順を行ってください：

1. [Microsoft Azure](https://azure.microsoft.com/ja-jp/free/)アカウントを作成し、ログインします。
2. [Azureポータル](https://portal.azure.com/#home)にアクセスし、リソースにカーソルを合わせ、ポップアップウィンドウで**Create**をクリックします。

   ![](/images/azure_blob_container_tutorial1.jpg)

3. グループ名を入力し、**Review + create**をクリック。入力内容を確認し、**Create**をクリックします。
4. [リソースグループページ](https://portal.azure.com/#view/HubsExtension/BrowseResourceGroups)に移動し、作成したグループを選択して**Create resources**をクリックします。
5. マーケットプレイスページで**Storage account**を検索し選択します。

   ![](/images/azure_blob_container_tutorial2.png)

6. **Storage account**をクリックし、次のページで**Create**をクリックします。
7. **Basics**タブで以下を入力します：

   - **Storage account name**：CVATからコンテナへアクセスする際の名前
   - 最寄りのリージョンを選択
   - **Performance**は**Standard**を選択
   - **Local-redundancy storage (LRS)**を選択
   - **next: Advanced>**をクリック

   ![](/images/azure_blob_container_tutorial4.png)

8. **Advanced**ページで以下を入力：
   - （任意）**Allow enabling public access on containers**を無効にすると、匿名アクセスを禁止できます。
   - **Next > Networking**をクリック

![](/images/azure_blob_container_tutorial5.png)

9. **Networking**タブで以下を入力：

   - パブリックアクセスを変更したい場合は**Public access from all networks**を有効化
   - **Next>Data protection**をクリック

     > 特別な設定が必要な場合以外、他のタブは変更不要です。

10. **Review**をクリックし、データの読み込みを待ちます。
11. **Create**をクリック。デプロイが開始されます。
12. デプロイ完了後、**Go to resource**をクリックします。

![](/images/azure_blob_container_tutorial6.jpg)

### コンテナの作成

コンテナを作成するには、以下の手順を行ってください：

1. コンテナセクションに移動し、トップメニューの**+Container**をクリック

![](/images/azure_blob_container_tutorial7.jpg)

3. コンテナ名を入力
4. （任意）**Public access level**ドロップダウンでアクセス種別を選択
   <br>**注意：** **Allow enabling public access on containers**を無効にした場合、この項目は非アクティブになります。
5. **Create**をクリック

### データのアップロード

アノテーション用データと`manifest.jsonl`ファイルをアップロードする必要があります。

1. データを準備します。
   詳細は[データセットの準備](#prepare-the-dataset)をご参照ください。
2. コンテナに移動し、**Upload**をクリック
3. **Browse for files**をクリックし、画像を選択
   > 注意：画像がフォルダ内の場合、**Advanced settings** > **Upload to folder**でフォルダを指定してください。
4. **Upload**をクリック

![](/images/azure_blob_container_tutorial9.jpg)

### SASトークンと接続文字列

SASトークンまたは接続文字列を用いて、コンテナへ安全にアクセスできます。

認証情報の設定方法：

1. **Home** > **Resource groups** > リソース名 > ストレージアカウントを選択
2. 左メニューで**Shared access signature**をクリック
3. 以下の項目を設定：
   - **Allowed services**：**Blob**を有効化。他はすべて無効
   - **Allowed resource types**：**Container**と**Object**を有効化。他はすべて無効
   - **Allowed permissions**：**Read**、**Write**、**List**を有効化。他はすべて無効
   - **Start and expiry date**：開始日と終了日を設定
   - **Allowed protocols**：**HTTPS and HTTP**を選択
   - その他の項目はデフォルトのまま
4. **Generate SAS and connection string**をクリックし、**SAS token**または**Connection string**をコピー

![](/images/azure_blob_container_tutorial3.jpg)

### 個人利用

個人利用の場合、CVATの**SAS Token**欄にストレージアカウントの**Access Key**を使用できます。

**Access Key**の取得方法：

1. Azureポータルで**Security + networking** > **Access Keys**に移動
2. **Show**をクリックし、キーをコピー

![](/images/azure_blob_container_tutorial8.jpg)

### Azure Blob Storageの接続

ストレージを接続するには、以下の手順を行ってください：

1. CVATにログインし、別タブでバケットページを開きます。
2. CVATのトップメニューで**Cloud storages**を選択し、開いたページで**+**をクリックします。

以下の項目を入力してください：

<!--lint disable maximum-line-length-->

| CVAT                    | Azure                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Display name**        | ストレージの表示名（任意の名称）。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Description**         | （任意）ストレージの説明を追加。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Provider**            | ドロップダウンから**Azure Blob Container**を選択。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Container name`**     | クラウドストレージのコンテナ名。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Authentication type** | コンテナの設定による。<br>**[アカウント名とSASトークン](https://docs.microsoft.com/ja-jp/azure/cognitive-services/translator/document-translation/create-sas-tokens?tabs=blobs)**：<ul><li>**Account name**にストレージアカウント名を入力<li>**SAS token**は[ストレージアカウント](#sas-token)の**Shared access signature**セクションで取得</ul>。**[匿名アクセス](https://docs.microsoft.com/ja-jp/azure/storage/blobs/anonymous-read-access-configure?tabs=portal)**：匿名アクセス用には**Allow enabling public access on containers**を有効にする必要があります。   |
| **Prefix**              | （任意）バケットデータをフィルタするプレフィックス。デフォルトプレフィックスを設定すると、CVATで特定フォルダのデータのみ使用されます。クラウドデータでタスク作成時に表示されるファイルに影響します。                                                                                                                                                                                                                                                                                                                                                                           |
| **Manifests**           | （任意）**+ Add manifest**をクリックし、拡張子付きファイル名を入力。例：`manifest.jsonl`。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

<!--lint enable maximum-line-length-->

全ての項目を入力したら、**Submit**をクリックしてください。

### ビデオチュートリアル：CVATにMicrosoft Azure Blob Storageをクラウドストレージとして追加

<!--lint disable maximum-line-length-->

<iframe width="560" height="315" src="https://www.youtube.com/embed/nvrm8oFBKMY?si=v2z6Rjlc250niXPX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<!--lint enable maximum-line-length-->

## データセットの準備

例として、データセットは[The Oxford-IIIT Pet Dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/)とします：

1. [画像アーカイブ](https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz)をダウンロードします。
2. アーカイブを準備したフォルダに展開します。
3. マニフェストを作成します。詳細は
   {{< ilink "/docs/manual/advanced/dataset_manifest" "**Dataset manifest**" >}}を参照してください：

```bash
python <cvat repository>/utils/dataset_manifest/create.py --output-dir <your_folder> <your_folder>
```