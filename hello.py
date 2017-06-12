#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('Hello,world!')

name = input('Please input your name: ')
print('Hello, ' + name)

a = 100
if a >= 100:
    print(a)
else:
    a = -a

str = '中文'
print(str + '的长度是%s' % len(str))

for x in range(5):
    print(x)