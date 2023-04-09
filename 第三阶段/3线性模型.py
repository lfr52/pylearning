# 回归---预测
import torch


x_data = torch.tensor([[1.0],[2.0],[3.0]]) # 3行1列的矩阵
y_data = torch.tensor([[2.0],[4.0],[6.0]])

class LinearModel(torch.nn.Module):
    def __init__(self) : # 构造函数
        super().__init__()
        self.linear = torch.nn.Linear(1, 1) # 输入维度1，输出维度1
    
    def forward(self, x):
        y_hat = self.linear(x)
        return y_hat
    
model = LinearModel()  # 这里的model是可调用的 y_hat = model(x)  因为父类中有__call__方法，会调用forward

criterion = torch.nn.MSELoss(size_average=False) # 构建了一个criterion对象，需要参数(y_hat, y)    size_average=是否求均值
optimizer = torch.optim.SGD(model.parameters(), lr=0.01) # 构建一个优化器对象

for epoch in range(100):
    y_hat = model(x_data)  # 算y_hat
    loss = criterion(y_hat, y_data) # 算损失
    print(epoch, loss.item())  # loss对象在打印时会调用__str__方法，得到标量，不会产生计算图????

    optimizer.zero_grad()
    loss.backward()   # 算梯度
    optimizer.step()  # 权重更新
print("w=", model.linear.weight.item())
print("b=", model.linear.bias.item())

x_test = torch.tensor([[4.0],[5.0]]) # 预测4和5的值
y_test = model(x_test)
print("y的预测结果为",y_test.data)
