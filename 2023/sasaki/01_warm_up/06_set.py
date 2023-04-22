"""
Let the sets of letter bi-grams from the words “paraparaparadise” and “paragraph” $X$ and $Y$, respectively. 
Obtain the union, intersection, difference of the two sets. 
In addition, check whether the bigram “se” is included in the sets $X$ and $Y$
https://nlp100.github.io/en/ch01.html#06-set
"""

from ngram_generator import generate_n_gram

word1 = "paraparaparadise"
word2 = "paragraph"

# https://docs.python.org/2/library/stdtypes.html#frozenset
X = frozenset(generate_n_gram(2, word1))
Y = frozenset(generate_n_gram(2, word2))

union_X_Y = X.union(Y)
intersection_X_Y = X.intersection(Y)
difference_X_Y = X.difference(Y)
difference_Y_X = Y.difference(X)

print("unioin X \cup Y: {}".format(union_X_Y))
print("intersection X \cap Y: {}".format(intersection_X_Y))
print("difference X - Y: {}".format(difference_X_Y))
print("difference Y - X: {}".format(difference_Y_X))

s = "se"
print("{} in X: {}".format(s, s in X))
print("{} in Y: {}".format(s, s in Y))
