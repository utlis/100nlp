"""
Improve the program of Problem 45 to append clause that depend on a predicate to a predicate and cases, divided by tab.
In addition to Problem 45 specification, the following need to be satisficated.
- Clause is the list of words that depends on a predicate
- If clauses that depend on a predicate are multiple, print all clauses with space-separated format and dictionary order.
https://nlp100.github.io/ja/ch05.html#46-%E5%8B%95%E8%A9%9E%E3%81%AE%E6%A0%BC%E3%83%95%E3%83%AC%E3%83%BC%E3%83%A0%E6%83%85%E5%A0%B1%E3%81%AE%E6%8A%BD%E5%87%BA
"""
from chunk_sentence import Chunk
from typing import Tuple

from morph import Morph
from chunk_sentence import Sentece
import load_data

root = load_data.load()

print("print dependency as normal text")
for sentence_node in root:

    if len(sentence_node) == 0:
        continue
    sentence = Sentece(sentence_node)

    # find verb chunk
    verb_chunks: list[Tuple[Chunk, Morph]] = []
    for chunk in sentence.chunks:

        for morph in chunk.morphs:
            if morph.pos == "動詞":
                verb_chunks.append((chunk, morph))
                break

    if len(verb_chunks) == 0:
        continue

    # find chunk depending on verb chunk and extract cases
    for verb_chunk, verb_morph in verb_chunks:
        src_chunks = sentence.find_chunks_by_dst_id(verb_chunk.id)

        # change below from question 45
        cases: list[Tuple[str, Chunk]] = []
        for chunk in src_chunks:
            for morph in chunk.morphs:
                if morph.pos == "助詞":
                    cases.append((morph.surface, chunk))

        cases.sort(key=lambda v: v[0])
        space_separated_cases = " ".join(map(lambda v: v[0], cases))
        space_separated_chunks = " ".join(map(lambda v: v[1].to_text(), cases))

        print(f"{verb_morph.base} {space_separated_cases} {space_separated_chunks}")
