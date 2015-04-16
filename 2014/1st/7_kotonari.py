# 1st (7)
f = open("col1.txt", "r")

words = f.readlines()
print(len(set(words)))

f.close()

# > sort col1.txt | uniq | wc
