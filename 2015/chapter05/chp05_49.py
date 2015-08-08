"""
49. 名詞間の係り受けパスの抽出
文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．ただし，名詞句ペアの文節番号がiとj（i<j）のとき，係り受けパスは以下の仕様を満たすものとする．

問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を"->"で連結して表現する
文節iとjに含まれる名詞句はそれぞれ，XとYに置換する
また，係り受けパスの形状は，以下の2通りが考えられる．

文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示
上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合: 文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，文節kの内容を"|"で連結して表示
例えば，「吾輩はここで始めて人間というものを見た。」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

Xは | Yで -> 始めて -> 人間という -> ものを | 見た
Xは | Yという -> ものを | 見た
Xは | Yを | 見た
Xで -> 始めて -> Y
Xで -> 始めて -> 人間という -> Y
Xという -> Y
"""

from itertools import combinations
from collections import namedtuple
import chp05_41 as p41
#import chp05_48 as p48


def pos_replaced_strlist(chunks, pos, repl, k=1):
	replaced_str = ""

	for morph in chunks[0].morphs:
		if morph.pos == pos and k > 0:
			replaced_str += repl
			k -= 1
		else:
			if morph.pos != '記号':
				replaced_str += morph.surface

	return [replaced_str] + [str(chunk) for chunk in chunks[1:]]


def extract_path2root_index(i_chunk, sentence):
	i, chunk = i_chunk
	#print('   i:', i, 'chunk: ', chunk)
	path2root_index = [i]
	dst = chunk.dst

	while dst != -1:
		path2root_index.append(dst)
		dst = sentence[dst].dst

	return path2root_index


def main():
	N2N_paths = []
	N2Npath = namedtuple('N2Npath', ['X', 'Y', 'is_linear'])

	sentences = p41.main()
	for sentence in sentences:
		noun_chunks = [(i, chunk) for i, chunk in enumerate(sentence) if chunk.include_pos('名詞')]
		if len(noun_chunks) > 1:
			for former, latter in combinations(noun_chunks, 2):
				# combinations don't cause error even if len(noun_chunks) < 2
				f_index = extract_path2root_index(former, sentence)
				l_index = extract_path2root_index(latter, sentence)
				f_i, l_i = list(zip(reversed(f_index), reversed(l_index)))[-1]
				linear_flg = (f_i == l_i)
				if linear_flg:
					f_index2 = f_index[:f_index.index(f_i)+1]
					l_index2 = l_index[:l_index.index(l_i)+1]
				else:
					f_index2 = f_index[:f_index.index(f_i)+2]
					l_index2 = l_index[:l_index.index(l_i)+2]

				X = [sentence[k] for k in f_index2]
				Y = [sentence[k] for k in l_index2]
				N2N_paths.append(N2Npath(X=X, Y=Y, is_linear=linear_flg))

	return N2N_paths


if __name__ == '__main__':
	N2N_paths = main()

	for N2N_path in N2N_paths:
		x = pos_replaced_strlist(N2N_path.X, '名詞', 'X')
		y = pos_replaced_strlist(N2N_path.Y, '名詞', 'Y')
		if N2N_path.is_linear:
			#x[-1] = y[0]  # follow given output written in problem definition
			x[-1] = 'Y'
			print(" -> ".join(x))
		else:
			print(" -> ".join(x[:-1]), " -> ".join(y[:-1]), N2N_path.X[-1], sep=' | ')
