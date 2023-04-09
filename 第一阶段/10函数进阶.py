# 1.函数的多返回值
def test_return():
    return 1,"hello",True

x, y, z = test_return()
print(x, y, z)

# 2.函数的传参方式
# 2.1 位置参数
def user_infor(name, age, gender):
    print(f"您的名字为{name},年龄是{age},性别是{gender}")

user_infor("小明", 20, "男")
# 2.2关键字参数
user_infor(name="小明", age=20, gender="男")
user_infor(age=20, name="小王", gender="男")
# 2.3缺省参数 （默认值只能在最后）
def user_infor(name, age, gender="男"):
    print(f"您的名字为{name},年龄是{age},性别是{gender}")

user_infor("小天", 20)
user_infor("小天", 20, "女")
# 2.4不定长参数
# 位置传递 得到一个元组
def user_infor(*args):
    print(args, type(args))

user_infor(1,2,3,"小明")
# 关键字传递 得到一个字典
def user_infor(**kwargs):
    print(kwargs, type(kwargs)) 

user_infor(age=20, name="小王", gender="男", addr="北京")

# 3.匿名函数
# 3.1函数作为参数传递  传递的是计算逻辑而非数据
def test_func(compute):
    result = compute(1, 2)
    print(type(compute))
    print(result)

def add(x, y):
    return x + y

test_func(add)

# 3.2 lambda匿名函数 只能临时使用一次
# lambda 传入参数: 函数体     只能写一行代码
def test_func(compute):
    result = compute(1, 2)
    print(type(compute))
    print(result)

test_func(lambda x, y: x + y)