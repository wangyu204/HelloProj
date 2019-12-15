# coding=utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 8888))
print('服务器启动...')

# 从客户端接收数据
data, client_address = s.recvfrom(1024)
print('从客户端接收消息：{0}'.format(data.decode()))
# 给客户端发送数据
s.sendto('你好'.encode(), client_address)  # 如果数据量很大会多次调用

# 释放资源
s.close()
