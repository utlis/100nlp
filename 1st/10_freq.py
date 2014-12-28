# 1st (10)
with open("col2.txt", "r") as file:
	keys = set([x.rstrip() for x in file.readlines()])
	zeros = [x*0 for x in range(0,len(keys))]
	counter = dict(zip(keys, zeros))
	file.seek(0)
	for line in file:
		counter[line.rstrip()] += 1

class Counter(dict):
	# 未定義のkeyに対して初期値0を返すdict
	def __missing__(self, key):
		return 0

c = Counter() # same as Hash.new(0) in Ruby

outset = ((k, counter[k]) for k in sorted(counter, key=counter.get, reverse=True))

with open("freq_ranking.txt", "w") as out:
	for i,j in outset:
		out.write(i + '\t' + str(j) + '\n')

# sort col2.txt | uniq -c | sort -n -r | less  >> freq_ranking.txt

# ver.miyata
# from operator import itemgetter, attrgetter
# import re
# import sys
# #argv = sys.argv
# f = open('col2.txt', 'r')
# #dicAddress = {}

# keyAddress = []
# valAddress = []

# count = {}

# # counting
# for line in f:
#   line = line.rstrip()
#   count[line] = count.get(line,0) + 1

# # sort by count
# d = [(v,k) for k,v in count.items()]
# d.sort()
# d.reverse()
# for count, word in d:
#     print(count, word)
