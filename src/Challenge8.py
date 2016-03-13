#!/usr/bin/env python3
# coding=utf-8

__author__ = 'Chi Qingjun'

import bz2

username = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
password = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

# 使用一次性解压缩函数。
un = bz2.decompress(username).decode('ascii')
pw = bz2.decompress(password).decode('ascii')

print(un, pw)
