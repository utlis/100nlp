"""
77. 正解率の計測
76の出力を受け取り，予測の正解率，正例に関する適合率，再現率，F1スコアを求めるプログラムを作成せよ．
"""


def accuracy(pred_data):
	tp = len([pred for actual, pred, p in pred_data if actual == pred == 1])
	tn = len([pred for actual, pred, p in pred_data if actual == pred == -1])
	alles = len(pred_data)

	return 1.0 * (tp + tn) / alles


def precision_recall_f1measure(pred_data):
	tp = len([pred for actual, pred, p in pred_data if actual == pred == 1])
	fp = len([pred for actual, pred, p in pred_data if actual == -1 and pred == 1])
	fn = len([pred for actual, pred, p in pred_data if actual == 1 and pred == -1])

	P = 1.0 * tp / (tp + fp)
	R = 1.0 * tp / (tp + fn)
	F = 2 * P * R / (P + R)

	return P, R, F


def main():
	with open('exp76_output.tsv', 'r') as file:
		pred_data_str = [tuple(line.strip().split('\t')) for line in file.readlines()]
		pred_data = [(int(actual), int(pred), float(p)) for actual, pred, p in pred_data_str]

	acc = accuracy(pred_data)
	P, R, F = precision_recall_f1measure(pred_data)

	return acc, P, R, F

if __name__ == '__main__':
	acc, P, R, F = main()
	print('accuracy ='.rjust(15), "{0:.3f}".format(acc))
	print('precision ='.rjust(15), "{0:.3f}".format(P))
	print('recall ='.rjust(15), "{0:.3f}".format(R))
	print('F-measure ='.rjust(15), "{0:.3f}".format(F))
