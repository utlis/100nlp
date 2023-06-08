"""
66. Evaluation on WordSimilarity-353
Download the test data from The WordSimilarity-353 Test Collection. 
Compute the spearman's rank correlation coefficient between two similarity rank scores: 
(1) similarity computed from word vectors and (2) similarity evaluated by the human.
"""

import time
import gensim
from tqdm import tqdm
import numpy as np
from scipy import stats

if __name__ == '__main__':
    start = time.time()
    model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
    wv_sim = []
    hu_sim = []
    with open('combined.csv', 'r') as f:
        for i, line in enumerate(tqdm(f)):
            if i != 0: # 最初の行はパス
                line = line.strip().split(',')
                hu_sim.append(line[2])
                vec = model.similarity(line[0], line[1])
                wv_sim.append(vec)
    result = stats.spearmanr(np.array(wv_sim), np.array(hu_sim))
    print(result)

    end = time.time()
    print(end - start, '[s]')
"""
354it [00:00, 19067.47it/s]
SpearmanrResult(correlation=0.6849564489532376, pvalue=3.3287848950141535e-50)
58.99576711654663 [s]
"""