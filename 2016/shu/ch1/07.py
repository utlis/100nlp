#! /usr/bin/env python
# coding: utf-8
# 07.py
# 2016-05-18
#

def template(x, y, z):
    return str(x) + '時の' + str(y) + 'は' + str(z)

print template(12, '気温', 22.4)
