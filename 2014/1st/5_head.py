# 1st (5)
import sys

f = open("address.txt", "r")
n = int(sys.argv[1])

while n > 0:
	print(f.readline().rstrip())
	n -= 1
	
f.close()

# head address.txt
