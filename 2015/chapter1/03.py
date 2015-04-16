# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

words = sentence.split(" ")

words_length = []

for word in words:
	if word.endswith((',', '.')):
		words_length.append(len(word.rstrip(',.')))
	else:
		words_length.append(len(word))

print(words_length)
