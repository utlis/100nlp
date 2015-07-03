"""
41. 係り受け解析結果の読み込み（文節・係り受け）
40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ
"""


import chp05_40 as p40


class Chunk():

	def __init__(self):
		self.morphs = []
		self.dst = -1
		self.srcs = []

	#def print_all(self):
		#return self.morphs + "\t" + self.dst + ", " + self.srcs

	def __str__(self):
		if self.morphs:
			surfs = [morph.surface for morph in self.morphs if morph.pos != '記号']
			return "".join(surfs)


def chunk_reader(cabochafile):
	sentences = []
	sentence = []
	for line in cabochafile:
		if line == "EOS\n":
			for i, c in enumerate(sentence[:-1]):
				if c.dst != -1:
					sentence[c.dst].srcs.append(i)
				# 係り元は再帰的にとらない

			sentences.append(sentence)
			# shallow/deep copy
			# del sentence[:]  # 参照
			sentence = []
		elif line[0] == "*":
			#sentence.append(line)
			#if len(sentence) > 0:
				#sentence.append(chunk)

			chunk = Chunk()
			chunk.dst = int(line.split(' ')[2].strip('D'))
			sentence.append(chunk)
		else:
			surface, feature = line.split("\t")
			features = feature.split(",")
			morph = p40.Morph(surface, features[6], features[0], features[1])
			sentence[-1].morphs.append(morph)

	return sentences


def main():
	with open("neko.txt.cabocha", 'r') as cabochafile:
		sentences = chunk_reader(cabochafile)

	#chunk_sentences = chunk_builder(sentences)

	#return chunk_sentences
	return sentences


if __name__ == '__main__':
	sentences = main()
	print("Here is chunks of 8th sentence of the given text.")
	print("---")
	for i, chunk in enumerate(sentences[7]):
		surfaces = ""
		for morph in chunk.morphs:
			surfaces += morph.surface

		print("%d:" % i, surfaces, "=>", chunk.dst)
