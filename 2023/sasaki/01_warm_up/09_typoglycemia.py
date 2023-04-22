"""
Write a program with the specification:
- Receive a word sequence separated by space
- For each word in the sequence:
    - If the word is no longer than four letters, keep the word unchanged
    - Otherwise,
        - Keep the first and last letters unchanged
        - Shuffle other letters in other positions (in the middle of the word)

Observe the result by giving a sentence, 
e.g., “I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind “.
https://nlp100.github.io/en/ch01.html#09-typoglycemia
"""

# https://en.wikipedia.org/wiki/Transposed_letter_effect#Internet_meme


import random


def typoglycemia(src: str) -> str:
    """
    空白区切りの文字列を受け取り、5文字以上の単語について真ん中の文字列をランダムにシャッフルする
    """
    words = src.split(" ")
    out = []

    for w in words:
        if len(w) <= 4:
            out.append(w)
            continue

        middle = w[1:-1]
        shuffled = "".join(random.sample(middle, len(middle)))
        out.append(w[0] + shuffled + w[-1])

    return " ".join(out)


sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind"
print(typoglycemia(sentence))
