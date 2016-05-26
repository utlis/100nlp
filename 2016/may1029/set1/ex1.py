# !/usr/bin/python3
# coding:UTF-8
# 準備運動

from itertools import chain
import re
import random

def n_gram(uni,n):
    lst = []

    for i in range(0, len(uni)-n+1):
        lst.append(uni[i:i+n])

    return lst

def lst_change(bigram):
    lst = []

    for i in bigram:
        lst.append(''.join(i))

    return lst

def str_check(list, string):
    if string in list:
        return 'Hit'
    else:
        return 'nothing'

def return_string(x, y, z):
    string = str(x)+'時の'+y+'は'+str(z)

    return string

def cipher(string):
    lst = []

    for i in string:
        search = re.search('[a-z]', i)
        if search:
            c = 219-ord(i)
            lst.append(chr(c))
        else:
            lst.append(i)

    return lst

def string_shuffle(string):
    lst = []

    print(string)

    return lst

def main():

    #00:文字列の逆順
    #文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
    s0 = list('stressed')
    print('00:', ''.join(reversed(s0)))

    #01:「パタトクカシーー」
    #「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
    s1 = list('パタトクカシーー')
    print('{0}{1}{2}{3}{4}'.format('01:',s1[0],s1[2],s1[4],s1[6]))

    #02:「パトカー」＋「タクシー」＝「パタトクカシーー」
    #「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
    s2_a = list('パトカー')
    s2_b = list('タクシー')
    print('{0}{1}{2}{3}{4}{5}{6}{7}{8}'.format('02:',s2_a[0],s2_b[0],s2_a[1],s2_b[1],s2_a[2],s2_b[2],s2_a[3],s2_b[3]))

    #03:円周率
    #"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
    s3 = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    for i in s3.split():
        search1 = re.search('(\w+)\\,', i)
        search2 = re.search('(\w+)\\.', i)
        if search1:
            print(len(search1.group(1)), end=' ')
        elif search2:
            print(len(search2.group(1)), end=' ')
        else:
            print(len(i), end=' ')
    print()

    #04:元素記号
    #"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ
    s4 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    lst = [1,5,6,7,8,9,15,16,19]
    dict = {}
    for index, i in enumerate(s4.split()):
        if index+1 in lst:
            dict[index+1] =list(i)[0]
        else:
            dict[index+1] = ''.join(list(i)[0:2])
    print('04:', dict)

    #05:n-gram
    #与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
    s5 = 'I am an NLPer'
    word = n_gram(s5.split(), 2)
    string = n_gram(list(chain.from_iterable(s5)), 2)

    print('word bi-gram:', word)
    print('string bi-gram:', string)

    #06:集合
    #"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
    s6_a = 'paraparaparadise'
    s6_b = 'paragraph'

    x = lst_change(n_gram(list(chain.from_iterable(s6_a)), 2))
    y = lst_change(n_gram(list(chain.from_iterable(s6_b)), 2))

    s = set(x)
    print('union:', s.union(y))
    print('intersection:', s.intersection(y))
    print('difference:', s.difference(y))

    check_x = str_check(x, 'se')
    check_y = str_check(y, 'se')

    print(check_x)
    print(check_y)

    #07. テンプレートによる文生成
    #引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ
    s7 = return_string(12, '気温', 22.4)
    print('07:', s7)

    #08:暗号文
    #与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
    #英小文字ならば(219 - 文字コード)の文字に置換
    #その他の文字はそのまま出力
    #この関数を用い，英語のメッセージを暗号化・復号化せよ．

    s8 = 'NovbeLNoteSelection'
    print('08:', s8, end='-->')

    c = cipher(list(chain.from_iterable(s8)))
    print(''.join(c))

    #09:Typoglycemia
    #スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
    s9 = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    string = s9.split()
    print(string)
    shuffle = []
    sentence = []

    sentence.append(string[0])

    for i in string[1:-1]:
        if len(i) < 5:
            if len(shuffle) == 0:
                sentence.append(i)
            else:
                random.shuffle(shuffle)
                sentence.extend(shuffle)
                sentence.append(i)
                shuffle = []
        else:
            shuffle.append(i)

    sentence.append(string[-1])
    print(sentence)

if __name__ == '__main__':
    main()
