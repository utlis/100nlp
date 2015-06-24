"""
37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
"""

import chp04_36 as p36
import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = 14, 10
fp = FontProperties(fname="/Users/shuntaroy/Library/Fonts/rounded-mgenplus-2cp-regular.ttf")
#plt.rcParams['font.family'] = 'IPAexGothic'


def main():
	counter = p36.main()
	word10 = []
	count10 = []
	for word, count in counter.most_common(10):
		word10.append(word)
		count10.append(count)

	plt.bar(range(10), count10, align='center')
	plt.xticks(range(0, 10), word10)
	plt.savefig('fig37.png')


if __name__ == '__main__':
	main()
