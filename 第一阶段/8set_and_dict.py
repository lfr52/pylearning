# 一、集合set

# 1.定义
s = set()
s = {"itheima","itheima", "itheima", 123, 'python', True}
print(s)

# 2.常用操作
# 2.1添加元素 集合.add(元素)
s = {"itheima","itheima", "itheima", 123, 'python', True}
s.add("程序")
print(s)
# 2.2移除元素 集合.remove(元素)
s = {"itheima","itheima", "itheima", 123, 'python', True}
s.remove("python")
print(s)
# 2.3随机取出元素 集合.pop()
s = {"itheima","itheima", "itheima", 123, 'python', True}
element = s.pop()
print(s, element)
# 2.4清空集合 集合.clear()
# 2.5取两个集合的差集 返回新集合  集合1.difference(集合2)  取出集合1有但集合2没有的
s1 = {1,2,3}
s2 = {1,5,6}
s = s1.difference(s2)
print(s)
# 2.6消除差集 集合1.difference_update(集合2)  在集合1内删除和2相同的内容  直接改变集合1
s1 = {1,2,3}
s2 = {1,5,6}
s1.difference_update(s2)
print(s1)
# 2.7集合的合并  返回新集合  集合1.union(集合2)
s1 = {1,2,3}
s2 = {1,5,6}
s = s1.union(s2)
print(s)
# 2.8统计集合内元素数量 len(集合)

# 3.遍历
# 不支持下标索引，故不能while循环遍历
s = {1,1,2,3,4,5}
for i in s:
    print(i)


# 二、字典dict

# 1.定义 key和value可以为任意类型(key不可为字典)
d = {}
d = dict()
d = {"小王": 99, "小张": 98, "小林": 88} # key不可重复,重复添加相当于覆盖


# 2.数据的获取 字典[key] = value
d = {"小王": 99, "小张": 98, "小林": 88}
print(d["小张"])


# 3.字典的嵌套
d = {"小王": {"语文": 77, "数学": 66, "英语": 33}, 
     "小张": {"语文": 88, "数学": 86, "英语": 55}, 
     "小林": {"语文": 99, "数学": 96, "英语": 66}}
print(d)
# 数据的获取
d = {"小王": {"语文": 77, "数学": 66, "英语": 33}, 
     "小张": {"语文": 88, "数学": 86, "英语": 55}, 
     "小林": {"语文": 99, "数学": 96, "英语": 66}}
print(d["小林"]["语文"])


# 4.常用操作
# 4.1新增/更新元素 字典[key] = value
d = {"小王": 99, "小张": 98, "小林": 88}
d["小李"] = 90
d["小张"] = 88
print(d)
# 4.2删除元素 字典.pop(key)
d = {"小王": 99, "小张": 98, "小林": 88}
score = d.pop("小王")
print(d, score)
# 4.3清空元素 字典.clear()
# 4.4获取全部key 字典.keys()
d = {"小王": 99, "小张": 98, "小林": 88}
keys= d.keys()
print(keys, type(keys))
# 4.5统计字典内元素数量 len(字典)


# 5.遍历
# 方法1
d = {"小王": 99, "小张": 98, "小林": 88}
for key in d:
    print(key)
    print(d[key])

# 方法2
d = {"小王": 99, "小张": 98, "小林": 88}
keys= d.keys()
for key in keys:
    print(key)
    print(d[key])


