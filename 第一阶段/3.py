

# while循环语句
# i= 1
# sum = 0 
# while i <= 100:
#     sum += i
#     i += 1

# print(f"0-100的和为{sum}")

# import random
# num = random.randint(1,50)
# flag = True
# i = 0
# while flag:
#     guess = int(input("输入猜测数字："))
#     if guess == num:
#         print("猜中！")
#         flag = False
#     else:
#         if guess > num:
#             print("你猜大了")
#         else:
#             print("你猜小了")
#     i += 1
# print(f"一共猜了{i}次")

# print("hello", end='') #输出不换行
# print("word", end='')
# print()

# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(f"{j}*{i}={i*j}\t", end='')
#         j +=1
#     i += 1
#     print()


# for循环   for 变量 in 被处理数据集:        遍历循环！！
# 被处理数据集严格的说法是序列类型
# name = "itheima"
# for x in name:
#     print(x, type(x))

# name = "itheima is a brand of itcast"
# i = 0
# for x in name:
#     if x=='a':
#         i += 1
# print(f"{name}中一共有{i}个字母a")

# range(5) # 0,1,2,3,4
# range(2,8) # 2,3,4,5,6,7
# range(2,8,2) # 2,4,6,

# # 作用域
# i = 0
# for i in range(5):
#     print(i)
# print(i)

# 循环中断 break continue 只针对本层循环

import random

sum = 10000
for i in range(1,21):
    if sum == 0:
        break
    num = random.randint(1,10)
    if num < 5:
        print(f"员工{i}，绩效分{num}，低于5，不发工资，下一位")
    else:
        sum = sum - 1000
        print(f"向员工{i}发放工资1000元，账户余额还剩{sum}元")
print("工资发完了，下个月再领吧！")
