#! /usr/bin/env python
# coding: utf-8
# 08.py
# 2016-05-18
#

def cipher(message):
    result = ''
    for character in message:
        if ord(character) >= 97 and ord(character) <= 122:
            ciphered = chr(219 - ord(character))
        else:
            ciphered = character
        result += ciphered
    return result

message = 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness.'

jp = 'ストレイ・シープ'

print cipher(message)
