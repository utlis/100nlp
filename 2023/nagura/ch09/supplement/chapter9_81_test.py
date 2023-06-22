import sys

#for 80
import re
import string

#for 81
import nltk
from nltk import stem
import csv
import numpy as np
import tensorflow as tf
from tensorflow import keras
import pandas as pd

TRAINING_NUM = 500

TRAINING_EPOCHS = 5

WORD_TO_VEC_DIM = 300

def preprocessing(text: str): # same function in problem 50
    text = text.lower()
    text = re.sub('[0-9]+', '', text)
    text = "".join([i for i in text if i not in string.punctuation])

    tokens = nltk.word_tokenize(text)
    stemmer = stem.PorterStemmer()
    stem_tokens = [stemmer.stem(token) for token in tokens]
    return " ".join(stem_tokens)

def texts_to_id(texts: pd.Series):
    word_counter: dict[str, int] = {}
    for title in texts:
        for word in title.split():
            word_counter.setdefault(word, 0)
            word_counter[word] += 1
    map = {
        k: i + 1 for i, (k, v) in # 順番に取り出したとき、keyにはi+1を与える
        enumerate([
        (k, v) for (k, v) in # keyとvalueについて
        sorted([(k, v) for (k, v) in word_counter.items()], key=lambda x:x[1], reverse=True) # 出現頻度でsortされたkeyとvalueの中の
        if v >= 1
        ])
    }
    def mapper(title: str) -> list[int]:
        return[
            map.get(word, 0)
            for word in title.split()
        ]
    ids = texts.apply(mapper)
    return ids

def get_data(training_num: int):
    ## load the data
    train = pd.read_csv('./train.txt', sep='\t', quoting=csv.QUOTE_NONE)
    if training_num:
        print(f'Training Data is currently loaded {training_num} lines for test')
        train = train[:training_num]
    X_train = train['title']
    
    valid = pd.read_csv('./valid.txt', sep='\t', quoting=csv.QUOTE_NONE) 
    # validation data for problem 82
    X_valid = valid['title']

    category_dict = {'b': 0, 't': 1, 'e': 2, 'm': 3}
    y_train = train['category'].map(category_dict)
    y_valid = valid['category'].map(category_dict)

    ## convert texts to the sequence of ids
    X_train = X_train.apply(preprocessing)
    X_valid = X_valid.apply(preprocessing)

    ## use a part of texts_to_ids()
    word_counter: dict[str, int] = {}
    for title in X_train:
        for word in title.split():
            word_counter.setdefault(word, 0)
            word_counter[word] += 1

    map = {
        k: i + 1 for i, (k, v) in
        enumerate([
        (k, v) for (k, v) in
        sorted([(k, v) for (k, v) in word_counter.items()], key=lambda x : x[1])
        if v >= 1
        ])
    }
    def mapper(title: str) -> list[int]:
        return [
            map.get(word, 0)
            for word in title.split()
        ]
    X_train = X_train.apply(mapper)
    X_valid = X_valid.apply(mapper)

    return X_train.tolist(), X_valid.tolist(), y_train.tolist(), y_valid.tolist(), len(map) + 1

X_train, X_valid, y_train, y_valid, id_count = get_data(TRAINING_NUM)

### ここからテスト（上記コードは本体ファイルと一緒）
### RNNなので、理屈上は1つずつonehotベクトルを渡せば、1つ1つの長さが違っていても学習できる。

def get_onehots(id_count: int):
    X_train_onehot = []
    for id_sequence in X_train:
        one_hot_vector = tf.one_hot(id_sequence, depth=id_count)
        X_train_onehot.append(one_hot_vector)

    X_valid_onehot = []
    for id_sequence in X_valid:
        one_hot_vector = tf.one_hot(id_sequence, depth=id_count)
        X_valid_onehot.append(one_hot_vector)
    return X_train_onehot, X_valid_onehot

X_train_onehot, X_valid_onehot = get_onehots(id_count)

model = keras.models.Sequential([
    keras.layers.SimpleRNN(32, input_shape=[None, id_count]),
    keras.layers.Dense(4, activation="softmax"),
])

model.summary()
model.compile(loss='sparse_categorical_crossentropy',
          optimizer=keras.optimizers.Adam(learning_rate=1e-3),
          metrics=['accuracy']) # to save accuracy and loss

print(len(X_train_onehot), len(y_train))

for i, mini_batch in enumerate(X_train_onehot):
    model.train_on_batch(
        np.array([mini_batch]),
        np.array([y_train[i]]),
    )
