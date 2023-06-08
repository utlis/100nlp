"""
65. Accuracy score on the analogy task
From the output of the problem 64, compute the accuracy score on both the semantic analogy and the syntactic analogy.
"""

import time
from tqdm import tqdm

"""
# 参考情報
$ grep : questions-words.txt
: capital-common-countries
: capital-world
: currency
: city-in-state
: family
: gram1-adjective-to-adverb
: gram2-opposite
: gram3-comparative
: gram4-superlative
: gram5-present-participle
: gram6-nationality-adjective
: gram7-past-tense
: gram8-plural
: gram9-plural-verbs
"""

if __name__ == '__main__':
    start = time.time()

    topic = ''
    syn_all = 0
    syn_cor = 0
    sem_all = 0
    sem_cor = 0
    with open('ch07_64-answer.txt', 'r') as f:
        for line in f:
            line = line.strip().split(' ')
            if len(line) != 6:
                if line[1].startswith('gram'): # compute syntactic analogy
                    topic = 'syntactic'
                else:
                    topic = 'semantic'
            else:
                if topic == 'syntactic':
                    syn_all += 1
                    if line[3] == line[4]:
                        syn_cor += 1
                else: # if topic == 'syntactic':
                    sem_all += 1
                    if line[3] == line[4]:
                        sem_cor += 1
    print(f'the accuracy score on semantic analogy: {sem_cor/sem_all}\n\
the accuracy score on syntactic analogy: {syn_cor/syn_all}')

    end = time.time()
    print(end - start, '[s]')
"""
the accuracy score on semantic analogy: 0.7308602999210734
the accuracy score on syntactic analogy: 0.7400468384074942
0.02226996421813965 [s]
"""