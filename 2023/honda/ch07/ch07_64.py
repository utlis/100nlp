"""
64. Analogy data experiment
Download word analogy evaluation dataset. 
Compute the vector as follows: vec(word in second column) - vec(word in first column) + vec(word in third column). 
From the output vector, (1) find the most similar word and (2) compute the similarity score with the word. 
Append the most similar word and its similarity to each row of the downloaded file.
"""
import time
import gensim
from tqdm import tqdm

# ファイルの作成
def analogy_data_experiment(wv, dataset, new_files):
    with open(dataset, 'r') as f:
        with open(new_files, 'w') as g:
            for line in tqdm(f):
                line = line.strip().split(' ')
                if len(line) == 4:
                    vector = wv.most_similar(positive = [line[1], line[2]], negative = [line[0]], topn = 1)
                    result = ' '.join(line + [vector[0][0], str(vector[0][1])])
                    g.write(f'{result}\n')
                else:
                    result = ' '.join(line)
                    g.write(f'{result}\n')


if __name__ == '__main__':
    start = time.time()
    model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
    analogy_data_experiment(model, 'questions-words-copy.txt', 'ch07_64-answer.txt')
    end = time.time()
    print(end - start, '[s]')
"""
19558it [1:07:01,  4.86it/s]
4080.8371748924255 [s]
"""