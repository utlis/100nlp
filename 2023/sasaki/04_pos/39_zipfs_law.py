"""
Plot a log-log graph with the x-axis being rank order and the y-axis being frequency.
https://nlp100.github.io/en/ch04.html#39-zipfs-law
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

# default x value is `range(len(y))`
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
ax.loglog(values)
ax.set_xlabel("rank number")
ax.set_ylabel("word frequency")
ax.set_title('[39] Zipf\'s law')

# you can choose to save or show graph. Choosing both at once do not work
# plt.show()
plt.savefig("result_39_zipfs_law.png")
