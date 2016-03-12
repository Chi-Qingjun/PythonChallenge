#!/usr/bin/env python3
# coding=utf-8

__author__ = 'Chi Qingjun'

from PIL import Image

image_path = '/Users/chiqingjun/Downloads/oxygen.png'
y_pixel = 48
x_start = 3
x_step = 7
x_stop = 610

im = Image.open(image_path, 'r')
text = []

for x_pixel in range(x_start, x_stop, x_step):
    rgba_tuple = im.getpixel((x_pixel, y_pixel))
    text.append(chr(rgba_tuple[0]))
print(''.join(text))
# smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

next_level = [105, 110, 116, 101, 103, 114, 105, 116, 121]
text = list(map(chr, next_level))
print(''.join(text))
# integrity
# 下一关 http://www.pythonchallenge.com/pc/def/integrity.html
