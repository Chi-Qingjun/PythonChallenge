#!/usr/bin/env python3
# coding=utf-8

__author__ = 'Chi Qingjun'

from PIL import Image

im_path = '/Users/chiqingjun/Downloads/cave.jpg'

im = Image.open(im_path)
width, height = im.size
im.show()

im1 = Image.new(im.mode, (width // 2, height // 2))
im2 = Image.new(im.mode, (width // 2, height // 2))
im3 = Image.new(im.mode, (width // 2, height // 2))
im4 = Image.new(im.mode, (width // 2, height // 2))

for x in range(width):
    for y in range(height):
        pix = im.getpixel((x, y))
        if x % 2 == 0 and y % 2 == 0:
            im1.putpixel((x // 2, y // 2), pix)
        elif x % 2 == 1 and y % 2 == 0:
            im2.putpixel((x // 2, y // 2), pix)
        elif x % 2 == 0 and y % 2 == 1:
            im3.putpixel((x // 2, y // 2), pix)
        elif x % 2 == 1 and y % 2 == 1:
            im4.putpixel((x // 2, y // 2), pix)

im1.show()
im2.show()
im3.show()
im4.show()
