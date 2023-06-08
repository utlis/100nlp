"""
67. k-means clustering
Extract the word vectors of the country names. 
Apply k-means clustering where k=5.
"""
"""
# 参考情報
grep -n : ch07_64-answer.txt  
1:: capital-common-countries
508:: capital-world
5033:: currency
5900:: city-in-state
8368:: family
8875:: gram1-adjective-to-adverb
9868:: gram2-opposite
10681:: gram3-comparative
12014:: gram4-superlative
13137:: gram5-present-participle
14194:: gram6-nationality-adjective
15794:: gram7-past-tense
17355:: gram8-plural
18688:: gram9-plural-verbs
"""
import time
import pandas as pd
from sklearn.cluster import KMeans
import gensim
from tqdm import tqdm

def get_names_vectors(model, file):
    country_names = []
    country_vectors = []
    with open(file, 'r') as f:
        for line in tqdm(f):
            line = line.strip().split(' ')
            if len(line) != 4:
                if line[1] == 'capital-world': 
                    topic = 'country'
                else:
                    topic = 'others'
            else:
                if topic == 'country':
                    if line[1] not in country_names:
                        vector = model[line[1]]
                        country_names.append(line[1])
                        country_vectors.append(vector)
    return country_names, country_vectors


if __name__ == '__main__':
    start = time.time()

    model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
    country_names, country_vectors = get_names_vectors(model, 'questions-words.txt')

    kmeans = KMeans(n_clusters = 5, random_state = 0).fit_predict(country_vectors)

    for country, cluster in zip(country_names, kmeans):
        print(f'cluster {cluster}\t{country}')

    end = time.time()
    print(end - start, '[s]')
"""
19558it [00:00, 787793.96it/s]
cluster 4       Nigeria
cluster 4       Ghana
cluster 2       Algeria
cluster 2       Jordan
cluster 1       Turkey
cluster 4       Madagascar
cluster 0       Samoa
cluster 1       Turkmenistan
cluster 4       Eritrea
cluster 1       Kazakhstan
cluster 1       Greece
cluster 2       Iraq
cluster 1       Azerbaijan
cluster 4       Mali
cluster 2       Thailand
cluster 4       Gambia
cluster 2       China
cluster 2       Lebanon
cluster 1       Serbia
cluster 0       Belize
cluster 3       Germany
cluster 3       Switzerland
cluster 1       Kyrgyzstan
cluster 1       Slovakia
cluster 3       Belgium
cluster 1       Romania
cluster 1       Hungary
cluster 4       Burundi
cluster 2       Egypt
cluster 3       Australia
cluster 0       Venezuela
cluster 1       Moldova
cluster 4       Guinea
cluster 3       Denmark
cluster 4       Senegal
cluster 2       Syria
cluster 2       Bangladesh
cluster 2       Qatar
cluster 3       Ireland
cluster 1       Tajikistan
cluster 0       Tuvalu
cluster 4       Botswana
cluster 0       Guyana
cluster 2       Vietnam
cluster 4       Zimbabwe
cluster 0       Cuba
cluster 3       Finland
cluster 2       Pakistan
cluster 2       Indonesia
cluster 2       Afghanistan
cluster 4       Uganda
cluster 2       Nepal
cluster 4       Sudan
cluster 1       Ukraine
cluster 4       Rwanda
cluster 0       Jamaica
cluster 4       Gabon
cluster 4       Malawi
cluster 0       Peru
cluster 3       Portugal
cluster 1       Slovenia
cluster 3       England
cluster 4       Angola
cluster 4       Zambia
cluster 3       Spain
cluster 0       Nicaragua
cluster 2       Bahrain
cluster 0       Philippines
cluster 4       Mozambique
cluster 1       Belarus
cluster 4       Somalia
cluster 4       Liberia
cluster 0       Uruguay
cluster 1       Russia
cluster 2       Oman
cluster 4       Kenya
cluster 0       Bahamas
cluster 4       Niger
cluster 1       Cyprus
cluster 4       Mauritania
cluster 3       Greenland
cluster 3       Norway
cluster 3       Canada
cluster 0       Suriname
cluster 3       France
cluster 1       Montenegro
cluster 0       Ecuador
cluster 2       Morocco
cluster 1       Latvia
cluster 3       Italy
cluster 0       Dominica
cluster 0       Chile
cluster 1       Macedonia
cluster 1       Bulgaria
cluster 3       Sweden
cluster 0       Fiji
cluster 0       Taiwan
cluster 1       Estonia
cluster 1       Uzbekistan
cluster 1       Georgia
cluster 0       Honduras
cluster 2       Iran
cluster 2       Bhutan
cluster 1       Albania
cluster 3       Japan
cluster 2       Libya
cluster 2       Tunisia
cluster 3       Liechtenstein
cluster 3       Malta
cluster 3       Austria
cluster 2       Laos
cluster 1       Lithuania
cluster 1       Poland
cluster 4       Namibia
cluster 1       Armenia
cluster 1       Croatia
57.54950189590454 [s]
"""