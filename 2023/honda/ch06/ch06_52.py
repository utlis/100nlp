"""
52. Training
Use the training data from the problem 51 and train the logistic regression model.
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
# from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import time

if __name__ == '__main__':
    start = time.perf_counter()
    time.sleep(5)

    X_train = pd.read_csv('train.feature.txt', sep = '\t', header = None)
    y_train = pd.read_csv('train.txt', sep = '\t')['CATEGORY']
    model = LogisticRegression(random_state = 1, max_iter = 1000)
    model.fit(X_train, y_train) # モデルを訓練データに適合

    with open('model.pkl', 'wb') as g:
        pickle.dump(model, g)
    end = time.perf_counter()
    processing_time = end - start
    print(processing_time) # 67.816453292