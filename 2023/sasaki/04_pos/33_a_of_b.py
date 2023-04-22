"""
Extract noun phrases in the form of “A of B”, where A and B are nouns.
https://nlp100.github.io/en/ch04.html#33-a-of-b
"""

from typing import Literal
from load_data import Token, load_data


tokens = load_data()


MODE: Literal["SEARCHING_FIRST_NOUN", "SEARCHING_OF",
              "SEARCHING_AFTER_NOUN"] = "SEARCHING_FIRST_NOUN"

result: list[list[Token]] = []
buffered: list[Token] = []

for token in tokens:

    match token["pos"]:
        case "名詞":
            if MODE == "SEARCHING_AFTER_NOUN":
                buffered.append(token)
                result.append(buffered)
                buffered = []
                MODE = "SEARCHING_FIRST_NOUN"

            elif MODE == "SEARCHING_FIRST_NOUN" or MODE == "SEARCHING_OF":
                buffered = []
                MODE = "SEARCHING_OF"
                buffered.append(token)

        case "助詞":
            if MODE == "SEARCHING_OF" and token["text"] == "の":
                buffered.append(token)
                MODE = "SEARCHING_AFTER_NOUN"
            else:
                buffered = []
                MODE = "SEARCHING_FIRST_NOUN"

        case _:
            MODE = "SEARCHING_FIRST_NOUN"
            buffered = []


for tokens in result:
    phrase = ""
    for token in tokens:
        phrase += token["text"]

    print(phrase)
