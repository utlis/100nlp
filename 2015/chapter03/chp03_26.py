"""
26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．
"""

import chp03_25 as p25
import re
import json


def strengthen_remover(string):
	strengthen = re.compile(r"''('*)(.+)''\1")
	return strengthen.sub(r"\2", string)

	#strengthen = re.compile(r"''+")
	#return strengthen.sub("", string)


def main():
	f = open('jawiki-england.txt', 'r')
	fundamentals = p25.fundamental_extractor(f, strengthen_remover)
	f.close()
	with open('jawiki-england-fundamentals-rm_st.json', 'w') as o:
		json.dump(fundamentals, o, ensure_ascii=False)


if __name__ == '__main__':
	main()
