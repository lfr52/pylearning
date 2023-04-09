# 数据容器

# 一、列表list

# 1.定义
# l = ["itheima", 123, True]
# l = [[1,2,3], [4,5,6]]
# print(l)
# l = []
# l = list()

# 2.下标索引
# l = ["itheima", 123, True]
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[-1])
# print(l[-2])
# print(l[-3])
# l = [[1,2,3], [4,5,6]]
# print(l[0][1])

# 3.常用操作
# 如果函数定义为class的成员，则函数会称为方法
# 函数的使用 num = add(4, 5)
# 方法的使用 stu = Student()  num = stu.add(4, 5)
# 3.1查询下标 列表.index(元素)
l = ["itheima", 123, True]
index = l.index("itheima")
print(index)
# 3.2修改元素的值 列表[下标] = 值
# 3.3插入元素 列表.insert(下标, 元素)
l = ["itheima", 123, True]
l.insert(1, 'best')
print(l)
# 3.4追加元素 列表.append(元素)
l = ["itheima", 123, True]
l.append('python')
print(l)
# 3.4追加元素2  列表.extend(其他数据容器)
l_1 = [1,2,3]
l_2 = [4,5,6]
l_1.extend(l_2)
print(l_1)
# 3.5删除元素 del 列表[下标]   列表.pop(下标)
l = ["itheima", 123, 'python', True]
element = l.pop(2)
print(l, element)
# 3.5删除元素2  列表.remove(元素)
l = ["itheima", 123, 'python', True]
l.remove("python")
print(l)
# 3.5清空列表 列表.clear()
# 3.6统计数量 列表.count(元素)
l = ["itheima","itheima", "itheima", 123, 'python', True]
print(l.count("itheima"))
# 3.7统计全部元素数量 len(列表)   这个不属于列表的方法

# 4.遍历
# while实现
index = 0
l = ["itheima","itheima", "itheima", 123, 'python', True]
while index < len(l):
    element = l[index]
    print(element)
    index = index + 1
# for实现
l = ["itheima","itheima", "itheima", 123, 'python', True]
for element in l:
    print(element)


# 二、元组tuple  不能被修改

# 1.定义
t = ()
t = tuple()
t = (1, "hello", True)
t = ((1,2,3),(4,5,6))
# 定义只有一个数据要加逗号
t = ("hello", )

# 2.下标索引
t = ((1,2,3),(4,5,6))
print(t[1][2])

# 3.常用操作
# 3.1查询下标 t.index(元素)
# 3.2统计数量 t.count(元素)
# 3.3统计全部元素数量 len(t)

# 4.遍历
index = 0
t = (1, "hello", True)
while index < len(t):
    element = t[index]
    print(element)
    index = index + 1

t = (1, "hello", True)
for element in t:
    print(element)

# 5.元组内容不可修改，但嵌套list的话list可以改
t = (1, 2, ["itheima", 123, True])
t[2][1] = "hello"
print(t)