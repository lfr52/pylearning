from torch import nn
import torch

class Modle(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input):
        return input + 1
    
model = Modle()
x = torch.tensor(1.0)
y = model(x)
print(y)
