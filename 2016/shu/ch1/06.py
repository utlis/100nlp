#! /usr/bin/env python
# coding: utf-8
# 06.py
# 2016-05-18
#

def c_ngram(word, n):
    if isinstance(n, (int, long)):

        character_results = []
        w_len = len(word)
        if w_len >= n:
            for j in range(0, w_len - n + 1):
                character_results.append(word[j:j + n])
        return character_results

    else:
        print "Please input an integer."

word1 = 'paraparaparadise'
word2 = 'paragraph'

X = set(c_ngram(word1, 2))
Y = set(c_ngram(word2, 2))

union = X | Y
intersection = X & Y
difference = X - Y

print 'Union: ' + str(union)
print 'Intersect: ' + str(intersection)
print 'Difference: ' + str(difference) + '\n'

bi_gram = 'se'

if bi_gram in X:
    print '\'' + bi_gram + '\'' + ' is in ' + '\'' + word1 + '\''
else:
    print '\'' + bi_gram + '\'' + ' is not in ' + '\'' + word1 + '\''


if bi_gram in Y:
    print '\'' + bi_gram + '\'' + ' is in ' + '\'' + word2 + '\''
else:
    print '\'' + bi_gram + '\'' + ' is not in ' + '\'' + word2 + '\''