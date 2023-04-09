import torch


input = torch.tensor([[1, 2, 0, 3, 1],
                      [0, 1, 2, 3, 1],
                      [1, 2, 1, 0, 0],
                      [5, 2, 3, 1, 1],
                      [2, 1, 0, 1, 1]],dtype=torch.float32)

input = torch.reshape(input, (-1, 1, 5, 5))


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.maxpool1 = torch.nn.MaxPool2d(kernel_size=3, ceil_mode=False)  # ceil_mode为True或Fale，默认为False


    def forward(self, x):
        x = self.maxpool1(x)
        return x
    
model = Model()
output = model(input)
print(output.shape)
print(output)