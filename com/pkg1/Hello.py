# coding=utf-8


import re

s = 'img1.jpg,img2.jpg,img3.bmp'

# 捕获分组
p = r'\w+(\.jpg)'
mlist = re.findall(p, s)
print(mlist)

# 非捕获分组
p = r'\w+(?:\.jpg)'
mlist = re.findall(p, s)
print(mlist)
