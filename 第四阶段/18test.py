
from PIL import Image
import torchvision
import torch

image = Image.open('dog.png')
transform = torchvision.transforms.Compose([torchvision.transforms.Resize((32, 32)),
                                            torchvision.transforms.ToTensor()])
image = transform(image)

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
    
model = torch.load('model/net_9.pth')
print(model)

image = torch.reshape(image, (1, 3, 32, 32))
model.eval()
with torch.no_grad():
    output = model(image)
print(output)

print(output.argmax(1))