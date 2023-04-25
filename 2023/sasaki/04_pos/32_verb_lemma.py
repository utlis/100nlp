"""
Extract lemmas of all verbs appearing in the text.
https://nlp100.github.io/en/ch04.html#32-base-forms-of-verbs
"""

from load_data import Token, load_data


tokens = load_data()

verbs: list[Token] = []
for token in tokens:
    if token["pos"] == "動詞":
        verbs.append(token)

for token in verbs:
    print(token["lemma"])
