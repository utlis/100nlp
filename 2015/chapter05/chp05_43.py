"""
43. 名詞を含む文節が動詞を含む文節に係るものを抽出 名詞を含む文節が,動詞を含む文節に係るとき,これらをタブ区切り形式で抽出せよ.ただし,句読点などの記号は出力しないようにせよ.
"""

import chp05_42 as p42


def find_noun2verb_pair(chunk_pair):
	noun_flg = False
	verb_flg = False

	former, latter = chunk_pair

	if '名詞' in [morph.pos for morph in former.morphs]:
		noun_flg = True

	if '動詞' in [morph.pos for morph in latter.morphs]:
		verb_flg = True

	return noun_flg and verb_flg


def main():
	paired_sentences = p42.main()

	noun2verb_pairs = []
	for paired_sentence in paired_sentences:
		for chunk_pair in paired_sentence:
			if find_noun2verb_pair(chunk_pair):
				noun2verb_pairs.append(chunk_pair)

	return noun2verb_pairs


if __name__ == '__main__':
	noun2verb_pairs = main()
	for noun2verb_pair in noun2verb_pairs:
		former, latter = noun2verb_pair
		print(former, latter, sep='\t')
