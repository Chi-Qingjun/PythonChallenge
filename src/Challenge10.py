#!/usr/bin/env python3
# coding=utf-8

__author__ = 'Chi Qingjun'

a = ['1']

# a[30]是a中的第31个元素，所以循环条件设为a中元素数为31个时停止
while len(a) != 31:
    # 取出a的最后一个元素
    last_element = a[-1]
    # 初始化下一个要追加到a末尾的元素
    next_element = ''
    # 初始化元素中当前计数的字符
    now_char = last_element[0]
    # 初始化元素中当前计数字符的个数
    now_num = 0
    # 分析当前a中的最后一个元素
    for char in last_element:
        # 如果取到的字符和当前正在计数的字符相同，计数＋1
        if char == now_char:
            now_num += 1
        # 如果不同
        else:
            # 把字符个数和字符本身追加到next_element中
            next_element += str(now_num)
            next_element += now_char
            # 更新当前计数的字符和计数个数
            now_char = char
            now_num = 1
    # 对元素中最后计数的字符的处理
    next_element += str(now_num)
    next_element += now_char
    # 把计算好的下一个元素写入到a的末尾
    a.append(next_element)

print(len(a[30]))
