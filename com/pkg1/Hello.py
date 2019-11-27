# coding=utf-8


def print_area(width, height):
    area = width * height
    print("{0} x {1} 长方形的面积:{2}".format(width, height, area))


print_area(320.0, 480.0)  # 没有采用关键字参数函数调用
print_area(width=320.0, height=480.0)  # 采用关键字参数函数调用
print_area(320.0, height=480.0)  # 采用关键字参数函数调用
# print_area(width=320.0, height)  # 发生错误
print_area(height=480.0, width=320.0)  # 采用关键字参数函数调用
