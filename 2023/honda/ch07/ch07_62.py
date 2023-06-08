"""
62. Top-10 most similar words 
Find the top-10 words that have the highest cosine similarity with the word “United States” and print out the similarity score.
"""
import time
import gensim

if __name__ == '__main__':
    start = time.time()
    model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
    print(model.most_similar(positive = ['United_States'], topn = 10))
    end = time.time()
    print(end - start, '[s]')

"""
[('Unites_States', 0.7877248525619507), ('Untied_States', 0.7541370987892151), ('United_Sates', 0.7400725483894348), ('U.S.', 0.7310774922370911), ('theUnited_States', 0.6404394507408142), ('America', 0.6178409457206726), ('UnitedStates', 0.6167312264442444), ('Europe', 0.6132988929748535), ('countries', 0.6044804453849792), ('Canada', 0.6019068956375122)]
65.07272219657898 [s]
"""
