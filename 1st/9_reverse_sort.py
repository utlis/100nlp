# 1st (9)
adrs = []
with open("address.txt", "r") as file:
	for line in file:
		adrs.append(line.rsplit('\t'))

adrs.sort(key=lambda x: x[1], reverse=True)

prv = adrs[0][1]
scnd = []
out = open("reverse_sort.txt", "w")
for i in adrs:
	# global prv, scnd, out
	if i[1] == prv:
		scnd.append(i[0])
	else:
		scnd.sort(reverse=True)
		for j in scnd:
			out.write(j + '\t' + prv)
		prv = i[1]
		scnd = []
		scnd.append(i[0])

out.close()

# with open("col2.txt", "r") as file:
# 	global keys
# 	keys = set(file.readlines())

# adrs = []
# with open("address.txt", "r") as file:
# 	for line in file.readlines():
# 		adrs.append(line.rsplit('\t'))

# rvs = []
# sort(keys, reverse=True)
# for key in keys:
# # filter() and lambda
