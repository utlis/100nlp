"""
52. ステミング
51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と語幹をタブ区切り形式で出力せよ． Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．
"""

import sys
from nltk.stem.porter import PorterStemmer

for line in sys.stdin.readlines():
	stemmer = PorterStemmer()
	stripped = line.strip()
	print(stripped, stemmer.stem(stripped), sep='\t')
