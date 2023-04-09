import torchvision
import torch

# vgg16 = torchvision.models.vgg16()

# # 保存方法一
# torch.save(vgg16, 'model/vgg16_1.pth') # 保存模型和参数

# # 方法一加载模型
model = torch.load('model/vgg16_1.pth') # 要让模型访问到定义的方式
print(model)


# # 保存方式二
# torch.save(vgg16.state_dict(), 'model/vgg16_2.pth') # 保存模型参数

# 方法二加载模型
# model = torch.load('model/vgg16_2.pth') 
# print(model) # 打印出参数，但是无网络结构
# vgg16 = torchvision.models.vgg16()
# vgg16.load_state_dict(torch.load('model/vgg16_2.pth'))
# print(vgg16)


