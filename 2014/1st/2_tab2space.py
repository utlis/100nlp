# 1st set (2)
import re

f = open("address.txt", "r")
o = open("address_t2s.txt", "w")

for line in f:
	o.write(re.sub('\t', ' ', line))

f.close()
o.close()

# > sed -e "s/\t/ /g" address.txt >> address_t2s_sed.txt
# > cat address.txt | tr "\t" " " >> address_t2s_tr.txt
# > expand -t 1 address.txt >> address.t2s_expand.txt
