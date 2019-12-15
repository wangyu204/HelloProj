# coding=utf-8

import urllib.parse
import urllib.request

url = 'http://www.51work6.com/service/mynotes/WebService.php'
email = '414875346@qq.com'
params_dict = {'email': email, 'type': 'JSON', 'action': 'query'}
params_str = urllib.parse.urlencode(params_dict)
print(params_str)

url = url + '?' + params_str  # HTTP参数放到URL之后
print(url)

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = response.read()
    json_data = data.decode()
    print(json_data)
