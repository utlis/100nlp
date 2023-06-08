"""
63. Analogy based on the additive composition
Subtract the vector of “Madrid” from the vector of “Spain” and then add the vector of “Athens”. 
Compute the top-10 most similar words with the output vector.
"""
import time
import gensim

if __name__ == '__main__':
    start = time.time()
    model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
    vector = model.most_similar(positive = ['Spain', 'Athens'], negative = ['Madrid'], topn = 1)
    # print(vector) # [('Greece', 0.6898480653762817)]
    # print(vector[0][0]) # ('Greece', 0.6898480653762817)
    print(model.most_similar(positive = vector[0][0]))
    end = time.time()
    print(end - start, '[s]')
"""
[('Greek', 0.7041071057319641), ('Greeks', 0.6697883009910583), ('Portugal', 0.6540822386741638), ('Greeces', 0.6317958235740662), ('Ioannis_Drymonakos', 0.6196171045303345), ('Officer_Gary_Pignato', 0.616828978061676), ('eurozone', 0.6108282208442688), ('Mihalis_Kakiouzis', 0.604263424873352), ('Cyprus', 0.602921724319458), ('Ioannis_Christou', 0.6002818942070007)]
65.33345007896423 [s]
"""
