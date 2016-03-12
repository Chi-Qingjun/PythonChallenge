#!/usr/bin/env python3
# coding=utf-8

__author__ = 'Chi Qingjun'

import re

with open('Challenge3.txt', 'r') as f:
    text = f.read()

# 文本中除了答谢字母就是小写字母，要想让两边是3个大写字母，那么最外围应该是两个小写字母，这样才能构造出正确的表达式。
result = re.findall(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', text)
str = ''
for i in result:
    str += i
print(str)
