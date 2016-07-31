#! /usr/bin/env python
# coding: utf-8
# e19.py
# 2016-07-31
#
import codecs
from collections import Counter

def counterCol(filename):
    f = codecs.open(filename, 'r', 'utf-8')
    wordcount = Counter(f.readlines())
    results = ''

    for word, cnt in wordcount.most_common():
        results += str(cnt) + ' ' + word.encode('utf-8')

    return results.strip('\n')
    f.close()

if __name__ == '__main__':
    print counterCol('col1.txt')

# cut -f1 hightemp.txt | sort | uniq -c | sort -r