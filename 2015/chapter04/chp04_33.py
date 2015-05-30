"""
33. サ変名詞
サ変接続の名詞をすべて抽出せよ．
"""

import chp04_30 as p30


def sahen_noun_extractor(sentences):
	sahen_nouns = []
	for sentence in sentences:
		for morpheme in sentence:
			if morpheme['pos1'] == "サ変接続":
				sahen_nouns.append(morpheme['surface'])

	return sahen_nouns


def main():
	sentences = p30.main()
	return sahen_noun_extractor(sentences)


if __name__ == '__main__':
	sahen_nouns = main()
	for sahen_noun in sahen_nouns:
		print(sahen_noun)
