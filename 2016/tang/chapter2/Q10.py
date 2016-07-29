#Q10: 行数をカウントせよ．確認にはwcコマンドを用いよ．

txt="hightemp.txt"

with open(txt,encoding="utf-8") as fr:
    l=fr.readlines()

print(len(l))

# $ wc hightemp.txt
