#!/usr/bin/env python3
# coding=utf-8

__author__ = 'Chi Qingjun'

import collections
import string


def my_solver():
    with open('Challenge2.txt', 'r') as f:
        str = f.read()
    # 计数器
    cnt = collections.Counter(str)
    print(cnt)
    # 出现次数最少的字母是aeilqtuy，组成单词equality
    # 下一关地址 http://www.pythonchallenge.com/pc/def/equality.html


# 线索是find rare characters，所以就是在一堆字符中找到字母，使用filter来过滤
# 这种方法的好处是字母按出现顺序排列，比较容易得到答案
def recommended_solver():
    with open('Challenge2.txt', 'r') as f:
        str = f.read()
    tmp = filter(lambda x: x in string.ascii_letters, str)
    result = ''
    for i in tmp:
        result += i
    print(result)


if __name__ == '__main__':
    my_solver()
    print('*' * 30)
    recommended_solver()
