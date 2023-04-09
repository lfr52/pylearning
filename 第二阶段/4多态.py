
# 以父类做声明，子类做实际工作
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")
    

def make_noise(animal):
    animal.speak()

dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)

# 抽象方法：方法体为空实现（pass）
# 抽象类：含有抽象方法的类，多用于顶层设计   也可以称为接口
# 抽象类做规范，子类具体实现
