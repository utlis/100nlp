"""
39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
"""

import chp04_36 as p36
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = 14, 10
fp = FontProperties(fname="/Users/shuntaroy/Library/Fonts/rounded-mgenplus-2cp-regular.ttf")
#plt.rcParams['font.family'] = 'IPAexGothic'


def main():
	counter = p36.main()
	#freq = pd.Series(list(counter.values()), index=list(counter.keys()))

	#plot = freq.hist()
	#fig = plot.get_figure()
	#fig.savefig('fig38.png')

	plt.figure()
	plt.xscale('log')
	plt.yscale('log')
	plt.plot(sorted(list(counter.values()), reverse=True), range(1, len(list(counter))+1))
	plt.savefig('fig39-2.png')

if __name__ == '__main__':
	main()
