#Q19: 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

from collections import Counter

def frq(f):
    l=[e.strip() for e in f.readlines()]
    frq_table=["\t".join(map(str,e)) for e in Counter(l).most_common()]
    return "\n".join(frq_table)

if __name__ == '__main__':
    with open("col1.txt",encoding="utf-8") as f:
        rslt=frq(f)
    print(rslt)

# $ cut -f 1 hightemp.txt | sort | uniq -c | sort -r
