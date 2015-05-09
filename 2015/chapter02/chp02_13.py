"""
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
"""

col1 = open("col1.txt", "r")
col2 = open("col2.txt", "r")
o = open("resurrection.txt", "w")

for l1 in col1:
	o.write(l1.rstrip("\n") + '\t' + col2.readline())  # readline() read \n
	# rstrip("\n") == rstrip()
	# whitespace \s\t\r\n\f\v
	# replace =~ gsub (ruby)

col1.close()
col2.close()
o.close()

# paste col1.txt col2.txt
# 行数が違う場合
