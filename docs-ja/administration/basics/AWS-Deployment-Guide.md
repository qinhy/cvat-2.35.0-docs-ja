---
title: 'AWS-デプロイメントガイド'
linkTitle: 'AWS-デプロイメントガイド'
weight: 4
description: 'Nvidia GPUおよびその他のAWSマシン上でCVATをデプロイするための手順。'
---

CVATをデプロイする方法は2つあります。

1. **Nvidia GPUマシン上でのデプロイ：** Tensorflowアノテーション機能はGPUハードウェアに依存しています。
   tf-annotationアプリとともにCVATを起動する簡単な方法の1つは、NVIDIA GPUを提供するAWS P3インスタンスを使用することです。
   [P3インスタンスについて詳しくはこちら。](https://aws.amazon.com/about-aws/whats-new/2017/10/introducing-amazon-ec2-p3-instances/)
   全体のセットアップ手順は[メインのREADMEファイル](https://github.com/cvat-ai/cvat/)で説明されていますが、
   Nvidiaドライバーのインストールは含まれていません。
   そのため、ドライバーをダウンロードしてインストールする必要があります。
   Amazon P3インスタンスの場合、NvidiaのウェブサイトからNvidiaドライバーをダウンロードしてください。
   詳細は[LinuxインスタンスへのNVIDIAドライバーのインストール](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-nvidia-driver.html)
   のリンクを参照してください。

2. **その他のAWSマシン上でのデプロイ：** 
   {{< ilink "/docs/administration/basics/installation" "インストール手順" >}}で説明されているガイドと同じ手順を実行できます。
   追加のステップとして、[セキュリティグループとルールを追加して外部からの接続を許可](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html)する必要があります。

いずれの場合も、`CVAT_HOST`環境変数を公開されているAWSのパブリックIPアドレスまたはホスト名に設定することを忘れないでください：

```bash
export CVAT_HOST=your-instance.amazonaws.com
```

ホスト名の使用で問題が発生した場合は、ホスト名の代わりにパブリックIPV4を使用することもできます。
AWSや他のクラウドベースのマシンでは、インスタンスを終了または停止する必要がある場合、
パブリックIPV4とホスト名は停止・再起動のたびに変更されます。
この問題に効率的に対処するには、停止できないスポットインスタンスの使用を避けてください。
スポットインスタンスではEBSをAMIにコピーして再起動しようとすると問題が発生します。
一方、通常のインスタンスを停止して再起動した場合は、
新しいホスト名/IPV4を使って`CVAT_HOST`環境変数を設定できます。