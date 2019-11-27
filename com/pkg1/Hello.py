# coding=utf-8


i = 0

while i * i < 10:
    i += 1
    if i == 3:
        break
    print("{0} * {0} = {1}".format(i, i * i))
else:
    print('While Over!')


for item in range(10):
    print("Count is : {0}".format(item))
else:
    print('For Over!')
