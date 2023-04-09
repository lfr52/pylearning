
# 1.异常的捕获
# try:
#     f = open("abc.txt", "r")
# except:  # Exception as e
#     print("出现异常，将文件改为w模式")
#     f = open("abc.txt", "w")

# 捕获指定异常
# try:
#     print(name)
# except NameError as e:
#     print("出现异常，变量未定义")
#     print(e)

# 捕获多个异常
# try:
#     print(name)
#     # 1 / 0
# except (NameError, ZeroDivisionError) as e:
#     print("出现变量未定义或除以0的异常")

# 异常的else
# try:
#     print(name)
# except NameError as e:
#     print("出现异常，变量未定义")
#     print(e)
# else:
#     print("没有异常")

# finally  有无异常均需要执行,通常用于文件关闭
# try:
#     f = open("abc.txt", "r")
# except Exception as e:
#     print("出现异常，文件不存在")
#     f = open("abc.txt", "w")
#     print(e)
# else:
#     print("没有异常")
# finally:
#     print("我是finally，有无异常均需执行")
#     f.close()

# 2.异常的传递性  # 从最底层向上查看
def fun1():
    print("fun1开始")
    1 / 0
    print("fun1结束")
def fun2():
    print("fun2开始")
    fun1()
    print("fun2结束")

def main():
    try:
        fun2()
    except Exception as e:
        print(f"出现异常，信息是{e}")

main()

# 3.模块  一个.py文件，其中有变量，类，方法等
# from 模块名 import 类、变量、方法、*
# import 模块名 【as 别名】
# import time # 本质是time.py文件
# time.sleep(2)
# print("你好1")

# from time import sleep
# sleep(2)
# print("你好2")

# from time import *
# sleep(2)
# print("你好3")

# 4.自定义模块
# __main__变量可以用于测试
# __all__ 可以控制*可以使用哪些功能
from my_model1 import *
print(test_add(2, 3))
# print(test_add2(4, 3))

# 5.python的包
# 一堆模块+__init__.py文件就构成一个package  (包相当于文件夹)
# import 包名.模块名
# from 包名 import 模块名
# import my_package.module1
# import my_package.module2
# my_package.module1.print1()
# my_package.module2.print2()

# from my_package import module1
# from my_package import module2
# module1.print1()
# module2.print2()

# from  my_package.module1 import print1
# from  my_package.module2 import print2
# print1()
# print2()

# from my_package import *
# module1.print()
# # module2.print2()

