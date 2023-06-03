"""
51. Feature extraction
Extract a set of features from the training, validation and test data, respectively. 
Save the features into files as follows: train.feature.txt, valid.feature.txt and test.feature.txt. 
Design the features that are useful for the news classification. 
The minimum baseline for the features is the tokenized sequence of the news headline.
"""

import pandas as pd
import os
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import time



def preprocessing(title):
    title = ''.join([char for char in title if char not in string.punctuation]) # removing punctuation
    title = nltk.word_tokenize(title) # tokenization
    # lemmatizer = WordNetLemmatizer()
    # title = [lemmatizer.lemmatize(word) for word in title] # lemmatize
    porter = PorterStemmer()
    title = [porter.stem(word) for word in title]   # stemming
    stop_words = stopwords.words('english') 
    title = ' '.join([word for word in title if word not in stop_words]) # stopword Filtering
    return title

    
if __name__ == '__main__':
    start = time.perf_counter()
    time.sleep(5)

    train_df = pd.read_csv('train.txt', sep = '\t')
    valid_df = pd.read_csv('valid.txt', sep = '\t')
    test_df = pd.read_csv('test.txt', sep = '\t')

    train_df['TITLE'] = train_df['TITLE'].apply(preprocessing)
    valid_df['TITLE'] = valid_df['TITLE'].apply(preprocessing)
    test_df['TITLE'] = test_df['TITLE'].apply(preprocessing)

    vectorizer = TfidfVectorizer()
    vectorizer.fit(train_df['TITLE'])

    train_tfidf = vectorizer.transform(train_df['TITLE'])
    valid_tfidf = vectorizer.transform(valid_df['TITLE'])
    test_tfidf = vectorizer.transform(test_df['TITLE'])

    pd.DataFrame(train_tfidf.toarray()).to_csv('train.feature.txt', sep = '\t', index = False, header = None)
    pd.DataFrame(valid_tfidf.toarray()).to_csv('valid.feature.txt', sep = '\t', index = False, header = None)   
    pd.DataFrame(test_tfidf.toarray()).to_csv('test.feature.txt', sep = '\t', index = False, header = None)

    with open('vocabulary.pkl', 'wb') as f:
        pickle.dump(vectorizer.vocabulary_, f)
    
    end = time.perf_counter()

    processing_time = end - start
    print(processing_time) # 129.67255708399998