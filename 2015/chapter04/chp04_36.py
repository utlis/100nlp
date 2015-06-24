"""
36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""

import chp04_30 as p30
#from ..chapter02 import chp02_19 as p19
from collections import Counter


def main():
	sentences = p30.main()
	all_surface = []
	for sentence in sentences:
		for morpheme in sentence:
			all_surface.append(morpheme['surface'])

	return Counter(all_surface)


if __name__ == '__main__':
	counter = main()
	for word, count in counter.most_common():
		print(word, count)
