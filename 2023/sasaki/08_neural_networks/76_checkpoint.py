import torch
from torch import nn
import load_tensor
from utils import calc_acc


train_X, train_Y = load_tensor.load_tensor("train")
valid_X, valid_Y = load_tensor.load_tensor("valid")

net = nn.Linear(300, 4)

loss = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(net.parameters(), lr=0.01)


for epoch in range(100):
    optimizer.zero_grad()

    train_y_pred_prob = net(train_X)
    train_loss = loss(train_y_pred_prob, train_Y)
    train_acc = calc_acc(train_y_pred_prob, train_Y)

    train_loss.backward()
    optimizer.step()

    valid_y_pred_prob = net(valid_X)
    valid_loss = loss(valid_y_pred_prob, valid_Y)
    valid_acc = calc_acc(valid_y_pred_prob, valid_Y)

    # generate check point per 20 epoch
    if epoch % 20 == 0:
        torch.save(net.state_dict(), f"76_net_epoch{epoch}.pth")
        torch.save(optimizer.state_dict(), f"76_optimizer_epoch{epoch}.pth")
