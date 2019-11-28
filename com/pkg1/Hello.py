# coding=utf-8


import configparser

config = configparser.ConfigParser()  # 创建配置解析器对象

config.read('data/Setup.ini', encoding='utf-8')  # 读取并解析配置文件

# 写入配置文件
config['Startup']['RequireMSI'] = '8.0'
config['Product']['RequireMSI'] = '4.0'

config.add_section('Section2')  # 添加节
config.set('Section2', 'name', 'Mac')  # 添加配置项

with open('data/Setup.ini', 'w') as fw:
    config.write(fw)
