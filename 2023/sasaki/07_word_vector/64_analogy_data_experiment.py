from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format(
    './GoogleNews-vectors-negative300.bin.gz', binary=True)


rf = open('./questions-words.txt', 'r')
wf = open('./questions-words-add.txt', 'w')

for line in rf:
    line = line.split()
    if line[0] == ':':
        category = line[1]
    else:
        word, cos = model.most_similar(
            positive=[line[1], line[2]], negative=[line[0]], topn=1)[0]
        wf.write(' '.join([category] + line + [word, str(cos) + '\n']))

# 1h26m8s
