import random


x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = 1.0

# def forward(x):
#     return w * x

# def cost(x_set, y_set):
#     cost = 0
#     for x, y in zip(x_set, y_set):
#         y_hat = forward(x)
#         cost += (y_hat - y) ** 2
#     return cost / len(x_set)

# def grad(x_set, y_set):
#     grad = 0
#     for x, y in zip(x_set, y_set):
#         grad += 2 * x * (forward(x) - y)
#     return grad / len(x_set)

# for epoch in range(100):
#     cost_val = cost(x_data, y_data)
#     grad_val = grad(x_data, y_data)
#     w -= 0.01 * grad_val
#     print("epoch:%d, w=%.4f, loss=%.4f" %(epoch, w, cost_val))


# 随机梯度下降
def forward(x):
    return w * x

def loss(x, y):
    y_hat = forward(x)
    loss = (y_hat - y) ** 2
    return loss

def gradient(x, y):
    grad = 2 * x * (forward(x) - y)
    return grad

for epoch in range(100):
    r = random.randrange(0, 3)
    x = x_data[r]
    y = y_data[r]
    grad = gradient(x, y)
    w -= 0.01 * grad
    l = loss(x, y)
    print("epoch:%d, w=%.4f, loss=%.4f, 选择数据为：(%.1f,%.1f)" %(epoch, w, l, x, y))
