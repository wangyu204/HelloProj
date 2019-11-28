# coding=utf-8


import re

# 使用贪婪量词
m = re.search(r'\d{5,8}', '87654321')  # 出现数字8次
print(m)  # 匹配字符'87654321'

# 使用惰性量词
m = re.search(r'\d{5,8}?', '87654321')  # 出现数字5次
print(m)  # 匹配字符'87654'
