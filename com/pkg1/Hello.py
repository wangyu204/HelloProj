# coding=utf-8

# 鸭子类型  不一定要有继承关系，只看方法
class Animal(object):
    def run(self):
        print('动物跑...')


class Dog(Animal):
    def run(self):
        print('狗狗跑...')


class Car:
    def run(self):
        print('汽车跑...')


def go(animal):  # 接收参数是Animal
    animal.run()


go(Animal())
go(Dog())
go(Car())
