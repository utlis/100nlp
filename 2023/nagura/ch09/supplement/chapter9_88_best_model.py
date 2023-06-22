import streamlit as st
import sys
import altair as alt

#for 80
import re
import string

#for 81
import nltk
from nltk import stem
import itertools
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

# for 88
from scipy.stats import reciprocal
from sklearn.model_selection import RandomizedSearchCV

from sklearn.model_selection import GridSearchCV


st.title('chapter9. CNN and RNN (88)')

TRAINING_NUM = 0

### data loading 

def preprocessing(text): # same function in problem 50
    text = text.lower()
    text = re.sub('[0-9]+', '', text)
    text = "".join([i for i in text if i not in string.punctuation])

    tokens = nltk.word_tokenize(text)
    stemmer = stem.PorterStemmer()
    stem_tokens = [stemmer.stem(token) for token in tokens]
    return " ".join(stem_tokens)

@st.cache_resource(max_entries=1)
def get_data(training_num: int):
    # load the data
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

    # convert texts to the sequence of ids
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

# then, convert ids to one-hot vectors
@st.cache_resource(max_entries=1)
def get_onehots(training_num: int, id_count: int):
    max_len = max(list(map(len, X_train)) + list(map(len, X_valid)))
    for ids in X_train:
        ids += [0 for _ in range(max_len - len(ids))]

    for ids in X_valid:
        ids += [0 for _ in range(max_len - len(ids))]

    X_train_onehot = tf.one_hot(X_train, depth=id_count)
    X_valid_onehot = tf.one_hot(X_valid, depth=id_count)
    return X_train_onehot, X_valid_onehot

X_train_onehot, X_valid_onehot = get_onehots(TRAINING_NUM, id_count)

@st.cache_resource(max_entries=1)
def history_to_plot(histr):
    histr = pd.DataFrame(histr)
    st.write(histr)
    histr.reset_index(inplace= True)
    histr = histr.rename(columns={'index': 'epoch'})
    histr = pd.melt(histr, id_vars = ['epoch'], value_vars=['loss', 'accuracy', 'val_loss', 'val_accuracy'])

    c = alt.Chart(histr).mark_line().encode( 
        x=alt.X("epoch:O"), y=alt.Y("value:Q"),
        color=('variable')
    ).properties(height=300)

    st.altair_chart(c, use_container_width=True)

st.header('88. Hyper-parameter Tuning')

## get max length of title words (to give same dimensional inputs to model created later)
max_len = max([len(words) for words in X_train] + [len(words) for words in X_valid])

## best model settings:
# arch = CNN-RNN comb ## 'Bi-RNN', 'CNN', 'CNN-RNN-comb'
n_hidden=2 #'n_hidden': list(range(1,5,1)),
n_neurons=30
activation='tanh' #'n_hidden': list(range(1,5,1)),
learning_rate=0.0010272025683152849 #'learning_rate': reciprocal(3e-4, 3e-2),
filter_num=20 #'filter_num': list(range(10,40,5)),
kernel_size=10 #'kernel_size': list(range(2,15,1)),
stride=1 #'stride': list(range(1,5,1)),
rnn_unit_size=60 #'rnn_unit_size': list(range(10,100,10)),
input_shape=[max_len, id_count]

model = keras.models.Sequential()
model.add(keras.layers.Conv1D(filter_num,kernel_size,strides=stride,padding='same',activation=activation,input_shape=input_shape))
model.add(keras.layers.MaxPooling1D(2))
model.add(keras.layers.Bidirectional(keras.layers.SimpleRNN(rnn_unit_size, return_sequences=True)))
model.add(keras.layers.Bidirectional(keras.layers.SimpleRNN(rnn_unit_size)))

for i in range(n_hidden):
    model.add(keras.layers.Dense(n_neurons, activation=activation))

model.add(keras.layers.Dense(4,activation="softmax"))

model.compile(loss='sparse_categorical_crossentropy',
              optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
              metrics=['accuracy']
              )

start = time.time()

history = model.fit(
    X_train_onehot,
    np.array(y_train),
    epochs=10,
    validation_data=(X_valid_onehot, np.array(y_valid)),
)

elapsed = time.time() -start

history_to_plot(history.history)

