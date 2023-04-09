# 函数
# name = "itheima"

# def my_len(data):
#     count = 0
#     for i in data:
#         count = count + 1
#     print(f"字符串{data}的长度为{count}")

# my_len(name)

# 不写返回值则返回None   类型为class<NoneType>
# def check_age(age):
#     if(age > 18):
#         return "success"
#     else:
#         return None  # 条件判断中等同于False

# result = check_age(16)
# if not result:
#     print("未成年不允许进入")

# 函数的说明文档
def add(x, y):
    '''
    add进行两数相加的功能
    :param x: 相加的参数
    :param y: 相加的另一个参数
    :return:  返回两数相加的结果
    '''
    result = x + y
    return result

r = add(4, 5)
print(r)

num = 200

def test_a():
    print(f"test_a:{num}")

def test_b():
    # num = 500  # 只在内部生效
    # 关键字global声明变量为全集变量
    global num
    num = 500
    print(f"test_b:{num}")

test_a()
test_b()
print(num)
