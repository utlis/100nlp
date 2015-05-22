"""
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""

import re

f = open('jawiki-england.txt', 'r')
o = open('jawiki-england-category-names.txt', 'w')

category = re.compile("\[\[Category:(.+)\]\]")

for line in f:
	m = re.match(category, line)
	if m:
		o.write(m.group(1)+"\n")

f.close()
o.close()
