"""
28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
"""

import chp03_25 as p25
#import chp03_26 as p26
import chp03_27 as p27
import re
import json


#  .は改行を含まない!
def mediawiki_remover(string):
	mediawiki = [
		r"#REDIRECT\s?(.+)",  # リダイレクト
		r"<!--\s?(.+)\s?-->",  # comment out
		r"\{\{[Ll]ang\|\w+\|(.+)\}\}",  # template
		r"\[https?://[a-zA-Z./]+\s(.+)?\]",  # external link
		r"\d+px\|(.+)",  # 画像の残滓
		r"(.*)<ref.+(</ref>)?>",  # 出典
		r"(.*?)<br\s?/?>",  # 改行マーク
		r"<[a-z]+.*>(.*?)</[a-z]+>",  # HTML tag
	]

	removed = p27.internallink_remover(string)
	for pattern in mediawiki:
		removed = re.compile(pattern).sub(r"\1", removed)

	return removed


def main():
	f = open('jawiki-england.txt', 'r')
	fundamentals = p25.fundamental_extractor(f, mediawiki_remover)
	f.close()
	with open('jawiki-england-fundamentals-rm_markup.json', 'w') as o:
		json.dump(fundamentals, o, ensure_ascii=False)


if __name__ == '__main__':
	main()
