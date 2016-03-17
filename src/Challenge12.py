#!/usr/bin/env python3
# coding=utf-8

__author__ = 'Chi Qingjun'

from PIL import Image
from io import BytesIO

GFX_FILE = '/Users/chiqingjun/Downloads/evil2.gfx'

def my_solver():
    with open(GFX_FILE, 'rb') as f:
        gfx_bytes = f.read()
    for i in range(5):
        with open('/Users/chiqingjun/Downloads/Challenge12-%s.jpg' % i, 'wb') as f:
            f.write(gfx_bytes[i::5])


# 实际上5幅图片格式并不相同，使用Pillow模块能够自动得到它们的扩展名。
def recommended_solver():
    with open(GFX_FILE, 'rb') as f:
        gfx_bytes = f.read()
    for i in range(5):
        piece = gfx_bytes[i::5]
        im = Image.open(BytesIO(piece)) # 第4幅图用im.show()和im.save()方法会报错，所以只能存成文件，这里用Image类来获取扩展名
        with open('/Users/chiqingjun/Downloads/Challenge12-%s.%s' % (i, im.format.lower()), 'wb') as f:
            f.write(piece)


if __name__ == '__main__':
# 第四幅图显示不正常，放到Chrome浏览器里就好了。
    recommended_solver()
