# 07. テンプレートによる文生成
# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．

def weather(x, y, z):
	"""
	input: int(x=hour), str(y), float(z=value)
	output: "x時のyはz"
	"""
	print(str(x)+"時の"+str(y)+"は"+str(z))

# コマンドラインアプリ化する
# import sys
# sys.argv = [filename, 1, 2, 3]

from string import Template
s = Template('$x時の$yは$z')  # as usual, you have to diliminate keys by whitespace, but unicode works as well
s.substitute(x='12', y="気温", z='22.4')

# print "%d時の%sは%.1f" % (x, y, z)
