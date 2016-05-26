#! /usr/bin/env python
# coding: utf-8
# 05.py
# 2016-05-16
#

def nGram(sentence, n):
    if isinstance(n, (int, long)):

        word_results = []
        character_results = []
        s_len = len(sentence.split())
        words = sentence.split()

        if s_len >= n:
            for i in range(0, s_len - n + 1):
                word_results.append(words[i:i + n ])

        for word in sentence.split():
            w_len = len(word)
            if w_len >= n:
                for j in range(0, w_len - n + 1):
                    character_results.append(word[j:j + n])

        return [word_results, character_results]

    else:
        print "Please input an integer."


w_results, c_results = nGram('I am an NLPer', 2)
print '単語: ' + str(w_results)
print '文字: ' + str(c_results)
