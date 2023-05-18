"""
Extract a path from all clauses that have a noun to the root.
The path on syntax structure tree satisfy the following specification
- Every clause is represented by the list of surfaces of morpheme
- Join every element on the path by " -> "
https://nlp100.github.io/ja/ch05.html#48-%E5%90%8D%E8%A9%9E%E3%81%8B%E3%82%89%E6%A0%B9%E3%81%B8%E3%81%AE%E3%83%91%E3%82%B9%E3%81%AE%E6%8A%BD%E5%87%BA
"""
from chunk_sentence import Sentece
import load_data

root = load_data.load()

for sentence_node in root:

    if len(sentence_node) == 0:
        continue
    sentence = Sentece(sentence_node)

    for chunk in sentence.chunks:
        is_noun_chunk = False
        for morph in chunk.morphs:
            if morph.pos == "名詞":
                is_noun_chunk = True
                break

        if is_noun_chunk == False:
            continue

        path_to_root = sentence.gather_chunks_to_root(chunk.id)
        print(" -> ".join(map(lambda v: v.to_text(), path_to_root)))
