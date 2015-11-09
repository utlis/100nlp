"""
78. 5分割交差検定
76-77の実験では，学習に用いた事例を評価にも用いたため，正当な評価とは言えない．すなわち，分類器が訓練事例を丸暗記する際の性能を評価しており，モデルの汎化性能を測定していない．そこで，5分割交差検定により，極性分類の正解率，適合率，再現率，F1スコアを求めよ
"""

import numpy as np
from sklearn.metrics import precision_recall_fscore_support, accuracy_score
from sklearn.cross_validation import KFold
import exp08_72to76 as ml


def kfolding(clf_generator, X, y):
	accuracies = []
	pscores = []
	rscores = []
	fscores = []

	cv = KFold(n=len(X), n_folds=5)
	for train, test in cv:
		X_train, y_train = X[train], y[train]
		X_test, y_test = X[test], y[test]

		clf = clf_generator()
		clf.fit(X_train, y_train)

		y_pred = clf.predict(X_test)
		A = accuracy_score(y_test, y_pred)
		P, R, F, _ = precision_recall_fscore_support(y_test, y_pred, average='binary')

		accuracies.append(A)
		pscores.append(P)
		rscores.append(R)
		fscores.append(F)

	return map(np.mean, [A, P, R, F])


def main():
	x, y = ml.get_sentiments()
	clf_generator = ml.create_model

	return kfolding(clf_generator, x, y)

if __name__ == '__main__':
	summary = main()
	label = ['accuracy', 'precision', 'recall', 'F-measure']
	for lbl, val in zip([(l+' =').rjust(15) for l in label], map("{0:.3f}".format, summary)):
		print(lbl, val)
