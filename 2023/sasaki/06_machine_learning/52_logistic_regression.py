import pickle
from sklearn.linear_model import LogisticRegression
import pandas as pd

x_train = pd.read_csv("train.feature.txt", sep="\t")
train_data = pd.read_csv("train.txt", sep="\t",
                         quoting=False, names=["title", "category"])
y_train = train_data["category"]

print(f"x_train: {x_train.shape}")
print(f"y_train: {y_train.shape}")

# increase max_iter because "OP: TOTAL NO. of ITERATIONS REACHED LIMIT." warning is displayed
model = LogisticRegression(max_iter=3000)
model.fit(x_train, y_train)

wf = open("logstic_regression.model.pickle", "wb")
pickle.dump(model, wf)


# 13m5s
