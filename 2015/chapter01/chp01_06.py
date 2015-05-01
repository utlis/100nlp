# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

import chp01_05 as p05

X = set(p05.n_gramizer("paraparaparadise", 2, unit="char"))
Y = set(p05.n_gramizer("paragraph", 2, unit="char"))

print(X | Y)
print(X & Y)
print(X - Y)

print("check containment of 'se'")
print(('s', 'e') in X)
print(('s', 'e') in Y)
