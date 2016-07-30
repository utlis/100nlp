#Q14: 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ

import sys

def head(f,n=1):
    heads=[f.readline() for i in range(n)]
    return "".join(heads)

if __name__ == '__main__':
    f=sys.argv[1]
    with open(f,encoding="utf-8") as f14:
        headcontents=head(f14,int(sys.argv[2]))
    print(headcontents)

# $ head -i hightemp.txt
