---
title: 'クラウドストレージのマウント'
linkTitle: 'クラウドストレージのマウント'
weight: 30
description: 'AWS S3バケット、Microsoft Azureコンテナ、またはGoogle Driveをファイルシステムとしてマウントする手順。'
---

<!--lint disable heading-style-->

## AWS S3バケットをファイルシステムとしてマウント

### <a name="aws_s3_ubuntu_2004">Ubuntu 20.04</a>

#### <a name="aws_s3_mount">マウント方法</a>

1. s3fsをインストール:

   ```bash
   sudo apt install s3fs
   ```

1. 認証情報を`${HOME}/.passwd-s3fs`というファイルに入力し、所有者のみに権限を設定:

   ```bash
   echo ACCESS_KEY_ID:SECRET_ACCESS_KEY > ${HOME}/.passwd-s3fs
   chmod 600 ${HOME}/.passwd-s3fs
   ```

1. `/etc/fuse.conf`ファイルの`user_allow_other`のコメントアウトを外す: `sudo nano /etc/fuse.conf`
1. s3fsを実行し、`bucket_name`と`mount_point`を置き換える:

   ```bash
   s3fs <bucket_name> <mount_point> -o allow_other -o passwd_file=${HOME}/.passwd-s3fs
   ```

詳細は[こちら](https://github.com/s3fs-fuse/s3fs-fuse)を参照してください。

#### <a name="aws_s3_automatically_mount">自動マウント</a>

上記のマウント手順の最初の3ステップに従ってください。

##### <a name="aws_s3_using_fstab">fstabを使用する場合</a>

1. aws_s3_fuseという名前のbashスクリプトを作成します（例：/usr/binにrootで作成）。内容は以下の通り
   （`user_name`：ディスクをマウントするユーザー、`backet_name`、`mount_point`、`/path/to/.passwd-s3fs`を置き換えてください）:

   ```bash
   #!/bin/bash
   sudo -u <user_name> s3fs <backet_name> <mount_point> -o passwd_file=/path/to/.passwd-s3fs -o allow_other
   exit 0
   ```

1. 実行権限を与える:

   ```bash
   sudo chmod +x /usr/bin/aws_s3_fuse
   ```

1. `/etc/fstab`を編集し、以下のような行を追加します（`mount_point`は適宜変更）:

   ```bash
   /absolute/path/to/aws_s3_fuse  <mount_point>     fuse    allow_other,user,_netdev     0       0
   ```

##### <a name="aws_s3_using_systemd">systemdを使用する場合</a>

1. ユニットファイルを作成: `sudo nano /etc/systemd/system/s3fs.service`
   （`user_name`、`bucket_name`、`mount_point`、`/path/to/.passwd-s3fs`を置き換えてください）:

   ```bash
   [Unit]
   Description=FUSE filesystem over AWS S3 bucket
   After=network.target

   [Service]
   Environment="MOUNT_POINT=<mount_point>"
   User=<user_name>
   Group=<user_name>
   ExecStart=s3fs <bucket_name> ${MOUNT_POINT} -o passwd_file=/path/to/.passwd-s3fs -o allow_other
   ExecStop=fusermount -u ${MOUNT_POINT}
   Restart=always
   Type=forking

   [Install]
   WantedBy=multi-user.target
   ```

1. システム構成を更新し、システム起動時に自動起動を有効化、バケットをマウント:

   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable s3fs.service
   sudo systemctl start s3fs.service
   ```

#### <a name="aws_s3_check">確認方法</a>

`/etc/mtab`ファイルには現在マウントされているファイルシステムの記録が含まれます。

```bash
cat /etc/mtab | grep 's3fs'
```

#### <a name="aws_s3_unmount_filesystem">ファイルシステムのアンマウント</a>

```bash
fusermount -u <mount_point>
```

バケットのマウントに[systemd](#aws_s3_using_systemd)を使った場合:

```bash
sudo systemctl stop s3fs.service
sudo systemctl disable s3fs.service
```

## Microsoft Azureコンテナをファイルシステムとしてマウント

### <a name="azure_ubuntu_2004">Ubuntu 20.04</a>

#### <a name="azure_mount">マウント方法</a>

1. Microsoftパッケージリポジトリを設定します。（詳細は[こちら](https://docs.microsoft.com/en-us/windows-server/administration/Linux-Package-Repository-for-Microsoft-Software#configuring-the-repositories)）

   ```bash
   wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb
   sudo dpkg -i packages-microsoft-prod.deb
   sudo apt-get update
   ```

1. `blobfuse`と`fuse`をインストール:

   ```bash
   sudo apt-get install blobfuse fuse
   ```

   詳細は[こちら](https://github.com/Azure/azure-storage-fuse/wiki/1.-Installation)を参照してください。

1. 環境変数の設定（`account_name`、`account_key`、`mount_point`を置き換え）:

   ```bash
   export AZURE_STORAGE_ACCOUNT=<account_name>
   export AZURE_STORAGE_ACCESS_KEY=<account_key>
   MOUNT_POINT=<mount_point>
   ```

1. キャッシュ用のフォルダを作成:

   ```bash
   sudo mkdir -p /mnt/blobfusetmp
   ```

1. ファイルの所有者がマウントするユーザーであることを確認:

   ```bash
   sudo chown <user> /mnt/blobfusetmp
   ```

1. マウントポイントを作成（存在しない場合）:

   ```bash
   mkdir -p ${MOUNT_POINT}
   ```

1. `/etc/fuse.conf`ファイルの`user_allow_other`のコメントアウトを外す: `sudo nano /etc/fuse.conf`
1. コンテナをマウント（`your_container`を置き換え）:

   ```bash
   blobfuse ${MOUNT_POINT} --container-name=<your_container> --tmp-path=/mnt/blobfusetmp -o allow_other
   ```

#### <a name="azure_automatically_mount">自動マウント</a>

上記のマウント手順の最初の7ステップに従ってください。

##### <a name="azure_using_fstab">fstabを使用する場合</a>

1. `connection.cfg`という設定ファイルを作成し、アカウント情報を入力。
   accountNameを変更し、accountKeyまたはsasTokenのいずれか一方を選択して自分の値に置き換えてください:

   ```bash
   accountName <account-name-here>
   # Please provide either an account key or a SAS token, and delete the other line.
   accountKey <account-key-here-delete-next-line>
   #change authType to specify only 1
   sasToken <shared-access-token-here-delete-previous-line>
   authType <MSI/SAS/SPN/Key/empty>
   containerName <insert-container-name-here>
   ```

1. `azure_fuse`というbashスクリプトを作成（例：/usr/binにrootで作成）。内容は以下
   （`user_name`：ディスクをマウントするユーザー、`mount_point`、`/path/to/blobfusetmp`、`/path/to/connection.cfg`を置き換え）:

   ```bash
   #!/bin/bash
   sudo -u <user_name> blobfuse <mount_point> --tmp-path=/path/to/blobfusetmp  --config-file=/path/to/connection.cfg -o allow_other
   exit 0
   ```

1. 実行権限を与える:

   ```bash
   sudo chmod +x /usr/bin/azure_fuse
   ```

1. `/etc/fstab`を編集し、blobfuseスクリプトの行を追加（パスを適宜置き換え）:

   ```bash
   /absolute/path/to/azure_fuse </path/to/desired/mountpoint> fuse allow_other,user,_netdev
   ```

##### <a name="azure_using_systemd">systemdを使用する場合</a>

1. ユニットファイルを作成: `sudo nano /etc/systemd/system/blobfuse.service`
   （`user_name`、`mount_point`、`container_name`、`/path/to/connection.cfg`を置き換え）:

   ```bash
   [Unit]
   Description=FUSE filesystem over Azure container
   After=network.target

   [Service]
   Environment="MOUNT_POINT=<mount_point>"
   User=<user_name>
   Group=<user_name>
   ExecStart=blobfuse ${MOUNT_POINT} --container-name=<container_name> --tmp-path=/mnt/blobfusetmp --config-file=/path/to/connection.cfg -o allow_other
   ExecStop=fusermount -u ${MOUNT_POINT}
   Restart=always
   Type=forking

   [Install]
   WantedBy=multi-user.target
   ```

1. システム設定を更新し、ユニットの自動起動を有効化、コンテナをマウント:

   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable blobfuse.service
   sudo systemctl start blobfuse.service
   ```

   詳細は[こちら](https://github.com/Azure/azure-storage-fuse/tree/master/systemd)を参照してください。

#### <a name="azure_check">確認方法</a>

`/etc/mtab`ファイルには現在マウントされているファイルシステムの記録が含まれます。

```bash
cat /etc/mtab | grep 'blobfuse'
```

#### <a name="azure_unmount_filesystem">ファイルシステムのアンマウント</a>

```bash
fusermount -u <mount_point>
```

コンテナのマウントに[systemd](#azure_using_systemd)を使った場合:

```bash
sudo systemctl stop blobfuse.service
sudo systemctl disable blobfuse.service
```

マウントに問題がある場合は、[よくある質問とその回答](https://github.com/Azure/azure-storage-fuse/wiki/3.-Troubleshoot-FAQ)もご覧ください。

## Google Driveをファイルシステムとしてマウント

### <a name="google_drive_ubuntu_2004">Ubuntu 20.04</a>

#### <a name="google_drive_mount">マウント方法</a>

ユーザースペースでGoogle Driveをファイルシステムとしてマウントするには（FUSE）、
[google-drive-ocamlfuse](https://github.com/astrada/google-drive-ocamlfuse)を使用できます。
以下の手順に従ってください。

1. google-drive-ocamlfuseをインストール:

   ```bash
   sudo add-apt-repository ppa:alessandro-strada/ppa
   sudo apt-get update
   sudo apt-get install google-drive-ocamlfuse
   ```

1. パラメータなしで`google-drive-ocamlfuse`を実行:

   ```bash
   google-drive-ocamlfuse
   ```

   このコマンドはデフォルトのアプリケーションディレクトリ（~/.gdfuse/default）を作成し、
   設定ファイルconfigを含みます（設定の詳細は[wiki](https://github.com/astrada/google-drive-ocamlfuse/wiki)ページを参照）。
   また、Google Driveへのアクセス許可を取得するためにウェブブラウザが起動されます。
   これによりファイルシステムをマウントする前にデフォルト設定を変更できます。

   その後、Google Driveをマウントするローカルディレクトリを選択してください（例: ~/GoogleDrive）。

1. マウントポイントを作成（存在しない場合、`mount_point`を置き換え）:

   ```bash
   mountpoint="<mount_point>"
   mkdir -p $mountpoint
   ```

1. `/etc/fuse.conf`ファイルの`user_allow_other`のコメントアウトを外す: `sudo nano /etc/fuse.conf`
1. ファイルシステムをマウント:

   ```bash
   google-drive-ocamlfuse -o allow_other $mountpoint
   ```

#### <a name="google_drive_automatically_mount">自動マウント</a>

上記のマウント手順の最初の4ステップに従ってください。

##### <a name="google_drive_using_fstab">fstabを使用する場合</a>

1. gdfuseという名前のbashスクリプトを作成します（例：/usr/binにrootで作成）。内容は以下の通り
   （`user_name`：ディスクをマウントするユーザー、`label`、`mount_point`を置き換え）:

   ```bash
   #!/bin/bash
   sudo -u <user_name> google-drive-ocamlfuse -o allow_other -label <label> <mount_point>
   exit 0
   ```

1. 実行権限を与える:

   ```bash
   sudo chmod +x /usr/bin/gdfuse
   ```

1. `/etc/fstab`を編集し、以下のような行を追加します（`mount_point`は適宜変更）:

   ```bash
   /absolute/path/to/gdfuse  <mount_point>     fuse    allow_other,user,_netdev     0       0
   ```

   詳細は[こちら](https://github.com/astrada/google-drive-ocamlfuse/wiki/Automounting)も参照してください。

##### <a name="google_drive_using_systemd">systemdを使用する場合</a>

1. ユニットファイルを作成: `sudo nano /etc/systemd/system/google-drive-ocamlfuse.service`
   （`user_name`、`label`（デフォルトは`label=default`）、`mount_point`を置き換え）:

   ```bash
   [Unit]
   Description=FUSE filesystem over Google Drive
   After=network.target

   [Service]
   Environment="MOUNT_POINT=<mount_point>"
   User=<user_name>
   Group=<user_name>
   ExecStart=google-drive-ocamlfuse -label <label> ${MOUNT_POINT}
   ExecStop=fusermount -u ${MOUNT_POINT}
   Restart=always
   Type=forking

   [Install]
   WantedBy=multi-user.target
   ```

1. システム構成を更新し、ユニットの自動起動を有効化、ドライブをマウント:

   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable google-drive-ocamlfuse.service
   sudo systemctl start google-drive-ocamlfuse.service
   ```

   詳細は[こちら](https://github.com/astrada/google-drive-ocamlfuse/wiki/Automounting)を参照してください。

#### <a name="google_drive_check">確認方法</a>

`/etc/mtab`ファイルには現在マウントされているファイルシステムの記録が含まれます。

```bash
cat /etc/mtab | grep 'google-drive-ocamlfuse'
```

#### <a name="google_drive_unmount_filesystem">ファイルシステムのアンマウント</a>

```bash
fusermount -u <mount_point>
```

ドライブのマウントに[systemd](#google_drive_using_systemd)を使った場合:

```bash
sudo systemctl stop google-drive-ocamlfuse.service
sudo systemctl disable google-drive-ocamlfuse.service
```
