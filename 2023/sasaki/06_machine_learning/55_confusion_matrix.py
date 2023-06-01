"""
Create the confusion matrix of the logistic regression model from the problem 52 for both the training data and the test data.
https://nlp100.github.io/en/ch06.html#55-confusion-matrix
"""
from sklearn.metrics import confusion_matrix
import pandas as pd
import numpy as np

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

labels = np.unique(Y_train_pred)

train_confusion_matrix = confusion_matrix(y_train, Y_train_pred, labels=labels)
test_confusion_matrix = confusion_matrix(y_test, Y_test_pred, labels=labels)

print(f"label: {labels}")
print("training data")
print(train_confusion_matrix)
print("test data")
print(test_confusion_matrix)
