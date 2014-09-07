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

# ver.miyata
# from operator import itemgetter, attrgetter
# import re
# import sys
# argv = sys.argv
# f = open(argv[1], 'r')
# #dicAddress = {}

# keyAddress = []
# valAddress = []

# for line in f:
#   temp = line.split('	')
#   try:
#     keyAddress.append(temp[0])
#     valAddress.append(temp[1].rstrip())
#   except:
#     print("Error")
#     print(temp)
# #    keyAddress.append(temp[0])
# #    valAddress.append("Nil")

# #    print("not none")
# #  print(temp[1].rstrip())

# print(len(keyAddress))
# print(len(valAddress))

# dicAddress = dict(zip(keyAddress, valAddress))
# #print(dicAddress)

# #keyでソート
# #for k, v in sorted(dicAddress.items()):
# #  print(k, v)

# #valueの逆順でソート(http://docs.python.jp/3.3/howto/sorting.html)
# for k, v in sorted(dicAddress.items(), key=itemgetter(1,0),reverse=True):
#     print (k, v)

