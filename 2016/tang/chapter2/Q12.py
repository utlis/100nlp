#Q12: 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ

with open("col1.txt","w",encoding="utf-8") as f1, open("col2.txt","w",encoding="utf-8") as f2, open("hightemp.txt",encoding="utf-8") as f:
	for line in f.readlines():
		line_list=line.split("\t")
		f1.write(line_list[0]+"\n"); f2.write(line_list[1]+"\n")

# $ cut -f 1 <hightemp.txt >col1_cut.txt
