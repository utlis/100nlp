"""
35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""

import chp04_30 as p30


def Nseq_extractor(sentences):
	Nseqs = []
	Nseq = []
	for sentence in sentences:
		for morpheme in sentence:
			if morpheme['pos'] == '名詞':
				Nseq.append(morpheme['surface'])
			else:
				if len(Nseq) > 1:
					Nseqs.append(Nseq)
				Nseq = []

	return Nseqs


def main():
	sentences = p30.main()
	return Nseq_extractor(sentences)


if __name__ == '__main__':
	Nseqs = main()
	for Nseq in Nseqs:
		print("".join(Nseq))
