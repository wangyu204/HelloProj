# coding=utf-8


# 列表 list [] 也是一种序列结构
n_list = []
for x in range(10):
    if x % 2 == 0:
        n_list.append(x ** 2)
print(n_list)

n_list = [x ** 2 for x in range(10) if x % 2 == 0]
print(n_list)

n_list = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]
print(n_list)
