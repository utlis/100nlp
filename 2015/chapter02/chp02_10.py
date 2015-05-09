# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

import sys


def line_counter(file):
	count = 0
	for line in file:
		count += 1
	return count


def main():
	f = open(sys.argv[1])
	print(line_counter(f))
	f.close()


if __name__ == '__main__':
	main()

# subprocess.popen()
