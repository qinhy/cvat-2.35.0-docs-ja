---
title: '組織向けCVAT 完全ワークフローガイド'
linkTitle: '組織向けCVAT 完全ワークフローガイド'
weight: 2
---

CVAT.aiへようこそ。このページは、チームで
Computer Vision Annotation Tool（CVAT）を使ったアノテーションプロセスを始めるための出発点です。

このガイドは、貴組織がCVATを効果的に活用するために必要な知識と
ベストプラクティスを提供することを目的としています。

CVATの初期セットアップから高度な機能まで、
ワークフローのすべてのステップを順を追ってご案内します。

以下をご覧ください：

- [ワークフローダイアグラム](#workflow-diagram)
- [組織向けエンドツーエンドワークフロー](#end-to-end-workflow-for-organizations)
- [完全ワークフローガイド動画チュートリアル](#complete-workflow-guide-video-tutorial)

## ワークフローダイアグラム

ワークフローダイアグラムは、全体的なプロセスの概要を高いレベルで示しています。

[![ワークフローダイアグラム](/images/cvat-workflow-bpmn.png)](/images/cvat-workflow-bpmn.png)

## 組織向けエンドツーエンドワークフロー

組織内でCVATを使用するには、以下の手順に従ってください：

1. {{< ilink "/docs/manual/basics/registration" "CVATでアカウントを作成" >}}します。
2. {{< ilink "/docs/manual/advanced/organization" "**組織**を作成" >}}します。
3. 作成した**組織**に切り替え、
   {{< ilink "/docs/enterprise/subscription-management#team-plan" "**チームプラン**に加入" >}}します。
4. {{< ilink "/docs/manual/advanced/organization#invite-members-into-organization"
     "**組織へのメンバー招待**" >}}および
   招待したメンバーに{{< ilink "/docs/manual/advanced/iam_user_roles" "ユーザーロール" >}}を割り当てます。
5. {{< ilink "/docs/manual/advanced/projects" "**プロジェクト**を作成" >}}します。
6. （オプション）{{< ilink "/docs/manual/basics/attach-cloud-storage" "**クラウドストレージ**" >}}を**プロジェクト**に紐付けます。
7. {{< ilink "/docs/manual/basics/create_an_annotation_task" "**タスク**" >}}または [
   **マルチタスク**](/docs/manual/basics/create-multi-tasks/)を作成します。
   <br>このステップでCVATプラットフォームが自動的に
   ジョブを作成します。
8. （オプション）{{< ilink "/docs/manual/advanced/analytics-and-monitoring/auto-qa" "**グラウンドトゥルースジョブ**" >}}を作成します。
   <br>手動QAアプローチを採用している場合、このステップは省略できます。
9. （オプション）{{< ilink "/docs/manual/advanced/specification" "**アノテーター向け指示書**" >}}を追加します。
10. （オプション）{{< ilink "/docs/administration/advanced/webhooks" "**Webhook**" >}}を設定します。
11. アノテーター名を**担当者**に追加し、
    {{< ilink "/docs/manual/advanced/iam_user_roles#job-stage" "**ジョブステージ**" >}}を
    **アノテーション**に変更してジョブをアノテーターに割り当てます。
12. アノテーターは割り当てられたジョブを確認し、アノテーションを行います。
13. （オプション）もし
    {{< ilink "/docs/manual/advanced/analytics-and-monitoring/auto-qa" "**グラウンドトゥルースジョブ**" >}}
    を作成した場合は、CVATプラットフォームがデータを蓄積するまで少し待ち、
    アノテーションの精度を確認します。
14. 手動検証を行う場合は、
    バリデーター名を**担当者**に追加し、
    {{< ilink "/docs/manual/advanced/iam_user_roles#job-stage" "**ジョブステージ**" >}}
    を**バリデーション**に変更してジョブをバリデーターに割り当てます。
15. バリデーターは割り当てられたジョブを確認し、問題点を報告します。
    <br>バリデーターは問題点の修正も可能です。詳しくは
    {{< ilink "/docs/manual/advanced/analytics-and-monitoring/manual-qa" "**手動QAとレビュー**" >}}をご参照ください。
16. 問題点を確認し、追加の改善が必要な場合は、ジョブを
    バリデーターまたはアノテーターに再割り当てします。
17. （オプション）{{< ilink "/docs/manual/advanced/analytics-and-monitoring/analytics-in-cloud" "**アナリティクス**" >}}を確認します。
18. {{< ilink "/docs/manual/advanced/formats" "**データをエクスポート**" >}}します。

## 完全ワークフローガイド動画チュートリアル

<!--lint disable maximum-line-length-->

<iframe width="560" height="315" src="https://www.youtube.com/embed/uI2OEoR08ME?si=0OTHPwgxGx30Gax7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<!--lint enable maximum-line-length-->