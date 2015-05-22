"""
27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
"""

import chp03_25 as p25
import chp03_26 as p26
import re
import json


def internallink_remover(string):
	internallink = re.compile(r"\[\[((.+?)\|)?(.+?)\]\]")
	strengthen_removed = p26.strengthen_remover(string)
	return internallink.sub(r"\3", strengthen_removed)


def main():
	f = open('jawiki-england.txt', 'r')
	fundamentals = p25.fundamental_extractor(f, internallink_remover)
	f.close()
	with open('jawiki-england-fundamentals-rm_st_link.json', 'w') as o:
		json.dump(fundamentals, o, ensure_ascii=False)


if __name__ == '__main__':
	main()
