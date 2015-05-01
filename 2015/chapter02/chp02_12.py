"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
"""

import sys


f = open(sys.argv[1], "r")
col1 = open("col1.txt", "w")
col2 = open("col2.txt", "w")

for line in f:
	cols = line.split('\t')
	col1.write(cols[0].rstrip("\n") + "\n")  # write don't put \n
	col2.write(cols[1].rstrip("\n") + "\n")  # generalize to every tsv structure

f.close()
col1.close()
col2.close()

# > cut -f 1 hightemp.txt > col1_cut.txt
# > cut -f 2 hightemp.txt > col2_cut.txt
