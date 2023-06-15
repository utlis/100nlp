import load_tensor
import torch
from torch import nn
from utils import make_graph, calc_acc


train_X, train_Y = load_tensor.load_tensor("train")
valid_X, valid_Y = load_tensor.load_tensor("valid")

net = nn.Linear(300, 4)

loss = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(net.parameters(), lr=0.01)

train_losses = []
train_accs = []
valid_losses = []
valid_accs = []

for epoch in range(100):
    optimizer.zero_grad()

    # predicat train data
    train_y_pred_prob = net(train_X)

    # calc losses of train data
    train_loss = loss(train_y_pred_prob, train_Y)
    train_loss.backward()

    optimizer.step()

    # calc accuracy of train data
    train_acc = calc_acc(train_y_pred_prob, train_Y)

    # for validation data
    valid_y_pred_prob = net(valid_X)
    valid_loss = loss(valid_y_pred_prob, valid_Y)
    valid_acc = calc_acc(valid_y_pred_prob, valid_Y)

    # store result to plot
    train_accs.append(train_acc)
    train_losses.append(train_loss.data)
    valid_accs.append(valid_acc)
    valid_losses.append(valid_loss.data)


# plot graph
losses = {"train": train_losses, "valid": valid_losses}
accs = {"train": train_accs, "valid": valid_accs}

make_graph(losses, "losses", 75)
make_graph(accs, "accs", 75)
