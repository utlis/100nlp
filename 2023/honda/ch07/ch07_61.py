"""
61. Word similarity
Compute the cosine similarity between “United States” and “U.S.”
"""
import time
import gensim

if __name__ == '__main__':
    start = time.time()
    model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
    print(model.similarity('United_States', 'U.S.'))
    end = time.time()
    print(end - start, '[s]')
"""
0.73107743
55.61709690093994 [s]
"""