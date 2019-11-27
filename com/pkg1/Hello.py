# coding=utf-8


class Animal(object):
    """定义动物类"""

    def __init__(self, age, sex=1, weight=0.0):
        self.age = age  # 定义年龄实例变量
        self.sex = sex  # 定义性别实例变量
        self.__weight = weight  # 定义体重实例变量

    def eat(self):
        self.__weight += 0.05
        print('eat...')

    def run(self):
        self.__weight -= 0.01
        print('run...')


a1 = Animal(2, 0, 10.0)

# print('a1体重：{0:0.2f}'.format(a1.weight)) #私有变量不可访问
a1.eat()
a1.run()
print('a1体重：{0:0.2f}'.format(a1._Animal__weight))
