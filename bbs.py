#!/usr/bin/python3

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

#CGIとして実行した際のフォーム情報を取り出すライブラリ
import cgi
form_data = cgi.FieldStorage(keep_blank_values = True)

#MySQLデータベース接続用ライブラリ
import MySQLdb
con = None
cur = None

#設定情報を外部設定ファイル（.env）から読み取るライブラリ
#今回はデータベースに接続するための各情報を設定ファイルから読み取るために使用
import os
from pathlib import Path
env_path = Path('.') / '.env'
from dotenv import load_dotenv
load_dotenv( dotenv_path = env_path, verbose = True )

#トップ画面のHTMLを出力する関数
def print_html():
	
	print('<!DOCTYPE html>')
	print('<html>')
	print()

	print('<head>')
	print('<meta charset="UTF-8">')
	print('</head>')

	print('<body>')
	print('<p>ひとこと掲示板</p>')

	print('<form action="" method="POST">')
	print('<input type="hidden" name="method_type" value="tweet">')
	print('<input type="text" name="poster_name" value="" placeholder="なまえ">')
	print('<br>')
	print('<textarea name="body_text" value="" placeholder="本文"></textarea>')
	print('<input type="submit" value="投稿">')
	print('</form>')

	#罫線を出力
	print('<hr>')

	#書き込みの一覧を取得するSQL文を作成
	sql = "select * from posts"

	cur.execute(sql)

	rows = cur.fetchall()

	for row in rows:
		print('<div class="meta">')
		print('<span class="id">' + str(row[ 'id' ]) + '</span>')
		print('<span class="name">' + str(row[ 'name' ]) + '</span>')
		print('<span class="date">' + str(row[ 'created_at' ]) + '</span>')
		print('</div>')
		print('<div class="message"><span>' + str(row[ 'body' ]) + '</span></div>')

	print('</body>')
	
	print('</html>')

#フォーム経由のアクセスを処理する関数
def proceed_methods():
	method = form_data[ 'method_type' ].value

	if(method == 'tweet'):
		poster_name = form_data[ 'poster_name' ].value
		body_text = form_data[ 'body_text' ].value

		sql = 'insert into posts (name, body) values (%s, %s)'
		cur.execute(sql, (poster_name, body_text) )
		con.commit()
	
	#処理に成功したらトップ画面に自動遷移するページ
	print('<!DOCTYPE html>')
	print('<html>')
	print('	<head>')
	print('		<meta http-equiv="refresh" content="5; url=./bbs.py">')
	print('	</head>')
	print('	<body>')
	print('		処理が成功しました。5秒後に元のページに戻ります。')
	print('	</body>')
	print('</html>')


#メイン処理を実行する関数
def main():
	print('Content-Type: text/html; charset=utf-8')
	print('')

	#ここでデータベースに接続しておく
	global con, cur
	try:
		con = MySQLdb.connect(
			host = os.environ.get( 'bbs_db_host' ),
			user = str(os.environ.get( 'bbs_db_user' )),
			passwd = str(os.environ.get( 'bbs_db_pass' )),
			db = str(os.environ.get( 'bbs_db_name' )),
			use_unicode = True,
			charset = 'utf8'
		)

	except MySQLdb.Error as e:
		print('データベース接続に失敗しました。')
		print(e)
		exit()

	cur = con.cursor(MySQLdb.cursors.DictCursor)

	if('method_type' in form_data):
		proceed_methods()
	else:
		print_html()
	
	cur.close()
	con.close()

if __name__=="__main__":
	main()
