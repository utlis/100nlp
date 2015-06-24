"""
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
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
	freq = pd.Series(list(counter.values()), index=list(counter.keys()))

	plot = freq.hist()
	fig = plot.get_figure()
	fig.savefig('fig38.png')

if __name__ == '__main__':
	main()
