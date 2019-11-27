# coding=utf-8


for item in range(10):
    if item == 3:
        # 跳出循环
        break
    print("Count0 is : {0}".format(item))


for item in range(10):
    if item == 3:
        continue
    print("Count1 is : {0}".format(item))