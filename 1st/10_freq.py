# 1st (10)
with open("col2.txt", "r") as file:
	keys = set([x.rstrip() for x in file.readlines()])
	zeros = [x*0 for x in range(0,len(keys))]
	counter = dict(zip(keys, zeros))
	file.seek(0)
	for line in file:
		counter[line.rstrip()] += 1

outset = ((k, counter[k]) for k in sorted(counter, key=counter.get, reverse=True))

with open("freq_ranking.txt", "w") as out:
	for i,j in outset:
		out.write(i + '\t' + str(j) + '\n')

# sort col2.txt | uniq -c | sort -n -r | less  >> freq_ranking.txt
