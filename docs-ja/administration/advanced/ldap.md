---

title: 'LDAP バックエンド認証'
linkTitle: 'LDAP ログイン'
weight: 40
description: 'ユーザーが中央の情報源の認証情報でログインできるようにする'

---

### `settings.py` の作成

LDAPログインを統合する際には、デフォルトのCVAT設定（[cvat/settings/production.py](https://github.com/cvat-ai/cvat/blob/develop/cvat/settings/production.py)）へのオーバーレイを作成する必要があります。このオーバーレイでDjangoをLDAPサーバーに接続するように設定します。

LDAPの利用における主な問題は、LDAPの実装ごとにパラメータが異なる点です。Active Directory バックエンド認証で使用するオプションは、FreeIPAを使用する場合とは異なります。

### `docker-compose.override.yml` の更新

オーバーライド設定で、設定ファイルをパススルーし、`DJANGO_SETTINGS_MODULE` 変数を設定してCVATにそれを使用させる必要があります。

```yml
services:
  cvat_server:
    environment:
      DJANGO_SETTINGS_MODULE: settings
    volumes:
      - ./settings.py:/home/django/settings.py:ro
```

### Active Directory の例

以下の例では、ユーザーがActive Directoryに対して自身を認証できるようになります。この例では、`cvat_bind` というダミーユーザーが必要です。バインドアカウントの設定には特別な権限は不要です。

`AUTH_LDAP_BIND_DN` の更新時、アカウント情報の書き方は2通りあります。どちらも下記の設定で説明しています。

この設定はWindows Server 2022で動作確認済みですが、古いバージョンやSambaのActive Directory実装でも機能するはずです。

```py
# production設定をオーバーレイします
from cvat.settings.production import *

# 以下カスタムコード
import ldap
from django_auth_ldap.config import LDAPSearch
from django_auth_ldap.config import NestedActiveDirectoryGroupType

# CVATにLDAP認証を使用していることを通知
IAM_TYPE = 'LDAP'

# LDAPサーバーとの通信
AUTH_LDAP_SERVER_URI = "ldap://ad.example.com" # IPアドレスも可
ldap.set_option(ldap.OPT_REFERRALS, 0)

_BASE_DN = "CN=Users,DC=ad,DC=example,DC=com"

# LDAPサーバーへの認証
AUTH_LDAP_BIND_DN = "CN=cvat_bind,%s" % _BASE_DN
# AUTH_LDAP_BIND_DN = "cvat_bind@ad.example.com"
AUTH_LDAP_BIND_PASSWORD = "SuperSecurePassword^21"

AUTH_LDAP_USER_SEARCH = LDAPSearch(
    _BASE_DN,
    ldap.SCOPE_SUBTREE,
    "(sAMAccountName=%(user)s)"
)

AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    _BASE_DN,
    ldap.SCOPE_SUBTREE,
    "(objectClass=group)"
)

# Djangoフィールド名とActive Directory属性のマッピング
AUTH_LDAP_USER_ATTR_MAP = {
    "user_name": "sAMAccountName",
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}

# グループ管理
AUTH_LDAP_GROUP_TYPE = NestedActiveDirectoryGroupType()

# Django LDAPバックエンドの登録
AUTHENTICATION_BACKENDS += ['django_auth_ldap.backend.LDAPBackend']

# Active DirectoryグループとDjango/CVATグループのマッピング
AUTH_LDAP_ADMIN_GROUPS = [
    'CN=CVAT Admins,%s' % _BASE_DN,
]
AUTH_LDAP_WORKER_GROUPS = [
    'CN=CVAT Workers,%s' % _BASE_DN,
]
AUTH_LDAP_USER_GROUPS = [
    'CN=CVAT Users,%s' % _BASE_DN,
]

DJANGO_AUTH_LDAP_GROUPS = {
    "admin": AUTH_LDAP_ADMIN_GROUPS,
    "user": AUTH_LDAP_USER_GROUPS,
    "worker": AUTH_LDAP_WORKER_GROUPS,
}
```

### FreeIPA の例

以下の例では、ユーザーがFreeIPAに対して自身を認証できるようになります。この例では、`cvat_bind` というダミーユーザーが必要です。バインドアカウントの設定には特別な権限は不要です。

`AUTH_LDAP_BIND_DN` の更新時、[Active Directory](#active-directory-example) とは異なり、ユーザー情報の書き方は一通りのみです。

この設定はAlmaLinux 8で動作確認済みですが、他のEnterprise Linux系のバージョンや派生でも動作する可能性があります。

```py
# production設定をオーバーレイします
from cvat.settings.production import *

# 以下カスタムコード
import ldap
from django_auth_ldap.config import LDAPSearch
from django_auth_ldap.config import GroupOfNamesType

# CVATにLDAP認証を使用していることを通知
IAM_TYPE = 'LDAP'

_BASE_DN = "CN=Accounts,DC=ipa,DC=example,DC=com"

# LDAPサーバーとの通信
AUTH_LDAP_SERVER_URI = "ldap://ipa.example.com" # IPアドレスも可
ldap.set_option(ldap.OPT_REFERRALS, 0)

# LDAPサーバーへの認証
AUTH_LDAP_BIND_DN = "UID=cvat_bind,CN=Users,%s" % _BASE_DN
AUTH_LDAP_BIND_PASSWORD = "SuperSecurePassword^21"

AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "CN=Users,%s" % _BASE_DN,
    ldap.SCOPE_SUBTREE,
    "(uid=%(user)s)"
)

AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    "CN=Groups,%s" % _BASE_DN,
    ldap.SCOPE_SUBTREE,
    "(objectClass=groupOfNames)"
)

# Djangoフィールド名とFreeIPA属性のマッピング
AUTH_LDAP_USER_ATTR_MAP = {
    "user_name": "uid",
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}

# グループ管理
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()

# Django LDAPバックエンドの登録
AUTHENTICATION_BACKENDS += ['django_auth_ldap.backend.LDAPBackend']

# FreeIPAグループとDjango/CVATグループのマッピング
AUTH_LDAP_ADMIN_GROUPS = [
    'CN=cvat_admins,CN=Groups,%s' % _BASE_DN,
]
AUTH_LDAP_WORKER_GROUPS = [
    'CN=cvat_workers,CN=Groups,%s' % _BASE_DN,
]
AUTH_LDAP_USER_GROUPS = [
    'CN=cvat_users,CN=Groups,%s' % _BASE_DN,
]

DJANGO_AUTH_LDAP_GROUPS = {
    "admin": AUTH_LDAP_ADMIN_GROUPS,
    "user": AUTH_LDAP_USER_GROUPS,
    "worker": AUTH_LDAP_WORKER_GROUPS,
}
```

### 参考資料
- [Microsoft - LDAP 識別名](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ldap/distinguished-names)
  - 識別名を構成する要素。ユーザー／グループ検索で使用。
- [Django LDAP リファレンスマニュアル](https://django-auth-ldap.readthedocs.io/en/latest/reference.html)
  - DjangoでLDAP認証に使用できる他のオプション。
- [Active Directoryを使ったDjango LDAPガイド（非公式）](https://techexpert.tips/django/django-ldap-authentication-active-directory)
  - CVATに特化していませんが、ファイアウォールルールなどの参考になります。