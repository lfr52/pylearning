import torch
import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10(root='dataset', train=False, transform=torchvision.transforms.ToTensor(), download=True)

dataloader = DataLoader(dataset, batch_size=64)

writer = SummaryWriter('logs_8')
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 6, kernel_size=3)


    def forward(self, x):
        x = self.conv1(x)
        return x
    
model = Model()
print(model)
step = 0
for data in dataloader:
    img, target = data 
    output = model(img)
    writer.add_images('intput', img, step)
    output = torch.reshape(output, (-1, 3, 30, 30))
    writer.add_images('output', output, step)
    step += 1

writer.close()