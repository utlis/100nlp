"""
68. Ward's method clustering
Apply hierarchical clustering to the word vectors of the country names. 
Use Ward's method for the distance metric between two clusters. 
Visualize the clustering result as the dendrogram.
"""

import time
import gensim
from tqdm import tqdm
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from ch07_67 import get_names_vectors

if __name__ == '__main__':
    start = time.time()

    model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
    country_names, country_vectors = get_names_vectors(model, 'questions-words.txt')
    
    Z = linkage(country_vectors, method = 'ward')
    dn = dendrogram(Z, labels = country_names)
    
    plt.savefig('dendrogram.png')
    plt.show()

    end = time.time()
    print(end - start, '[s]')
"""
19558it [00:00, 703746.39it/s]
132.3689670562744 [s]
"""
    
