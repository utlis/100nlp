# 1st (6)
import sys

f = open("address.txt", "r")
n = int(sys.argv[1])

line_counter = 0
for line in f:
	line_counter += 1

head = line_counter - n
f.seek(0,0)

while head > 0:
	f.readline()
	head -= 1

while n > 0:
	print(f.readline().rstrip())
	n -= 1
	
f.close()

# tail address.txt
