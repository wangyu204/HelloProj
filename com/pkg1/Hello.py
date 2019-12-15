# coding=utf-8

import urllib.parse
import urllib.request

url = 'http://www.51work6.com/service/mynotes/WebService.php'
# 准备HTTP参数
email = '414875346@qq.com'
params_dict = {'email': email, 'type': 'JSON', 'action': 'query'}
params_str = urllib.parse.urlencode(params_dict)
print(params_str)
params_bytes = params_str.encode()  # 字符串转换为字节序列对象

req = urllib.request.Request(url, data=params_bytes)  # 发送POST请求
with urllib.request.urlopen(req) as response:
    data = response.read()
    json_data = data.decode()
    print(json_data)
