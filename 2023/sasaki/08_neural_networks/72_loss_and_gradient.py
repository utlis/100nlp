import torch
from torch import Tensor, nn
import load_tensor

Y_pred: Tensor = torch.load("71.pt")

_, Y = load_tensor.load_tensor("train")

# calculate loss
# "交差エントロピー誤差" in japanese
# the wider the gap between predication data and label is, the higher loss is
loss = nn.CrossEntropyLoss()
output: Tensor = loss(Y_pred[0:1], Y[0:1])

print(output)

# calculate gradient
# X is initialized with `required_grad = True`, so gradient of X is caluculated under the hood.
print(Y_pred.grad)
output.backward()
print(Y_pred.grad)

# tensor(1.4939, grad_fn=<NllLossBackward0>)
# None
# tensor([[-0.7755,  0.3138,  0.2592,  0.2025],
#         [ 0.0000,  0.0000,  0.0000,  0.0000],
#         [ 0.0000,  0.0000,  0.0000,  0.0000],
#         ...,
#         [ 0.0000,  0.0000,  0.0000,  0.0000],
#         [ 0.0000,  0.0000,  0.0000,  0.0000],
#         [ 0.0000,  0.0000,  0.0000,  0.0000]])

# execution for a set of samples x1,x2,x3,x4
print("\n\n---a set of samples x1,x2,x3,x4---")
Y_pred: Tensor = torch.load("71.pt")
output: Tensor = loss(Y_pred[0:4], Y[0:4])
print(output)
print(Y_pred.grad)
output.backward()
print(Y_pred.grad)

# tensor(1.3806, grad_fn=<NllLossBackward0>)
# None
# tensor([[-0.1939,  0.0784,  0.0648,  0.0506],
#         [ 0.0457, -0.1343,  0.0443,  0.0443],
#         [ 0.0463,  0.1128,  0.0458, -0.2050],
#         ...,
#         [ 0.0000,  0.0000,  0.0000,  0.0000],
#         [ 0.0000,  0.0000,  0.0000,  0.0000],
#         [ 0.0000,  0.0000,  0.0000,  0.0000]])
