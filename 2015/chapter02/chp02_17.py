"""
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
"""

import sys

def kotonarizer(file):
	kotonari = set()

	for line in file:
		kotonari.add(line.split("\t")[0])

	return kotonari
	

def main():
	with open(sys.argv[1], "r") as f:
		return kotonarizer(f)

if __name__ == '__main__':
	print(main())

# sort col1.txt | uniq | wc
