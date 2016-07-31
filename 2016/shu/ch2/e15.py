#! /usr/bin/env python
# coding: utf-8
# e15.py
# 2016-07-31
#
import sys
from e10 import lineCount

def tail(numbers, filename):
    f = open(filename, 'r')
    numbers = int(numbers)
    allnumbers = lineCount(filename)
    line = allnumbers - numbers
    lines = f.readlines()

    while line < allnumbers:
        print lines[line].strip('\n')
        line += 1

    f.close()

if __name__ == '__main__':
    tail(sys.argv[1], sys.argv[2])

# tail -numbers filename
# tail -3 hightemp.txt
