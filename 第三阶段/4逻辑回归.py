# 分类

import torchvision
import torch
import numpy as np
import matplotlib.pyplot as plt

# train_set = torchvision.datasets.MNIST(root='H:/pylearning/第三阶段/dataset/mnist', train=True, download=True)
# test_set = torchvision.datasets.MNIST(root='H:/pylearning/第三阶段/dataset/mnist', train=False, download=True)

x_data = torch.tensor([[1.0],[2.0],[3.0]]) 
y_data = torch.tensor([[0.0],[0.0],[1.0]])

class LogisticModel(torch.nn.Module):
    def __init__(self) : # 构造函数
        super().__init__()
        self.linear = torch.nn.Linear(1, 1) # 输入维度1，输出维度1
    
    def forward(self, x):
        y_hat = torch.sigmoid(self.linear(x))
        return y_hat
    
model = LogisticModel()

criterion = torch.nn.BCELoss(size_average=False)    # 交叉熵损失函数
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

for epoch in range(100):
    y_hat = model(x_data)  # 算y_hat
    loss = criterion(y_hat, y_data) # 算损失
    print(epoch, loss.item())  

    optimizer.zero_grad()
    loss.backward()   # 算梯度
    optimizer.step()  # 权重更新


x = np.linspace(0, 10, 200)
x_t = torch.FloatTensor(x).view((200,1))
y_t = model(x_t)
y = y_t.data.numpy()
plt.plot(x, y)
plt.plot([0, 10], [0.5, 0.5], c='r')
plt.xlabel('hours')
plt.ylabel('Probability of Pass')
plt.grid()
plt.show()
