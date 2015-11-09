"""
79. 適合率-再現率グラフの描画
ロジスティック回帰モデルの分類の閾値を変化させることで，適合率-再現率グラフを描画せよ
"""

#import numpy as np
from sklearn.metrics import precision_recall_curve
from sklearn.cross_validation import KFold
import exp08_72to76 as ml

import matplotlib.pyplot as plt


def kfolding(clf_generator, X, y):
	precisions = []
	recalls = []

	cv = KFold(n=len(X), n_folds=5)
	for train, test in cv:
		X_train, y_train = X[train], y[train]
		X_test, y_test = X[test], y[test]

		clf = clf_generator()
		clf.fit(X_train, y_train)

		y_pred_p = clf.predict_proba(X_test)
		# choose probabilty values of label=1
		P, R, thresholds = precision_recall_curve(y_test, y_pred_p[:, 1])
		precisions.append(P)
		recalls.append(R)

	return precisions, recalls


def plot_pr(precisions, recalls):
	plt.clf()
	plt.figure(num=None, figsize=(5, 5))
	plt.grid(True)
	for p, r in zip(precisions, recalls):
		plt.plot(r, p)
	plt.xlim([0.0, 1.0])
	plt.ylim([0.0, 1.0])
	plt.xlabel('Recall')
	plt.ylabel('Precision')
	plt.title('P/R curve')
	plt.savefig("PRcurve_exp08_79.png")


def main():
	x, y = ml.get_sentiments()
	clf_generator = ml.create_model

	precisions, recalls = kfolding(clf_generator, x, y)
	plot_pr(precisions, recalls)

if __name__ == '__main__':
	main()
