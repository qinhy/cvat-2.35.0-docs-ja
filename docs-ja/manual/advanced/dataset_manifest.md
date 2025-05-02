---

title: 'データセットマニフェスト'
linkTitle: 'データセットマニフェスト'
weight: 30
description:

---

## 概要

CVATで新しいタスクを作成する際、入力データの取得元を指定する必要があります。
CVATは、ローカルファイルのアップロード、サーバー上のマウントされたファイル共有、クラウドストレージ、リモートURLなど、さまざまなデータソースに対応しています。場合によっては、CVATが入力データについて追加情報を必要とすることがあります。この情報はデータセットマニフェストファイルで提供することができます。これらは主にクラウドストレージ利用時のネットワークトラフィック削減やタスク作成の高速化のために使われます。
ただし、他の場合にも使用でき、その詳細は以下で説明します。

データセットマニフェストファイルはJSONL形式のテキストファイルです。これらのファイルは[専用のコマンドラインツール](https://github.com/cvat-ai/cvat/tree/develop/utils/dataset_manifest)で自動生成するか、[マニフェストファイルフォーマット仕様](#file-format)に従って手動で作成できます。

## マニフェストファイルの利用方法と利用タイミング

マニフェストファイルは以下の場合に利用できます：
- 動画ファイルまたは画像セットをデータソースとして使用し、キャッシュモードが有効になっている場合。{{< ilink "/docs/manual/advanced/data_on_fly" "詳細はこちら" >}}
- データがクラウドストレージに存在する場合。{{< ilink "/docs/manual/basics/cloud-storages" "詳細はこちら" >}}
- `predefined` ファイルソート方式を指定している場合。
  {{< ilink "/docs/manual/basics/create_an_annotation_task#sorting-method" "詳細はこちら" >}}

### predefinedソート方式

使用するファイルソースにかかわらず、タスク設定で`predefined`ソート方式が選択されている場合、入力ファイルリスト内に`.jsonl`マニフェストファイルが見つかれば、その順序に従ってソースファイルが並びます。
マニフェストが見つからない場合は、入力ファイルリストで指定された順序が使用されます。

画像アーカイブ（例：`.zip`）で`predefined`ファイル順序を使う場合、マニフェストファイル（`*.jsonl`）が必須です。マニフェストファイルはアーカイブの隣に、入力ファイルリスト上で提供する必要があり、アーカイブ内には含めないでください。

入力ファイルリストに複数のマニフェストファイルが存在する場合はエラーとなります。

## マニフェストファイルの生成方法

CVATはマニフェストファイル生成専用のPythonツールを提供しています。
ソースコードは[こちら](https://github.com/cvat-ai/cvat/tree/develop/utils/dataset_manifest)にあります。

このツールを使ってマニフェストファイルを作成するのが推奨されます。データはツールからローカルでアクセス可能である必要があります。

### 使用方法

```bash
usage: create.py [-h] [--force] [--output-dir .] source

positional arguments:
  source                ソースパス

optional arguments:
  -h, --help            このヘルプメッセージを表示して終了
  --force               デフォルトで動画が要件を満たさず、マニフェストファイルが準備されない場合、このフラグで動画データのマニフェストファイルを強制生成
  --output-dir OUTPUT_DIR
                        マニフェストファイルの保存先ディレクトリ
```

### Dockerイメージからスクリプトを実行する

これが推奨される利用方法です。

スクリプトは`cvat/server`イメージから利用できます：

```bash
docker run -it --rm -u "$(id -u)":"$(id -g)" \
  -v "${PWD}":"/local" \
  --entrypoint python3 \
  cvat/server \
  utils/dataset_manifest/create.py --output-dir /local /local/<path/to/sources>
```

ファイルの場所に合わせてコマンドを適宜修正してください。

### スクリプトを直接利用する

#### Ubuntu 20.04

依存関係のインストール：

```bash
# 一般
sudo apt-get update && sudo apt-get --no-install-recommends install -y \
    python3-dev python3-pip python3-venv pkg-config
```

```bash
# ライブラリコンポーネント
sudo apt-get install --no-install-recommends -y \
    libavformat-dev libavcodec-dev libavdevice-dev \
    libavutil-dev libswscale-dev libswresample-dev libavfilter-dev
```

環境を作成し、必要なpythonモジュールをインストール：

```bash
python3 -m venv .env
. .env/bin/activate
pip install -U pip
pip install -r utils/dataset_manifest/requirements.in
```

> この方法で動画に使う場合、サーバーがデコードした結果と異なる場合があります。これはffmpegライブラリのバージョンによるものです。そのため、Dockerベースのツール利用が推奨されます。

### 使用例

十分なキーフレームを含む動画のデータセットマニフェストを現在のディレクトリに作成：

```bash
python utils/dataset_manifest/create.py ~/Documents/video.mp4
```

キーフレームが十分でない動画のデータセットマニフェストを作成：

```bash
python utils/dataset_manifest/create.py --force --output-dir ~/Documents ~/Documents/video.mp4
```

画像のデータセットマニフェストを作成：

```bash
python utils/dataset_manifest/create.py --output-dir ~/Documents ~/Documents/images/
```

パターンを使ってデータセットマニフェストを作成（`*`、`?`、`[]`が利用可）：

```bash
python utils/dataset_manifest/create.py --output-dir ~/Documents "/home/${USER}/Documents/**/image*.jpeg"
```

Dockerイメージを使ってデータセットマニフェストを作成：

```bash
docker run -it --rm -u "$(id -u)":"$(id -g)" \
  -v ~/Documents/data/:${HOME}/manifest/:rw \
  --entrypoint '/usr/bin/bash' \
  cvat/server \
  utils/dataset_manifest/create.py --output-dir ~/manifest/ ~/manifest/images/
```

### ファイルフォーマット

データセットマニフェストファイルはJSONL形式のテキストファイルです。これらのファイルには2つのサブフォーマットがあります：
_動画用_ と _画像および3dデータ用_ です。

> 波括弧で囲まれた各トップレベルエントリは1つの文字列でなければならず、空文字列は禁止です。
> 下記の説明におけるフォーマットは説明用です。

#### 動画用データセットマニフェスト

このファイルは1つの動画を記述します。

`pts` - フレームがユーザーに表示されるべき時刻  
`checksum` - 特定の画像/フレームをデコードしたMD5ハッシュ値

```json
{ "version": <string, バージョンID> }
{ "type": "video" }
{ "properties": {
  "name": <string, ファイル名>,
  "resolution": [<int, 幅>, <int, 高さ>],
  "length": <int, フレーム数>
}}
{
  "number": <int, フレーム番号>,
  "pts": <int, フレームpts>,
  "checksum": <string, MD5フレームハッシュ>
} （繰り返し可能）
```

#### 画像および他データ形式用データセットマニフェスト

このファイルは順序付きの画像や3D点群を記述します。

`name` - ファイルのベース名とデータセットルートからのディレクトリ  
`checksum` - 特定の画像/フレームをデコードしたMD5ハッシュ値

```json
{ "version": <string, バージョンID> }
{ "type": "images" }
{
  "name": <string, 画像ファイル名>,
  "extension": <string, .+ファイル拡張子>,
  "width": <int, 幅>,
  "height": <int, 高さ>,
  "meta": <dict, オプション>,
  "checksum": <string, MD5ハッシュ, オプション>
} （繰り返し可能）
```

### ファイル例

#### 動画のマニフェスト

```json
{"version":"1.0"}
{"type":"video"}
{"properties":{"name":"video.mp4","resolution":[1280,720],"length":778}}
{"number":0,"pts":0,"checksum":"17bb40d76887b56fe8213c6fded3d540"}
{"number":135,"pts":486000,"checksum":"9da9b4d42c1206d71bf17a7070a05847"}
{"number":270,"pts":972000,"checksum":"a1c3a61814f9b58b00a795fa18bb6d3e"}
{"number":405,"pts":1458000,"checksum":"18c0803b3cc1aa62ac75b112439d2b62"}
{"number":540,"pts":1944000,"checksum":"4551ecea0f80e95a6c32c32e70cac59e"}
{"number":675,"pts":2430000,"checksum":"0e72faf67e5218c70b506445ac91cdd7"}
```

#### 画像データセットのマニフェスト

```json
{"version":"1.0"}
{"type":"images"}
{"name":"image1","extension":".jpg","width":720,"height":405,"meta":{"related_images":[]},"checksum":"548918ec4b56132a5cff1d4acabe9947"}
{"name":"image2","extension":".jpg","width":183,"height":275,"meta":{"related_images":[]},"checksum":"4b4eefd03cc6a45c1c068b98477fb639"}
{"name":"image3","extension":".jpg","width":301,"height":167,"meta":{"related_images":[]},"checksum":"0e454a6f4a13d56c82890c98be063663"}
```