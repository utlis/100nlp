"""
69. t-SNE Visualization
Visualize the word vector space of the country names by t-SNE.
"""
import time
import gensim
from tqdm import tqdm
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from ch07_67 import get_names_vectors

if __name__ == '__main__':
    start = time.time()

    model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
    country_names, country_vectors = get_names_vectors(model, 'questions-words.txt')
    
    embedding = TSNE(random_state = 0).fit_transform(country_vectors)

    # print(embedding)
    # print(len(embedding), len(country_names), len(country_vectors))

    plt.figure(figsize = (16, 12))
    for i, vec in enumerate(embedding):
        plt.scatter(vec[0], vec[1])
        plt.annotate(country_names[i], (vec[0], vec[1]))
    plt.savefig('tsne.png')
    plt.show()


    end = time.time()
    print(end - start, '[s]')

"""
19558it [00:00, 668025.52it/s]
/Users/tomonohonda/opt/anaconda3/lib/python3.9/site-packages/sklearn/manifold/_t_sne.py:780: FutureWarning: The default initialization in TSNE will change from 'random' to 'pca' in 1.2.
  warnings.warn(
/Users/tomonohonda/opt/anaconda3/lib/python3.9/site-packages/sklearn/manifold/_t_sne.py:790: FutureWarning: The default learning rate in TSNE will change from 200.0 to 'auto' in 1.2.
  warnings.warn(
101.51794934272766 [s]
"""

