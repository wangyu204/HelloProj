# coding=utf-8

import sys

score = int(sys.argv[1]) # 获得命令行传入的参数

result = '及格' if score >= 60 else '不及格'
print(result)
