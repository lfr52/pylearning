import torch
import numpy as np


xy = np.loadtxt('H:/pylearning/第三阶段/diabetes.csv.gz', delimiter=',', dtype=np.float32)
x_data = torch.from_numpy(xy[:,:-1])
y_data = torch.from_numpy(xy[:,[-1]])


class Model(torch.nn.Module):
    def __init__(self) : # 构造函数
        super().__init__()
        self.linear1 = torch.nn.Linear(8, 6) # 输入维度8，输出维度6
        self.linear2 = torch.nn.Linear(6, 4) # 输入维度6，输出维度4
        self.linear3 = torch.nn.Linear(4, 1) # 输入维度4，输出维度1
    
    def forward(self, x):
        x = torch.relu(self.linear1(x))
        x = torch.relu(self.linear2(x))
        x = torch.sigmoid(self.linear3(x))
        return x
    
model = Model()


criterion = torch.nn.BCELoss(size_average=True)    # 交叉熵损失函数
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

for epoch in range(100):
    y_hat = model(x_data)  # 算y_hat
    loss = criterion(y_hat, y_data) # 算损失
    print(epoch, loss.item())  

    optimizer.zero_grad()
    loss.backward()   # 算梯度
    optimizer.step()  # 权重更新
