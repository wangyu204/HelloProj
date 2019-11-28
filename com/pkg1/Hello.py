# coding=utf-8


import re

p = r'\d+'
text = 'AB12CD34EF'

clist = re.split(p, text)
print(clist)

clist = re.split(p, text, maxsplit=1)
print(clist)

clist = re.split(p, text, maxsplit=2)
print(clist)
