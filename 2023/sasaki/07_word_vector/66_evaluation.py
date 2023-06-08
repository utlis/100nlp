from gensim.models import KeyedVectors
import pandas as pd
import numpy as np
from tqdm import tqdm
tqdm.pandas()

model = KeyedVectors.load_word2vec_format(
    './GoogleNews-vectors-negative300.bin.gz', binary=True)


def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


model = KeyedVectors.load_word2vec_format(
    './GoogleNews-vectors-negative300.bin.gz', binary=True)
combined_df = pd.read_csv('combined.csv')
combined_df['cos_sim'] = combined_df.progress_apply(
    lambda row: cos_sim(model[row['Word 1']], model[row['Word 2']]), axis=1)
spearman_corr = combined_df[['Human (mean)', 'cos_sim']].corr(
    method='spearman')
print(f'spearman corr: {spearman_corr}')

# spearman corr:               Human (mean)   cos_sim
# Human (mean)      1.000000  0.700017
# cos_sim           0.700017  1.000000
