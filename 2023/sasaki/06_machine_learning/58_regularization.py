"""
When training a logistic regression model, one can control the degree of overfitting by manipulating the regularization parameters. 
Use different regularization parameters to train the model. 
Then, compute the accuracy score on the training data, validation data and test data. 
Summarize the results on the graph, where x-axis is the regularization parameter and y-axis is the accuracy score.
https://nlp100.github.io/en/ch06.html#58-regularization
"""

import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Svg')

x_train = pd.read_csv("train.feature.txt", sep="\t")
train_data = pd.read_csv("train.txt", sep="\t",
                         quoting=False, names=["title", "category"])
y_train = train_data["category"]
x_valid = pd.read_csv("valid.feature.txt", sep="\t")
x_test = pd.read_csv("test.feature.txt", sep="\t")
test_data = pd.read_csv("test.txt", sep="\t",
                        quoting=False, names=["title", "category"])
y_test = test_data["category"]
valid_data = pd.read_csv("valid.txt", sep="\t",
                         quoting=False, names=["title", "category"])
y_valid = valid_data["category"]


def LR_pred(x_data, y_data, model: LogisticRegression):
    Y_pred_data = model.predict(x_data)
    accuracy = accuracy_score(Y_pred_data, y_data)
    return accuracy


train_accracies = []
valid_accracies = []
test_accracies = []


params = np.linspace(0.001, 0.1, 5)
for param in params:
    model_file_name = f"logstic_regression_param_{param}.model.pickle"

    model = LogisticRegression(C=param, max_iter=3000)

    try:
        print(f"try to load pre-trained model(param = {param})")
        rf = open(model_file_name,  "rb")
        model = pickle.load(rf)
        print("loading complete successfully")
    except Exception as e:
        print("loading failed", e)
        print(f"start: fitting model(param = {param})")
        model.fit(x_train, y_train)
        print("complete fitting")
        print("saving model")
        wf = open(model_file_name,  "wb")
        pickle.dump(model, wf)

    pre_train = LR_pred(x_train, y_train, model)
    pre_valid = LR_pred(x_valid, y_valid, model)
    pre_test = LR_pred(x_test, y_test, model)

    train_accracies.append(pre_train)
    valid_accracies.append(pre_valid)
    test_accracies.append(pre_test)

plt.plot(params, train_accracies, label="train", marker="o")
plt.plot(params, valid_accracies, label="valid", marker="o")
plt.plot(params, test_accracies, label="test", marker="o")

plt.legend()
plt.grid(True)
plt.xlabel("Regularization")
plt.ylabel("Accuracy")
plt.savefig("58_params.svg")
