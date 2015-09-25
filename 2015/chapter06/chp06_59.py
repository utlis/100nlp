"""
59. S式の解析
Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての名詞句（NP）を表示せよ．入れ子になっている名詞句もすべて表示すること．
"""

import sys
import chp06_56 as p56

# nltk.Tree でS式をTreeなObjectで操作できる

class TreeParser():

	def __init__(self):
		self.root = None
		self._stack = [[]]
		# ネストを解釈するパーサは2重のスタックが有効
		# 新しい入れ子が現れるたびに外側にスタックを生成
		# 入れ子が閉じられるたびに、いま操作しているスタックをその直前まで操作していたスタックに入れ込む(pop)

	def parse(self, tree_string):
		reading = []
		for character in tree_string.strip():
			if character == '(':
				self._stack.append([])
			elif character == ' ':
				if reading:
					self._stack[-1].append(''.join(reading))
					reading.clear()
			elif character == ')':
				if reading:
					self._stack[-1].append(''.join(reading))
					reading.clear()
				self._stack[-2].append(self._stack.pop())
			else:  # string
				reading.append(character)

		self.root = self._stack.pop()

	def get_phrase(self, tag):
		s = self.root[0][1]
		return self._recursive_finder(s, tag)

	def _recursive_finder(self, lst, tag):
		result = []

		if lst[0] == tag:
			result.append(lst)

		for i in lst[1:]:
			if isinstance(i, list):
				result.extend(self._recursive_finder(i, tag))

		return result

		## below script has a bug

		#for i in lst:
		#	if isinstance(i, list):
		#		result += self._recursive_finder(i, tag)
		#	else:  #string
		#		if i == tag:
		#			result.append(lst)


def main(xmlfilename, tag):
	doc = p56.StanfordDocument(xmlfilename)
	sentences = doc.sentences.findall('sentence')
	all_tag_phrases = []

	for sentence in sentences:
		parser = TreeParser()
		tree_string = sentence.find('parse').text
		parser.parse(tree_string)
		all_tag_phrases.append(parser.get_phrase(tag))

	return all_tag_phrases


def str_phrase(phrase):
	output = []

	for i in phrase:
		if isinstance(i, list):
			if isinstance(i[1], list):
				output += str_phrase(i)
			else:
				output.append(i[1])

	return output

if __name__ == '__main__':
	all_np_phrases = main(sys.argv[1], 'NP')

	for np_phrases in all_np_phrases:
		for np_phrase in np_phrases:
			phrase_list = str_phrase(np_phrase)
			np_string = p56.sentence_prettify(phrase_list)
			print(np_string)
