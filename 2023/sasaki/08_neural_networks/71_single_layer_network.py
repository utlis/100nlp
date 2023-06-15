import pickle
import numpy as np
import pandas as pd
import torch
from torch import nn

train: pd.DataFrame = pickle.load(open("train.pickle", "rb"))

X_df = train["TITLE_VECTOR"]

# convert data_series of numpy._object to pure numpy matrix
X = []
for row in X_df:
    X.append(row.tolist())
X = np.array(X)

# input layer
# when requires_grad is True, tensor stores gradient
X = torch.tensor(X, dtype=torch.float, requires_grad=True)
# initialize weight at random
W = torch.randn(300, 4, dtype=torch.float)
# expect (10685, 300) * (300, 4) = (10685, 4)
print(X.shape, W.shape)
XW = torch.matmul(X, W)

# use softmax as activation function
# softmax function enable vector of output being considered as probability
activation_function = nn.Softmax(dim=1)
output = activation_function(XW)

y1 = output[0]
Y_hat = output[0:4]

print("print y1")
print(f"y1:  {y1}\n")

print("print Y_hat")
for y_n in Y_hat:
    print(y_n)

# sum of every element has to be 1 because of softmax function
print("check every vector represents a probability distribution")
print(torch.sum(output, 1))

# why is extension "pt"?
torch.save(output, "71.pt")
