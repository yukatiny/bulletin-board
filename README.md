# ひとこと掲示板の作り方

<img width="168" alt="readme_pic" src="https://user-images.githubusercontent.com/75052592/100316830-a1f02280-2ffe-11eb-8d7c-918012d12d1c.png">

UbuntuでPython3とMySQLデータベースを使い、ひとこと掲示板を作りました。<br>「なまえ」と「本文」を入力し、「投稿」のボタンを押すと入力内容が投稿されます。<br>投稿されたものは掲示板の下部に表示されていき、記録として残るようになっています。<br>作成手順は以下の通りです。

## 環境

作成者の使用環境はこちらです。

```bash
* Ubuntu20.04
* Python3.8.5
* MySQL Community Server 8.0.22
```

## 準備

* Apache2でCGIを有効化する

```bash
# a2enmod cgid
```

```bash
# systemctl restart apache2
```

* ホームディレクトリ配下に「public_html」ディレクトリを作成する

## pythonスクリプト作成

「public_html」ディレクトリにPython3スクリプトを作成・保存します。

リポジトリにある「bbs.py」をそのままコピー・保存で大丈夫です。

## データベース作成

掲示板に投稿された内容はデータベースに保存されるので、データベースを作成します。

データベースの作成方法は以下の通りです。

1. 「public_html」配下にsqlファイルを作成

    例：create_db.sql（ファイル名は何でも構いません）

2. MySQLにログインし、作成したsqlファイルを実行

```bash
mysql> SOURCE create_db.sql
```

これで投稿された内容がデータベースに保存され、掲示板ページの下部に記録として残るようになります。

## 「.env」ファイル作成

ファイル作成の前に、python-dotenvをインストールします。

```bash
$ pip3 install python-dotenv
```

「public_html」配下に「.env」ファイルを作成し、以下の内容を記述します。

```bash
bbs_db_host="ホスト名"
bbs_db_user="ユーザ名"
bbs_db_pass="パスワード"
bbs_db_name="db名"
```

これで「ひとこと掲示板」の完成です。

## 作成者
 
yukatiny

## ライセンス

This is under MIT license (https://en.wikipedia.org/wiki/MIT_License).
