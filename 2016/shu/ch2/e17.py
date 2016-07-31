#! /usr/bin/env python
# coding: utf-8
# e17.py
# 2016-07-31
#
import codecs

def unique(filename):
    f = codecs.open(filename, 'r', 'utf-8')
    uniq = ''
    for item in set(f.readlines()):
        uniq += item.encode('utf-8')
    return uniq.strip('\n')
    f.close()

if __name__ == '__main__':
    print unique('col1.txt')

# cut -f1 hightemp.txt | sort | uniq
# cat col1.txt | sort | uniq
