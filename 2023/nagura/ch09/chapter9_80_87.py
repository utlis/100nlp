import streamlit as st
import sys
import altair as alt

st.title('Chapter 9: RNN and CNN (80-87)')

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

#for 82
#import matplotlib.pyplot as plt

# for 84
from gensim.models import KeyedVectors
# others
import time

st.header('80. Turning words into numeric IDs')

TRAINING_NUM = 0

TRAINING_EPOCHS = 10

WORD_TO_VEC_DIM = 300

def preprocessing(text: str): # same function in problem 50
    text = text.lower()
    text = re.sub('[0-9]+', '', text)
    text = "".join([i for i in text if i not in string.punctuation])

    tokens = nltk.word_tokenize(text)
    stemmer = stem.PorterStemmer()
    stem_tokens = [stemmer.stem(token) for token in tokens]
    return " ".join(stem_tokens)

@st.cache_resource(max_entries=1)
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

titles = pd.read_csv('./train.txt', sep='\t', quoting=csv.QUOTE_NONE) # quotationを無視して読み込むオプション
titles = titles['title'][:10]
st.write('##### 5 titles')
st.write(titles)

titles = titles.apply(preprocessing)
st.write('##### 5 titles after converted to ID sequence')
titles_id = texts_to_id(titles)
st.write(titles_id)


st.header('81. Prediction with an RNN')

# firstly, get ids for each title
st.subheader('Conversion titles to onehot vectors')
@st.cache_resource(max_entries=1)
def get_data(training_num: int):
    ## load the data
    train = pd.read_csv('./train.txt', sep='\t', quoting=csv.QUOTE_NONE)
    if training_num:
        st.text(f'Training Data is currently loaded {training_num} lines for test')
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

st.text(f'types: words which appear more than 2 times are {id_count} types')

st.write('##### Train data and validation data converted to ids')
st.write('X_train:', X_train[0:3], 'y_train:', y_train[0:3])

# then, convert ids to one-hot vectors
@st.cache_resource(max_entries=1)
def get_onehots(training_num: int, id_count: int):
    max_len = max(list(map(len, X_train)) + list(map(len, X_valid))) ## ここでベクトルの長さを揃えなくてはいけない
    for ids in X_train:
        ids += [0 for _ in range(max_len - len(ids))]

    for ids in X_valid:
        ids += [0 for _ in range(max_len - len(ids))]

    X_train_onehot = tf.one_hot(X_train, depth=id_count)
    X_valid_onehot = tf.one_hot(X_valid, depth=id_count)
    return X_train_onehot, X_valid_onehot, max_len


X_train_onehot, X_valid_onehot, max_len = get_onehots(TRAINING_NUM, id_count)

st.write('##### Data converted to onehot vectors')
st.write('X_train_onehot' , X_train_onehot[0])
st.write('X_valid_onehot' , X_valid_onehot[0])

#@st.cache_resource(max_entries=1)
def get_model(dim, learning_rate=1e-3) -> keras.Model:
    model = keras.models.Sequential([
        keras.layers.SimpleRNN(32, input_shape=[None, dim]),
        keras.layers.Dense(4, activation="softmax"),
    ])
        # units(dimentionality of output space), input_shape(optional)
        # dimention of d_w = len(word_id_dic), d_n = 4
    model.summary()
    model.compile(loss='sparse_categorical_crossentropy',
              optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
              metrics=['accuracy']) # to save accuracy and loss
    return model

model = get_model(id_count)

st.subheader('Prediction before training')

res = model.predict(X_train_onehot[:3])
st.write(res)
st.write(y_train[:3])

st.header('82. Training with Stochastic Gradient Descent')
# training
start = time.time()

history = model.fit(
    X_train_onehot,
    np.array(y_train),
    epochs=TRAINING_EPOCHS,
    validation_data=(X_valid_onehot, np.array(y_valid)),
)

elapsed = time.time() -start

# output prediction
st.subheader('Prediction after training!')

res = model.predict(X_train_onehot[:3])
st.write(res)
st.write(y_train[:3])

st.text(f'training time: {elapsed: .4f} seconds!')

st.subheader('Loss and accuracy')
# plot accuracy rate and loss
## "Its History.history attribute is a record of training loss values and metrics values at successive epochs, as well as validation loss values and validation metrics values (if applicable)."

st.write('history.history:', history.history)

@st.cache_resource(max_entries=1)
def history_to_plot(histr):
    histr = pd.DataFrame(histr)
    histr.reset_index(inplace= True)
    histr = histr.rename(columns={'index': 'epoch'})
    histr = pd.melt(histr, id_vars = ['epoch'], value_vars=['loss', 'accuracy', 'val_loss', 'val_accuracy'])

    c = alt.Chart(histr).mark_line().encode( 
        x=alt.X("epoch:O"), y=alt.Y("value:Q"),
        color=('variable')
    ).properties(height=300)

    st.altair_chart(c, use_container_width=True)

history_to_plot(history.history)

st.subheader('Using sgd as optimizer')

model = keras.models.Sequential([
    keras.layers.SimpleRNN(32, input_shape=[None, id_count]),
    keras.layers.Dense(4, activation="softmax"),
])
model.compile(loss='sparse_categorical_crossentropy',
        optimizer="sgd",
        metrics=['accuracy'])

model = get_model(id_count)

# training
start = time.time()

history = model.fit(
    X_train_onehot,
    np.array(y_train),
    epochs=TRAINING_EPOCHS,
    validation_data=(X_valid_onehot, np.array(y_valid)),
)

elapsed = time.time() -start

res = model.predict(X_train_onehot[:3])
st.write(res)
st.write(y_train[:3])

st.text(f'training time: {elapsed: .4f} seconds!')

history_to_plot(history.history)


st.header('83. Mini-batch Training, GPU Training')

bsizes = [4,8,32,64]

for bsize in bsizes:
    start = time.time()

    model = get_model(id_count)
    history = model.fit(
        X_train_onehot,
        np.array(y_train),
        epochs=TRAINING_EPOCHS,
        validation_data=(X_valid_onehot, np.array(y_valid)),
        batch_size=bsize # update line in problem 83
    )

    elapsed = time.time() - start
    st.text(f'batch_size: {bsize}, training time: {elapsed: .4f} seconds!')
    history_to_plot(history.history)

st.header('84. Add Pretrained Word Embeddings')

st.subheader('Word embeddings')

# transform words to vectors
@st.cache_resource(max_entries=1)
def get_embd_model():
    emb_model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
    return emb_model

def transform_vec(text, embd_model, max_title):
    text = text.lower() #小文字化
    text = re.sub('[0-9]+', '', text) #数字変換
    words = "".join([i for i in text if i not in string.punctuation]).split() # 記号なくす
    # 語幹抽出すると次の行で0になってしまう場合があるのでしない
    # ここでタイトルの語数を合わせる
    words += ['thisisdummydummy' for _ in range(max_title - len(words))]
    # 'thisisdummydummy'または辞書にない単語は0ベクトルとする
    vec = [embd_model[word] if word in embd_model else np.zeros((WORD_TO_VEC_DIM,)) for word in words]
    return np.array(vec) #np.array型にする

@st.cache_resource(max_entries=1)
def get_new_data(training_num: int):
    ## load the data
    train = pd.read_csv('./train.txt', sep='\t', quoting=csv.QUOTE_NONE)
    if training_num:
        train = train[:training_num]
    X_train = train['title']

    embd_model = get_embd_model()

    valid = pd.read_csv('./valid.txt', sep='\t', quoting=csv.QUOTE_NONE) # validation data for problem 82
    X_valid = valid['title']

    category_dict = {'b': 0, 't': 1, 'e': 2, 'm': 3}
    y_train = train['category'].map(category_dict)
    y_valid = valid['category'].map(category_dict)

    ## get max length of title words (to give same dimensional inputs to model created later)
    max_title = max([len(title.split()) for title in X_train] + [len(title.split()) for title in X_valid])

    ## convert texts to vectors (update line from prblem 80-83!)
    X_train = [transform_vec(title, embd_model, max_title) for title in X_train]
    X_valid = [transform_vec(title, embd_model, max_title) for title in X_valid]

    return np.array(X_train), np.array(X_valid), y_train.tolist(), y_valid.tolist()

X_train, X_valid, y_train, y_valid = get_new_data(TRAINING_NUM)

st.write('X_train:', X_train[1])

st.subheader('Training')

new_model = get_model(WORD_TO_VEC_DIM)

# training
start = time.time()

history = new_model.fit(
    X_train,
    np.array(y_train),
    epochs=TRAINING_EPOCHS,
    validation_data=(X_valid, np.array(y_valid)),
    batch_size=32,
)

elapsed = time.time() -start
st.text(f'training time: {elapsed: .4f} seconds!')
history_to_plot(history.history)


st.header('85. Bi-directional RNN and Multi-layer RNN')

def get_bidirectional_rnn(dim) -> keras.Model:
    model = keras.models.Sequential([
        keras.layers.Bidirectional(keras.layers.SimpleRNN(32, return_sequences=True), input_shape=[None, dim]),
        keras.layers.Bidirectional(keras.layers.SimpleRNN(32)),
        keras.layers.Dense(4, activation="softmax"),
    ])
        # units(dimentionality of output space), input_shape(optional)
        # dimention of d_w = len(word_id_dic), d_n = 4
    model.summary()
    model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy']) # to save accuracy and loss
    return model

model = get_bidirectional_rnn(WORD_TO_VEC_DIM)

history = model.fit(
    X_train,
    np.array(y_train),
    epochs=TRAINING_EPOCHS,
    # steps_per_epoch=10, ここを設定すると、epoch = batch_size*steps_per_epochとなり、
    # よりaccuracyが上がっていくところがわかりやすいグラフがかける
    batch_size=32,
    validation_data=(X_valid, np.array(y_valid)),
    validation_batch_size=200,
)

history_to_plot(history.history)

st.header('86. Convolutional Neural Networks (CNN)')

def get_cnn(input_dim1, input_dim2) -> keras.Model:
    model = keras.models.Sequential([
        keras.layers.Conv1D(10,3,strides=1,padding="same",activation="relu",input_shape=[input_dim1, input_dim2]),
        keras.layers.MaxPooling1D(2),
        keras.layers.Flatten(),
        keras.layers.Dense(4, activation="softmax"),
    ])

    model.summary()

    model.compile(loss='sparse_categorical_crossentropy',
                optimizer='adam',
                metrics=['accuracy'])

    return model

model = get_cnn(max_len, id_count)

st.subheader('Prediction before training')

res = model.predict(X_train_onehot[:3])
st.write(res)
st.write(y_train[:3])

st.header('87. CNN Learning via Stochastic Gradient Descent')

start = time.time()
history = model.fit(
    X_train_onehot,
    np.array(y_train),
    epochs=TRAINING_EPOCHS,
    validation_data=(X_valid_onehot, np.array(y_valid)),
    validation_batch_size=200,
)
elapsed = time.time() -start

st.subheader('Prediction after training')

res = model.predict(X_train_onehot[:3])
st.write(res)
st.write(y_train[:3])
st.text(f'training time: {elapsed: .4f} seconds!')

history_to_plot(history.history)
