"""
29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
"""

import requests
import json

with open('jawiki-england-fundamentals-rm_markup.json', 'r') as f:
	template = json.load(f)

wikipedia_api = "http://ja.wikipedia.org/w/api.php?"
prop = {
	'action': "query",
	#'titles': "Image:",
	'prop': "imageinfo",
	'iiprop': "url",
	'format': "json",
	'formatversion': '2',
	'utf8': '',
	'continue': ''
}

for country in template:
	if '国旗画像' in country:
		filename = country['国旗画像']
		prop['titles'] = "Image:" + filename
		res = requests.get(url=wikipedia_api, params=prop)
		datum = json.loads(res.text)
		try:
			file_url = datum['query']['pages'][0]['imageinfo'][0]['url']
		except:
			print(datum)
			break
		print(filename, file_url)
