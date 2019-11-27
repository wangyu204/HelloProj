# coding=utf-8


class Animal(object):
    """定义动物类"""

    def __init__(self, age, sex=1, weight=0.0):
        self.age = age  # 定义年龄实例变量
        self.sex = sex  # 定义性别实例变量
        self.__weight = weight  # 定义体重实例变量

    def eat(self):
        self.__weight += 0.05
        self.__run()
        print('eat...')

    def __run(self):
        self.__weight -= 0.01
        print('run...')


a1 = Animal(2, 0, 10.0)

a1.eat()
# a1.run()  #私有方法 不可调用

a1._Animal__run();
