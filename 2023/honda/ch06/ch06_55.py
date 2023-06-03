"""
55. Confusion matrix
Create the confusion matrix of the logistic regression model from the problem 52 for both the training data and the test data.
"""

import pandas as pd
import time
from sklearn.metrics import confusion_matrix
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
    
    confusion_matrix_train = confusion_matrix(y_train, y_train_predict)
    confusion_matrix_test = confusion_matrix(y_test, y_test_predict)
    labels = model.classes_
    
    print('confusion matrix for training data:', confusion_matrix_train, labels)
    print('confusion matrix for test data:', confusion_matrix_test, labels)

    end = time.perf_counter()
    processing_time = end - start
    print('time:', processing_time)
"""
confusion matrix for training data: [[4416   43    3   31]
 [  33 4193    0    6]
 [  84  115  514    4]
 [ 167   97    1  965]] ['b' 'e' 'm' 't']
confusion matrix for test data: [[535  14   0  15]
 [  4 512   0   1]
 [ 18  21  55   2]
 [ 31  19   1 106]] ['b' 'e' 'm' 't']
time: 46.901230459
"""