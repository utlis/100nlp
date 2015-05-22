"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
"""

import re

f = open('jawiki-england.txt', 'r')
o = open('jawiki-england-section.txt', 'w')

section = re.compile(r"=(=+) (.+) =\1")

for line in f:
	m = re.match(section, line)
	if m:
		o.write("sec {}: ".format(len(m.group(1))))
		o.write(m.group(2)+"\n")

f.close()
o.close()
