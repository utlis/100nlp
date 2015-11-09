"""
70. データの入手・整形
文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ．

rt-polarity.posの各行の先頭に"+1 "という文字列を追加する（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
rt-polarity.negの各行の先頭に"-1 "という文字列を追加する（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．
"""


import random

positives = []
negatives = []

with open('rt-polaritydata/rt-polaritydata/rt-polarity.pos', 'r') as pos:
	for line in pos:
		positives.append('+1 ' + line)

with open('rt-polaritydata/rt-polaritydata/rt-polarity.neg', 'r') as neg:
	for line in neg:
		negatives.append('-1 ' + line)

sentiment = positives + negatives
random.shuffle(sentiment)

print('pos: ', len(positives))
print('neg: ', len(negatives))

with open('sentiment.txt', 'w') as output:
	for line in sentiment:
		output.write(line)
