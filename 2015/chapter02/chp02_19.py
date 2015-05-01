"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
"""

import sys
import chp02_18 as p18


class Counter(dict):
	"""
	未定義のkeyに対して初期値0を返すdict
	RubyのHash.new(0)と同じ
	"""
	def __missing__(self, key):
		return 0


def freq_counter(lst):
	c = Counter()

	for i in lst:
		c[i] += 1

	return c



def main():
	with open(sys.argv[1], "r") as file:
		file_ary = p18.split_col2ary(file)
		print(freq_counter([line[0] for line in file_ary]))


if __name__ == '__main__':
	main()

# sort col1.txt | uniq -c | sort -n -r | less  > freq_ranking.txt
