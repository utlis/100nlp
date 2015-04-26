# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

# from 05.py (due to the restriction that number-named file cannot be imported)
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

X = set(n_gramizer("paraparaparadise", 2, unit="char"))
Y = set(n_gramizer("paragraph", 2, unit="char"))

print(union = X | Y)
print(interseption = X & Y)
print(difference = X - Y)

print("check containment of 'se'")
print(('s', 'e') in X)
print(('s', 'e') in Y)
