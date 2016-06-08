#Q05: 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

def ngram_word(sequence,n=2):
	listw = sequence.split(' ')
	return [' '.join(listw[i:i+n]) for i in range(0,len(listw)-1)]

def ngram_alphabet(sequence,n=2):
	seqa = sequence.replace(' ','')
	return [seqa[i:i+n] for i in range(0,len(seqa)-1)]

sequence = 'I am an NLPer'
print(ngram_word(sequence))
print(ngram_alphabet(sequence))
