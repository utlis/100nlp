"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""

import sys
import chp02_10 as p10

source = open(sys.argv[1])
N = int(sys.argv[2])
wc = p10.line_counter(source)
source.seek(0, 0)
output_lineno, mod = divmod(wc, N)
#if mod == wc:
#	raise ValueError("error: N is bigger than total lines of {}".format(sys.argv[1]))
#elif mod < N:

# i'm not sure how to handle mod error
if mod != 0:
	raise ValueError("can not split the file by given N.")


files = [open("splitted_{0:02d}.txt".format(i+1), "w") for i in range(N)]

for file in files:
	count = output_lineno
	while count > 0:
		file.write(source.readline())  # 末尾まで来てもエラーでない
		count -= 1
	else:
		continue

source.close()

# split hightemp.txt -l line_number
# optparse.OptionParser()
# .add_option()

"""
splitに合わせて実装するのが正解？
"""
