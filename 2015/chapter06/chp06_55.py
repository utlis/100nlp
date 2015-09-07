"""
55. 固有表現抽出
入力文中の人名をすべて抜き出せ．
"""

import sys
import re

token = ""
person = []
WORD = re.compile(r"<word>(\w+)</word>")
NER = re.compile(r"<NER>(.+)</NER>")

with open(sys.argv[1], 'r') as xmlfile:
	for line in xmlfile:
		word = WORD.search(line.strip())
		if word:
			token = word.group(1)
			next

		ner = NER.search(line.strip())
		if ner:
			if ner.group(1) == 'PERSON':
				person.append(token)
				print(person)
				person.clear()
			#else:
			#	print("\s".join(person))
			#	person.clear()

			# id で連続する人名を考慮する？
