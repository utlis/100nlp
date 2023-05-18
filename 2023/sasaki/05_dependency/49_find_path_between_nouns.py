"""
Extract the shortest paths between all pairs of noun clauses in a sentence
If index of noun clauses are i, j(i < j), the dependency path satisfy the following specifications.
- Same as Problem 48, Join every element on the path by " -> "
- Noun phrases in the clause i and j need to be replaced to X and Y

A shape of dependency path can be following 2 pattern.
- The case where clause j exists on the path from clause i to the root: show the path from clause i to j.
- The case where the paths from each noun clause to the root have the same clause k: join the paths from i or j to k(exluding k) and k by "|" , and show it

https://nlp100.github.io/ja/ch05.html#49-%E5%90%8D%E8%A9%9E%E9%96%93%E3%81%AE%E4%BF%82%E3%82%8A%E5%8F%97%E3%81%91%E3%83%91%E3%82%B9%E3%81%AE%E6%8A%BD%E5%87%BA
"""
import copy
from typing import Tuple
from chunk_sentence import Chunk, Sentece
import load_data

root = load_data.load()

for sentence_node in root:

    if len(sentence_node) == 0:
        continue
    sentence = Sentece(sentence_node)

    # get pairs of noun chunks
    noun_chunks: list[Chunk] = []
    for chunk in sentence.chunks:
        is_noun_chunk = False
        for morph in chunk.morphs:
            if morph.pos == "名詞":
                is_noun_chunk = True
                break

        if is_noun_chunk == True:
            noun_chunks.append(chunk)

    noun_chunk_pairs: list[Tuple[Chunk, Chunk]] = []
    for first_index in range(0, len(noun_chunks)):
        for second_index in range(first_index + 1, len(noun_chunks)):
            noun_chunk_pairs.append(
                (copy.deepcopy(noun_chunks[first_index]), copy.deepcopy(noun_chunks[second_index])))

    # extract the path between noun pairs
    for first_chunk, second_chunk in noun_chunk_pairs:
        first_chunk_path_to_root = sentence.gather_chunks_to_root(
            first_chunk.id)

        # convert nouns to X, Y
        is_X_found = False
        for morph in first_chunk.morphs:
            if morph.pos == "名詞":
                # prevent X from duplicating
                if is_X_found == False:
                    morph.surface = "X"
                    is_X_found = True
                else:
                    morph.surface = ""

        is_Y_found = False
        for morph in second_chunk.morphs:
            if morph.pos == "名詞":
                if is_Y_found == False:
                    morph.surface = "Y"
                    is_Y_found = True
                else:
                    morph.surface = ""

        # see if second_chunk is in the path from first_chunk to root
        chunk_buffer = [first_chunk]
        is_second_chunk_in_path = False
        for c in first_chunk_path_to_root[1:]:
            chunk_buffer.append(c)
            if c.id == second_chunk.id:
                print(" -> ".join(map(lambda v: v.to_text(),
                      [*chunk_buffer[:-1], second_chunk])))
                is_second_chunk_in_path = True
                break

        if is_second_chunk_in_path == True:
            continue

        # case of second pattern
        second_chunk_path_to_root = sentence.gather_chunks_to_root(
            second_chunk.id)

        # search k
        ids_of_first_chunk_path_to_root = list(
            map(lambda c: c.id, first_chunk_path_to_root))
        k: Chunk | None = None
        for c in second_chunk_path_to_root[1:]:
            if c.id in ids_of_first_chunk_path_to_root:
                k = c
                break

        # print the path with specified format
        path_first_to_k = [first_chunk]
        path_second_to_k = [second_chunk]
        for c in first_chunk_path_to_root[1:]:
            if k.id == c.id:
                break
            path_first_to_k.append(c)
        for c in second_chunk_path_to_root[1:]:
            if k.id == c.id:
                break
            path_second_to_k.append(c)

        first_path_text = " -> ".join(map(lambda v: v.to_text(),
                                      path_first_to_k))
        second_path_text = " -> ".join(map(lambda v: v.to_text(),
                                       path_second_to_k))

        print(f"{first_path_text} | {second_path_text} | {k.to_text()}")
