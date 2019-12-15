# coding=utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务器
s.connect(('127.0.0.1', 8888))

# 给服务器端发送数据
s.send(b'Hello')
# 从服务器端接收数据
data = s.recv(1024)
print('从服务器端接收消息：{0}'.format(data.decode()))

# 释放资源
s.close()
