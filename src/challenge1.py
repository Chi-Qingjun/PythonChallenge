#!/usr/bin/env python3
# coding=utf-8

__author__ = 'Chi Qingjun'

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


def my_solver(cypher_text):
    clear_text = ''
    step = 2
    for cypher_letter in cypher_text:
        if 'a' <= cypher_letter <= 'z':
            clear_letter = chr((ord(cypher_letter) - ord('a') + 2) % 26 + ord('a'))
        else:
            clear_letter = cypher_letter
        clear_text += clear_letter
    return clear_text


# str.maketrans制作一个映射表，用于字符转换
def recommended_solver(cypher_text):
    x = 'abcdefghijklmnopqrstuvwxyz'
    y = 'cdefghijklmnopqrstuvwxyzab'
    trans_table = str.maketrans(x, y)
    return cypher_text.translate(trans_table)


if __name__ == '__main__':
    print(my_solver(text))
    print('*' * 30)
    print(recommended_solver(text))
    print('*' * 30)
    print('http://www.pythonchallenge.com/pc/def/%s.html' % recommended_solver('map'))
