# 01. 「パタトクカシーー」
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

text = "パタトクカシーー"
arr = list(text)

odd = ""
even = ""

for i in range(len(text)):
	if i % 2 == 0:
		even += text[i]
	else:
		odd += text[i]

print(odd)
print(even)
