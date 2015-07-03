"""
44． 係り受け木の可視化
与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語 (http://ja.wikipedia.org/wiki/DOT%E8%A8%80%E8%AA%9E)に変換し，Graph
(http://www.graphviz.org/)を用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydot (https://code.google.com/p/pydot/)を使うとよい．
"""

#import chp05_41 as p41
import chp05_42 as p42
#import string
import sys


def sentence2dot(i, paired_sentence):
	header = "digraph sentence{0} ".format(i)
	body_head = "{ graph [rankdir = LR]; "
	body = ''
	for chunk_pair in paired_sentence:
		former, latter = chunk_pair
		body += ('"'+str(former)+'"->"'+str(latter)+'"; ')

	dot_string = header + body_head + body + '}'

	return dot_string


def main():
	paired_sentences = p42.main()

	dot_sentences = []
	for i, paired_sentence in enumerate(paired_sentences):
		dot_sentence = sentence2dot(i, paired_sentence)
		dot_sentences.append(dot_sentence)

	return dot_sentences


if __name__ == '__main__':
	if len(sys.argv) > 1:
		target = int(sys.argv[1])
		sentences = p42.main()
		print(sentence2dot(target, sentences[target]))
	else:
		dot_sentences = main()
		for dot_sentence in dot_sentences:
			print(dot_sentence)
