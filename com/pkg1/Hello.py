# coding=utf-8


import re

# p = r'[^0123456789]'
p = r'\D'

m = re.search(p, '1000')
print(m)  # 不匹配

m = re.search(p, 'Python 3')
print(m)  # 匹配

text = '你们好Hello'
m = re.search(r'\w', text)
print(m)  # 匹配
