#Q00: 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．


sequence = 'stressed'
strtolist = list(sequence)
strtolist.reverse()
print(''.join(strtolist))
