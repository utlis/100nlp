# 1st (3)
import re

f = open("address.txt", "r")
col1 = open("col1.txt", "w")
col2 = open("col2.txt", "w")

for line in f:
	cols = re.split('\t', line)
	col1.write(cols[0] + "\n") # write don't put \n
	col2.write(cols[1])

f.close()
col1.close()
col2.close()

# > cut -f 1 address.txt >> col1_cut.txt
# > cut -f 2 address.txt >> col2_cut.txt
