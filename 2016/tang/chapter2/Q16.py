#Q16: 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ

import sys

def div(f,n=1):
    txt=f.readlines()
    length=len(txt)
    # m/n:quotient(float); m//n:quotient(int); m%n:reminder(int)
    if length % n == 0:
        divisions="\n".join(["".join(txt[i:i+length//n]) for i in range(0,length,length//n)])
        return divisions
    else:
        return "please try those numbers:"+",".join(map(str,[n for n in range(1,length+1) if length % n == 0]))

# reminder-ignored version:
#     def div(f,n=1):
#         divisions="\n".join("".join(paragraph) for paragraph in itertools.zip_longest(*[iter(txt)]*length//n,fillvalue=""))
#         return divisions

if __name__ == '__main__':
    with open("hightemp.txt",encoding='utf-8') as f:
        rslt=div(f,int(sys.argv[1]))
    print(rslt)

# $ split -l i hightemp.txt
