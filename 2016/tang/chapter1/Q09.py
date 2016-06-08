#Q09: スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

import random

def Typoglycemia(sequence):
	sequence=sequence.replace(":","").replace(".","").replace("  "," ").replace("'","a").strip()
	l=sequence.split(" ")
	for n in range(0,len(l)):
		if len(l[n])>=4:
            l[n]=l[n][0]+"".join(random.sample(l[n][1:-1],len(l[n][1:-1])))+l[n][-1]
	return " ".join(l)

sequence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(Typoglycemia(sequence))
