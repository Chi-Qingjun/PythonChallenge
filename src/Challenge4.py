#!/usr/bin/env python3
# coding=utf-8

__author__ = 'Chi Qingjun'

import requests
import re

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
nothing = '12345'

while nothing:
    payload = {'nothing': nothing}
    resp = requests.get(url, params = payload)
    print(resp.text)
    nothing = re.search(r'the next nothing is (\d+)', resp.text)
    if nothing:
        nothing = nothing.group(1)
        if nothing == '16044':
            nothing = str(int(nothing)//2)

print('http://www.pythonchallenge.com/pc/def/%s' % resp.text)
