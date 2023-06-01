"""
Download News Aggregator Data Set and create training data (train.txt), validation data (valid.txt) and test data (test.txt) as follows:

- Unpack the downloaded zip file and read readme.txt.
- Extract the articles such that the publisher is one of the followings: 
  “Reuters”, “Huffington Post”, “Businessweek”, “Contactmusic.com” and “Daily Mail”.
- Randomly shuffle the extracted articles.
- Split the extracted articles in the following ratio: the training data (80%), the validation data (10%) and the test data (10%). 
  Then save them into files train.txt, valid.txt and test.txt, respectively. 
  In each file, each line should contain a single instance. 
  Each instance should contain both the name of the category and the article headline. Use Tab to separate each field.

After creating the dataset, check the number of instances contained in each category.
https://nlp100.github.io/en/ch06.html#50-download-and-preprocess-dataset
"""
import csv
import math
import random

SPECIFIED_PUBLISHERS = ["Reuters", "Huffington Post",
                        "Businessweek", "Contactmusic.com", "Daily Mail"]

TRAIN_RATIO = 0.8
VALIDATION_RATIO = 0.1

rf = open("newsCorpora.csv")
# clear quote character because bad format data is included, such as following data
# 210713	"The Best Reactions To The Supposed Video of Solange Knowles & Jay Z  ...	http://www...
csv_reader = csv.reader(rf, delimiter="\t", quotechar=None)

matched_news = []

for row in csv_reader:
    publisher = row[3]
    # how deal with branches of "Reuters", like "Reuters India"
    if publisher in SPECIFIED_PUBLISHERS:
        matched_news.append(row)

random.seed(100)
random.shuffle(matched_news)

l = len(matched_news)
train_last_index = math.ceil(TRAIN_RATIO*l)
valid_last_index = math.ceil((TRAIN_RATIO + VALIDATION_RATIO)*l)

train_data = matched_news[:train_last_index]
valid_data = matched_news[train_last_index + 1:valid_last_index]
test_data = matched_news[valid_last_index + 1:]


print(f"""data count:
train_data: {len(train_data)}
valid_data: {len(valid_data)}
test_data: {len(test_data)}""")

train_wf = csv.writer(open("train.txt", "w"), delimiter="\t", quotechar=None)
valid_wf = csv.writer(open("valid.txt", "w"), delimiter="\t", quotechar=None)
test_wf = csv.writer(open("test.txt", "w"), delimiter="\t", quotechar=None)

writer_pairs = [(train_wf, train_data), (valid_wf,
                                         valid_data), (test_wf, test_data)]
for wf, data in writer_pairs:
    d = list(map(lambda r: [r[1], r[4]], data))
    wf.writerows(d)

# count data grouped by categories
# cat train.txt valid.txt test.txt | cut -f 2 | sort -n | uniq -c
