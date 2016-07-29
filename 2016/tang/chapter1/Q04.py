#Q04: "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

sequence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

list04 = sequence.split()
list04 = [a.strip(',.') for a in list04]
key04 = list(range(len(list04)))

dict04 = dict(zip(key04,list04))

target04 = [1,5,6,7,8,9,15,16,19]

for num in dict04:
	if num+1 in target04:
		dict04[num] = dict04[num][0]
	else:
		dict04[num] = dict04[num][:2]

print(dict04)
