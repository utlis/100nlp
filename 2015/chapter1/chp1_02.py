# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

patocar = "パトカー"
taxi = "タクシー"

outcome = ""

for p, t in zip(patocar, taxi):
	outcome += p + t

print(outcome)
