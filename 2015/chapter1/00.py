# 00. 文字列の逆順
# 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

text = "stressed"
source = list(text)
outcome = ""

for i in source:
	outcome += source.pop()

print(outcome)

# quotient, remainder = divmod(len(listbox), 2)  # => (x // y, x % y)

# if remainder == 0:
# 	box = ["head", "tail"]
# 	for i in range(quotient):
# 		box[0] = listbox[i]
# 		box[1] = listbox[-i]
# 		listbox[i] = box[1]
# 		listbox[-i] = box[0]
# 	return listbox.join()
# else:
