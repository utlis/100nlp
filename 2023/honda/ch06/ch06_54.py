"""
54. Accuracy score
Compute the accuracy score of the logistic regression model from the problem 52 on both the training data and the test data.
"""

import pandas as pd
import time
from sklearn.metrics import accuracy_score
import pickle

if __name__ == '__main__':
    start = time.perf_counter()
    time.sleep(5)
    with open('model.pkl', 'rb') as g:
        model = pickle.load(g)
    X_train = pd.read_csv('train.feature.txt', sep = '\t', header = None)
    X_test = pd.read_csv('test.feature.txt', sep = '\t', header = None)
    y_train = pd.read_csv('train.txt', sep = '\t')['CATEGORY']
    y_test = pd.read_csv('test.txt', sep = '\t')['CATEGORY']
    
    y_train_predict = model.predict(X_train)
    y_test_predict = model.predict(X_test)
    
    accuracy_train = accuracy_score(y_train, y_train_predict)
    accuracy_test = accuracy_score(y_test, y_test_predict)
    
    print('accuracy score on training data:', accuracy_train)
    print('accuracy score on test data:', accuracy_test)

    end = time.perf_counter()
    processing_time = end - start
    print('time:', processing_time)

"""
accuracy score on training data: 0.9452773613193404
accuracy score on test data: 0.9055472263868066
time: 46.946219208
"""
