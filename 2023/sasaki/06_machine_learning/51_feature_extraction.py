"""
Extract a set of features from the training, validation and test data, respectively. 
Save the features into files as follows: train.feature.txt, valid.feature.txt and test.feature.txt. 
Design the features that are useful for the news classification. 
The minimum baseline for the features is the tokenized sequence of the news headline.
https://nlp100.github.io/en/ch06.html#51-feature-extraction
"""

# ref. https://utokyo-ipp.github.io/7/7-2.html

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

files = ["train", "valid", "test"]

all_data: pd.DataFrame = None


each_data_length: list[int] = []

for file in files:
    file_path = f"{file}.txt"
    print(f"load: {file_path}")
    filedata = pd.read_csv(file_path, delimiter="\t",
                           quoting=False, names=["title", "category"])

    each_data_length.append(filedata.shape[0])

    all_data = pd.concat([all_data, filedata])


print(all_data.head(5))

# https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
# use words count as title feature
vec_count = CountVectorizer()
count_vector = vec_count.fit_transform(all_data["title"])
count_vector = pd.DataFrame(count_vector.toarray(),
                            columns=vec_count.get_feature_names_out())

print(count_vector.head(5))

index_from = 0
for i in range(len(files)):
    d = count_vector[index_from:each_data_length[i]]
    print(d.shape[0])
    d.to_csv(f"{files[i]}.feature.txt", sep="\t")
