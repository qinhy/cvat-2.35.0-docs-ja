---
title: 'シェイプのグループ化'
linkTitle: 'シェイプのグループ化'
weight: 27
description: 'アノテーション中に複数のシェイプをグループ化する機能。'
---

この機能を使うと、複数のシェイプをグループ化できます。

`グループ化`ボタンまたはショートカットを使用できます。

- `G` — グループモードで選択開始／終了
- `Esc` — グループモードを終了
- `Shift+G` — 選択したシェイプのグループをリセット

シェイプはクリックまたは範囲選択で選択できます。

グループ化されたシェイプは、出力アノテーションに `group_id` フィールドが付きます。

また、インスタンス（デフォルト）からグループ単位での色分けに切り替えることも可能です。
そのためには `グループごとに色分け` チェックボックスを切り替えてください。

`group_id` を持たないシェイプは白色でハイライト表示されます。

![](/images/image078_detrac.jpg)

![](/images/image077_detrac.jpg)

## シェイプグループ化のビデオチュートリアル

<!--lint disable maximum-line-length-->

<iframe width="560" height="315" src="https://www.youtube.com/embed/m8bB9f23wLs?si=N5EzIRG-1Wn6R15G" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<!--lint enable maximum-line-length-->
