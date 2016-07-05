#! /usr/bin/env python
# coding: utf-8
# 10.py
# 2016-05-22
#

def lineCount(path):
    file = open(path)
    lines = 0
    for line in file:
        lines += 1
    file.close()
    return lines

print lineCount('hightemp.txt')


# wc -l hightemp.txt
# 行数ではなく、改行数を数える
