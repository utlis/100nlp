"""
31. 動詞
動詞の表層形をすべて抽出せよ．
"""

import chp04_30 as p30


def verb_extractor(sentences):
	verbs = []
	for sentence in sentences:
		for morpheme in sentence:
			if morpheme['pos'] == "動詞":
				verbs.append(morpheme['surface'])

	return verbs


def main():
	sentences = p30.main()
	return verb_extractor(sentences)


if __name__ == '__main__':
	verbs = main()
	for verb in verbs:
		print(verb)
