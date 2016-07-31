#! /usr/bin/env python
# coding: utf-8
# e16.py
# 2016-07-31
#
import sys
from e10 import lineCount

def split(numbers, filename):
    filenumbers = int(numbers)
    f = open(filename, 'r')
    allnumbers = lineCount(filename)
    numbers = allnumbers / filenumbers
    # mod = allnumbers % filenumbers
    lines = f.readlines()
    j = 0

    for i in range(0, filenumbers - 1):
        fileout = open(filename.strip('.txt') + '_' + str(i+1) + '.txt', 'w')
        while j < numbers * (i + 1):
            fileout.write(lines[j])
            j += 1
        fileout.close()
    fileout = open(filename.strip('.txt') + '_' + str(filenumbers) + '.txt', 'w')
    while j < allnumbers:
        fileout.write(lines[j])
        j += 1
    fileout.close()

    f.close()

if __name__ == '__main__':
    split(sys.argv[1], sys.argv[2])

# split -l numbers filename
