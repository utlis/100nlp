# 00. 文字列の逆順
# 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

text = "stressed"
source = list(text)

print(''.join(reversed(source)))
# reversed()はコピー、[list].reverseは破壊的

# text[::-1]

#outcome = ""
#for i in source:
#	outcome += source.pop()

#print(outcome)

# quotient, remainder = divmod(len(listbox), 2)  # => (x // y, x % y)
