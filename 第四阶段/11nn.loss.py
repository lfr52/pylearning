import torch
from torch.nn import L1Loss, MSELoss, CrossEntropyLoss

input = torch.tensor([1, 2, 3], dtype=torch.float32)
target = torch.tensor([2, 3, 5], dtype=torch.float32)

inputs = torch.reshape(input, (1, 1, 1, 3))
targets = torch.reshape(target, (1, 1, 1, 3))

loss = L1Loss(reduction='sum')
loss2 = MSELoss(reduction='mean')
result = loss(inputs, targets)
result2 = loss2(inputs, targets)

print(result)
print(result2)


x = torch.tensor([[0.1, 0.2, 0.3],
                  [0.2, 0.3, 0.2]])  # 2个样本为一个batch，算2个的loss和

y = torch.tensor([1, 2]) # 第一个样本target为1，第二个样本target为2
# x = torch.reshape(x, (1, 3))
loss3 = CrossEntropyLoss()
result3 = loss3(x, y)
print(result3)