
import time
import load_tensor

import torch
from torch import Tensor, nn
from torch.utils.data import DataLoader

from utils import TextDataset
from models import NetSingleLayer


# <-------------------- change from here
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

net = NetSingleLayer(in_shape=train_X.shape[1], out_shape=4).to(device)
# <---------------------

loss = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(net.parameters(), lr=0.01)

dataset = TextDataset(train_X, train_Y)

batchsizes = [1, 2, 4, 8, 16, 32, 64, 128]
for batchsize in batchsizes:
    loader = DataLoader(dataset, batch_size=batchsize, shuffle=True)

    for epoch in range(1):

        start = time.time()

        for dataloader_x, dataloader_y in loader:
            optimizer.zero_grad()

            dataloader_y_pred_prob = net(dataloader_x)

            dataloader_loss: Tensor = loss(
                dataloader_y_pred_prob, dataloader_y)
            dataloader_loss.backward()

            optimizer.step()

        calcuration_time = time.time() - start
        print(f"batchsize{batchsize} time:{calcuration_time: .2f}")

# interesting !!!
# batchsize1 time: 190.29
# batchsize2 time: 83.23
# batchsize4 time: 43.20
# batchsize8 time: 22.79
# batchsize16 time: 12.03
# batchsize32 time: 7.38
# batchsize64 time: 5.15
# batchsize128 time: 4.08

# use `watch nvidia-smi` to make sure that GPU is used
