

import torch
from torchvision import transforms
from torchvision import datasets
from torch.utils.data import Dataset
from torch.utils.data import DataLoader


batch_size = 64
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307, ),(0.3081, ))]) # 均值和标准差
test_dataset = datasets.MNIST(root='H:/pylearning/第三阶段/dataset/mnist', train=False, transform=transform, download=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)

print(test_dataset[0].size)