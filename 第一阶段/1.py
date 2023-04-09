

'''
# 字面量——固定的值  
print(123)
'''


'''
# 注释


多行注释

'''

'''
# 变量
money =50
print("钱包还有", money)
money = money - 10
print("花费10元还有", money, "元")
print("花费10元还有", money, "元")
'''

'''
# 数据类型 int float string
int_type = type(123)
print(type(123))
print(type(3.14))
print(type("hello"))
'''

'''
# 数据类型转换 int(x) float(x) str(x)
num = str(12)
print(type(num), num)

num2 = int("11")
print(type(num2), num2)

num3 = float('3.14')
print(type(num3), num3)

num4 = int(3.64) # 向下取整
print(type(num4), num4)
'''

'''
# 标识符——用户起的名字（变量名、类名、方法名）
# 数字不能开头，大小写敏感，不能使用关键字
'''

'''
# 运算符
print(4 / 2) 
print(11 // 2) # 整除
print(9 % 2) # 取余
print(2 ** 3) # 指数
'''

# 字符串扩展
name = '''
hello
word
'''
print(name) 

'''
name = '"hello"'
print(name) 
name = "\"hahahha\""
print(name) 

# 字符串拼接
name = "lalala"
num = str(1562020)
print("我是" + name + ",我来了," + "电话为" + num)

# 字符串格式化 %s %d %f
name = "lalala"
tel = 123456789
message = "我是：%s,电话为：%s" % (name, tel)
print(message)

# 格式化的精度控制 m.n的形式 m为宽度，n为小数位数  如 %.2f %7.2f

# 快速格式化写法  f：format 
name = "lalala"
tel = 123456789
message = f"我是：{name},电话为：{tel}" # 此方法不做精度控制
print(message)

# 表达式的格式化
# 表达式的定义：有具体结果的代码语句
print("1*1的结果为：%d" % (1 * 1))
print(f"1*2的结果为：{1 * 2}" )
print("字符串的类型为%s" % type("hello"))
'''
# 数据输入   intput()接收的均为字符串
# print('你是谁？')
# name = input()
name = input('你是谁？') # 与上两行等价
print('我知道了，你是%s' % name)

