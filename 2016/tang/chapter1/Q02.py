#Q02: 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

sequence1 = "パトカー"
sequence2 = "タクシー"

list02_1 = list(sequence1)
list02_2 = list(sequence2)

list02 = [x+y for (x,y) in zip(list02_1,list02_2)]

print("".join(list02))
