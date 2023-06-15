from load_tensor import load_tensor
import torch
from torch import Tensor, nn


X, Y = load_tensor("train")

net = nn.Linear(300, 4)

loss = nn.CrossEntropyLoss()
# SGD is abbreviation for stochastic gradient descent
# "確率的勾配降下法" in Japanese
# set `net` parameter as target of optimization
# lr is learning rate, which defines how much parameters are changed every epoch.
optimizer = torch.optim.SGD(net.parameters(), lr=0.01)

print("Before")
print(net.state_dict()["weight"])

for step in range(100):
    # reset gradient!!
    optimizer.zero_grad()

    y_pred = net(X)

    output: Tensor = loss(y_pred, Y)
    # update gradient!!
    output.backward()

    optimizer.step()

print("After")
print(net.state_dict()["weight"])

# why is extension "pth"?
net_path = "73_net.pth"
torch.save(net.state_dict(), net_path)

# Before
# tensor([[-0.0309, -0.0159, -0.0039,  ..., -0.0071, -0.0046,  0.0029],
#         [-0.0502,  0.0474, -0.0059,  ..., -0.0419,  0.0168,  0.0297],
#         [ 0.0309, -0.0499,  0.0456,  ..., -0.0415, -0.0438, -0.0336],
#         [ 0.0485,  0.0347,  0.0576,  ...,  0.0218, -0.0058,  0.0231]])
# After
# tensor([[-3.3098e-02, -1.2206e-02, -6.2726e-03,  ...,  1.5130e-03,
#           6.1263e-03, -9.4518e-03],
#         [-5.2476e-02,  4.4215e-02, -2.3165e-05,  ..., -4.1397e-02,
#           8.8872e-03,  3.1525e-02],
#         [ 4.0749e-02, -4.6130e-02,  3.5520e-02,  ..., -5.2531e-02,
#          -4.0746e-02, -2.8182e-02],
#         [ 4.3154e-02,  3.0397e-02,  6.4158e-02,  ...,  2.3707e-02,
#          -1.1692e-02,  2.8281e-02]])
