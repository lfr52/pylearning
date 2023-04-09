
import torch
import torchvision
from torch.utils.data import DataLoader
from torch.nn import L1Loss, MSELoss, CrossEntropyLoss

dataset = torchvision.datasets.CIFAR10(root='dataset', train=False, transform=torchvision.transforms.ToTensor(), download=True)

dataloader = DataLoader(dataset, batch_size=64)

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
    

# input = torch.rand(64, 3, 32, 32)
model = Model()
# output = model(input)
# print(output.shape)

loss_func = CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoach in range(20):
    running_loss = 0.0
    for data in dataloader:
        imgs, targets = data 

        output = model(imgs)
        loss = loss_func(output, targets)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    print(running_loss)
