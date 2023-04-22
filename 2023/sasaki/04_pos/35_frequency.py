"""
Obtain the list of words and frequencies of their occurrences sorted by descending order of frequency.
https://nlp100.github.io/en/ch04.html#35-frequency-of-words
"""

from load_data import load_data


tokens = load_data()

freq = {}

for token in tokens:
    text = token["text"]

    if text not in freq:
        freq[text] = 0

    freq[text] += 1

freq = list(freq.items())
freq.sort(key=lambda x: x[1], reverse=True)

for text, num in freq:
    print(f"{num}: {text}")
