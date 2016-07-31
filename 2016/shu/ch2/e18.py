#! /usr/bin/env python
# coding: utf-8
# e18.py
# 2016-07-31
#
import codecs

def sortCol(col, filename):
    f = codecs.open(filename, 'r', 'utf-8')
    itemtuples = []
    results = ''
    for line in f.readlines():
        itemtuples.append(tuple(line.split('\t')))
    for item in sorted(itemtuples, key=lambda line: line[col - 1], reverse=True):
        for i in xrange(len(item) - 1):
            results += item[i].encode('utf-8') + '\t'
        results += item[len(item) - 1].encode('utf-8')
    return results
    f.close()

if __name__ == '__main__':
    print sortCol(3, 'hightemp.txt')

# sort -k3 -r hightemp.txt
