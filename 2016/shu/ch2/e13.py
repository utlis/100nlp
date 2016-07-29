#! /usr/bin/env python
# coding: utf-8
# e13.py
# 2016-07-05
#

def fileMerge(filea, fileb):
    file_ina = open(filea)
    linesa = list(file_ina.readlines())
    file_inb = open(fileb)
    linesb = list(file_inb.readlines())
    linec = ''
    for linea, lineb in zip(linesa, linesb):
        linec += linea + '\t' + lineb
    file_out = open('results.txt', 'w')
    file_out.write(linec)

fileMerge('col1.txt', 'col2.txt')
