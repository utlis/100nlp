"""
Use different training algorithms and parameters to train the model for the news classification. 
Search for the training algorithms and parameters that achieves the best accuracy score on the validation data. 
Then compute its accuracy score on the test data.
https://nlp100.github.io/en/ch06.html#59-hyper-parameter-tuning
"""

import pickle
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
import pandas as pd

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

# this would be correct code, but executing this code failed, displaying "killed" after 40 min wait time.
# the reason can be a lack of memory.
params = {"solver": ['lbfgs', 'liblinear',
                     'newton-cg', 'newton-cholesky', 'sag', 'saga']}

# do grid search
gs_model = GridSearchCV(LogisticRegression(
    max_iter=1500), params, cv=5, verbose=1)
gs_model.fit(x_train, y_train)

best_gs_model = gs_model.best_estimator_

wf = open("best_logstic_regression_param_by_grid_search.pickle",  "wb")
pickle.dump(best_gs_model, wf)

print(best_gs_model.get_params())
print("\ntrain_score: {:.2%}".format(best_gs_model.score(x_train, y_train)))
print("valid_score: {:.2%}".format(best_gs_model.score(x_valid, y_valid)))
print("test_score: {:.2%}".format(best_gs_model.score(x_test, y_test)))
