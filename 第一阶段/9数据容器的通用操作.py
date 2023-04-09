l = [1,2,3,4,5]
t = (1,2,3,4,5)
str1 = "abcdefg"
s = {1,2,3,4,5}
d = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

# 元素个数len

# 最大小元素 max()  min()

# 容器的转换
print(list(l))
print(list(t))
print(list(str1))
print(list(s))
print(list(d))

print(tuple(l))
print(tuple(t))
print(tuple(str1))
print(tuple(s))
print(tuple(d))

print(str(l))
print(str(t))
print(str(str1))
print(str(s))
print(str(d))

print(set(l))
print(set(t))
print(set(str1))
print(set(s))
print(set(d))

# 通用排序  返回一个列表  sorted(容器, [reverse=False])  reverse默认False，改为True则倒序
print(sorted(l))
print(sorted(t))
print(sorted(str1))
print(sorted(s))
print(sorted(d))
