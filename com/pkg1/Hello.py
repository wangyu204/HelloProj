# coding=utf-8


import re

p = r'(121){2}'
m = re.search(p, '121121abcabc')
print(m)  # 匹配
print(m.group())  # 返回匹配字符串
print(m.group(1))  # 获得第一组内容  分组默认从1开始
print(m.groups())  # 获得所有组内容

p = r'(\d{3,4})-(\d{7,8})'
m = re.search(p, '010-87654321')
print(m)  # 匹配
print(m.group())  # 返回匹配字符串
print(m.groups())  # 获得所有组内容  一个小括号就是1组
