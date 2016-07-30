#Q15: 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

import sys

def tail(f,n=1):
    tails=f.readlines()[-n:]
    return "".join(tails)

if __name__ == '__main__':
    f=sys.argv[1]
    with open(f,encoding="utf-8") as f15:
        tailcontents=tail(f15,int(sys.argv[2]))
    print(tailcontents)

# $ tail -n i hightemp.txt
