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

# ver.miyata
# import re
# fcol1 = open('col1.txt', 'r')
# fcol2 = open('col2.txt', 'r')

# listcol1 = []
# listcol2 = []

# for line in fcol1:
#   listcol1.append(line)

# for line in fcol2:
#   listcol2.append(line.rstrip())

# for i in range(len(listcol1)):
#     print(listcol1[i]+"\t"+listcol2[i])
