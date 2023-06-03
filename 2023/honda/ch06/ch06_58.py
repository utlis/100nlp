"""
58. Regularization
When training a logistic regression model, one can control the degree of overfitting by manipulating the regularization parameters. 
Use different regularization parameters to train the model. 
Then, compute the accuracy score on the training data, validation data and test data. 
Summarize the results on the graph, where x-axis is the regularization parameter and y-axis is the accuracy score.
"""
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import time
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

if __name__ == '__main__':
    # start = time.perf_counter()
    # time.sleep(5)
    # start = time.time()

    X_train = pd.read_csv('train.feature.txt', sep = '\t', header = None)
    y_train = pd.read_csv('train.txt', sep = '\t')['CATEGORY']
    X_valid = pd.read_csv('valid.feature.txt', sep = '\t', header = None)
    y_valid = pd.read_csv('valid.txt', sep = '\t')['CATEGORY']
    X_test = pd.read_csv('test.feature.txt', sep = '\t', header = None)
    y_test = pd.read_csv('test.txt', sep = '\t')['CATEGORY']

    parameters = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
    train_accuracies = []
    valid_accuracies = []
    test_accuracies = []
    for c in parameters:
        model = LogisticRegression(C = c, random_state = 1, max_iter = 1000)
        model.fit(X_train, y_train) 
        train_accuracies.append(accuracy_score(y_train, model.predict(X_train)))
        valid_accuracies.append(accuracy_score(y_valid, model.predict(X_valid)))
        test_accuracies.append(accuracy_score(y_test, model.predict(X_test)))
    
    print('accuracy score on training data:', train_accuracies)
    print('accuracy score on valid data:', valid_accuracies)
    print('accuracy score on test data:', test_accuracies)
    
    plt.plot(parameters, train_accuracies, label = 'training data')
    plt.plot(parameters, valid_accuracies, label = 'validation data')
    plt.plot(parameters, test_accuracies, label = 'test data')
    plt.xlabel('C: Inverse of regularization strength')
    plt.ylabel('Accuracy score')
    plt.xscale('log')
    plt.savefig('ch06_58.png')
    plt.legend()
    plt.show()
    

    # end = time.perf_counter()
    # end = time.time()
    # processing_time = end - start
    # print(processing_time, '[s]')
"""
accuracy score on training data: [0.4330022488755622, 0.7849512743628186, 0.8014430284857571, 0.9452773613193404, 0.99821964017991, 0.9994377811094453, 0.9994377811094453]
accuracy score on valid data: [0.43853073463268366, 0.7908545727136432, 0.7946026986506747, 0.9032983508245878, 0.9265367316341829, 0.9355322338830585, 0.9310344827586207]
accuracy score on test data: [0.43553223388305845, 0.7788605697151424, 0.7916041979010495, 0.9055472263868066, 0.9197901049475262, 0.9205397301349325, 0.9160419790104948]
"""