#Q08: 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(l):
    for n in range(0,len(l)):
        if l[n].islower() == True:l[n] = chr(219-ord(l[n]))
    return "".join(l)

print(cipher(list("WhatEver08")))
