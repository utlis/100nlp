"""
Use the logistic regression model from the problem 52. 
Create a program that predicts the category of a given news headline and computes the prediction probability of the model.
https://nlp100.github.io/en/ch06.html#53-prediction
"""

import pickle
from sklearn.linear_model import LogisticRegression
import pandas as pd


rf = open("logstic_regression.model.pickle", "rb")
model: LogisticRegression = pickle.load(rf)

x_valid = pd.read_csv("valid.feature.txt", sep="\t")
Y_pred = model.predict(x_valid)

valid_data = pd.read_csv("valid.txt", sep="\t",
                         quoting=False, names=["title", "category"])
y_valid = valid_data["category"]

for i in range(len(Y_pred)):
    print(f"{Y_pred[i]}, {y_valid[i]}")
