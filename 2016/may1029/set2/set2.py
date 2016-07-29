# !/usr/bin/python3
# coding:UTF-8
# NLP100knock set2

from collections import Counter
import re
import sys
import itertools

def merge(fname1, fname2):
    print('(13).col1.txtとcol2.txtのマージ ')
    f1 = open(fname1, 'r')
    f2 = open(fname2, 'r')

    for line1 in f1.readlines():
        print(line1.strip(), f2.readline().strip(), sep='\t')

    f1.close()
    f2.close()

#14. 先頭からN行を出力
#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
def head(num):
    cnt = 0
    print('(14).先頭からn行出力')

    with open('hightemp.txt', mode='r', encoding='UTF-8') as f:
        for line in f:
            cnt += 1

            if int(num) >= cnt:
                print(line.strip())

#15. 末尾のN行を出力
#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
def tail(num, total_num):
    cnt = 0
    print('(15).末尾からn行出力')

    with open('hightemp.txt', mode='r', encoding='UTF-8') as f:
        for line in f:
            cnt += 1

            if cnt > total_num - int(num):
                print(line.strip())

#16.ファイルをN分割する
#自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
def division(num):

    print('(16).n分割')
    with open('hightemp.txt', mode='r', encoding='UTF-8') as f:
        data = [line.strip() for line in f.readlines()]

        for i in itertools.zip_longest(*[iter(data)]* int(num)):
            for j in i:
                print(j)
            print('---->next')

def main():

    argvs = sys.argv
    with open("hightemp.txt", mode='r', encoding='UTF-8') as f:
        cnt = 0
        fw1 = open('col1.txt', 'w')
        fw2 = open('col2.txt', 'w')

        for line in f:
            line = line.strip()

            #(10).行数のカウント
            #行数をカウントせよ．確認にはwcコマンドを用いよ．
            cnt += 1

            #(11).タブをスペースに置換する
            #タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
            line = line.replace('\t',' ')

            #(12).1列目をcol1.txtに，2列目をcol2.txtに保存
            #各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
            line = line.split()
            fw1.write(line[0]+'\n')
            fw2.write(line[1]+'\n')

            print(line)
        print('(10).行数のカウント：', cnt)
        fw1.close()
        fw2.close()
    #(13).col1.txtとcol2.txtをマージ
    #12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
    merge('col1.txt', 'col2.txt')

    if len(argvs) == 1:
        print('input the number with file name')
    else:
        head(argvs[1])
        tail(argvs[1], cnt)
        division(argvs[1])

    #17. １列目の文字列の異なり
    #1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
    with open('col1.txt', mode='r', encoding='UTF-8') as f:
        data = [line.strip() for line in f]
        print('(17).文字列の異なり数:', len(set(data)))

    #18.各行を3コラム目の数値の降順にソート
    #各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
    with open('hightemp.txt', mode='r', encoding='UTF-8') as f:
        data = [line.strip().split('\t') for line in f]

        print('(18).ソート')
        d_sort = sorted(data, key=lambda x:x[2], reverse=False)
        
        for i in d_sort:
            print(i)

        #19.各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
        #各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
        print('(19).出現頻度の検索')

        column1 = [i[0] for i in data]
        counter = Counter(column1)

        for word, cnt in counter.most_common():
            print(word, cnt)

if __name__ == '__main__':
    main()

