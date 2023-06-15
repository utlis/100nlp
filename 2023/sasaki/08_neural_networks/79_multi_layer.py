
import time
import load_tensor

import torch
from torch import nn
from torch.utils.data import DataLoader
from utils import make_graph

from utils import TextDataset, calc_acc
from models import NetThreeLayer

if torch.cuda.is_available():
    print("cuda is available!!")
else:
    print("No cuda")

device = (
    torch.device("cuda:0") if torch.cuda.is_available(
    ) else torch.device("cpu")
)

train_X, train_Y = load_tensor.load_tensor("train")
valid_X, valid_Y = load_tensor.load_tensor("valid")

train_X, train_Y, valid_X, valid_Y = train_X.to(device), train_Y.to(
    device), valid_X.to(device), valid_Y.to(device)

# setup multi layer model
net = NetThreeLayer(in_shape=train_X.shape[1], out_shape=4).to(device)

loss = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(net.parameters(), lr=0.01)

dataset = TextDataset(train_X, train_Y)

batchsize = 128
loader = DataLoader(dataset, batch_size=batchsize, shuffle=True)

train_losses = []
train_accs = []
valid_losses = []
valid_accs = []

for epoch in range(100):

    start = time.time()

    train_running_loss = 0.0
    valid_running_loss = 0.0

    for dataloader_x, dataloader_y in loader:

        optimizer.zero_grad()

        dataloader_y_pred_prob = net(dataloader_x)

        dataloader_loss = loss(dataloader_y_pred_prob, dataloader_y)
        dataloader_loss.backward()

        train_running_loss += dataloader_loss.item()
        valid_running_loss += loss(net(valid_X), valid_Y).item()

        optimizer.step()

    train_acc = calc_acc(net, train_X, train_Y)
    valid_acc = calc_acc(net, valid_X, valid_Y)

    train_accs.append(train_acc)
    train_losses.append(train_running_loss)
    valid_accs.append(valid_acc)
    valid_losses.append(valid_running_loss)

    if epoch % 20 == 0:
        torch.save(net.state_dict(),
                   f"79_net_bs{batchsize}_epoch{epoch}.pth")
        torch.save(
            optimizer.state_dict(),
            f"79_optimizer_bs{batchsize}_epoch{epoch}.pth",
        )

    calcuration_time = time.time() - start
    print(f"{epoch}: valid_acc={valid_acc} train_acc={train_acc} time={calcuration_time: .2f}")


losses = {"train": train_losses, "valid": valid_losses}
accs = {"train": train_accs, "valid": valid_accs}

make_graph(losses, "losses", 79)
make_graph(accs, "accs", 79)
