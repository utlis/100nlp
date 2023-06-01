"""
Compute the accuracy score of the logistic regression model from the problem 52 on both the training data and the test data.
https://nlp100.github.io/en/ch06.html#54-accuracy-score
"""

from sklearn.metrics import accuracy_score
import pandas as pd

import pickle
from sklearn.linear_model import LogisticRegression

train_data = pd.read_csv("train.txt", sep="\t",
                         quoting=False, names=["title", "category"])
y_train = train_data["category"]

test_data = pd.read_csv("test.txt", sep="\t",
                        quoting=False, names=["title", "category"])
y_test = test_data["category"]


rf = open("logstic_regression.model.pickle", "rb")
model: LogisticRegression = pickle.load(rf)


x_train = pd.read_csv("train.feature.txt", sep="\t")
Y_train_pred = model.predict(x_train)
x_test = pd.read_csv("test.feature.txt", sep="\t")
Y_test_pred = model.predict(x_test)

train_accuracy = accuracy_score(y_train, Y_train_pred)
test_accuracy = accuracy_score(y_test, Y_test_pred)

print(f"""train_accuracy: {train_accuracy}
test_accuracy: {test_accuracy}""")

# train_accuracy: 0.9390734674777725
# test_accuracy: 0.35907046476761617
