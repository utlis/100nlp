"""
72. 素性抽出
極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが最低限のベースラインとなるであろう．
73. 学習
72で抽出した素性を用いて,ロジスティック回帰モデルを学習せよ. 
74. 予測
73で学習したロジスティック回帰モデルを用い,与えられた文の極性ラベル(正例なら"+1",負例なら"-1")と,その予測確率を計算するプログラムを実装せよ.
75. 素性の重み
73で学習したロジスティック回帰モデルの中で,重みの高い素性トップ10と,重みの低い素性トップ10を確認せよ.
"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
#from nltk.stem.porter import PorterStemmer

#from collections import OrderedDict

#import exp08_71 as p71

# exercise 72
class LemmaTokenizer(object):

	def __init__(self):
		self.wnl = WordNetLemmatizer()

	def __call__(self, doc):
		return [self.wnl.lemmatize(t) for t in word_tokenize(doc)]


def get_sentiments():
	sentiments = open('sentiment.txt', 'r').readlines()
	x = np.array([line[3:] for line in sentiments])
	y = np.array([int(line[:3].strip()) for line in sentiments])

	return x, y


def create_model():
	tfidf = TfidfVectorizer(stop_words='english', tokenizer=LemmaTokenizer())
	logint = LogisticRegression()
	pipeline = Pipeline([('vect', tfidf), ('clf', logint)])

	return pipeline


def exp73():
	x, y = get_sentiments()
	pipeline = create_model()

	# exercise 73
	return pipeline.fit(x, y)


def exp74(pipeline, test):
	print('= exercise 74 =')
	predictions = pipeline.predict_proba(test)
	for i, (neg, pos) in enumerate(predictions):
		if neg > pos:
			print("[-1] (p={0:.2f}) {1}".format(neg, test[i]))
		else:
			print('[+1] (p={0:.2f}) {1}'.format(pos, test[i]))


def exp75(pipeline):
	print('= exercise 75 =')
	features = pipeline.named_steps['vect'].get_feature_names()
	weights = pipeline.named_steps['clf'].coef_

	ranking = sorted(list(zip(features, weights[0])), key=lambda t: t[1])
	print('== Top 10 features ==')
	for best in reversed(ranking[-10:]):
		print(best[0].rjust(15), "{0: .3f}".format(best[1]), sep="\t")
	print('== Worst 10 features ==')
	for worst in ranking[:10]:
		print(worst[0].rjust(15), "{0:.3f}".format(worst[1]), sep="\t")
	print()
	abs_ranking = sorted(list(zip(features, weights[0])), key=lambda t: abs(t[1]))
	print('== Top 10 features (abs_val) ==')
	for best in reversed(abs_ranking[-10:]):
		print(best[0].rjust(15), "{0: .3f}".format(best[1]), sep="\t")
	print('== Worst 10 features (abs_val) ==')
	for worst in abs_ranking[:10]:
		print(worst[0].rjust(15), "{0: .3f}".format(worst[1]), sep="\t")


def exp76(pipeline):
	x, y = get_sentiments()
	y_pred = pipeline.predict_proba(x)
	with open("exp76_output.tsv", 'w') as output:
		for actual, (p_neg, p_pos) in zip(y, y_pred):
			if p_neg > p_pos:
				print(actual, "-1", "{0:.3f}".format(p_neg), sep='\t', file=output)
			else:
				print(actual, "1", "{0:.3f}".format(p_pos), sep='\t', file=output)


def main():
	learned_clf = exp73()
	test = ["that's too bad.", "wow, great!!", "this is a pen", "go read the book"]
	exp74(learned_clf, test)
	exp75(learned_clf)
	exp76(learned_clf)

if __name__ == '__main__':
	main()
