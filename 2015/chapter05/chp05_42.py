"""
42. 係り元と係り先の文節の表示 係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ.
ただし,句読点などの記号は出力しないようにせよ.
"""

import chp05_41 as p41


#def make_chunk_pair(sentences):
#	pairs = []
#	for sentence in sentences:
#		for chunk in sentence:
#			if chunk.dst != -1:
#				pairs.append((chunk, sentence[chunk.dst]))

#	return pairs


def make_chunk_pair(sentence):
	pairs = []

	for chunk in sentence:
		if chunk.dst != -1:
			pairs.append((chunk, sentence[chunk.dst]))

	return pairs


def main():
	sentences = p41.main()

	new_sentences = []
	for sentence in sentences:
		paired_sentence = make_chunk_pair(sentence)
		new_sentences.append(paired_sentence)

	return new_sentences


if __name__ == '__main__':
	sentences = main()
	for sentence in sentences:
		for pair in sentence:
			print("\t".join([str(chunk) for chunk in pair]))
