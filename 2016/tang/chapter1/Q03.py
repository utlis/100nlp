#Q3: "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

sequence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
list03 = [a.strip(',.') for a in list(sequence.split(' '))]
list03 = list(map(lambda a:len(a), list03))
print(list03)
