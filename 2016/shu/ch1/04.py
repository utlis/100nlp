#! /usr/bin/env python
# coding: utf-8
# 04.py
# 2016-05-16
#

str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

# 先頭の1文字か2文字のみ取り出すので句読点は無関係
words = str.split()
# 先頭の1文字を取り出す単語の番号
index = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dict = {}

# 1から数えはじめる（デフォルトでは0から）
for i, word in enumerate(words, start=1):
    if i in index:
        dict[word[:1]] = i
    else:
        dict[word[:2]] = i

print dict
