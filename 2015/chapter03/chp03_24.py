"""
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
"""

import re

f = open('jawiki-england.txt', 'r')
o = open('jawiki-england-media.txt', "w")

# ex) [[ファイル:Coat_of_arms_of_Egypt.svg|100px|エジプトの国章]]
# \s , . \d の考慮が必要
media = re.compile(r"[ファイル|File|file]:([\w\-_\s.,\d]+\.[a-zA-Z\d]+).*\|")

for line in f:
	m = media.search(line)
	if m:
		o.write(m.group(1)+"\n")

f.close()
o.close()
