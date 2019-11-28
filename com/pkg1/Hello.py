# coding=utf-8


import re

p = r'\d+'
text = 'AB12CD34EF'

repace_text = re.sub(p, ' ', text)
print(repace_text)

repace_text = re.sub(p, ' ', text, count=1)
print(repace_text)

repace_text = re.sub(p, ' ', text, count=2)
print(repace_text)
