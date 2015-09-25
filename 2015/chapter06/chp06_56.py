"""
56. 共参照解析
Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．
"""

import sys
import xml.etree.ElementTree as ET
import re
from functools import partial


LRB = re.compile(r'-LRB- ')
RRB = re.compile(r' -RRB-')
NOTATION = re.compile(r' ([,\.:;])')
LDQ = re.compile(r'`` ')
RDQ = re.compile(r" \'\'")
SQ = re.compile(r" '")
SQS = re.compile(r" 's")


class StanfordDocument():

	def __init__(self, xmlfilename):
		self.xmltree = ET.parse(xmlfilename)

		root = self.xmltree.getroot()
		self.sentences = root.find('document/sentences')
		self.coreferences = root.find('document/coreference')

	def get_list_of_sentences(self):
		sentences = []
		for sentence in self.sentences.findall('sentence'):
			sentences.append([word.text for word in sentence.findall('tokens/token/word')])

		return sentences


def main(xmlfilename):
	doc = StanfordDocument(xmlfilename)
	sentences = doc.get_list_of_sentences()

	for coref in doc.coreferences.findall('coreference'):
		mentions = coref.findall('mention')
		represent = coref.find("mention[@representative='true']")
		for mention in mentions:
			if mention != represent:
				sentence_i = int(mention.find('sentence').text) - 1
				start_i = int(mention.find('start').text) - 1
				# 'end' word is not inclusive
				end_i = int(mention.find('end').text) - 2

				target_sentence = sentences[sentence_i]
				target_sentence[start_i] = represent.find('text').text.strip() + ' (' + target_sentence[start_i]
				target_sentence[end_i] = target_sentence[end_i] + ')'

	return sentences


def sentence_prettify(sentence):
	str_sentence = ' '.join(sentence)

	# ugly verbatim operation
	#str_sentence = LRB.sub('(', str_sentence)
	#str_sentence = RRB.sub(')', str_sentence)
	#str_sentence = NOTATION.sub(r'\1', str_sentence)
	#str_sentence = LDQ.sub('\"', str_sentence)
	#str_sentence = RDQ.sub('\"', str_sentence)

	# curry function 関数の部分適用
	partials = map(
		lambda x: partial(x[0], x[1]),
		[  # carefully order regex
			(LRB.sub, '('),
			(RRB.sub, ')'),
			(LDQ.sub, '\"'),
			(RDQ.sub, '\"'),
			(SQS.sub, "'s"),  # not need?
			(SQ.sub, "'"),
			(NOTATION.sub, r'\1'),
		])

	for part in partials:
		str_sentence = part(str_sentence)

	return str_sentence


if __name__ == '__main__':
	sentences = main(sys.argv[1])
	for sentence in sentences:
		str_sentence = sentence_prettify(sentence)
		print(str_sentence)
