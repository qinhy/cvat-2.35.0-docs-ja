---
title: 'CVAT ユーザーロール'
linkTitle: 'CVAT ユーザーロール'
weight: 4
---

CVAT には、2つの異なる種類のロールがあります。

- **グローバルロール**: これはシステム全体に適用される共通のロールです。CVAT.ai プラットフォームにログインしたすべてのユーザーに自動的に割り当てられます。CVAT.ai 全体で、登録ユーザーすべてが持つ基本的な権限を設定します。個々のタスクや役割に関係なく適用されます。
- **組織ロール**: これは組織内でユーザーができることを決定し、ユーザーの職務や責任に基づいた、より細やかなアクセス制御を可能にします。

組織ロールはグローバルロールを補完し、タスクやジョブなど、さまざまなリソースの可視性を決定します。

**制限**: 制限は、[**フリープラン**](https://www.cvat.ai/pricing/cloud) を利用するCVAT.aiクラウドプラットフォームのすべてのユーザーに適用され、  
{{< ilink "/docs/enterprise/subscription-management" "**サブスクリプションの選択**" >}} により解除できます。

すべてのロールはあらかじめ定義されており、ユーザーインターフェースから変更することはできません。  
ただし、_セルフホスト型ソリューション_ では、`cvat/apps/*/rules/` に保存された `.rego` ファイルを使ってロールを調整できます。  
Rego は OPA（Open Policy Agent）ポリシーを定義するために使われる宣言型言語で、その構文は [**OPAドキュメント**](https://www.openpolicyagent.org/docs/latest/policy-language/) で詳しく説明されています。

> 注意: `.rego` ファイルを変更した後は、Docker Compose を再構築・再起動して変更を適用する必要があります。  
> この場合、Docker Compose コマンドを実行する際に `docker-compose.dev.yml` 構成ファイルを含めることを忘れないでください。

参照：

- [CVAT.ai のグローバルロール](#global-roles-in-cvatai)
- [CVAT.ai の組織ロール](#organization-roles-in-cvatai)
- [ジョブステージ](#job-stage)

## CVAT.ai のグローバルロール

> **注意:** グローバルロールはセルフホスト型ソリューションでのみ調整可能です。

CVAT には、ユーザーグループとして分類される3つのグローバルロールがあります。各ロールは以下の通りです。

<!--lint disable maximum-line-length-->

| ロール                        | 説明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **管理者**                    | 管理者はCVATインスタンスおよびそのインスタンス内のすべての活動に対する無制限のアクセス権を持ちます。管理者はすべてのタスクやプロジェクトを表示・管理・変更することができます。このロールはセルフホスト型インスタンス専用であり、包括的な監督と制御を保証します。                                                                                                                                                                                                            |
| **ユーザー <br>（デフォルト）** | ユーザーは、CVATに登録されたすべてのユーザーに自動的に割り当てられるデフォルトのロールです。ユーザーは自身のアカウント内のすべてのタスクやプロジェクトを表示・管理できますが、その活動には特定の制限があります（フリープランを参照）。<br><br>* CVATアカウントを持たないユーザーが、組織オーナーまたはメンテナーによって組織に招待された場合、自動的に組織ロールが割り当てられ、組織内での操作時にはそのロールの制限が適用されます。                       |
| **ワーカー**                  | ワーカーは特定の機能に限定されており、タスクの作成やロールの割り当て、その他の管理操作を行う権限はありません。主に割り当てられたロールの範囲内（ジョブのバリデーションやアノテーション）でコンテンツの閲覧や操作を行います。                                                                                                                                                                                                                                   |

<!--lint enable maximum-line-length-->

## CVAT.ai の組織ロール

組織ロールは、
{{< ilink "/docs/manual/advanced/organization" "**CVAT組織**" >}} 内でのみ利用できます。

![組織ロール](/images/user-roles.png)

組織ロールは、ユーザーが組織に招待された際に割り当てられます。

![組織ロール](/images/org-roles.png)

CVATで利用可能なロールは以下の通りです。

<!--lint disable maximum-line-length-->

| ロール         | 説明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **オーナー**   | オーナーは組織を作成した人物です。このロールは組織の作成者にデフォルトで割り当てられ、最大限の権限を持ち、他のユーザーに変更または再割り当てすることはできません。<br><br>オーナーには組織内で追加の制限はなく、選択した組織プラン（[フリーおよびチーム](https://www.cvat.ai/pricing/cloud)プラン参照）によってのみ制限されます。<br><br>オーナーは他のユーザーを組織に招待し、ロールを割り当ててチームでコラボレーションできます。         |
| **メンテナー** | メンテナーは組織にユーザーを招待し、タスクやジョブの作成・更新、組織内のすべてのタスクの閲覧ができます。メンテナーはクラウドストレージへの完全なアクセス権を持ち、メンバーやそのロールの変更も可能です。                                                                                                                                                                                                                                                                     |
| **スーパーバイザー** | スーパーバイザーは管理職のロールです。スーパーバイザーはジョブ、タスク、プロジェクトを作成し、組織メンバーに割り当てることができます。ただし、新しいメンバーの招待やロールの変更はできません。                                                                                                                                                                                                                                                               |
| **ワーカー**    | ワーカーの主な役割はアノテーション作業およびレビューです。特定の機能に限定されており、割り当てられたジョブのみアクセスできます。                                                                                                                                                                                                                                                                                                                                |

<!--lint enable maximum-line-length-->

## ジョブステージ

ジョブの**ステージ**は、どのチームメンバーにも割り当てることができます。

**ステージ**はロールではありません。

ジョブには、どのロールのユーザーでも**アサイン**でき、その**アサインされたユーザー**が、  
「アノテート」「バリデート」「承認」など、ステージ固有の作業を行います。

![ジョブステージ](/images/job-stage.png)

ジョブの**ステージ**には以下のものがあります。

<!--lint disable maximum-line-length-->

| ステージ          | 説明                                                                                                                                                                                                              |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **アノテーション** | アノテーションツールへのアクセスを提供します。アサインされたユーザーは自分のジョブを表示し、アノテートできます。デフォルトでは、「アノテーション」ステージのユーザーはアノテーションのエラーや問題を報告できません。       |
| **バリデーション** | QAツールへのアクセスを提供します。アサインされたユーザーは自分のジョブを表示し、バリデーションおよび問題報告が可能です。デフォルトでは、「バリデーション」ステージのユーザーはエラー修正やデータセットのアノテートができません。 |
| **承認**           | 追加のアクセス権やアノテーターのインターフェース変更はありません。ただ単にジョブを完了済みとしてマークします。                                                                                                     |

<!--lint enable maximum-line-length-->

**アサインされたユーザー**は、アノテーションインターフェースのツールバーから、割り当てられた**ステージ**固有の機能を切り替えることができます。

![ジョブステージの変更](/images/change-stage.png)

- **標準**: インターフェースを**アノテーション**モードに切り替えます。
- **レビュー**: インターフェースを**バリデーション**モードに切り替えます。