"""
45. 動詞の格パターンの抽出

今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい． 動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ． ただし，出力は以下の仕様を満たすようにせよ．

動詞を含む文節において，最左の動詞の基本形を述語とする
述語に係る助詞を格とする
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

コーパス中で頻出する述語と格パターンの組み合わせ
「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
"""

import chp05_41 as p41


def exreact_verbcase_pat(sentence):
    """
    return list of (verb_chunk, src_chunks)
    src_chunks is list of chunk that contain '格助詞'
    """

    verbcase_pat = []

    for chunk in sentence:
        if chunk.include_pos('動詞'):
            src_chunks = [sentence[src] for src in chunk.srcs]
            src_chunks_case = list(filter(lambda src_chunk: src_chunk.morphs_of_pos1('格助詞'), src_chunks))
            if src_chunks_case:
                verbcase_pat.append((chunk, src_chunks_case))

    return verbcase_pat


def main():
    sentences = p41.main()
    verbcase_pats = []

    for sentence in sentences:
        verbcase_pats.append(exreact_verbcase_pat(sentence))

    return verbcase_pats

if __name__ == '__main__':
    verbcase_pats = main()
    for verbcase_pat in verbcase_pats:
        for verb, src_chunks in verbcase_pat:
            col1 = verb.morphs_of_pos('動詞')[-1].base
            cases = [src_chunk.morphs_of_pos1('格助詞')[-1].base for src_chunk in src_chunks]
            col2 = " ".join(sorted(cases))
            print(col1, col2, sep='\t')
