"""
Japanese ver
Extract all the pairs of source clause that has a noun and destination clause that have a verb,  with tab-separated format.
Marks such as punctuation have to be excluded.
https://nlp100.github.io/ja/ch05.html#43-%E5%90%8D%E8%A9%9E%E3%82%92%E5%90%AB%E3%82%80%E6%96%87%E7%AF%80%E3%81%8C%E5%8B%95%E8%A9%9E%E3%82%92%E5%90%AB%E3%82%80%E6%96%87%E7%AF%80%E3%81%AB%E4%BF%82%E3%82%8B%E3%82%82%E3%81%AE%E3%82%92%E6%8A%BD%E5%87%BA

English ver
Show all pairs of verb governors (parents) and their noun dependents (children) from all sentences in the text.
https://nlp100.github.io/en/ch05.html#43-show-verb-governors-and-noun-dependents
"""

from chunk_sentence import Sentece
import load_data

root = load_data.load()

print("print dependency as normal text")
for sentence_node in root:
    if len(sentence_node) == 0:
        continue
    sentence = Sentece(sentence_node)
    print(sentence.dependency_as_text(divider="\t", exclude_pos=[
          "特殊"], required_pos_in_dst=["動詞"], required_pos_in_src=["名詞"]))
    print("""
------
""")
