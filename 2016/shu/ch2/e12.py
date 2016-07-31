#! /usr/bin/env python
# coding: utf-8
# 12.py
# 2016-05-22
#

def writeCols(path, col):
    filein = open(path, 'r')
    column = ''
    for line in filein:
        columns = line.split('\t')
        column += columns[col-1] + '\n'
    filename = 'col' + str(col) + '.txt'
    fileout = open(filename, 'w')
    fileout.write(column)
    fileout.close()

if __name__ == '__main__':
    writeCols('hightemp.txt', 1)
    writeCols('hightemp.txt', 2)

# cut -f1,2 hightemp.txt