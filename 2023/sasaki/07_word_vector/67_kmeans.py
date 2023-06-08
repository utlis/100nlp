import numpy as np
import pandas as pd
from gensim.models import KeyedVectors
from sklearn.cluster import KMeans

CLUSTER_NUMBER = 5

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

# get vectors of country names
countries_vec = [model[country]
                 for country in countries_df['Country'].tolist()]

kmeans = KMeans(n_clusters=CLUSTER_NUMBER, random_state=42, n_init="auto")
kmeans.fit(countries_vec)
for i in range(CLUSTER_NUMBER):
    cluster = np.where(kmeans.labels_ == i)[0]
    print(f'cluster: {i}')
    print(countries_df.iloc[cluster]["Country"].tolist())

# cluster: 0
# ['Bahamas', 'Barbados', 'Belize', 'Chile', 'Colombia', 'Cuba', 'Dominica', 'Ecuador', 'Fiji', 'Grenada', 'Guatemala', 'Guyana', 'Haiti', 'Honduras', 'Jamaica', 'Kiribati', 'Mexico', 'Nauru', 'Nicaragua', 'Palau', 'Panama', 'Peru', 'Philippines', 'Samoa', 'Suriname', 'Tonga', 'Tuvalu', 'Vanuatu']
# cluster: 1
# ['Albania', 'Armenia', 'Azerbaijan', 'Belarus', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia', 'Estonia', 'Georgia', 'Greece', 'Hungary', 'Kazakhstan', 'Kyrgyzstan', 'Latvia', 'Lithuania', 'Malta', 'Montenegro', 'Poland', 'Romania', 'Serbia', 'Slovakia', 'Slovenia', 'Tajikistan', 'Türkiye', 'Turkmenistan', 'Ukraine', 'Uzbekistan']
# cluster: 2
# ['Andorra', 'Argentina', 'Australia', 'Austria', 'Belgium', 'Brazil', 'Canada', 'Denmark', 'Finland', 'France', 'Germany', 'Iceland', 'Ireland', 'Italy', 'Japan', 'Liechtenstein', 'Luxembourg', 'Monaco', 'Netherlands', 'Norway', 'Paraguay', 'Portugal', 'Spain', 'Sweden', 'Switzerland', 'Uruguay']
# cluster: 3
# ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burundi', 'Cameroon', 'Comoros', 'Congo', 'Djibouti', 'Eritrea', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Kenya', 'Lesotho', 'Liberia', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Senegal', 'Seychelles', 'Somalia', 'Sudan', 'Togo', 'Uganda', 'Zambia', 'Zimbabwe']
# cluster: 4
# ['Afghanistan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Cambodia', 'Chad', 'China', 'Egypt', 'India', 'Indonesia', 'Iraq', 'Israel', 'Jordan', 'Kuwait', 'Lebanon', 'Libya', 'Malaysia', 'Maldives', 'Mauritius', 'Mongolia', 'Morocco', 'Myanmar', 'Nepal', 'Oman', 'Pakistan', 'Qatar', 'Singapore', 'Thailand', 'Tunisia', 'Yemen']
