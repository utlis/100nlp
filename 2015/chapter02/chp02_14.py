"""
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
"""

import sys

n = int(sys.argv[1])
f = open(sys.argv[2], "r")

while n > 0:
	print(f.readline(), end="")  # e.g. print(sep=' ')
	n -= 1

f.close()

# head -n N hightemp.txt
# readlines() => list
