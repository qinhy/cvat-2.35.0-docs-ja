---
title: '用語集'
linkTitle: '用語集'
weight: 21
description: 'CVATのアノテーションに関する用語一覧。'
---
## ラベル
ラベルはアノテーション対象のオブジェクトの種類です（例：人、自動車、車両など）。

![](/images/image032_detrac.jpg)

---

## 属性
属性はアノテーション対象オブジェクトの特性です（例：色、モデル、品質など）。属性には2種類あります。

### 固有
固有属性は不変であり、フレームごとに変更できません（例：年齢、性別、色など）。

  ![](/images/image073.jpg)

### 一時的
一時的属性は可変であり、任意のフレームで変更できます（例：品質、ポーズ、切り取られた状態など）。

  ![](/images/image072.jpg)

---

## トラック
トラックは、1つのオブジェクトに対応する異なるフレーム上のシェイプの集合です。
トラックは「トラックモード」で作成されます。

![](/images/gif003_detrac.gif)

---

## アノテーション
アノテーションはシェイプとトラックの集合です。アノテーションにはいくつかの種類があります。

- _手動_：人によって作成されるもの
- _半自動_：主に自動で作成されるが、ユーザーが一部データ（例：補間）を提供するもの
- _自動_：人の介在なしに自動で作成されるもの

---

## 近似
近似はポリゴンの頂点数を減らすことができます。
アノテーションファイルの軽量化や、ポリゴン編集の容易化に利用できます。

![](/images/approximation_accuracy.gif)

---

## トラッカブル
トラッカブルオブジェクトは、前のフレームがそのオブジェクトの最新キー フレームであれば自動で追跡されます。詳細は
{{< ilink "/docs/manual/advanced/ai-tools#trackers" "トラッカー" >}}のセクションを参照してください。

![](/images/tracker_indication_detrac.jpg)

---

## モード

### 補間
動画アノテーション用のモードで、[`トラック`](#track)オブジェクトを利用します。
キー フレーム上のオブジェクトのみ手動でアノテーションし、中間フレームは線形補間されます。

関連セクション：
- {{< ilink "/docs/manual/basics/track-mode-basics" "トラックモード" >}}

### アノテーション
画像アノテーション用のモードで、`シェイプ`オブジェクトを利用します。

関連セクション：
- {{< ilink "/docs/manual/basics/shape-mode-basics" "シェイプモード" >}}

---

## 次元

タスクデータの種類によって異なります。これは
{{< ilink "/docs/manual/basics/create_an_annotation_task" "タスク作成時" >}}に定義されます。

### 2D

2Dタスクのデータ形式は画像と動画です。
関連セクション：
- {{< ilink "/docs/manual/basics/create_an_annotation_task" "アノテーションタスクの作成" >}}

### 3D

3Dタスクのデータ形式はポイントクラウドです。
{{< ilink "/docs/manual/basics/create_an_annotation_task#data-formats-for-a-3d-task" "3Dタスクのデータ形式" >}}

関連セクション：
- {{< ilink "/docs/manual/basics/3d-task-workspace" "3Dタスクワークスペース" >}}
- {{< ilink "/docs/manual/basics/standard-3d-mode-basics" "標準3Dモード" >}}
- {{< ilink "/docs/manual/basics/3d-object-annotation" "3Dオブジェクトアノテーション" >}}

---

## ステート
ジョブの状態。状態は割り当てられたユーザーが
{{< ilink "/docs/manual/basics/CVAT-annotation-Interface/navbar.md#top-panel" "ジョブ内のメニュー" >}}で変更できます。
状態は `新規`, `作業中`, `却下`, `完了` のいずれかです。

---

## ステージ
ジョブの段階。タスクページの
{{< ilink "/docs/manual/basics/tasks-page" "ドロップダウンリスト" >}}で指定します。
段階は `アノテーション`, `検証`, `受け入れ` の3つがあり、この値がタスクの進捗バーに反映されます。

---

## サブセット
プロジェクトにはサブセットを設定できます。サブセットはタスクをグループ化して、データセットの扱いを容易にします。
`テスト`, `トレイン`, `バリデーション` またはカスタムサブセットが指定可能です。

---

## 資格情報
`資格情報`とは `キー＆シークレットキー`, `アカウント名とトークン`, `匿名アクセス`, `キーファイル` を指します。
{{< ilink "/docs/manual/basics/attach-cloud-storage#attach-new-cloud-storage" "クラウドストレージの接続" >}}に利用されます。

---

## リソース

`リソース`とは `バケット名` または `コンテナ名` を指します。
{{< ilink "/docs/manual/basics/attach-cloud-storage#attach-new-cloud-storage" "クラウドストレージの接続" >}}に利用されます。