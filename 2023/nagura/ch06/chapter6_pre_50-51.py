import string
import numpy as np
from dataclasses import dataclass
import nltk
nltk.download('punkt')
import sys
from nltk import stem
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# 50. データの入手・整形'

newscorpora: pd.DataFrame = pd.read_csv('./NewsAggregatorDataset/newsCorpora.csv', sep = '\t', header=None)
newscorpora.columns = ['id','title','url','publisher','category','story','hostname','timestamp']

# 特定の記事のみ抽出
news = newscorpora[newscorpora['publisher'].isin(['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail'])]

# シャッフルする
news = news.sample(frac=1, random_state=0)

print(news.head(5))
# 切り分ける
train, val_test = train_test_split(news, train_size=0.8)
val, test = train_test_split(val_test, test_size=0.5)

#保存する
train.to_csv('./train.txt', columns = ['category', 'title'], sep='\t', index=False) # 学習データ
val.to_csv('./valid.txt', columns = ['category', 'title'], sep='\t', index=False) # 検証データ
test.to_csv('./test.txt', columns = ['category', 'title'], sep='\t', index=False) # 評価データ


# データ数（カテゴリ（数））を確認する関数
def category_count(df):
    business_len = len(df[df['category'] == 'b'])
    science_len = len(df[df['category'] == 't'])
    entertainment_len = len(df[df['category'] == 'e'])
    health_len = len(df[df['category'] == 'm'])
    return print(f'business: {business_len}, science and technology: {science_len}, entertainment: {entertainment_len}, health: {health_len}')

# それぞれ出力
## 学習データ
train = pd.read_csv('./train.txt', sep='\t')
print(train.head(10))
#print(len(train[train['category']=='b']))
print('学習データ')
category_count(train)

## 検証データ
valid = pd.read_csv('./valid.txt', sep='\t')
print('検証データ')
category_count(valid)
## 評価データ
test = pd.read_csv('./test.txt', sep='\t')
print('評価データ')
category_count(test)


# 51. 特徴量抽出
## 前処理を行う関数
def preprocessing(text):
    text = text.lower() #小文字化
    text = re.sub('[0-9]+', '', text)
    text = "".join([i for i in text if i not in string.punctuation])

    tokens = nltk.word_tokenize(text)
    stemmer = stem.PorterStemmer()
    stem_tokens = [stemmer.stem(token) for token in tokens]
    return " ".join(stem_tokens)

train['title'] = train['title'].apply(preprocessing)
print(train['title'])
valid['title'] = valid['title'].apply(preprocessing)
test['title'] = test['title'].apply(preprocessing)

#train = pd.DataFrame(preprocessing(train['title']))


# 単語ベクトル化する
vec_tfidf = TfidfVectorizer()

vec_tfidf.fit(train['title'])

train_tfidf = vec_tfidf.transform(train['title'])
valid_tfidf = vec_tfidf.transform(valid['title'])
test_tfidf = vec_tfidf.transform(test['title'])

### ファイルを保存

train_tfidf = pd.DataFrame(train_tfidf.toarray(), columns = vec_tfidf.get_feature_names_out())
valid_tfidf = pd.DataFrame(valid_tfidf.toarray(), columns = vec_tfidf.get_feature_names_out())
test_tfidf = pd.DataFrame(test_tfidf.toarray(), columns = vec_tfidf.get_feature_names_out())

train_tfidf.to_csv('./train.feature.txt', sep='\t', index=False)
valid_tfidf.to_csv('./valid.feature.txt', sep='\t', index=False)
test_tfidf.to_csv('./test.feature.txt', sep='\t', index=False)

