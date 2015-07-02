"""
40. 係り受け解析結果の読み込み（形態素）
形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
"""


class Morph():

	def __init__(self, surface, base, pos, pos1):
		self.surface = surface
		self.base = base
		self.pos = pos
		self.pos1 = pos1

	def print_all(self):
		return self.surface + "\t" + self.base + ", " + self.pos + ", " + self.pos1


def morpheme_reader(cabochafile):
	sentences = []
	sentence = []
	for line in cabochafile:
		if line == "EOS\n":
			sentences.append(sentence)
			# shallow/deep copy
			# del sentence[:]  # 参照
			sentence = []
		elif line[0] == "*":  # ignore 係り受け情報
			continue
		else:
			surface, feature = line.split("\t")
			features = feature.split(",")
			morph = Morph(surface, features[6], features[0], features[1])
			sentence.append(morph)

	return sentences


def main():
	with open("neko.txt.cabocha", 'r') as cabochafile:
		sentences = morpheme_reader(cabochafile)

	return sentences


if __name__ == '__main__':
	sentences = main()
	print("Here is morphs of third sentence of the given text.")
	print("---")
	for morph in sentences[2]:
		print(morph.print_all())
