my_str = "itheima and itcast"

# 1.下标索引
print(my_str[2]) # h
print(my_str[-3])# a

# 2.常用操作
# 2.1查询下标
my_str = "itheima and itcast"
value = my_str.index("and")
print(value)
# 2.2字符串替换 此方法返回新字符串 字符串.replace(字符串1, 字符串2)
new_str = my_str.replace("it", "程序")
print(new_str)
# 2.3字符串的分割  字符串.split(分隔符字符串)  得到列表
my_str = "itheima and itcast"
l = my_str.split(" ")
print(l)
# 2.4字符串的规整 字符串.strip() ---去除前后空格   字符串.strip(字符串) ---去除指定字符(只能前后)
my_str = "  itheima and itcast   "
new_str = my_str.strip()
print(new_str)
my_str = "12itheima1 and itcast212"
new_str = my_str.strip("12")
print(new_str)
# 2.5统计数量 字符串.count(字符串)
# 2.6统计字符串长度 len(字符串)

# 3.遍历类似列表、元组