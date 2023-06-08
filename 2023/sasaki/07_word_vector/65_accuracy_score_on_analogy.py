from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format(
    './GoogleNews-vectors-negative300.bin.gz', binary=True)

rf = open('./questions-words-add.txt', 'r')

sem_count = 0
sem_correct = 0
syn_count = 0
syn_correct = 0
for line in rf:
    line = line.split()
    if not line[0].startswith('gram'):
        sem_count += 1
        if line[4] == line[5]:
            sem_correct += 1
    else:
        syn_count += 1
        if line[4] == line[5]:
            syn_correct += 1

print(f'accuracy score on semantic analogy: {sem_correct/sem_count:.3f}')
print(f'accuracy score on syntactic analogy: {syn_correct/syn_count:.3f}')

# accuracy score on semantic analogy: 0.731
# accuracy score on syntactic analogy: 0.740
