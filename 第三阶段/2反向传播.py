import torch

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = torch.Tensor([1.0])
w.requires_grad = True

print(w, type(w))
print(w.data, type(w.data))  # data也是一个tensor
print(w.item(), type(w.item()))

def forward(x):
    return x * w

def loss(x, y):
    y_hat = forward(x)
    return (y_hat - y) ** 2

print('perdict(before training):', 4, forward(4).item())

for epoch in range(100):
    for x, y in zip(x_data, y_data):
        l = loss(x, y) # 构建了计算图
        l.backward()  # 把所有导数算出来，释放计算图
        print('\tgrad:', x, y, w.item(), w.grad.item())  # item()得到一个标量
        w.data = w.data - 0.01 * w.grad.data
        w.grad.data.zero_() # 将梯度清零
    print('epoch:', epoch, 'loss', l.item())

print('perdict(after training):', 4, forward(4).item())

# 练习 y = w1*x^2 + w2*x + b
# 损失loss = (y_hat - y)^2
# w1 = torch.Tensor([0.5])
# w1.requires_grad = True

# w2 = torch.Tensor([1.0])
# w2.requires_grad = True

# b = torch.Tensor([0.5])
# b.requires_grad = True

# def forward(x):
#     return w1 * x * x + w2 * x + b

# def loss(x, y):
#     y_hat = forward(x)
#     return (y_hat - y) ** 2

# print('perdict(before training):', 4, forward(4).item())

# for epoch in range(300):
#     for x, y in zip(x_data, y_data):
#         l = loss(x, y) # 构建了计算图
#         l.backward()
#         # print('\tgrad:', x, y, w.item(), w.grad.item())  # item()得到一个标量
#         w1.data = w1.data - 0.01 * w1.grad.data
#         w2.data = w2.data - 0.01 * w2.grad.data
#         b.data = b.data - 0.01 * b.grad.data
#         w1.grad.data.zero_()
#         w2.grad.data.zero_()
#         b.grad.data.zero_()
#     print('epoch:', epoch, 'loss', l.item())
# print('w1:', w1.item(), 'w2:', w2.item(), 'b:', b.item())
# print('perdict(after training):', 4, forward(4).item())