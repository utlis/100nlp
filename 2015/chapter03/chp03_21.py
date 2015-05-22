"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
"""

import re

f = open('jawiki-england.txt', 'r')
o = open('jawiki-england-category.txt', 'w')

category = re.compile(r"\[\[Category:.+\]\]")

for line in f:
	m = re.match(category, line)
	if m:
		o.write(line.strip()+"\n")  # "|*" は取り除くべきか？

f.close()
o.close()
