"""
Draw a histogram of word frequency (x-axis is a scalar range representing a frequency ranging 
from 1 to the largest frequency of a given word in the entire corpus, 
and the y-axis is the count of unique words that fall into the count of the x value).
https://nlp100.github.io/en/ch04.html#38-histogram
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


# get largest frequency and value list
freq = list(freq.items())
freq.sort(key=lambda x: x[1], reverse=True)
values = list(map(lambda t: t[1], freq))
x_max = values[0]

# draw graph
fig, ax = plt.subplots()

ax.hist(values, bins=(x_max // 100))
ax.set_xlabel("word frequency")
ax.set_ylabel("count of unique words")
ax.set_title('[38] histogram of word frequency')

# you can choose to save or show graph. Choosing both at once do not work
# plt.show()
plt.savefig("result_38_histogram.png")
