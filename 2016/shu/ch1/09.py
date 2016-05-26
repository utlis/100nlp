#! /usr/bin/env python
# coding: utf-8
# 09.py
# 2016-05-18
#

import re
import random

def typoglycemia(sentence):
    results = []
    for word in re.split('\W+', sentence):
        w_len = len(word)
        if w_len <= 4:
            reordered = word
        else:
            w_head = word[0]
            w_middle = random.sample(word[1:w_len-1], w_len - 2)
            w_tail = word[-1]
            reordered = w_head + ''.join(w_middle) + w_tail

        results.append(reordered)

    return ' '.join(results)


sentence = 'I couldn\'t believe that I could actually understand what I was reading: the phenomenal power of the human mind.'
print typoglycemia(sentence)
