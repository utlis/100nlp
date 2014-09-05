# 1st (4)
col1 = open("col1.txt", "r")
col2 = open("col2.txt", "r")
o = open("resurrection.txt", "w")

for l1 in col1:
	o.write(l1.strip() + '\t' + col2.readline())

col1.close()
col2.close()
o.close()

# paste col1.txt col2.txt
