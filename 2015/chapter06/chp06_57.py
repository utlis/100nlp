"""
57. 係り受け解析
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
"""

import sys
import chp06_56 as p56


def dependency2dot(i, dependency):
	header = "digraph sentence{0} ".format(i)
	body_head = "{ graph [rankdir = LR]; "
	body = ''
	# idxを考慮しないと同じ単語が1文中に出てきたとき重複が起こる
	for dep in dependency:
		governor, dependent, label = dep.find('governor').text, dep.find('dependent').text, dep.get('type')
		body += ('"{gov}"->"{dep}" [label = "{label}"]; '.format(gov=governor, dep=dependent, label=label))

	dot_string = header + body_head + body + '}'

	return dot_string


def main(xmlfilename):
	doc = p56.StanfordDocument(xmlfilename)
	sentences = doc.sentences.findall('sentence')
	dot_sentences = []

	for i, sentence in enumerate(sentences):
		dependency = sentence.find("dependencies[@type='collapsed-dependencies']")
		dot_sentences.append(dependency2dot(i+1, dependency))

	return dot_sentences


if __name__ == '__main__':
	dot_sentences = main(sys.argv[1])
	if len(sys.argv) > 2:
		target = int(sys.argv[2]) - 1
		print(dot_sentences[target])
	else:
		for dot_sentence in dot_sentences:
			print(dot_sentence)
