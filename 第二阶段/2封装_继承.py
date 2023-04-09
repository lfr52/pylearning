# 1.封装
# 私有的成员变量、成员方法命名以__开头即可
# class Phone:
#     __current = None
#     def __keep(self):
#         print("保持")

# phone = Phone()
# phone.__keep()

# 私有成员类内可以访问
class Phone:
    __current = 1

    def __keep(self):
        print("保持")
    def call(self):
        if self.__current > 0.5:
            print("可以通话")
        else:
            self.__keep()
            print("无法通话")

phone = Phone()
phone.call()
print()

# 2.继承  对老的类进行修改、增加新功能
class Phone:
    IMEI = None
    producer = "HM"

    def call_by_4G(self):
        print("4g通话")
    
class Phone2022(Phone):
    face = "10010"

    def call_by_5G(self):
        print("5g通话")

phone = Phone2022()
print(phone.producer)
phone.call_by_4G()
print()
# 多继承  同名的成员属性（方法）左边的优先
# class 类名(父类1，父类2)：
#   类内容体
# pass可以用于补充语法

# 2.2复写以及使用父类成员
class Phone:
    IMEI = None
    producer = "HM"

    def call_by_5G(self):
        print("父类5g通话")
    
class Phone2022(Phone):
    face = "10010"
    producer = "ITCAST"

    def call_by_5G(self):
        print("子类5g通话")
        # 仍需使用父类的成员属性或方法
        # 方法一
        # print(f"父类的厂商为{Phone.producer}")
        # Phone.call_by_5G(self)
        # 方法二
        print(f"父类的厂商为{super().producer}")
        super().call_by_5G()

phone = Phone2022()
print(phone.producer)
phone.call_by_5G()
print()

