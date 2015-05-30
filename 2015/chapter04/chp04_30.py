"""
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""


def morpheme_reader(mecabfile):
	sentences = []
	sentence = []
	for morpheme in mecabfile:
		if morpheme == "EOS\n":
			sentences.append(sentence)
			# shallow/deep copy
			# del sentence[:]  # 参照
			sentence = []
		else:
			surface, feature = morpheme.split("\t")
			features = feature.split(",")

			morpheme_dict = {
					'surface': surface,
					'base': features[6],
					'pos': features[0],
					'pos1': features[1],
				}
			sentence.append(morpheme_dict)

	return sentences


def main():
	with open("neko.txt.mecab", 'r') as mecabfile:
		sentences = morpheme_reader(mecabfile)

	return sentences


if __name__ == '__main__':
	sentences = main()
	print("[")
	for sentence in sentences:
		print(sentences)
	print("]")
