# 1st (8)
from operator import itemgetter

file = []
with open("address.txt", "r") as f:
	for line in f:
		file.append(line.rsplit('\t'))

sort = sorted(file, key=itemgetter(1))

with open("sorted_address.txt", "w") as o:
	for s in sort:
		o.write(s[0] + '\t' + s[1])

# > sort -k 2 address.txt >> sorted_address.txt

# none itemgetter!
# file.append(tupple(line.rsplit('\t')))
# sorted(file, key=lambda x: x[1])

## ver.miyata
# import re
# import sys
# argv = sys.argv
# f = open(argv[1], 'r')
# #dicAddress = {}

# keyAddress = []
# valAddress = []

# for line in f:
#   temp = line.split('\t')
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

# # print(len(keyAddress))
# # print(len(valAddress))

# #リストから辞書作成（http://d.hatena.ne.jp/yumimue/20071207/1197016595）
# dicAddress = dict(zip(keyAddress, valAddress))
# #print(dicAddress)

# #keyでソート
# #for k, v in sorted(dicAddress.items()):
# #  print(k, v)

# #valueでソート（http://blog.livedoor.jp/yawamen/archives/51492355.html）
# for k, v in sorted(dicAddress.items(), key=lambda x:x[1]):
#     print (k, v)
