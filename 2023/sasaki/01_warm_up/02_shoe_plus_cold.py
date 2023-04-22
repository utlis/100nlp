"""
Obtain the string “schooled” by concatenating the letters in “shoe” and “cold” one after the other from head to tail.
https://nlp100.github.io/en/ch01.html#02-shoe--cold--schooled
"""

word1 = "shoe"
word2 = "cold"
length = 4

ans = ""
for i in range(0, length):
    ans += word1[i] + word2[i]

print(ans)
