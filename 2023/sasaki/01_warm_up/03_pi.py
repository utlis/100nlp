"""
Split the sentence “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.” into words, 
and create a list whose element presents the number of alphabetical letters in the corresponding word.
https://nlp100.github.io/en/ch01.html#03-pi
"""

sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# word でないものを除外する
# カンマや空白の処理方法は、場合によりそう
normalized = sentence.replace(",", "").replace(".", "")

splitted = normalized.split(" ")

ans = []
for word in splitted:
    ans.append(len(word))

print(ans)
