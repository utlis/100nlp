"""
Obtain the string that concatenates the 1st, 3rd, 5th, and 7th letters in the string “schooled”.
https://nlp100.github.io/en/ch01.html#01-schooled
"""

word = "schooled"
ans_index = [1, 3, 5, 7]

ans = ""
for i in ans_index:
    ans += word[i - 1]

print(ans)
