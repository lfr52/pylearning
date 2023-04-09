import torchvision
import torch
from torch.utils.data import DataLoader
# train_set = torchvision.datasets.ImageNet('data_imagenet',split='train', download=True, transform=torchvision.transforms.ToTensor())

dataset = torchvision.datasets.CIFAR10(root='dataset', train=False, transform=torchvision.transforms.ToTensor(), download=True)

dataloader = DataLoader(dataset, batch_size=64)

vgg16 = torchvision.models.vgg16(weights='VGG16_Weights.IMAGENET1K_V1')
vgg16_2 = torchvision.models.vgg16()

vgg16.classifier.add_module('add_linear',torch.nn.Linear(1000, 10)) # 增加网络层
vgg16_2.classifier[6] = torch.nn.Linear(4096, 10) # 修改原网络层


print(vgg16)

for data in dataloader:
    imgs, targets = data 
    output = vgg16(imgs)
    print(output.shape)