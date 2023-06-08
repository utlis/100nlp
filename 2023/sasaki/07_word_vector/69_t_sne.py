import numpy as np
import pandas as pd
from gensim.models import KeyedVectors
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Svg')

# https://stefangabos.github.io/world_countries/
countries_df = pd.read_csv('country_names.csv')

model = KeyedVectors.load_word2vec_format(
    './GoogleNews-vectors-negative300.bin.gz', binary=True)

# extract valid country names
registered_countries = countries_df['Country'].tolist()
conclusion_model_countries = list(
    filter(lambda name: name in model, registered_countries))


countries_df = countries_df[countries_df['Country'].isin(
    conclusion_model_countries)].reset_index(drop=True)

countries_vec = np.array([model[country]
                          for country in countries_df['Country'].tolist()])

tsne = TSNE(random_state=42, n_iter=15000, metric='cosine')
embs = tsne.fit_transform(countries_vec)

plt.figure(figsize=(10, 10))
plt.scatter(np.array(embs).T[0], np.array(embs).T[1])
for (x, y), name in zip(embs, countries_df['Country'].tolist()):
    plt.annotate(name, (x, y))
plt.savefig("69_result.svg")
