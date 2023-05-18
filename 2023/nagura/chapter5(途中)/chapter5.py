import streamlit as st
from dataclasses import dataclass
import re

'''
40. 係り受け解析結果の読み込み（形態素）

'''

## クラス定義
class Morph:
    def __init__(self, line):
        surface, others = line.split('\t')
        others = others.split(',')
        self.surface = surface
        self.pos = others[0]
        self.pos1 = others[1]
        self.base = others[6]

file_name = './ai.ja/ai.ja.txt.parsed'
morphs = []
sentences = []

## 読み込みと処理
with open(file_name, 'r') as f:
    lines = f.readlines()
    for line in lines:
        if line[0] == "*":
            continue
        elif line != 'EOS\n':
            morphs.append(Morph(line))
        else:
            sentences.append(morphs)
            morphs = []

## 確認（冒頭の文を出力）
# for morph in sentences[2]: 
#    st.write(vars(morph))

'''
41. 係り受け解析結果の読み込み（文節・係り受け）
'''

@dataclass
class Chunk:
    morphs: list[Morph] # __init__はinstanceをつくるときに呼ばれるメソッド
    dst: int
    srcs: list[int]

    @property
    def text(self) -> str: #文節の文字列を得る
        return ''.join([morph.surface for morph in morphs])

@dataclass
class Chunk_info:
    index: int
    chunk_info: Chunk

all_sentences = [] # list[list[Chunk[Morph]]]
sentence = [] # linst[Chunk]
morphs = [] # = morphs? list[Morph]

for line in lines[:5]:
    st.write(line)
    if line[0] =='*':
       # 文節番号<space>かかり先の文節番号<space>主辞/機能語の位置<space>係り関係のスコア
        for m in re.finditer(r'\* (\d) (\d)D +', line):
            index = int(m.group(1))
            dst = int(m.group(2))
            # 一旦、文節番号と文節の情報を持ったChunk_infoを1文へ追加する
            # （但しsrcsは後で計算するので空にしておく）
            sentence.append(Chunk_info(index=index, chunk_info=Chunk(morphs=morphs, dst=dst, srcs=[])))

        #'*'ごとにChunk（文節）が確定できるので文へ追加。一旦
        morphs = [] # morphsは初期化

    elif line == 'EOS\n':
        all_sentences.append(sentence) # 'EOS'が来たら1文が確定できるので、すべての文リストへ追加
        sentence = []

    elif line != 'EOS\n':
        morphs.append(Morph(line))

st.write(all_sentences[0])

