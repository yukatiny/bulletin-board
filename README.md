# ひとこと掲示板の作り方

<img width="168" alt="readme_pic" src="https://user-images.githubusercontent.com/75052592/100316830-a1f02280-2ffe-11eb-8d7c-918012d12d1c.png">

UbuntuでPython3とMySQLデータベースを使い、ひとこと掲示板を作りました。投稿されたものは掲示板の下部に表示されていき、記録として残るようになっています。作成手順は以下の通りです。

## 環境

今回のひとこと掲示板作成にあたり、作成者の使用環境はこちらです。

```bash
* Ubuntu20.04
* Python3.8.5
* MySQL Community Server 8.0.22
```

## 準備

掲示板を作成する前に準備しておくことが2つあります。

* Apache2でCGIを有効化する
* ホームディレクトリ配下に「public_html」ディレクトリを作成する

## pythonスクリプト作成

「public_html」ディレクトリにPythonスクリプトを作成・保存します。

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

3. 


# Note
 
注意点などがあれば書く
 
## 作成者
 
yukatiny
 
## License
