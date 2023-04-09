import torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import numpy as np


class DiabetesDataset(Dataset):
    def __init__(self, path):
        xy = np.loadtxt(path, delimiter=',', dtype=np.float32)
        self.x_data = torch.from_numpy(xy[:,:-1])
        self.y_data = torch.from_numpy(xy[:,[-1]])
        self.len = xy.shape[0]  # 多少个样本

    def __getitem__(self, index):  # 可以使用下标索引取数据
        return self.x_data[index], self.y_data[index]  # 返回元组
    
    def __len__(self): # 可以使用len函数
        return self.len

dataset = DiabetesDataset('H:/pylearning/第三阶段/diabetes.csv.gz')
train_loader = DataLoader(dataset=dataset, 
                          batch_size=32,
                          shuffle=True,
                          num_workers=2) # num_workers读一个mini-batch的样本时是否用多线程

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

if __name__=='__main__':
    for epoch in range(10):
        for i, data in enumerate(train_loader, 0):  # 0表示索引起点
            inputs, labels = data
            y_hat = model(inputs)
            loss = criterion(y_hat, labels)
            print(epoch, i, loss.item())

            optimizer.zero_grad()
            loss.backward()   # 算梯度
            optimizer.step()


# from torchvision import transforms
# from torchvision import datasets

# train_set = datasets.MNIST(root='H:/pylearning/第三阶段/dataset/mnist', train=True, transform=transforms.ToTensor(), download=True)
# test_set = datasets.MNIST(root='H:/pylearning/第三阶段/dataset/mnist', train=False, transform=transforms.ToTensor(), download=True)

# train_loader = DataLoader(dataset=train_set, batch_size=32, shuffle=True)
# test_loader = DataLoader(dataset=test_set, batch_size=32, shuffle=False)

# for i,(intputs, target) in enumerate(train_loader):
#     pass


