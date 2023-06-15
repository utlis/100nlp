import pandas as pd
import gensim
import numpy as np


# load data
inputs = {
    "train": "./train.txt",
    "valid": "./valid.txt",
    "test": "./test.txt",
}

dfs: dict[str, pd.DataFrame] = {}
name_list: list[str] = []
for k, v in inputs.items():
    dfs[k] = pd.read_csv(v, delimiter="\t",
                         quoting=False, names=["TITLE", "CATEGORY"])
    name_list.append(k)

for k in inputs.keys():
    print(k, "---", dfs[k].shape)
    print(dfs[k].head())

model = gensim.models.KeyedVectors.load_word2vec_format(
    "GoogleNews-vectors-negative300.bin.gz", binary=True)


# word splitting
for name in name_list:
    dfs[name]["TITLE_SPLIT"] = [
        text.split(" ") for text in dfs[name]["TITLE"].tolist()
    ]


def get_mean_vector(model, sentence: list):
    # remove out-of-vocabulary words
    words = [word for word in sentence if word in model.key_to_index]
    if len(words) >= 1:
        return np.mean(model[words], axis=0)
    else:
        print("warning: there is no words")
        print(sentence)
        return np.zeros(300)


# get features
for name in name_list:
    w_list = dfs[name]["TITLE_SPLIT"].tolist()
    dfs[name]["TITLE_VECTOR"] = [
        get_mean_vector(model, text) for text in w_list
    ]

# convert label into integer
label_dict = {"b": 0, "t": 1, "e": 2, "m": 3}
for name in name_list:
    dfs[name]["CATEGORY"] = dfs[name]["CATEGORY"].map(label_dict)

# store data
for name in name_list:
    print(dfs[name]["TITLE_VECTOR"].head())
    dfs[name][["TITLE_VECTOR", "CATEGORY"]].to_csv(f"{name}.csv")
    dfs[name][["TITLE_VECTOR", "CATEGORY"]].to_pickle(f"{name}.pickle")
