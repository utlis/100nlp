"""
Implement a program that reads the result of part-of-speech tagging.
Here, represent a sentence as a list of mapping objects, 
each of which associates a surface form, lemma (base form), part-of-speech tag with the keys text, lemma, pos.
Use this representation in the rest of the problems.
https://nlp100.github.io/en/ch04.html#30-reading-the-result
"""

from load_data import load_data


tokens = load_data()

for token in tokens:
    print(token)
