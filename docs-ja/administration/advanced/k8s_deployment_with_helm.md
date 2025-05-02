---

title: 'Helmを使ったKubernetesでのCVATデプロイ'
linkTitle: 'Helmを使ったKubernetesでのCVATデプロイ'
weight: 1
description: 'KubernetesクラスターへのCVATデプロイ手順。'

---

<!--lint disable heading-style-->


- [前提条件](#prerequisites)
  - [依存関係のインストール](#installing-dependencies)
  - [オプション手順](#optional-steps)
- [設定](#configuration)
  - [Postgresqlパスワードについて](#postgresql-password)
  - [(オプション)自動アノテーション機能の有効化](#optional-enable-auto-annotation-feature)
  - [アナリティクス](#analytics)
- [デプロイ](#deployment)
  - [オーバーライドあり:](#with-overrides)
  - [オーバーライドなし:](#without-overrides)
- [デプロイ後の設定](#post-deployment-configuration)
  - [スーパーユーザーの作成方法](#how-to-create-superuser)
- [FAQ](#faq)
  - [Kubernetesとは？どのように動作する？](#what-is-kubernetes-and-how-it-is-working)
  - [Helmとは？どのように動作する？](#what-is-helm-and-how-it-is-working)
  - [Minikubeのセットアップ方法](#how-to-setup-minikube)
  - ['helm upgrade'でどんな差分が発生するか知りたい](#how-to-understand-what-diff-will-be-inflicted-by-helm-upgrade)
  - [自身のpostgresql/redisをチャートで使いたい](#i-want-to-use-my-own-postgresqlredis-with-your-chart)
  - [values.yamlの設定を一部上書きしたい](#i-want-to-override-some-settings-in-valuesyaml)
  - [なぜredisやpostgresに外部チャートを利用した？](#why-you-used-external-charts-to-provide-redis-and-postgres)

## 前提条件
1. [kubernetes](https://kubernetes.io/) クラスターがインストール・設定済みであること。まだクラスターを持っていない場合は、[Minikube](https://github.com/kubernetes/minikube/) を使って作成できます。[Minikubeのセットアップ方法](#how-to-setup-minikube)。
1. [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl) のインストール
1. [Helm](https://helm.sh/) のインストール
1. [依存関係](#installing-dependencies) のインストール

### 依存関係のインストール
インストールまたはアップデートするには以下を実行:
```shell
helm dependency update
```

### オプション手順
1. Traefik ingressコントローラーのingress設定はデフォルトで有効になっています。

   Minikube利用時の注意:
   - Traefikは主要サービスを `Loadbalanser` タイプで作成しますが、これはCloudによるexternalIPの割り当てが必要であり、Minikubeでは発生しません。
     そのため、traefikサービスに明示的にexternalIPを指定する必要があります。
     `values.override.yaml` ファイルに以下を追加してください:
     ```yaml
     traefik:
       service:
         externalIPs:
           - "あなたのMinikubeのIP（`minikube ip`コマンドで取得）"
     ```
   - また、CVATのingressがhostsファイル（/etc/hosts）にあることも確認してください。
     以下のコマンドで追加できます。
     デフォルトドメイン名は `cvat.local` ですが、`values.override.yaml` で変更可能です。
     ```shell
     echo "$(minikube ip) cvat.local" | sudo tee -a /etc/hosts
     ```

## 設定
1. `helm-chart` ディレクトリ内に `values.override.yaml` ファイルを作成します。
1. チャート用の新しいパラメータで `values.override.yaml` を記入します。
1. [Postgresqlパスワード](#postgresql-password)を上書きします。

### Postgresqlパスワードについて
以下を `values.override.yaml` に記載してください。
```yaml
postgresql:
  secret:
    password: <insert_password>
    postgres_password: <insert_postgres_password>
    replication_password: <insert_replication_password>
```
または独自のシークレットを作成し、以下のように指定できます:
```yaml
postgresql:
   global:
     postgresql:
       existingSecret: <secret>
```

### (オプション) 自動アノテーション機能の有効化

開始前に以下の前提条件を満たしていることを確認してください:
- Nuclioの[CLI (nuctl)](https://nuclio.io/docs/latest/reference/nuctl/nuctl/) がインストールされていること。
  CLIのインストールは[こちらから](https://github.com/nuclio/nuclio/releases)インストールマシンに適切なバージョンをダウンロードしてください。

1. `values.override.yaml` に `nuclio.enabled: true` を設定
1. `helm-chart` ディレクトリで `helm dependency update` を実行
1. Nuclio関数はイメージをレジストリにプッシュ・プルする必要があるため、
   好きなレジストリからpullできるように以下の設定で認証情報を記載してください。
   オプション:
   - `values.override.yaml` ファイル:
     ```yaml
     registry:
       loginUrl: someurl
       credentials:
         username: someuser
         password: somepass
     ```
   - または[ガイド](https://nuclio.io/docs/latest/setup/k8s/running-in-production-k8s/#the-preferred-deployment-method)に従いシークレットを作成し、
     `registry.secretName=your-registry-credentials-secret-name` を `values.override.yaml` に指定してください。

   - Minikubeの場合は、minikubeのアドオンでローカルの非認証レジストリを有効化できます:
     ```shell
     minikube addons enable registry
     minikube addons enable registry-aliases
     ```
     新たに作成した非認証レジストリにDockerイメージをプッシュするには、
     そのアドレス（`$(minikube ip):5000`）をDockerの非認証レジストリリストに追加する必要があります。
     [Docker公式ドキュメント](https://docs.docker.com/registry/insecure/#deploy-a-plain-http-registry)を参照してください。

   また、デプロイ前にインストールマシンでdocker login等でレジストリアカウントへのログインが必要な場合があります。

1. cvatプロジェクトを作成:
   ```shell
   nuctl --namespace <your cvat namespace> create project cvat
   ```
1. 最後に関数をデプロイします。例:
   - minikubeレジストリを使う場合:
     ```shell
     nuctl deploy --project-name cvat --path serverless/tensorflow/faster_rcnn_inception_v2_coco/nuclio --registry $(minikube ip):5000 --run-registry registry.minikube
     ```
   - Docker hubを使う場合:
     ```shell
     nuctl deploy --project-name cvat --path serverless/tensorflow/faster_rcnn_inception_v2_coco/nuclio --registry docker.io/your_username
     ```

### アナリティクス
Analyticsはデフォルトで有効です。無効にするには `values.override.yaml` に `analytics.enabled: false` を設定してください。

## デプロイ
正しいkubernetesコンテキストを使っているか確認してください。`kubectl config current-context`で確認できます。

> **警告:** Open Policy Agentのk8sサービス名はデフォルトでopaに固定されています。
> これはCVAT 2.0との互換性のためですが、このhelmチャートは1つのnamespaceにつき1リリースに制限されます。
> OPAのURLは現状環境変数で設定できません。
> 設定可能になり次第、cvat.opa.composeCompatibleServiceNameを
> value.override.yamlでfalseにして、opaのURLを追加envで設定してください。

以下のコマンドをリポジトリのルートディレクトリから実行
### オーバーライドあり:
```helm upgrade -n <desired_namespace> <release_name> -i --create-namespace ./helm-chart -f ./helm-chart/values.yaml  -f ./helm-chart/values.override.yaml```

### オーバーライドなし:
```helm upgrade -n <desired_namespace> <release_name> -i --create-namespace ./helm-chart -f ./helm-chart/values.yaml```

## デプロイ後の設定

1. [スーパーユーザー](#how-to-create-superuser)を作成

### スーパーユーザーの作成方法
```sh
HELM_RELEASE_NAMESPACE="<desired_namespace>" &&\
HELM_RELEASE_NAME="<release_name>" &&\
BACKEND_POD_NAME=$(kubectl get pod --namespace $HELM_RELEASE_NAMESPACE -l tier=backend,app.kubernetes.io/instance=$HELM_RELEASE_NAME,component=server -o jsonpath='{.items[0].metadata.name}') &&\
kubectl exec -it --namespace $HELM_RELEASE_NAMESPACE $BACKEND_POD_NAME -c cvat-backend -- python manage.py createsuperuser
```
## FAQ

### Kubernetesとは？どのように動作する？
<https://kubernetes.io/> を参照してください。
### Helmとは？どのように動作する？
<https://helm.sh/> を参照してください。
### Minikubeのセットアップ方法
1. 公式Minikubeインストール[ガイド](https://minikube.sigs.k8s.io/docs/start/)に従ってください。
1. ```shell
   minikube start --addons registry,registry-aliases
   ```
### 'helm upgrade'でどんな差分が発生するか知りたい
<https://github.com/databus23/helm-diff#install> を利用できます。
### 自身のpostgresqlをチャートで使いたい
オーバーライドファイルで `postgresql.enabled` を `false` に設定し、データベースインスタンスのパラメータを `external` フィールドに記載してください。
また、接続用の `username`、`database`、`password` フィールドも設定してください。
```yml
postgresql:
  enabled: false
  external:
    host: postgresql.default.svc.cluster.local
    port: 5432
  auth:
    username: cvat
    database: cvat
  secret:
    password: cvat_postgresql
```
上記例では該当シークレットが自動作成されますが、既存のシークレットを使いたい場合は `secret.create` を `false` にし、既存シークレットの `name` を指定してください:
```yml
postgresql:
  enabled: false
  external:
    host: postgresql.default.svc.cluster.local
    port: 5432
  secret:
    create: false
    name: "my-postgresql-secret"
```
シークレットには `database`、`username`、`password` キーを含めてください。例:
```yml
apiVersion: v1
kind: Secret
metadata:
  name: "my-postgresql-secret"
  namespace: default
type: generic
stringData:
  database: cvat
  username: cvat
  password: secretpassword
```

### 自身のredisをチャートで使いたい
オーバーライドファイルで `redis.enabled` を `false` に設定し、Redisインスタンスのパラメータを `external` フィールドに記載してください。
また、接続用の `password` フィールドも設定してください:
```yml
redis:
  enabled: false
  external:
    host: redis.hostname.local
  secret:
    password: cvat_redis
```
上記例では該当シークレットが自動作成されますが、既存のシークレットを使いたい場合は
`secret.create` を `false` にし、既存シークレットの `name` を指定してください:
```yml
redis:
  enabled: false
  external:
    host: redis.hostname.local
  secret:
    create: false
    name: "my-redis-secret"
```
シークレットには `redis-password` キーを含めてください。例:
```yml
apiVersion: v1
kind: Secret
metadata:
  name: "my-redis-secret"
  namespace: default
type: generic
stringData:
  redis-password: secretpassword
```

### values.yamlの設定を一部上書きしたい
`values.override.yaml` ファイルを作成し、`values.yaml` と同じ構造で設定変更を記載してください。
helm update/installコマンドで `-f` フラグで指定してください。
### なぜredisやpostgresに外部チャートを利用した？
彼らの方がより専門的な知見を持っており、品質が高く、サポート負担も減るためです。
### k8sデプロイでカスタムドメイン名を使う方法
デフォルト値の `cvat.local` は、`--set ingress.hosts[0].host` オプションで上書きできます。例:
```shell
helm upgrade -n default cvat -i --create-namespace helm-chart -f helm-chart/values.yaml -f helm-chart/values.override.yaml --set ingress.hosts[0].host=YOUR_FQDN
```
### `helm upgrade`失敗時（label field is immutable）エラーの対処方法
このようなエラーが出た場合:
```shell
Error: UPGRADE FAILED:cannot patch "cvat-backend-server" with kind Deployment: Deployment.apps "cvat-backend-server" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app":"cvat-app", "app.kubernetes.io/instance":"cvat", "app.kubernetes.io/managed-by":"Helm", "app.kubernetes.io/name":"cvat", "app.kubernetes.io/version":"latest", "component":"server", "helm.sh/chart":"cvat", "tier":"backend"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable
```
CVATのDeploymentをアップグレード前に削除してください。
```shell
kubectl delete deployments --namespace=foo -l app=cvat-app
```
### デフォルトストレージではなく既存のPersistentVolumeでCVATデータを保存する方法
`my-claim-name` というPersistentVolumeClaimと、それをバッキングするPersistentVolumeを作成済みであることを前提とします。
クレームはPodと同じnamespaceに存在する必要があります。
詳細は[こちら](https://kubernetes.io/docs/concepts/storage/persistent-volumes)。
`values.override.yaml`に以下を追加:
```yaml
cvat:
  backend:
    permissionFix:
      enabled: false
    defaultStorage:
      enabled: false
    server:
      additionalVolumes:
        - name: cvat-backend-data
          persistentVolumeClaim:
            claimName: my-claim-name
    worker:
      export:
        additionalVolumes:
          - name: cvat-backend-data
            persistentVolumeClaim:
              claimName: my-claim-name
      import:
        additionalVolumes:
          - name: cvat-backend-data
            persistentVolumeClaim:
              claimName: my-claim-name
      annotation:
        additionalVolumes:
          - name: cvat-backend-data
            persistentVolumeClaim:
              claimName: my-claim-name
    utils:
      additionalVolumes:
        - name: cvat-backend-data
          persistentVolumeClaim:
            claimName: my-claim-name

```