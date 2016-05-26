#! /usr/bin/env python
# coding: utf-8
# 03.py
# 2016-05-16
#

import re

def wordLength(str):
    list = []
    for word in re.split('\W+', str):
        list.append(len(word))
    return list

str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

print wordLength(str)
