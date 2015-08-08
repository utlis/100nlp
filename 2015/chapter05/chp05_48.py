"""
48. 名詞から根へのパスの抽出
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ． ただし，構文木上のパスは以下の仕様を満たすものとする．

各文節は（表層形の）形態素列で表現する
パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

吾輩は -> 見た
ここで -> 始めて -> 人間という -> ものを -> 見た
人間という -> ものを -> 見た
ものを -> 見た
"""

import chp05_41 as p41


def extract_path2root(chunk, sentence):
	path = [chunk]
	dst = chunk.dst
	while dst != -1:
		path.append(sentence[dst])
		dst = sentence[dst].dst
	#else:
		#path.append(sentence[dst])

	return path


def main():
	path2roots = []

	sentences = p41.main()
	for sentence in sentences:
		for chunk in sentence:
			if chunk.include_pos('名詞') and chunk.dst != -1:
				path2roots.append(extract_path2root(chunk, sentence))

	return path2roots


if __name__ == '__main__':
	path2roots = main()
	for path2root in path2roots:
		print(" -> ".join([str(chunk) for chunk in path2root]))
