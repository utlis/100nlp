#! /usr/bin/env python
# coding: utf-8
# 03.py
# 2016-05-16
#

import re

def wordLength(str):
    list = []
    # re.split(pattern, string, maxplit=0, flags=0): stringをpatternがあるたびに分割
    # \W: [^a-zA-Z0-9_]と同じ; +: \Wを1回以上繰り返したもの
    for word in re.split('\W+', str):
        list.append(len(word))
    return list

str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

print wordLength(str)
