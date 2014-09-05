# 1st set (1)

f = open("address.txt", "r")
line_counter = 0
for line in f:
	line_counter += 1

print(line_counter)

f.close()
