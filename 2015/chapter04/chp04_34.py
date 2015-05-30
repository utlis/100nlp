"""
34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""

import chp04_30 as p30


def NofN_extractor(sentences):
	NofNs = []
	for sentence in sentences:
		# len(sentence) > 2 を保証しておくべき
		for k in range(len(sentence)-3):
			triple = sentence[k:k+3]
			a = triple[0]['pos'] == "名詞"
			of = triple[1]['surface'] == "の"
			b = triple[2]['pos'] == "名詞"
			if a and of and b:
				NofNs.append((i['surface'] for i in triple))
		# for one, two, three in zip(sent, sent[1:], sent[2:]):

	return NofNs


def main():
	sentences = p30.main()
	return NofN_extractor(sentences)


if __name__ == '__main__':
	NofNs = main()
	for NofN in NofNs:
		print("".join(NofN))
