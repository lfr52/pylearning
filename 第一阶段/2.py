
'''
# 布尔类型和比较运算
bool_1 = True
bool_2 = False
print(f"bool_1的内容为{bool_1},类型为{type(bool_1)}")
# == != > < >= <= 可以比较数字和字符串
print("结果为：%s" % (10==10))
'''

'''
# if语句
age = 30
if age >= 18:
    print("我已经成年了！")

# if-else语句
# if-elif-else语句
if int(input("请输入身高（cm）：")) < 120:
    print("身高小于120，免费")
elif int(input("请输入vip等级（1-5）：")) >3:
    print("vip等级大于3，免费")
elif int(input("今天几号")) == 1:
    print("今天1号，免费")
else:
    print("收费10元")
'''

import random
num = random.randint(1,10)
