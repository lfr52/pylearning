import torch
from torchvision import transforms
from torchvision import datasets
from torch.utils.data import Dataset
from torch.utils.data import DataLoader

class ResidualBlock(torch.nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.channels = channels
        self.conv1 = torch.nn.Conv2d(channels, channels, kernel_size=3, padding=1)
        self.conv2 = torch.nn.Conv2d(channels, channels, kernel_size=3, padding=1)


    def forward(self, x):
        y = torch.relu(self.conv1(x))
        y = self.conv2(y)
        return x + y
    
class Model(torch.nn.Module):
    def __init__(self) : # 构造函数
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 16, kernel_size=5)
        self.conv2 = torch.nn.Conv2d(16, 32, kernel_size=5)
        self.pooling = torch.nn.MaxPool2d(2)
        self.fc = torch.nn.Linear(512, 10) 
        self.rblock1 = ResidualBlock(16)
        self.rblock2 = ResidualBlock(32)
    
    def forward(self, x):
        x = self.pooling(torch.relu(self.conv1(x)))
        x = self.rblock1(x)
        x = self.pooling(torch.relu(self.conv2(x)))
        x = self.rblock2(x)
        x = x.view(-1, 512)
        x = self.fc(x)
        return x

model = Model()
    


batch_size = 64
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307, ),(0.3081, ))]) # 均值和标准差

train_dataset = datasets.MNIST(root='H:/pylearning/第三阶段/dataset/mnist', train=True, transform=transform, download=True)
train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)


test_dataset = datasets.MNIST(root='H:/pylearning/第三阶段/dataset/mnist', train=False, transform=transform, download=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)


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