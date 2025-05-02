---
title: 'モデル'
linkTitle: 'モデル'
weight: 13
---

モデルをデプロイするには、必要なコンポーネントを
{{< ilink "/docs/administration/advanced/installation_automatic_annotation"
  "半自動および自動アノテーションガイド" >}}
を参考にインストールしてください。
モデルのデプロイ方法については、
{{< ilink "/docs/manual/advanced/serverless-tutorial" "サーバーレスチュートリアル" >}}
をお読みください。

「モデル」ページには、半自動および自動アノテーション用にデプロイされたディープラーニング（DL）モデルの一覧が表示されます。
「モデル」ページを開くには、ナビゲーションバーの「モデル」ボタンをクリックしてください。
モデルのリストはテーブル形式で表示されます。各モデルについて示されているパラメーターは以下の通りです：

- モデルが基づいている `フレームワーク`
- モデルの `名前`
- モデルの `タイプ`:
  - `detector` - 自動アノテーション用
    （{{< ilink "/docs/manual/advanced/ai-tools#detectors" "detectors" >}}
    および {{< ilink "/docs/manual/advanced/automatic-annotation" "自動アノテーション" >}} で利用可能）
  - `interactor` - 半自動形状アノテーション用
    （{{< ilink "/docs/manual/advanced/ai-tools#interactors" "interactors" >}} で利用可能）
  - `tracker` - 半自動トラックアノテーション用
    （{{< ilink "/docs/manual/advanced/ai-tools#trackers" "trackers" >}} で利用可能）
  - `reid` - 個別オブジェクトをトラックにまとめるために使用
    （{{< ilink "/docs/manual/advanced/automatic-annotation" "自動アノテーション" >}} で利用可能）
- `説明` - モデルの簡単な説明
- `ラベル` - 対応しているラベルのリスト（`detectors` タイプのモデルのみ）

![](/images/image099.jpg)
