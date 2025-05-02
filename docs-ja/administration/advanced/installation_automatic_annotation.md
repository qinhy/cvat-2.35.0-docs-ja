---

title: '半自動および自動アノテーション'
linkTitle: 'インストール：自動アノテーション'
weight: 10
description: '半自動および自動アノテーションに必要なコンポーネントのインストール情報。'

---

> **⚠ 警告: `docker compose up` を使用しないでください**
> もし使用した場合、`docker compose down` で全てのコンテナを停止してください。

- 自動アノテーションツール付きでcvatを起動するには、cvatのルートディレクトリから以下を実行してください:

  ```bash
  docker compose -f docker-compose.yml -f components/serverless/docker-compose.serverless.yml up -d
  ```

  Docker Composeファイルに変更を加えた場合は、最後に `--build` を追加してください。

  コンテナを停止するには、単純に次を実行します:

  ```bash
  docker compose -f docker-compose.yml -f components/serverless/docker-compose.serverless.yml down
  ```

- サーバーレス関数を構築しデプロイするには、`nuctl` コマンドラインツールをインストールする必要があります。
  [バージョン 1.13.0](https://github.com/nuclio/nuclio/releases/tag/1.13.0) をダウンロードしてください。
  ダウンロードするバージョンが
  [docker-compose.serverless.yml](https://github.com/cvat-ai/cvat/blob/develop/components/serverless/docker-compose.serverless.yml)
  のバージョンと一致していることが重要です。
  例として、wgetを使用する場合:

  ```bash
  wget https://github.com/nuclio/nuclio/releases/download/<version>/nuctl-<version>-linux-amd64
  ```

  Nuclioをダウンロードした後、適切な権限を与え、ソフトリンクを作成します。

  ```bash
  sudo chmod +x nuctl-<version>-linux-amd64
  sudo ln -sf $(pwd)/nuctl-<version>-linux-amd64 /usr/local/bin/nuctl
  ```

- いくつかの関数をデプロイします。
  これにより自動的に `cvat` Nuclioプロジェクトが作成され、関数が格納されます。
  以下のコマンドはCVATが `docker compose` でインストールされた後にのみ実行してください。
  これは全てのサーバーレス関数を管理するnuclioダッシュボードを起動するためです。

  ```bash
  ./serverless/deploy_cpu.sh serverless/openvino/dextr
  ./serverless/deploy_cpu.sh serverless/openvino/omz/public/yolo-v3-tf
  ```

  #### GPUサポート

  [Nvidia Container Toolkit](https://www.tensorflow.org/install/docker#gpu_support) をインストールする必要があります。
  また、nuclioデプロイコマンドに `--resource-limit nvidia.com/gpu=1 --triggers '{"myHttpTrigger": {"maxWorkers": 1}}'` を追加してください。
  GPUメモリに余裕がある場合はmaxWorkerを増やすことができます。
  例えば、以下はGPU上で実行されます:

  ```bash
  nuctl deploy --project-name cvat \
    --path serverless/tensorflow/matterport/mask_rcnn/nuclio \
    --platform local --base-image tensorflow/tensorflow:1.15.5-gpu-py3 \
    --desc "Python 3、Keras、TensorFlow上でのMask RCNNのGPUベース実装。" \
    --image cvat/tf.matterport.mask_rcnn_gpu \
    --triggers '{"myHttpTrigger": {"maxWorkers": 1}}' \
    --resource-limit nvidia.com/gpu=1
  ```

  **注意:**

  - GPUでデプロイできる関数の数は、お使いのGPUメモリに制限されます。
  - その他の例については [deploy_gpu.sh](https://github.com/cvat-ai/cvat/blob/develop/serverless/deploy_gpu.sh) スクリプトを参照してください。
  - 一部のモデル（特に{{< ilink "/docs/manual/advanced/ai-tools#trackers" "SiamMask" >}}）では [Nvidia driver](https://www.nvidia.com/en-us/drivers/unix/)
    バージョン450.80.02以上が必要です。

  **Windowsユーザー向け注意:**

  WindowsでCVATをインストールしnuclioを使用したい場合は、
  [こちら](https://docs.nvidia.com/cuda/wsl-user-guide/index.html) の手順に従いWSL用のNvidiaドライバをインストールしてください。
  “2.3 Installing Nvidia drivers” までの手順を実施してください。
  重要な要件: Docker Desktop最新版、WSL用Nvidiaドライバ最新版、およびWindows Insider Preview Devチャネルからの最新のアップデートが必要です。

**Nuclio関数のトラブルシューティング:**

- [localhost:8070](http://localhost:8070) でnuclioダッシュボードを開くことができます。
  関数のステータスが正常に稼働していることを確認してください。
- デプロイしたDLモデルをサーバーレス関数としてテスト可能です。以下のコマンドはLinuxおよびMac OSで動作します。

  ```bash
  image=$(curl https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png --output - | base64 | tr -d '\n')
  cat << EOF > /tmp/input.json
  {"image": "$image"}
  EOF
  cat /tmp/input.json | nuctl invoke openvino-omz-public-yolo-v3-tf -c 'application/json'
  ```

  <details>

  ```bash
  20.07.17 12:07:44.519    nuctl.platform.invoker (I) Executing function {"method": "POST", "url": "http://:57308", "headers": {"Content-Type":["application/json"],"X-Nuclio-Log-Level":["info"],"X-Nuclio-Target":["openvino-omz-public-yolo-v3-tf"]}}
  20.07.17 12:07:45.275    nuctl.platform.invoker (I) Got response {"status": "200 OK"}
  20.07.17 12:07:45.275                     nuctl (I) >>> Start of function logs
  20.07.17 12:07:45.275 ino-omz-public-yolo-v3-tf (I) Run yolo-v3-tf model {"worker_id": "0", "time": 1594976864570.9353}
  20.07.17 12:07:45.275                     nuctl (I) <<< End of function logs

  > レスポンスヘッダー:
  Date = Fri, 17 Jul 2020 09:07:45 GMT
  Content-Type = application/json
  Content-Length = 100
  Server = nuclio

  > レスポンスボディ:
  [
      {
          "confidence": "0.9992254",
          "label": "person",
          "points": [
              39,
              124,
              408,
              512
          ],
          "type": "rectangle"
      }
  ]
  ```

  </details>

- 内部サーバーエラーを確認するには `docker ps -a` を実行し、コンテナ一覧を表示します。
  確認したいコンテナ（例: `nuclio-nuclio-tf-faster-rcnn-inception-v2-coco-gpu`）を探してください。
  その後、`docker logs <コンテナ名>` でログを確認します。例:

  ```bash
  docker logs nuclio-nuclio-tf-faster-rcnn-inception-v2-coco-gpu
  ```

- コンテナ内のコードをデバッグするには、vscodeを使ってコンテナにアタッチできます。[手順はこちら](https://code.visualstudio.com/docs/remote/attach-container)。
  変更を反映するには、必ずコンテナを再起動してください。
  ```bash
  docker restart <コンテナ名>
  ```