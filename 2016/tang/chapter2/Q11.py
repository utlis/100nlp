#Q11: タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

with open("hightemp_Q11.txt","w",encoding="utf-8") as file_write:
	with open("hightemp.txt",encoding="utf-8") as file_read:
		for line in file_read.readlines():
			file_write.write(line.replace("\t"," "))

# $ sed -e $'s/\t/ /g' hightemp.txt >hightemp_sed.txt
## "$"を付けないと"\t"が展開されないらしい
# $ tr '\t' ' ' <hightemp.txt >hightemp_tr.txt
# $ expand -t 2 hightemp.txt >hightemp_expand.txt
