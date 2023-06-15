import torch
from torch import nn


class NetSingleLayer(nn.Module):
    def __init__(self, in_shape: int = 300, out_shape: int = 4):
        super().__init__()
        self.fc = nn.Linear(in_shape, out_shape, bias=True)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        x = self.fc(x)
        x = self.softmax(x)
        return x


class NetThreeLayer(nn.Module):
    def __init__(self, in_shape: int = 300, out_shape: int = 4):
        super().__init__()
        self.fc1 = nn.Linear(in_shape, 150, bias=True)
        self.dropout1 = nn.Dropout(0.25)
        self.bn1 = nn.BatchNorm1d(150)
        self.fc2 = nn.Linear(150, 150, bias=True)
        self.dropout2 = nn.Dropout(0.25)
        self.bn2 = nn.BatchNorm1d(150)
        self.fc3 = nn.Linear(300, out_shape, bias=True)
        self.softmax = nn.Softmax(dim=1)
        self.relu = nn.ReLU()

    def forward(self, x):
        x1 = self.fc1(x)
        x1 = self.dropout1(x1)
        x1 = self.bn1(x1)
        x1 = self.relu(x1)

        x2 = self.fc2(x1)
        x2 = self.dropout2(x2)
        x2 = self.bn2(x2)
        x2 = self.relu(x2)
        x2 = torch.cat([x1, x2], dim=1)

        x3 = self.fc3(x2)
        x3 = self.softmax(x3)

        return x3
