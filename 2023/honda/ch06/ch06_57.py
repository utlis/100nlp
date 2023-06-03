"""
57. Feature weights
Use the logistic regression model from the problem 52. 
Check the feature weights and list the 10 most important features and 10 least important features.
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
# from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import time

if __name__ == '__main__':
    start = time.perf_counter()
    time.sleep(5)
    with open('vocabulary.pkl', 'rb') as f:
        vocabulary = pickle.load(f) # 単語: idの辞書
    with open('model.pkl', 'rb') as g:
        model = pickle.load(g)
    coefs = model.coef_
    # print(len(coefs[2])) # 11293
    # print(len(vocabulary)) # 11293
    # categories = model.classes_ # ['b' 'e' 'm' 't']
    categories = ['business', 'entertaiment', 'health', 'science and technology'] 
    for i, features in enumerate(coefs):
        feature_dic = {}
        for word, id in vocabulary.items():
            feature_dic[word] = features[id]
        feature_dic = sorted(feature_dic.items(), key = lambda x: x[1], reverse = True) # 並び替え 
        # print(feature_dic[0], feature_dic[1])
        for j in range(10):
            print(f'Top {j+1} feature in {categories[i]}\t{feature_dic[j][0]}: {feature_dic[j][1]}')
        for j in range(10):
            print(f'Bottom {j+1} feature in {categories[i]}\t{feature_dic[-(j+1)][0]}: {feature_dic[-(j+1)][1]}')
    # print(feature_dic[1:4])
    # print(vocabulary)  
    end = time.perf_counter()
    processing_time = end - start
    print(processing_time) 
"""
Top 1 feature in business	bank: 3.779643279019193
Top 2 feature in business	fed: 3.4091899820888263
Top 3 feature in business	ecb: 3.0689651951682597
Top 4 feature in business	updat: 2.96323079621412
Top 5 feature in business	stock: 2.848878263846995
Top 6 feature in business	ukrain: 2.6449357140307344
Top 7 feature in business	china: 2.6411645534316506
Top 8 feature in business	profit: 2.5688529790798538
Top 9 feature in business	euro: 2.5587652519516055
Top 10 feature in business	buy: 2.446355001157935
Bottom 1 feature in business	facebook: -1.9111526075460756
Bottom 2 feature in business	googl: -1.880901046407094
Bottom 3 feature in business	ebola: -1.790221823102996
Bottom 4 feature in business	star: -1.7211476168285271
Bottom 5 feature in business	kardashian: -1.6643132437325208
Bottom 6 feature in business	video: -1.546005090673032
Bottom 7 feature in business	climat: -1.5189616387518987
Bottom 8 feature in business	aereo: -1.4666225370198724
Bottom 9 feature in business	mer: -1.445869436026335
Bottom 10 feature in business	could: -1.4450612563434062
Top 1 feature in entertaiment	kardashian: 3.3648813630721683
Top 2 feature in entertaiment	star: 2.764963451916072
Top 3 feature in entertaiment	chri: 2.676832692783225
Top 4 feature in entertaiment	movi: 2.5858880649630454
Top 5 feature in entertaiment	kim: 2.547411191456812
Top 6 feature in entertaiment	film: 2.5360308666845914
Top 7 feature in entertaiment	miley: 2.484938429050846
Top 8 feature in entertaiment	cyru: 2.418128468929661
Top 9 feature in entertaiment	wed: 2.3415419624974785
Top 10 feature in entertaiment	beyonc: 2.166244173614235
Bottom 1 feature in entertaiment	updat: -4.02663774398418
Bottom 2 feature in entertaiment	us: -3.0977374767942654
Bottom 3 feature in entertaiment	googl: -2.689643085844021
Bottom 4 feature in entertaiment	studi: -2.272898229225903
Bottom 5 feature in entertaiment	ceo: -2.2651925226323004
Bottom 6 feature in entertaiment	china: -2.2412421481368923
Bottom 7 feature in entertaiment	say: -2.216044182446634
Bottom 8 feature in entertaiment	buy: -2.120102358944678
Bottom 9 feature in entertaiment	facebook: -2.087718649171551
Bottom 10 feature in entertaiment	gm: -2.0283630393224943
Top 1 feature in health	ebola: 4.1375774890507016
Top 2 feature in health	studi: 3.681298017654345
Top 3 feature in health	cancer: 3.4492815307359335
Top 4 feature in health	drug: 3.306857794703176
Top 5 feature in health	mer: 3.249450129796003
Top 6 feature in health	fda: 3.162341946522138
Top 7 feature in health	ecigarett: 2.9767940104872577
Top 8 feature in health	health: 2.600498039332113
Top 9 feature in health	doctor: 2.534863699682902
Top 10 feature in health	outbreak: 2.5340823882006704
Bottom 1 feature in health	deal: -1.1031897565996729
Bottom 2 feature in health	facebook: -1.0159829437690444
Bottom 3 feature in health	gm: -1.0102858986115042
Bottom 4 feature in health	bank: -0.9361753147459071
Bottom 5 feature in health	appl: -0.8796648125511833
Bottom 6 feature in health	profit: -0.8598610547390728
Bottom 7 feature in health	googl: -0.851606586993934
Bottom 8 feature in health	climat: -0.8308972210649641
Bottom 9 feature in health	ceo: -0.8206015042972885
Bottom 10 feature in health	sale: -0.7783052799557107
Top 1 feature in science and technology	googl: 5.422150719245039
Top 2 feature in science and technology	facebook: 5.014854200486679
Top 3 feature in science and technology	appl: 4.228160280533907
Top 4 feature in science and technology	climat: 3.861672243623154
Top 5 feature in science and technology	microsoft: 3.5538010515506455
Top 6 feature in science and technology	gm: 2.86818683598764
Top 7 feature in science and technology	tesla: 2.827394331003576
Top 8 feature in science and technology	fcc: 2.62444549755479
Top 9 feature in science and technology	nasa: 2.503120069186873
Top 10 feature in science and technology	tmobil: 2.37563342208146
Bottom 1 feature in science and technology	drug: -1.3707852716969884
Bottom 2 feature in science and technology	fed: -1.2025048783285472
Bottom 3 feature in science and technology	rate: -1.1984983892227772
Bottom 4 feature in science and technology	high: -1.0819761906459833
Bottom 5 feature in science and technology	cancer: -1.026694527251823
Bottom 6 feature in science and technology	hi: -1.01900011600687
Bottom 7 feature in science and technology	case: -0.9836382858374282
Bottom 8 feature in science and technology	kardashian: -0.9768765863375586
Bottom 9 feature in science and technology	ecb: -0.9540361803220371
Bottom 10 feature in science and technology	ukrain: -0.9315763039269392
5.066612333
"""