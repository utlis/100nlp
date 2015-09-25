"""
50. 文区切り
(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．
"""

import re
import sys

END_PAT = re.compile(r"(?P<punct>[\.;:\?\!]) (?P<head>[A-Z])")
# []内では特殊文字は機能を失う！('\'不要)

with open(sys.argv[1], 'r') as textfile:
	for line in textfile:
		# simply numbering back reference
		#print(END_PAT.sub(r"\1\n\2", line))

		# you can not use below in re.sub()
		#print(END_PAT.sub(r"(?P=punct)\n(?P=head)", line))

		# In re.sub(), (?P<name>) -> \g<name>
		stripped = line.strip()
		#if stripped:
			#print(END_PAT.sub(r"\g<punct>\n\g<head>", stripped))
		if END_PAT.search(stripped):
			print(END_PAT.sub(r"\g<punct>\n\g<head>", stripped))
