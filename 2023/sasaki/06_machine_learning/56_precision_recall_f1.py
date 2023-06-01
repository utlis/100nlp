"""
Compute the precision, recall and F1 score of the logistic regression model from the problem 52. 
First, compute these metrics for each category. 
Then summarize the score of each category using (1) micro-average and (2) macro-average.
https://nlp100.github.io/en/ch06.html#56-precision-recall-and-f1-score
"""

from typing import Any, Literal, Tuple
from sklearn.metrics import precision_score, recall_score, f1_score
import pandas as pd

import pickle
from sklearn.linear_model import LogisticRegression


Average = Literal['binary', 'micro', 'macro', 'samples', 'weighted', None]


def metrics(y_data, y_pred, average: Average = None) -> Tuple[Any, Any, Any]:
    precision = precision_score(y_data, y_pred, average=average)
    recall = recall_score(y_data, y_pred, average=average)
    f1 = f1_score(y_data, y_pred, average=average)
    return (precision, recall, f1)


def format_metrics(precision, recall, f1) -> str:
    return f"""precision: {precision}
recall: {recall}
f1: {f1}"""


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

print(
    f"each category({model.classes_})\n\n{format_metrics(*metrics(y_test, Y_test_pred))}\n")
print(
    f"micro-average\n{format_metrics(*metrics(y_test, Y_test_pred, 'macro'))}\n")
print(
    f"macro-average\n{format_metrics(*metrics(y_test, Y_test_pred, 'micro'))}\n")

# each category(['b' 'e' 'm' 't'])

# precision: [0.41233766 0.39347409 0.06349206 0.11940299]
# recall: [0.44797178 0.38461538 0.04597701 0.10884354]
# f1: [0.42941674 0.38899431 0.05333333 0.113879  ]

# micro-average
# precision: 0.24717669979902482
# recall: 0.24685192870742953
# f1: 0.24640584535036913

# macro-average
# precision: 0.35907046476761617
# recall: 0.35907046476761617
# f1: 0.3590704647676161
