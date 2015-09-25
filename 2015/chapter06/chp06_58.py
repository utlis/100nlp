"""
58. タプルの抽出
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，「主語 述語 目的語」の組をタブ区切り形式で出力せよ．ただし，主語，述語，目的語の定義は以下を参考にせよ．

述語: nsubj関係とdobj関係の子（dependant）を持つ単語
主語: 述語からnsubj関係にある子（dependent）
目的語: 述語からdobj関係にある子（dependent）
"""

import sys
import chp06_56 as p56


def extract_triples(sentence):
	dependencies = sentence.find("dependencies[@type='collapsed-dependencies']")
	dep_triple = []
	dep_dic = {}

	for dep in dependencies:
		#(idx, governor): [(type, dependent), ...]
		gov = (dep.find('governor').get('idx'), dep.find('governor').text)
		if dep.get('type') in ['nsubj', 'dobj']:
			dep_dic.setdefault(gov, []).append((dep.get('type'), dep.find('dependent').text))

	verbs = [key for key, value in dep_dic.items() if set([t for (t, d) in value]) == set(['nsubj', 'dobj'])]
	#print(verbs)

	for verb in verbs:
		nsubj = [d for (t, d) in dep_dic[verb] if t == 'nsubj']
		dobj = [d for (t, d) in dep_dic[verb] if t == 'dobj']
		dep_triple += [[verb[1], n, d] for n in nsubj for d in dobj]

	return dep_triple


def main(xmlfilename):
	doc = p56.StanfordDocument(xmlfilename)
	sentences = doc.sentences.findall('sentence')
	dep_triples = []

	for sentence in sentences:
		dep_triples.append(extract_triples(sentence))

	return dep_triples

if __name__ == '__main__':
	dep_triples = main(sys.argv[1])
	for dep_triple in dep_triples:
		for dt in dep_triple:
			#print('\t'.join(dt))
			print(dt[1], dt[0], dt[2], sep="\t")
