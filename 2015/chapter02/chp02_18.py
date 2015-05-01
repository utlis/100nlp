"""
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）
"""

import sys


def split_col2ary(file):
	return [ tuple(line.split('\t')) for line in file.readlines() ]


def main():
	with open(sys.argv[1], "r") as f:
		out = open("sorted_col3_{}".format(sys.argv[1]), "w")
		file_ary = split_col2ary(f)
		sorted_f = sorted(file_ary, key=lambda x: float(x[2]))
		for line in sorted_f:
			out.write('\t'.join(line))
		out.close()


if __name__ == '__main__':
	main()

# sort -k 3 hightemp.txt > sorted_hightemp.txt
