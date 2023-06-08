from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
from gensim.models import KeyedVectors
import pandas as pd
# import matplotlib
# matplotlib.use('Svg')


# https://stefangabos.github.io/world_countries/
countries_df = pd.read_csv('country_names.csv')

model = KeyedVectors.load_word2vec_format(
    './GoogleNews-vectors-negative300.bin.gz', binary=True)


registered_countries = countries_df['Country'].tolist()
conclusion_model_countries = list(
    filter(lambda name: name in model, registered_countries))
countries_df = countries_df[countries_df['Country'].isin(
    conclusion_model_countries)].reset_index(drop=True)

countries_vec = [model[country]
                 for country in countries_df['Country'].tolist()]


Z = linkage(countries_vec, method='ward')
dendrogram(Z, labels=countries_df['Country'].tolist())

plt.figure()
plt.show()
# it did not work, why?
# plt.savefig('fig68.png')
