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
