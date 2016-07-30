#Q13: 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

with open("col1.txt",encoding="utf-8") as f1, open("col2.txt",encoding="utf-8") as f2:
    l1l2=[x.strip()+"\t"+y.strip() for x,y in zip(f1.readlines(),f2.readlines())]
with open("col1col2.txt","w",encoding="utf-8") as f:
    f.write("\n".join(l1l2))

# $ paste col1.txt col2.txt >col1col2_paste.txt
