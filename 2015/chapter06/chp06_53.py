"""
53. Tokenization
Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
"""

import sys
import re

WORD_PAT = re.compile(r"<word>(\w+)</word>")

with open(sys.argv[1], 'r') as xmlfile:
	for line in xmlfile:
		word = WORD_PAT.search(line.strip())
		if word:
			print(word.group(1))
