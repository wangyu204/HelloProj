# coding=utf-8


f = open('test.txt', 'w+')
f.write('world222')

f = open('test.txt', 'r+')
f.write('Hello')

f = open('test.txt', 'a')
f.write(' ')

fName = r'test.txt'
f = open(fName, 'a+')
f.write('World')
