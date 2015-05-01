# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．


def n_gramizer(text, n, unit="word"):
	"""
	Input: text (str), n (Int), unit (str, "word" or "char")
	Output: list of tuples
	"""
	#n = n-1
	#result = []
	if unit == "word":
		words = text.split(" ")  # or split() only
		return [tuple(words[i:i+n]) for i in range(len(words)-n+1)]
			#result.append((words[i], words[i+n]))
	elif unit == "char":
		return [tuple(text[i:i+n]) for i in range(len(text)-n+1)]
			#result.append((text[i], text[i+n]))
	else:
		# print error
		print("Please set 'unit' option as 'word' or 'char'.")

	#return result

if __name__ == '__main__':
	sentence = "I am an NLPer"
	print("word bi-gram: ", n_gramizer(sentence, 2))
	print("character bi-gram: ", n_gramizer(sentence, 2, unit="char"))
