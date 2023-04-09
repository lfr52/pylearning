__all__ = ['test_add'] # from my_model1 import * 的话只能调用函数test_add,其余不可用


def test_add(x, y):
    return x + y

def test_add2(x, y):
    return x - y

if __name__ == '__main__':
    print(test_add(3, 4))