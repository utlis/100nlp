import itertools
import pprint

#from collections import defaultdict
#from typing import Tuple

## 形態素解析ファイルの生成
# !mecab ./neko.txt -o ./neko.txt.mecab

## 30 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，
## 各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）を
## キーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．

# 最終結果が入るリストを定義.
sentences = []

# 1文中の形態素が格納されるリストを定義.
sentence = []

with open('./neko.txt.mecab') as f:
    lines = f.readlines()

# 1文を読み切るたびに結果に追加して、自身は初期化する.
    #sentence: list[dict] = []

    for line in lines:
        if line.strip() == 'EOS':
            if not sentence:
                continue 
            sentences.append(sentence)
            sentence = []
        else:
            surface, others = line.split('\t')
            elms = others.split(',')
            pos, pos1, base = elms[0], elms[1], elms[6]
            sentence.append({
                'surface': surface,
                'pos': pos,
                'pos1': pos1,
                'base': base,
             })
## 結果の確認
pprint.pprint(sentences[0:5])

## 31. 動詞
## 動詞の表層系をすべて抽出せよ
verbs = set()

for sentence in sentences:
    for dic in sentence:
        if dic['pos'] == '動詞':
            verbs.add(dic['surface'])
print(verbs)

### 別解 ### 
### '今回の場合文章毎に処理する必要がなく、全形態素について処理すればいいだけなので **itertools.chain** を使う'
### この関数は、型の異なる変数をつないでひとつのiteratorにすることができる
### '2重リストをフラットにして一度に処理してしまう、つまり、sentences = [{dic}, {dic}, ..]の形にならしてしまう  
### 動詞を判定する条件も簡単なのでジェネレータ式で簡単に書きます. ',
verb_surface_set = set(d['surface'] for d in itertools.chain(*sentences) if d['pos'] == '動詞')

## 32. 動詞の基本形
verb_base_set = set(d['base'] for d in itertools.chain(*sentences) if d['pos'] == '動詞')
print(verb_base_set)

## 33. 「AのB」
## 2つの名詞が「の」で連結されている名詞句を抽出せよ

