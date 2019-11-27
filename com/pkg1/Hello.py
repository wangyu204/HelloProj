# coding=utf-8


def make_coffee(name="卡布奇诺"):
    return "制作一杯{0}咖啡。".format(name)


coffee1 = make_coffee("拿铁")
coffee2 = make_coffee()

print(coffee1)  # 制作一杯拿铁咖啡。
print(coffee2)  # 制作一杯卡布奇诺咖啡。

