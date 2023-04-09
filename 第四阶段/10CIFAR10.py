import torch
from torch.utils.tensorboard import SummaryWriter
# class Model(torch.nn.Module):
#     def __init__(self) : 
#         super().__init__()
#         self.conv1 = torch.nn.Conv2d(3, 32, kernel_size=5, padding=2)
#         self.conv2 = torch.nn.Conv2d(32, 32, kernel_size=5, padding=2)
#         self.conv3 = torch.nn.Conv2d(32, 64, kernel_size=5, padding=2)
#         self.pooling = torch.nn.MaxPool2d(2)
#         self.flatten = torch.nn.Flatten()
#         self.linear1 = torch.nn.Linear(1024, 64) 
#         self.linear2 = torch.nn.Linear(64, 10) 
    
#     def forward(self, x):
#         x = self.conv1(x)
#         x = self.pooling(x)
#         x = self.conv2(x)
#         x = self.pooling(x)
#         x = self.conv3(x)
#         x = self.pooling(x)
#         x = self.flatten(x)
#         x = self.linear1(x)
#         x = self.linear2(x)
#         return x


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
    

input = torch.rand(64, 3, 32, 32)
model = Model()
output = model(input)
print(output.shape)


writer = SummaryWriter('logs_10')
writer.add_graph(model, input)
writer.close()
