#Q17: 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

def diff(f):
    return set([e.strip() for e in f.readlines()])

if __name__ == '__main__':
    with open("col1.txt",encoding="utf-8") as f:
        prefectures=diff(f)
    print(prefectures)

# $ sort col1.txt | uniq -c | sort -r
