# coding=utf-8


# 元组 tuple 一种序列结构
a = (21, 32, 43, 54)

for item in a:
    print(item)

print('-----')
for i, item in enumerate(a):
    print("{0} - {1}".format(i, item))
