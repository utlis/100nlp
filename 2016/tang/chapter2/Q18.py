#Q18: 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

def col3_sort(f):
    l=[e.strip().split("\t") for e in f.readlines()]
    l_sorted=sorted(l,key=lambda x: x[2],reverse=True)
    l_sorted=["\t".join(e2) for e2 in l_sorted]
    l_new="\n".join(l_sorted)
    return l_new

if __name__ == '__main__':
    with open("hightemp.txt",encoding="utf-8") as f:
        rslt=col3_sort(f)
    print(rslt)

# $ sort -k 3,3 -r hightemp.txt
