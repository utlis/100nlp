"""
Japanese ver
Extract all the pairs of src and dst chunks with tab-separated format.
Marks such as punctuation have to be excluded.
https://nlp100.github.io/ja/ch05.html#42-%E4%BF%82%E3%82%8A%E5%85%83%E3%81%A8%E4%BF%82%E3%82%8A%E5%85%88%E3%81%AE%E6%96%87%E7%AF%80%E3%81%AE%E8%A1%A8%E7%A4%BA

English ver
For each sentence, extract the root word (whose head is ROOT).
https://nlp100.github.io/en/ch05.html#42-show-root-words
"""

from chunk_sentence import Sentece
import load_data

root = load_data.load()

print("print dependency as normal text")
for sentence_node in root:
    if len(sentence_node) == 0:
        continue
    sentence = Sentece(sentence_node)
    print(sentence.dependency_as_text(divider="\t", exclude_pos=["特殊"]))
    print("""
------
""")
