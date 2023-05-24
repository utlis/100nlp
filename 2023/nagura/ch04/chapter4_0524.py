import itertools
import streamlit as st
import pprint
import itertools
from collections import defaultdict
from typing import Tuple

import pandas as pd
import altair as alt
#from collections import defaultdict
#from typing import Tuple

## 形態素解析ファイルの生成
# !mecab ./neko.txt -o ./neko.txt.mecab

st.title('NLP100　第4章 形態素解析')


st.subheader('30. 形態素解析結果の読み込み')
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
## 結果の確認i
st.markdown('> 最初の1行を出力')
st.write(sentences[0])



st.subheader('31. 動詞')
## 動詞の表層系をすべて抽出せよ
verbs = set()
for sentence in sentences:
    for dic in sentence:
        if dic['pos'] == '動詞':
            verbs.add(dic['surface'])

st.markdown('> 最初の5つを出力')
st.write(list(verbs)[:5])
### 別解 ### 
### '今回の場合文章毎に処理する必要がなく、全形態素について処理すればいいだけなので **itertools.chain** を使う'
### この関数は、型の異なる変数をつないでひとつのiteratorにすることができる
### '2重リストをフラットにして一度に処理してしまう、つまり、sentences = [{dic}, {dic}, ..]の形にならしてしまう  
### 動詞を判定する条件も簡単なのでジェネレータ式で簡単に書きます. ',
verb_surface_set = set(d['surface'] for d in itertools.chain(*sentences) if d['pos'] == '動詞')


st.subheader('32. 動詞の基本形')
verb_base_set = set(d['base'] for d in itertools.chain(*sentences) if d['pos'] == '動詞')
st.markdown('> 最初の5つを出力')
st.write(list(verb_base_set)[:5])




st.subheader('33. 「AのB」')
## 2つの名詞が「の」で連結されている名詞句を抽出せよ
phrases = []
for sentence in sentences:
    for i in range(len(sentence)-2):
        if all([
            sentence[i]['pos'] == "名詞",
            sentence[i+1]['surface'] == "の",
            sentence[i+2]['pos'] == "名詞",
            ]):
            phrases.append(sentence[i]['surface'] + sentence[i+1]['surface'] + sentence[i+2]['surface'])

st.markdown('> 最初の5つを出力')
for phrase in phrases[:5]:
    st.write(phrase)



st.subheader('34. 名詞の連接')
# 最長の連接を与える形態素リスト
max_morphs = []

for sentence in sentences:
    # カウンタを用意
    i = 0
    # 一時的に形態素を保持するリスト
    morphs  = []

    while i < len(sentence):
        morph = sentence[i]
        if morph['pos'] == '名詞': #続いている名詞はmorphに入れておく
            morphs.append(morph['surface'])
            
        else:
            # 名詞が終わったら、暫定最長のものと比較して、max_morphを更新（または維持）
            if len(morphs) > len(max_morphs):
                max_morphs = morphs
            # morphsは初期化
            morphs = []                
        i += 1        
        
st.write("".join(max_morphs)) 



st.subheader('35. 単語の出現頻度')
# 辞書を用意。defaultdict(int)は、キーが存在しないときに、初期値を0にしてくれる
d = defaultdict(int) 

# itertools.chainでフラットにして 1重ループを回す
for morph in itertools.chain(*sentences):
    if morph['pos'] != '記号': # パンクチュエーションは入れない
        d[morph['base']] += 1

# 辞書を、出現単語と出現回数を示すタプルのリストに変換
touples = []
for k, v in d.items():
    touples.append((k,v))

occurrence = sorted(touples, key=lambda t: t[1], reverse=True)
st.markdown('出現回数上位5つを出力')
st.write(occurrence[:5])



st.subheader('36. 頻度上位10語')
#まず 上位10語だけのデータフレーム（df）をつくる
df = pd.DataFrame(occurrence[:10], columns = ['word', 'freq'])
st.markdown('> 上位10語はこれ')
st.dataframe(df)

#dfからグラフを出力
c = alt.Chart(df).mark_bar().encode(
        x=alt.X('word:N', sort='-y'), #=yにしないと昇順になる
        y=alt.Y('freq:Q'),
        )
st.markdown('> グラフは以下のとおり')
st.altair_chart(c)



st.subheader('37. 「猫」と共起頻度の高い10語')
# sentences = [sentence[morphs{}]] という構造。
# 文内に'猫'が出現していたら、その文内の語の出現頻度を+1したい。
# ただし、「猫」の出現頻度は特に問わない。

# まず、「猫」が出現している文のリストをつくる
neko_sentences: list[dict] = []
for sentence in sentences:
    for morph in sentence:
        if morph['surface']=='猫':
            neko_sentences.append(sentence)
# カウント用の辞書を用意（decaultdict）
neko_d = defaultdict(int)
for morph in itertools.chain(*neko_sentences):
    if morph['pos'] != '助詞' and morph['pos'] != '助動詞' and morph['pos'] != '記号' and morph['surface']!='猫':
        neko_d[morph['base']] += 1 

# 辞書を、出現単語と出現回数を示すタプルのリストに変換
neko_touples = []
for k, v in neko_d.items():
    neko_touples.append((k,v))

neko_co_occurrence = sorted(neko_touples, key=lambda t: t[1], reverse=True)

#上位10語だけのデータフレーム（df）をつくる
neko_co_df = pd.DataFrame(neko_co_occurrence[:10], columns = ['word', 'freq'])
st.markdown('> 「猫」と共起する（助詞、助動詞、記号を除く）上位10語は以下（何故かアスタリスクが入ってしまう）')
st.dataframe(neko_co_df)

#dfからグラフを出力
neko_c = alt.Chart(neko_co_df).mark_bar().encode(
        x=alt.X('word:N', sort='-y'), #=yにしないと昇順になる
        y=alt.Y('freq:Q'),
        )
st.markdown('> グラフは以下のとおり')
st.altair_chart(neko_c)




st.subheader('38. ヒストグラム')
st.markdown('> ヒストグラムは以下のとおり')
df = pd.DataFrame({
    '単語': [x[0] for x in occurrence], '出現頻度': [x[1] for x in occurrence],
})
st.write(df)
#ヒストグラム作成
hist = alt.Chart(df).mark_bar().encode(
        x=alt.X('出現頻度:Q',
            bin=alt.Bin(step=1, extent=[0, occurrence[0][1]]),
            ),
        y=alt.Y('count():Q',
            ),
        ).properties(height=500)
st.altair_chart(hist,  use_container_width=True)



st.subheader('39. Zipfの法則')
st.markdown('> 順位を伴うデータフレームは以下')
df_oc = pd.DataFrame({
    '単語': [x[0] for x in occurrence], '出現頻度': [x[1] for x in occurrence],
    '出現頻度順位': df['出現頻度'].rank(method='min',ascending=False)}
    )
st.write(df_oc)
# グラフ作成
zipf_c = alt.Chart(df_oc).mark_circle().encode(
        x=alt.X('出現頻度順位:Q',
            scale=alt.Scale(type="log"),
            ),
        y=alt.Y('出現頻度:Q',scale=alt.Scale(type="log")),
        )
st.markdown('> グラフは以下のとおり。')
st.altair_chart(zipf_c, use_container_width=True)
