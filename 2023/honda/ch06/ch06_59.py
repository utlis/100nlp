"""
59. Hyper-parameter tuning
Use different training algorithms and parameters to train the model for the news classification. 
Search for the training algorithms and parameters that achieves the best accuracy score on the validation data. 
Then compute its accuracy score on the test data.
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import time
import matplotlib.pyplot as plt
# from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

def holdout_validation(X_train, y_train, X_valid, y_valid, X_test, y_test):
    solvers = ['newton-cg', 'sag', 'saga', 'lbfgs']
    C = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
    # penalry = ['None', 'l2']
    best_accuracy = 0
    best_parameters = {'solver': 'lbfgs' , 'C': 1} # default
    best_model = None
    for solver in solvers:
        for c in C:
            model = LogisticRegression(solver = solver, C = c, random_state = 1, max_iter = 1000)
            model.fit(X_train, y_train)
            y_predict = model.predict(X_valid)
            valid_accuracy = accuracy_score(y_valid, y_predict)
            print(f'solver: {solver}, C: {c}, accuracy score on validation data: {valid_accuracy}')
            if valid_accuracy > best_accuracy:
                best_accuracy = valid_accuracy
                best_parameters['solver'] = solver
                best_parameters['C'] = c
                best_model = model
    y_predict = best_model.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_predict)
    return f'Best parameters: {best_parameters}\tAccuracy score on validation data: {best_accuracy}\tAccuracy score on test data: {test_accuracy}'
    # return best_accuracy, best_parameters
    


if __name__ == '__main__':
    # start = time.perf_counter()
    # time.sleep(5)

    X_train = pd.read_csv('train.feature.txt', sep = '\t', header = None)
    y_train = pd.read_csv('train.txt', sep = '\t')['CATEGORY']
    X_valid = pd.read_csv('valid.feature.txt', sep = '\t', header = None)
    y_valid = pd.read_csv('valid.txt', sep = '\t')['CATEGORY']
    X_test = pd.read_csv('test.feature.txt', sep = '\t', header = None)
    y_test = pd.read_csv('test.txt', sep = '\t')['CATEGORY']

    holdout_validation(X_train, y_train, X_valid, y_valid, X_test, y_test)


    # end = time.perf_counter()
    # processing_time = end - start
    # print(processing_time) 

