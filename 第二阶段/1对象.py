# 1.对象
class Student: # 设计类
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None

stu1 = Student() # 创建对象

stu1.name = "小张"  # 属性赋值
stu1.gender = "男"
stu1.nationality = "中国"
stu1.native_place = "山东省"
stu1.age = 20

print()

# 2.成员方法
# def 方法名(self, 形参)：
#   方法体
# 方法内部，想要访问成员变量，需要使用self！
class Student: 
    name = None
    gender = None

    def say_hi(self):
        print(f"大家好,我是{self.name}")

    def say_hi2(self, msg):
        print(f"大家好,我是{self.name},{msg}")

stu = Student()
stu.name = "张三"
stu.say_hi()
stu.say_hi2("我来了")

print()

# 3.构造方法  __init__()方法称为构造方法
class Student: 
    # name = None  # 可省略
    # age = None  # 可省略
    # tel = None  # 可省略

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student创建了一个类对象")

stu = Student("张三", 18, "19420000000")
print(stu.name)
print(stu.age)
print(stu.tel)

print()

# class Student: 

#     def __init__(self, name, age, addr):
#         self.name = name
#         self.age = age
#         self.addr = addr

# l = []
# for i in range(10):
#     print(f"当前录入第{i + 1}位学生信息，总共需录入10位")
#     name = input("请输入学生姓名：")
#     age = input("请输入学生年龄：")
#     addr = input("请输入学生地址：")
#     stu = Student(name, age, addr)
#     print(f'学生{i + 1}信息录入完成，信息为【学生姓名：{stu.name},年龄：{stu.age},地址：{stu.addr}】')
#     l.append(stu)

# 4.魔术方法 ———类的一些内置方法
# 4.1字符串方法
class Student: 

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"学生姓名为{self.name},名称为{self.age}"



stu = Student("张三", 18)
print(stu)
print(str(stu))

# 4.2小于、大于符号比较  __lt__
class Student: 

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __lt__(self, other):
        return self.age < other.age

stu1 = Student("张三", 18)
stu2 = Student("李四", 15)
print(stu1 < stu2)
print(stu1 > stu2)
print()
# 4.3 小于等于、大于等于符号比较 __le__(self, other)
# 4.4 比较符号大小 __eq__(self, other)

