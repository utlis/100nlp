"""
54. 品詞タグ付け
Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．
"""

import sys
import re

token = []
WORD = re.compile(r"<word>(\w+)</word>")
LEMMA = re.compile(r"<lemma>(\w+)</lemma>")
POS = re.compile(r"<POS>(\w+)</POS>")

# 親を無視して該当タグをすべて上から順番にとってくる
# ElementTree.iter(tag)  # ET method
# ElementTree.findall('.//token')  # XPath

with open(sys.argv[1], 'r') as xmlfile:
	for line in xmlfile:
		if len(token) == 3:
			print('\t'.join(token))
			token.clear()
		else:
			if len(token) == 0:
				word = WORD.search(line.strip())
				if word: token.append(word.group(1))
			if len(token) == 1:
				lemma = LEMMA.search(line.strip())
				if lemma: token.append(lemma.group(1))
			if len(token) == 2:
				pos = POS.search(line.strip())
				if pos: token.append(pos.group(1))
