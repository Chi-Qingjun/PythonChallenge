#!/usr/bin/env python3
# coding=utf-8

__author__ = 'Chi Qingjun'

import os
import re
import zipfile

file_name = '../channel.zip'
nothing = '90052'

z = zipfile.ZipFile(file_name, 'r')
comments = ''

while nothing:
    text = z.read('%s.txt' % nothing)
    print(text.decode('utf-8'))
    comments += z.getinfo('%s.txt' % nothing).comment.decode('utf-8')
    nothing = re.search(r'Next nothing is (\d+)', text.decode('utf-8'))
    if nothing:
        nothing = nothing.group(1)

print(comments)

# 结果
# ****************************************************************
# ****************************************************************
# **                                                            **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
# **                                                            **
# ****************************************************************
#  **************************************************************
# 答案是组成上面图案的字母oxygen，即http://www.pythonchallenge.com/pc/def/oxygen.html
