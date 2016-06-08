#Q01: 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

sequence = 'パタトクカシーー'
strtolist = list(sequence)
list01 = strtolist[::2]
print(''.join(list01))
