#! /usr/bin/env python
# coding: utf-8
# 04.py
# 2016-05-16
#

str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

words = str.split()
index = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dict = {}

for i, word in enumerate(words):
    if i + 1  in index:
        dict[word[:1]] = i + 1
    else:
        dict[word[:2]] = i + 1

print dict
