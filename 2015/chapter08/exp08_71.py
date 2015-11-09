"""
71. ストップワード
英語のストップワードのリスト（ストップリスト）を適当に作成せよ．さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，それ以外は偽を返す関数を実装せよ．さらに，その関数に対するテストを記述せよ．
"""

STOPWORDS = [line.strip() for line in open('stopwords_en1.txt', 'r')]


def is_stopword(word):
	return word.lower() in STOPWORDS
	#if word.lower() in STOPWORDS:
	#	return True
	#else:
	#	return False


def main():
	print('stopword inclusion check...')
	for word in STOPWORDS:
		if not is_stopword(word):
			raise RuntimeError("word '{}' is excluded from STOPWORDS".format(word))

	print('success!')

	print('non-stopword exclusion check...')
	for word in "naive bayes support vector machine logistic regression random forest".split():
		if is_stopword(word):
			raise RuntimeError("word '{}' is included in STOPWORDS".format(word))

	print('success!')

if __name__ == '__main__':
	main()
