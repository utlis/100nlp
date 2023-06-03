"""
50. Download and Preprocess Dataset
Download News Aggregator Data Set and create training data (train.txt), validation data (valid.txt) 
and test data (test.txt) as follows:

1. Unpack the downloaded zip file and read readme.txt.
2. Extract the articles such that the publisher is one of the followings: 
“Reuters”, “Huffington Post”, “Businessweek”, “Contactmusic.com” and “Daily Mail”.
3. Randomly shuffle the extracted articles.
4. Split the extracted articles in the following ratio: the training data (80%), 
the validation data (10%) and the test data (10%). 
Then save them into files train.txt, valid.txt and test.txt, respectively. 
In each file, each line should contain a single instance. 
Each instance should contain both the name of the category and the article headline. 
Use Tab to separate each field.

After creating the dataset, check the number of instances contained in each category.
"""

import pandas as pd
# 1. unzip NewsAggregatorDataset.zip
# 1. cat readme.txt

# 2.
df = pd.read_csv('newsCorpora.csv', sep = '\t', names =\
    ('ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP'))
# print(df.head())
# print(df.info())

df = df[df['PUBLISHER'].isin(['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail'])]
# print(df.head())
# print(df.info())

# 3.
df = df.sample(frac=1, random_state=0)
# print(df.head())

# 4.
# extract the data of category (CATEGORY) and article headline (TITLE)
df = df[['TITLE', 'CATEGORY']]
# split training, validation, and test data
df_train = df[:int(len(df)*0.8)] # train
df_valid = df[int(len(df)*0.8): int(len(df)*0.9)] # validation
df_test = df[int(len(df)*0.9): ] # test
# save files
df_train.to_csv('train.txt', index = False, sep = '\t')
df_valid.to_csv('valid.txt', index = False, sep = '\t')
df_test.to_csv('test.txt', index = False, sep = '\t')

# check the number of instances contained in each category
def count_category(text):
    df = pd.read_csv(text, sep = '\t')
    business = len(df[df['CATEGORY'] == 'b'])
    science = len(df[df['CATEGORY'] == 't'])
    entertaiment = len(df[df['CATEGORY'] == 'e'])
    health = len(df[df['CATEGORY'] == 'm'])
    return print(f'business: {business}, science and technology: {science}, entertaiment: {entertaiment}, health: {health}')

if __name__ == '__main__':
    count_category('train.txt')
    count_category('valid.txt')
    count_category('test.txt')
