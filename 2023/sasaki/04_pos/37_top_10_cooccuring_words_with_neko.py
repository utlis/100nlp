"""
Extract the list of words that co-occur with the word “Alice”. 
Visualize with a chart (e.g., bar chart) the top-ten words co-occurring with the word “Alice” and their frequencies.
https://nlp100.github.io/en/ch04.html#37-top-ten-words-co-occurring-with-alice
"""

# definition of co-occurence:
# when I say that A co-occur with B, it means that A and B occur in the same sentence
#
# > 語彙ネットワークの頂点は内容語や名詞に 限定する場合が多く，同義語をまとめる場合もある。辺については同一文中での共出現関係を利用する場合が多い。
# ref. 浅石卓真. テキストの特徴を計量する指標の概観. 日本図書館情報学会誌. 2017;63(3):159-169. doi:10.20651/jslis.63.3_159. p164-5

import itertools
from typing import Literal
from load_data import Token, load_data
import matplotlib.pyplot as plt
# needed for displaying Japanese character
import japanize_matplotlib

TARGET_WORD = "猫"
# define stop words by their POS
STOP_WORDS = ["補助記号", "代名詞", "助詞", "助動詞"]
TOP_N = 10

tokens = load_data()


# extract sentences which have the target word.
MODE: Literal["TARGET_SENTENCE",
              "SEARCHING_TARGET_WORD"] = "SEARCHING_TARGET_WORD"
target_sentences: list[list[Token]] = []
sentence_buffer: list[Token] = []

for token in tokens:
    if token["pos1"] == "句点":
        if MODE == "TARGET_SENTENCE":
            sentence_buffer.append(token)
            target_sentences.append(sentence_buffer)
            MODE = "SEARCHING_TARGET_WORD"
        sentence_buffer = []
    else:
        if MODE == "SEARCHING_TARGET_WORD" and token["text"] == TARGET_WORD:
            MODE = "TARGET_SENTENCE"
        sentence_buffer.append(token)

# handling for the case that last word is not "句点"
if MODE == "TARGET_SENTENCE" and len(sentence_buffer) > 0:
    target_sentences.append(sentence_buffer)

# flatten sentence list to token list
tokens = list(itertools.chain.from_iterable(target_sentences))
# omit target word
tokens = filter(lambda t: t["text"] != TARGET_WORD, tokens)


# calucurate frequencies
freq = {}
freq_noun = {}
freq_verb = {}
freq_without_stopword = {}
for token in tokens:
    text = token["text"]

    # the same texts may have different pos
    # e.g. "出来" is verb or noun
    if text not in freq:
        freq[text] = 0
    if text not in freq_noun and token["pos"] == "名詞":
        freq_noun[text] = 0
    if text not in freq_verb and token["pos"] == "動詞":
        freq_verb[text] = 0
    if text not in freq_without_stopword and token["pos"] not in STOP_WORDS:
        freq_without_stopword[text] = 0

    freq[text] += 1
    if token["pos"] == "名詞":
        freq_noun[text] += 1
    if token["pos"] == "動詞":
        freq_verb[text] += 1
    if token["pos"] not in STOP_WORDS:
        freq_without_stopword[text] += 1

# sort frequencies
# TODO: refactor
freq = list(freq.items())
freq.sort(key=lambda x: x[1], reverse=True)

freq_noun = list(freq_noun.items())
freq_noun.sort(key=lambda x: x[1], reverse=True)

freq_verb = list(freq_verb.items())
freq_verb.sort(key=lambda x: x[1], reverse=True)

freq_without_stopword = list(freq_without_stopword.items())
freq_without_stopword.sort(key=lambda x: x[1], reverse=True)

top_n = freq[:TOP_N]
top_n_noun = freq_noun[:TOP_N]
top_n_verb = freq_verb[:TOP_N]
top_n_without_stopword = freq_without_stopword[:TOP_N]

top_ns = [top_n, top_n_noun, top_n_verb, top_n_without_stopword]
top_ns_labels = ["ALL", "NOUN", "VERB", "WITHOUT_STOPWORDS"]


# draw graph
fig, axs = plt.subplots(2, 2, figsize=[12, 8])

# TODO: refactor
i = 0
for ax in axs.flat:
    names = list(map(lambda t: t[0], top_ns[i]))
    values = list(map(lambda t: t[1], top_ns[i]))
    ax.barh(names, values)
    ax.invert_yaxis()
    ax.set_title(top_ns_labels[i])

    i += 1


fig.suptitle(f'[37] Top {TOP_N} cooccuring words with {TARGET_WORD}')

# you can choose to save or show graph. Choosing both at once do not work
# plt.show()
plt.savefig(f"result_37_top_{TOP_N}_cooccuring_words.png")
