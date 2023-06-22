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

param_disribs = {
    'arch':['Bi-RNN','CNN', 'CNN-RNN-comb'], # biderectional Multi-layer RNN model, CNN, CNN とRNNの2つの組み合わせでどれが一番良いか
    #'arch':['Bi-GRU'], # biderectional Multi-layer RNN model, CNN, CNN とRNNの2つの組み合わせでどれが一番良いか
    'learning_rate': reciprocal(3e-4, 3e-2),
    'filter_num': list(range(10,40,5)),
    'kernel_size': list(range(2,15,1)),
    'stride': list(range(1,5,1)),
    'rnn_unit_size': list(range(10,100,10)),
    'n_hidden': list(range(1,5,1)),
    'activation': ['relu','tanh','sigmoid'],
}

def build_model(arch='Bi-RNN', 
                n_hidden=1, n_neurons=30, activation='relu', 
                input_shape=[max_len, id_count], optimizer="adam", learning_rate=1e-3,
                filter_num=10, kernel_size=2, stride=1,
                rnn_unit_size=10): # 初期値の設定
    print(f'arch: {arch}')
    print(f'n_hidden: {n_hidden}')
    print(f'activation: {activation}')
    print(f'optimizer: {optimizer}')
    print(f'learning_rate: {learning_rate}')
    print(f'filter_num: {filter_num}')
    print(f'kernel_size: {kernel_size}')
    print(f'stride: {stride}')
    print(f'rnn_unit_size: {rnn_unit_size}')

    model = keras.models.Sequential()
    if  arch == 'Bi-RNN':
        model.add(keras.layers.Bidirectional(keras.layers.SimpleRNN(rnn_unit_size, return_sequences=True), input_shape=input_shape))
        model.add(keras.layers.Bidirectional(keras.layers.SimpleRNN(rnn_unit_size)))
    elif arch == 'CNN':
        model.add(keras.layers.Conv1D(filter_num,kernel_size,strides=stride,padding='same',activation=activation,input_shape=input_shape))
        model.add(keras.layers.MaxPooling1D(2))
        model.add(keras.layers.Flatten())
    elif arch == 'CNN-RNN-comb': #in case of 'CNN-RNN-comb'
        model.add(keras.layers.Conv1D(filter_num,kernel_size,strides=stride,padding='same',activation=activation,input_shape=input_shape))
        model.add(keras.layers.MaxPooling1D(2))
        model.add(keras.layers.Bidirectional(keras.layers.SimpleRNN(rnn_unit_size, return_sequences=True)))
        model.add(keras.layers.Bidirectional(keras.layers.SimpleRNN(rnn_unit_size)))
    else:
        raise Exception(f'Undefined arch: {arch}')

    for i in range(n_hidden):
        model.add(keras.layers.Dense(n_neurons, activation=activation))
    model.add(keras.layers.Dense(4,activation="softmax"))
    
    if optimizer=='adam':
        optimizer_factory=keras.optimizers.Adam
    elif optimizer=='adagrad':
        optimizer_factory=keras.optimizers.Adagrad
    else:
        optimizer_factory=keras.optimizers.SGD

    model.compile(loss='sparse_categorical_crossentropy',
                  optimizer=optimizer_factory(learning_rate=learning_rate),
                  )
    return model

keras_reg = keras.wrappers.scikit_learn.KerasRegressor(build_model)

rand_search_cv = RandomizedSearchCV(keras_reg, param_disribs, return_train_score=True, n_iter=30, cv=2)
    # n_iter = The number of parameter settings that are tried 
    # cv = n fold cross-validation spilitting strategy

rand_search_cv.fit(np.array(X_train_onehot), np.array(y_train), epochs=5)
# epoch5, training data全部, n_iter 30-100くらい
# だいたい2040-

# scikit.learnはテンソル型を読み込めないのでデータをnp.arrayにして渡す

st.write(rand_search_cv.best_params_)


### もしGridSearchをするのなら..（以下はCNN modelの場合）
#param_grid = {
#    'optimizer': ['adam', 'adagrad'],
#    'n_hidden': [1,2,3],
#    # add parameters 
#}
#
#def build_cnn_model(n_hidden=1, n_neurons=30, input_shape=[max_len, id_count], optimizer="adam"):
#    model = keras.models.Sequential()
#    model.add(keras.layers.Conv1D(3,3,strides=1,padding='same',activation='relu',input_shape=input_shape))
#    model.add(keras.layers.MaxPooling1D(2))
#    model.add(keras.layers.Flatten())
#    for i in range(n_hidden):
#        model.add(keras.layers.Dense(n_neurons, activation='relu'))
#    model.add(keras.layers.Dense(4,activation="softmax"))
#    model.compile(loss='sparse_categorical_crossentropy',
#                  optimizer=optimizer,
#                  )
#    return model
#
#keras_reg = keras.wrappers.scikit_learn.KerasRegressor(build_cnn_model)
#
#keras_reg.fit(X_train_onehot, np.array(y_train), epochs=10,
#              validation_data=(X_valid_onehot, np.array(y_valid)),
#              validation_batch_size=200)
#
#grid_search = GridSearchCV(keras_reg, param_grid, return_train_score=True)
#grid_search.fit(np.array(X_train_onehot), np.array(y_train))
#
#st.write(grid_search.best_params_)

### grid searchをもし手で書くと...（CNN modelの場合）
#history_all = pd.DataFrame()
#for cnn_layer_num in [1,2]:
#    for dense_layer_num in [1]:
#        for dense_unit_num in [4]:
#            for filter_num in [10]:
#                for kernel_size in [3]:
#                    for stride in [1]:
#                        for l_rate in [0.01]:
#                            model = get_cnn(max_len, id_count, cnn_layer_num, dense_layer_num, dense_unit_num, filter_num, kernel_size, stride, l_rate)
#
#                            history = model.fit(
#                                X_train_onehot,
#                                np.array(y_train),
#                                epochs=TRAINING_EPOCHS, 
#                                batch_size=32,
#                                validation_data=(X_valid_onehot, np.array(y_valid)),
#                                validation_batch_size=200,
#                            )
#                            ## save accuracy rates of each models
#                            model_name = 'model_CNN' + str(cnn_layer_num) + str(filter_num) + str(kernel_size) + str(stride) + '_Dense' + str(dense_layer_num) + '_' + str(dense_unit_num) + '_' + str(filter_num) + '_rate' + str(l_rate)
#                            history = pd.DataFrame(history.history)
#                            st.write(history)
#                            history.loc[:, 'model'] = model_name
#                            history.index = np.arange(1, len(history)+1)
#                            history.reset_index(inplace= True)
#                            history = history.rename(columns={'index': 'epoch'})
#                            history_all = pd.concat([history, history_all])
#
#c1 = alt.Chart(history_all).mark_line().encode(
#    x=alt.X("epoch:O"), y=alt.Y("accuracy:Q"),
#    color=('model')
#).properties(height=300)
#
#c2 = alt.Chart(history_all).mark_line().encode(
#    x=alt.X("epoch:O"), y=alt.Y("val_accuracy:Q"),
#    color=('model')
#).properties(height=300)
#st.altair_chart(c1, use_container_width=True)
#st.altair_chart(c2, use_container_width=True)
#

