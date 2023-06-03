"""
56. Precision, recall and F1 score
Compute the precision, recall and F1 score of the logistic regression model from the problem 52. 
First, compute these metrics for each category. 
Then summarize the score of each category using (1) micro-average and (2) macro-average.
"""

import pandas as pd
import time
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

import pickle

if __name__ == '__main__':
    start = time.perf_counter()
    time.sleep(5)
    with open('model.pkl', 'rb') as g:
        model = pickle.load(g)
    X_test = pd.read_csv('test.feature.txt', sep = '\t', header = None)
    y_test = pd.read_csv('test.txt', sep = '\t')['CATEGORY']
    
    y_predict = model.predict(X_test)
    
    precision = precision_score(y_test, y_predict, average = None)
    recall = recall_score(y_test, y_predict, average = None)
    f1score = f1_score(y_test, y_predict, average = None)
    
    micro_pre = precision_score(y_test, y_predict, average = 'micro')
    macro_pre = precision_score(y_test, y_predict, average = 'macro')
    micro_rec = recall_score(y_test, y_predict, average = 'micro')
    macro_rec = recall_score(y_test, y_predict, average = 'macro')
    micro_f1 = f1_score(y_test, y_predict, average = 'micro')
    macro_f1 = f1_score(y_test, y_predict, average = 'macro')
    
    print('precision:', precision)
    print('recall:', recall)
    print('f1 score:', f1score)
    print(f'micro-average:\tprecision: {micro_pre}\trecall: {micro_rec}\tf1 score: {micro_f1}')
    print(f'macro-average:\tprecision: {macro_pre}\trecall: {macro_rec}\tf1 score: {macro_f1}')

    end = time.perf_counter()
    processing_time = end - start
    print('time:', processing_time)
"""
precision: [0.90986395 0.90459364 0.98214286 0.85483871]
recall: [0.94858156 0.99032882 0.57291667 0.67515924]
f1 score: [0.92881944 0.9455217  0.72368421 0.7544484 ]
micro-average:	precision: 0.9055472263868066	recall: 0.9055472263868066	f1 score: 0.9055472263868066
macro-average:	precision: 0.9128597879936199	recall: 0.7967465706837996	f1 score: 0.8381184381328939
time: 9.754458875
"""