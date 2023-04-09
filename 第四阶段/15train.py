import torchvision
import torch
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset_transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor()
])

train_data = torchvision.datasets.CIFAR10(root='dataset', train=True, transform=dataset_transform, download=True)
test_data = torchvision.datasets.CIFAR10(root='dataset', train=False, transform=dataset_transform, download=True)

train_data_len = len(train_data)
test_data_len = len(test_data)

print(f'训练数据集的长度为：{train_data_len}')
print(f'测试数据集的长度为：{test_data_len}')

train_loader = DataLoader(dataset=train_data, batch_size=64)
test_loader = DataLoader(dataset=test_data, batch_size=64)

class Model(torch.nn.Module):
    def __init__(self) : 
        super().__init__()
        self.model1 = torch.nn.Sequential(
            torch.nn.Conv2d(3, 32, kernel_size=5, padding=2),
            torch.nn.MaxPool2d(2),
            torch.nn.Conv2d(32, 32, kernel_size=5, padding=2),
            torch.nn.MaxPool2d(2),
            torch.nn.Conv2d(32, 64, kernel_size=5, padding=2),
            torch.nn.MaxPool2d(2),
            torch.nn.Flatten(),
            torch.nn.Linear(1024, 64),
            torch.nn.Linear(64, 10) 
        )
    
    def forward(self, x):
        x = self.model1(x)
        return x
    
model = Model()

learning_rate = 0.01 # 1e-2
loss_func = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

train_step = 0
test_step = 0
epoch =10

writer = SummaryWriter('logs_15')

for i in range(epoch):
    print(f'--------第{i+1}轮训练开始--------')
    model.train()  # 网络进入训练状态，只对dropout，BN层等有作用，非必须
    for data in train_loader:
        img, target = data
        output = model(img)
        loss = loss_func(output, target)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        train_step += 1
        if train_step % 100 == 0:
            print(f'训练次数：{train_step}, loss：{loss.item()}')
            writer.add_scalar('train_loss', loss.item(), train_step)

    model.eval() # 网络进入测试状态，只对dropout，BN层等有作用，非必须
    total_test_loss = 0
    total_accuracy = 0
    with torch.no_grad():
        for data in test_loader:
            img, target = data
            output = model(img)
            loss = loss_func(output, target)
            total_test_loss +=loss
            accuracy = (output.argmax(1) == target).sum()
            total_accuracy += accuracy
    print(f'整体测试集的loss：{total_test_loss}')
    print(f'整体测试集的正确率：{total_accuracy / test_data_len}')
    writer.add_scalar('test_loss', total_test_loss, test_step)
    writer.add_scalar('test_accurancy', total_accuracy / test_data_len, test_step)
    test_step += 1

    torch.save(model, f'model/net_{i}.pth')
    print('模型已保存')


