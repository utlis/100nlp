#Q06: "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

import Q05

X=set(Q05.ngram_alphabet("paraparaparadise"))
Y=set(Q05.ngram_alphabet("paragraph"))

XuY = X&Y
XnY = X|Y
XdY =X-Y
print(X,Y,XuY,XnY,XdY)

assert "se" in XnY,"'se' not in X or Y"
