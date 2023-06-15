import pickle
import numpy as np
import pandas as pd
import torch


def load_tensor(type: str):

    train: pd.DataFrame = pickle.load(open(f"{type}.pickle", "rb"))
    X_df = train["TITLE_VECTOR"]
    # convert data_series of numpy._object to pure numpy matrix
    X = []
    for row in X_df:
        X.append(row.tolist())
    X = np.array(X)
    X = torch.tensor(X, requires_grad=True).float()

    Y = torch.from_numpy(train["CATEGORY"].to_numpy())

    return X, Y
