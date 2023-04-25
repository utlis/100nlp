"""
Implement a function that obtains n-grams from a given sequence object (e.g., string and list). 
Use this function to obtain word bi-grams and letter bi-grams from the sentence “I am an NLPer”
https://nlp100.github.io/en/ch01.html#05-n-gram
"""


from ngram_generator import generate_n_gram

sentence = "I am an NLPer"

word_bi_gram = generate_n_gram(2, sentence.split(" "))
letter_bi_gram = generate_n_gram(2, sentence)


print("word_bi_gram: {}".format(word_bi_gram))
print("letter_bi_gram: {}".format(letter_bi_gram))
