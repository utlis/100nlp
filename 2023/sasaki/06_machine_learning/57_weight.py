"""
Use the logistic regression model from the problem 52. 
Check the feature weights and list the 10 most important features and 10 least important features.
https://nlp100.github.io/en/ch06.html#57-feature-weights
"""

import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression

rf = open("logstic_regression.model.pickle", "rb")
model: LogisticRegression = pickle.load(rf)
x_train = pd.read_csv("train.feature.txt", sep="\t")

features = x_train.columns.values
for c, coef in zip(model.classes_, model.coef_):
    print(coef)
    top_10 = pd.DataFrame(features[np.argsort(-coef)[:10]], columns=[
                          f"top 10 feature (class: {c})"], index=[i for i in range(1, 11)])
    worst_10 = pd.DataFrame(features[np.argsort(coef)[:10]], columns=[
                            f"worst 10 feature (class： {c})"], index=[i for i in range(1, 11)])
    print(top_10, "\n"),
    print(worst_10, "\n")
    print("-"*50)

#    top 10 feature (class: b)
# 1                       euro
# 2                     stocks
# 3                       bank
# 4                        fed
# 5                        ecb
# 6                      china
# 7                     dollar
# 8                    billion
# 9                    ukraine
# 10                     forex

#    worst 10 feature (class： b)
# 1                          her
# 2                   kardashian
# 3                          she
# 4                         star
# 5                        ebola
# 6                        video
# 7                          kim
# 8                        miley
# 9                        chris
# 10                       cyrus
#  ----------------------------------------------------------------------
#    top 10 feature (class: e)
# 1                 kardashian
# 2                        kim
# 3                      chris
# 4                      miley
# 5                      cyrus
# 6                        her
# 7                        she
# 8                       star
# 9                       film
# 10                    justin

#    worst 10 feature (class： e)
# 1                        china
# 2                       google
# 3                         euro
# 4                      billion
# 5                     facebook
# 6                          ceo
# 7                         bank
# 8                        could
# 9                          fed
# 10                       apple
#  ----------------------------------------------------------------------
#    top 10 feature (class: m)
# 1                      ebola
# 2                      study
# 3                     cancer
# 4                        fda
# 5                       drug
# 6                       mers
# 7                      virus
# 8                      could
# 9                      heart
# 10                  outbreak

#    worst 10 feature (class： m)
# 1                   kardashian
# 2                         euro
# 3                          ceo
# 4                           gm
# 5                     facebook
# 6                         bank
# 7                        sales
# 8                         deal
# 9                          ecb
# 10                         kim
#  ----------------------------------------------------------------------
#    top 10 feature (class: t)
# 1                     google
# 2                   facebook
# 3                      apple
# 4                  microsoft
# 5                    climate
# 6                     mobile
# 7                      tesla
# 8                         gm
# 9                    samsung
# 10                      nasa

#    worst 10 feature (class： t)
# 1                       stocks
# 2                   kardashian
# 3                          fed
# 4                          her
# 5                          ecb
# 6                       shares
# 7                         euro
# 8                         york
# 9                     american
# 10                         kim
#  ----------------------------------------------------------------------
