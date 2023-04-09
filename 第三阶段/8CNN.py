# import torch

# in_channels, out_channels = 5, 10
# width, height = 100, 100
# kernel_size = 3
# batch_size = 1

# input = torch.randn(batch_size, in_channels, width, height)

# conv_layer = torch.nn.Conv2d(in_channels, out_channels, kernel_size=kernel_size)

# output = conv_layer(input)

# print(input.shape)  # torch.Size([1, 5, 100, 100])
# print(output.shape) # torch.Size([1, 10, 98, 98])
# print(conv_layer.weight.shape) # torch.Size([10, 5, 3, 3])

import torch
from torchvision import transforms
from torchvision import datasets
from torch.utils.data import Dataset
from torch.utils.data import DataLoader


batch_size = 64
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307, ),(0.3081, ))]) # 均值和标准差

train_dataset = datasets.MNIST(root='H:/pylearning/第三阶段/dataset/mnist', train=True, transform=transform, download=True)
train_loader = DataLoader(dataset=train_dataset, batch_size=32, shuffle=True)


test_dataset = datasets.MNIST(root='H:/pylearning/第三阶段/dataset/mnist', train=False, transform=transform, download=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=32, shuffle=False)


class Model(torch.nn.Module):
    def __init__(self) : # 构造函数
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = torch.nn.Conv2d(10, 20, kernel_size=5)
        self.pooling = torch.nn.MaxPool2d(2)
        self.fc = torch.nn.Linear(320, 10) 
    
    def forward(self, x):
        x = self.pooling(torch.relu(self.conv1(x)))
        x = self.pooling(torch.relu(self.conv2(x)))
        x = x.view(-1, 320)
        x = self.fc(x)
        return x
    
model = Model()

criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1, momentum=0.5)

def train(epoch):
    running_loss = 0.0
    for batch_idx, data in enumerate(train_loader, 0):
        intputs, target = data
        y_hat = model(intputs)
        loss = criterion(y_hat, target)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        if batch_idx % 300 == 299:
            print('[%d, %5d] loss:%.3f' % (epoch + 1, batch_idx + 1, running_loss / 300))
            running_loss = 0.0

def test():
    correct = 0
    total = 0
    with torch.no_grad():
        for data in test_loader:
            images, labels = data
            y_hat = model(images)
            _, predict = torch.max(y_hat.data, dim=1)  # 按行取每一行最大的索引
            total +=labels.size(0)   # labels.size(0)应该等于batch_size
            correct += (predict == labels).sum().item() # 一批次正确的个数

    print('正确率（在测试集上）：%d %% [%d/%d]' % (100 * correct / total, correct, total))

if __name__=='__main__':
    for epoch in range(10):
        train(epoch)
        test()