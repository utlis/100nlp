"""
47. 機能動詞構文のマイニング

動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．

「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，以下の出力が得られるはずである．

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

コーパス中で頻出する述語（サ変接続名詞+を+動詞）
コーパス中で頻出する述語と助詞パターン
"""

import chp05_45 as p45


def extract_sahen_chunk(src_chunks):
    for i, src_chunk in enumerate(src_chunks):
        morphs = src_chunk.morphs
        if len(morphs) > 1:
            if morphs[-2].pos1 == 'サ変接続' and morphs[-1].pos == '助詞' and morphs[-1].base == 'を':
                # find multiple sahen noun
                src_chunks.pop(i)

                # only return first sahen
                return src_chunk, src_chunks

    return None


if __name__ == '__main__':
    verbcase_pats = p45.main()
    for verbcase_pat in verbcase_pats:
        for verb, src_chunks in verbcase_pat:
            sahen_chunk_set = extract_sahen_chunk(src_chunks)
            if sahen_chunk_set:
                sahen_chunk, other_chunks = sahen_chunk_set
                col1 = str(sahen_chunk) + verb.morphs_of_pos('動詞')[-1].base
                col2_3 = [(other_chunk.morphs_of_pos1('格助詞')[-1].base, str(other_chunk)) for other_chunk in other_chunks]
                sorted_col2_3 = sorted(col2_3, key=lambda x: x[0])
                col2 = " ".join([i[0] for i in sorted_col2_3])
                col3 = " ".join([i[1] for i in sorted_col2_3])
                print(col1, col2, col3, sep='\t')
