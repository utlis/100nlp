"""
Research the cases(格) that can appear with a predicate(述語) by using this wikipedia document as corpus.
See a verb as a predicate, and a particle(助詞) as a case, and print them by tab-separated format.
Following specification need to be satisfied.
- In verb-included clause, define a base format of the first verb as a predict
- Define a particle that depends on a predicate as a case
- If clauses that have a case and depend on predicate are multiple, print all cases with space-separated format, and dictionary order.
https://nlp100.github.io/ja/ch05.html#45-%E5%8B%95%E8%A9%9E%E3%81%AE%E6%A0%BC%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%E3%81%AE%E6%8A%BD%E5%87%BA
"""

from typing import Tuple

from morph import Morph
from chunk_sentence import Chunk, Sentece
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
        cases: list[str] = []
        for chunk in src_chunks:
            for morph in chunk.morphs:
                if morph.pos == "助詞":
                    cases.append(morph.surface)

        cases.sort()
        space_separated_cases = " ".join(cases)

        print(f"{verb_morph.base}\t{space_separated_cases}")

# unix command comfilmination
# python 45_extract_verb_case.py | sort | uniq -c | sort -nr | head -n 10
# python 45_extract_verb_case.py | sort | uniq -c | sort -nr | grep "行う"
# python 45_extract_verb_case.py | sort | uniq -c | sort -nr | grep " なる" # 「なる」 hits also 「異なる」
# python 45_extract_verb_case.py | sort | uniq -c | sort -nr | grep "与える"
