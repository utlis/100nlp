"""
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
"""

import sys
import chp02_10 as p10

n = int(sys.argv[1])
f = open(sys.argv[2], "r")

lineno = p10.line_counter(f)

head = lineno - n
f.seek(0, 0)  # set cursol to the head of the file

# go to the head of tail_start
while head > 0:
	f.readline()
	head -= 1

# print tail N
while n > 0:
	print(f.readline(), end='')
	n -= 1

f.close()

# tail -n N hightemp.txt
# readlines()[-N:]
