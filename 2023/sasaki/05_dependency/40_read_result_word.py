"""
Design a class Word that represents a word. 
This class has three member variables, text (word surface), lemma (lemma), and pos (part-of-speech). 
Represent a sentence as an array of instances of Word class. 
Implement a program to load the parse result, and store the text as an array of sentences. 
Show the object of the first sentence of the body of the article.
https://nlp100.github.io/en/ch05.html#40-read-the-parse-result-words


Design a class `Morph` that represents a morpheme.
This class has four member variables, surface(word surface),
base(word basic format), pos(part-of-speach), pos1(detailed part-of-speach).
Represent a sentence as an array of instances of `Morph` class. 
Implement a program to load the parse result, and store the text as an array of sentences. 
Show the object of the first sentence of the body of the article.
https://nlp100.github.io/ja/ch05.html#40-%E4%BF%82%E3%82%8A%E5%8F%97%E3%81%91%E8%A7%A3%E6%9E%90%E7%B5%90%E6%9E%9C%E3%81%AE%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%81%BF%E5%BD%A2%E6%85%8B%E7%B4%A0
"""

from utils import parse_token_to_morph
from chunk_sentence import Morph
import load_data

root = load_data.load()
result: list[list[Morph]] = []

for sentence in root:
    sentence_buffer = []
    for chunk in sentence:
        for token in chunk:
            sentence_buffer.append(parse_token_to_morph(token))
    result.append(sentence_buffer)


first_sentence = result[1]


for morph in first_sentence:
    print(morph.to_str())
