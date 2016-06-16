#! /usr/bin/env python
# coding: utf-8
# 02.py
# 2016-05-16
#

str1 = u'パトカー'
str2 = u'タクシー'
str3 = u''

# 同じ長さの文字列なのでzip()が使える．
for a, b in zip(str1, str2):
    str3 += a + b
print str3.encode('utf-8')

# 内包表記
list = [x+y for (x, y) in zip(str1, str2)]
print ''.join(list).encode('utf-8')