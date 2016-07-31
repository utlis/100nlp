#! /usr/bin/env python
# coding: utf-8
# e14.py
# 2016-07-31
#

import sys

def head(numbers, filename):
    numbers = int(numbers)
    f = open(filename, 'r')

    while numbers > 0:
        print f.readline().strip('\n')
        numbers -= 1

if __name__ == '__main__':
    head(sys.argv[1], sys.argv[2])

# head -numbers filename
# head -3 hightemp.txt