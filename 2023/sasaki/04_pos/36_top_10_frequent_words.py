"""
Visualize the top-ten frequent words and their frequencies with a chart (e.g., bar chart).
https://nlp100.github.io/en/ch04.html#36-top-ten-frequent-words
"""

from load_data import load_data
import matplotlib.pyplot as plt
# needed for displaying Japanese character
import japanize_matplotlib

tokens = load_data()

freq = {}

for token in tokens:
    text = token["text"]

    if text not in freq:
        freq[text] = 0

    freq[text] += 1

freq = list(freq.items())
freq.sort(key=lambda x: x[1], reverse=True)

top_ten = freq[:10]

names = list(map(lambda t: t[0], top_ten))
values = list(map(lambda t: t[1], top_ten))


fig, ax = plt.subplots()

ax.barh(names, values)
ax.invert_yaxis()
ax.set_title('[36] Top 10 frequent words')

# you can choose to save or show graph. Choosing both at once do not work
# plt.show()
plt.savefig("result_36_top_10_frequent_words.png")
