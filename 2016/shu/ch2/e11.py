#! /usr/bin/env python
# coding: utf-8
# 11.py
# 2016-05-22
#

def tabToSpace(path):
    file = open(path)
    results = ''
    for line in file:
        result = line.expandtabs(1)
        results += result
    file.close()
    return results

print tabToSpace('hightemp.txt')

# sed s/$'\t'/' '/g hightemp.txt
# tr '\t' ' ' < hightemp.txt
# expand -t 1 hightemp.txt