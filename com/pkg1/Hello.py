# coding=utf-8

# 生成器  yield   不直接返回所有数据，而是返回一个生成器对象（一种可迭代的对象）  __next__()
def square(num):
    for i in range(1, num + 1):
        yield i * i


for i in square(5):
    print(i, end=' ')
