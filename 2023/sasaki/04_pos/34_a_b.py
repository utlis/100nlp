"""
Extract noun phrases in the form of “A of B”, where A and B are nouns.
https://nlp100.github.io/en/ch04.html#33-a-of-b
"""

from load_data import Token, load_data


tokens = load_data()

result: list[list[Token]] = []
buffered: list[Token] = []

for token in tokens:

    match token["pos"]:
        case "名詞":
            buffered.append(token)

        case _:
            if len(buffered) > 0:
                result.append(buffered)

            buffered = []


for tokens in result:
    phrase = ""
    for token in tokens:
        phrase += token["text"]

    print(phrase)
