import matplotlib.pyplot as plt
import torch
from torch.utils.data import Dataset


def make_graph(value_dict: dict, value_name: str, q_num: int) -> None:
    """value_dictに関するgraphを生成し、保存する。"""
    for phase in ["train", "valid"]:
        plt.plot(value_dict[phase], label=phase)
    plt.xlabel("epoch")
    plt.ylabel(value_name)
    plt.title(f"{value_name} per epoch")
    plt.legend()
    plt.savefig(f"{q_num}_{value_name}.png")
    plt.close()


def calc_acc(y_pred_prob, y_true) -> float:
    # get the highest probability
    _, y_pred = torch.max(y_pred_prob, 1)

    correct_num = (y_pred == y_true).sum()
    total_size = y_true.size(0)
    acc = (correct_num / total_size) * 100
    return acc


class TextDataset(Dataset):
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]
