---
title: '品質管理'
linkTitle: '品質管理'
weight: 21
description: '品質管理機能の概要'
---

CVATには、アノテーションの自動品質管理のための以下の機能があります：
- [タスクのバリデーションセットの設定](#how-to-enable-quality-control)
- ジョブ終了時のジョブ検証（「{{< ilink "/docs/enterprise/immediate-feedback" "即時フィードバック" >}}」）
- [発見された問題のレビュー モード](#how-to-review-problems-found)
- [品質分析](#how-to-check-task-quality-metrics)

このセクションでは、品質評価における主要なステップのみを紹介します。
CVATでの品質評価の詳細ガイドについては、
{{< ilink "/docs/manual/advanced/analytics-and-monitoring/auto-qa" "上級セクション" >}} をご覧ください。

## 品質管理を有効にする方法

{{< tabpane text=true >}}

{{%tab header="新しいタスクの場合" %}}

1. タスク作成画面に移動する
2. ソースメディアを選択し、他のタスクパラメータを設定する
3. 下にスクロールして**品質管理**セクションを表示する
4. 利用可能な
{{< ilink "/docs/manual/advanced/analytics-and-monitoring/auto-qa#validation-modes" "バリデーションモード" >}}
のいずれかを選択する

  ![バリデーションモード付きタスク作成](/images/honeypot09.jpg)

5. タスクを作成する
6. タスク内のGround TruthジョブにGround Truthアノテーションをアップロードまたは作成する
7. Ground Truthジョブを`acceptance`ステージおよび`completed`状態に切り替える

  ![ジョブステータス設定](/images/honeypot10.jpg)

{{% /tab %}}

{{%tab header="既存のタスクの場合" %}}

> 既存のタスクではGround Truthバリデーションモードのみ利用可能です。  
> Honeypotを使用したい場合は、タスクを再作成する必要があります。

1. タスクページを開く
2. ジョブリスト横の`+`ボタンをクリックする

  ![ジョブ作成](/images/honeypot01.jpg)

3. ジョブタイプで**Ground truth**を選択し、ジョブパラメータを設定する

  ![ジョブパラメータ設定](/images/honeypot02.jpg)

4. タスク内のGround TruthジョブにGround Truthアノテーションをアップロードまたは作成する
5. Ground Truthジョブを`acceptance`ステージおよび`completed`状態に切り替える

  ![ジョブステータス設定](/images/honeypot10.jpg)

{{% /tab %}}

{{< /tabpane >}}

## 即時ジョブフィードバックを有効にする方法

> **注記**: この機能には、タスク内でバリデーションセットの設定が必要です。  
> 詳細は[品質管理を有効にする方法](#how-to-enable-quality-control)および
> {{< ilink "/docs/manual/advanced/analytics-and-monitoring/auto-qa#configuring-quality-estimation" "完全ガイド" >}}を参照してください。

1. タスクの**アクション**メニュー > **品質管理** > **設定**を開く
2. **ジョブごとの最大バリデーション回数**を0より大きい値に設定する（3が推奨値）

  ![ジョブバリデーション設定](/images/immediate-feedback-quality-settings.png)

3. 設定を保存する
4. アノテーションジョブにアノテーターを割り当てる
5. ジョブをアノテーションする
6. メニューの該当ボタンでジョブを完了にする
7. ジョブ完了後、ジョブバリデーションダイアログが表示される

  <img src="/images/immediate-feedback-accept.png" style="max-width: 500px;">

各担当者は、指定された回数を超えてバリデーションを受けることはありません。

この機能の詳細については
{{< ilink "/docs/enterprise/immediate-feedback" "即時フィードバック" >}} セクションをご覧ください。

## タスクの品質指標を確認する方法

1. タスクの**アクション**メニュー > **品質管理**を開く
2. （任意）品質指標の計算をリクエストし、完了を待つ
3. サマリーまたは詳細レポートを確認する

  ![品質分析ページ](/images/honeypot05.png)

この機能の詳細については
{{< ilink "/docs/manual/advanced/analytics-and-monitoring/auto-qa#quality-analytics" "こちら" >}}をご覧ください。

## 発見された問題をレビューする方法

1. タスクの**アクション**メニュー > **品質管理**を開く
2. レビュー対象のアノテーションジョブを探し、そのジョブに最低1つのバリデーションフレームがあることを確認する
3. ジョブリンクをクリックする
4. **レビュー**モードに切り替える
5. Ground Truthアノテーションとコンフリクトの表示を有効にする

  ![GTコンフリクト](/images/honeypot06.gif)

この機能の詳細については
{{< ilink "/docs/manual/advanced/analytics-and-monitoring/auto-qa#reviewing-gt-conflicts" "こちら" >}}をご覧ください。