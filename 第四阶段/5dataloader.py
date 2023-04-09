import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

test_set = torchvision.datasets.CIFAR10(root='dataset', train=False, transform=torchvision.transforms.ToTensor(), download=True)

test_loader = DataLoader(dataset=test_set, batch_size=64, shuffle=True, num_workers=0, drop_last=False)

img, target = test_set[0]
print(img.shape)
print(target)
step = 0
writer = SummaryWriter('logs_5')
for data in test_loader:
    imgs, targets = data
    # print(imgs.shape)
    # print(targets)
    writer.add_images('test_data', imgs, step)
    step += 1
    
writer.close()
