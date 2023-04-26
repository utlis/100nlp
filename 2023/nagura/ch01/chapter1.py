import pprint
import string
import re
import random
# 00. 文字列の逆順

word = 'stressed'
word_rv = word[::-1]
print('00. 文字列の逆順:' + ' ' + word_rv)

# 01. 「パタトクカシーー」

def get_odd_character(word: str):
    word_odd = word[0::2]
    return word_odd

print('01. 「パタトクカシーー」:' + ' ' + get_odd_character('パタトクカシーー'))


# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」

def get_add_character(word_1: str, word_2: str):
    len_max = max([len(word_1), len(word_2)])
    word = ''
    for i in range(len_max):
        word += word_1[i]
        word += word_2[i]
    return word

print('02. 「パトカー」+ 「タクシー」=「パタトクカシーー」:' + ' ' + get_add_character('パトカー', 'タクシー'))

# 03. 円周率

def get_characters_count(text: str):
    text = text.translate(text.maketrans('', '', string.punctuation))
    words = text.split(' ')
    character_count = []

    for word in words:
        character_count.append(len(word))
    return character_count

word_count = get_characters_count('Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.')

print(f'03. 円周率:  {word_count}')


# 04. 元素記号

text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can'
text = text.translate(text.maketrans('', '', string.punctuation))

words = text.split(' ')

dic = {}
for num, word in enumerate(words,1):
    if num in [1,5,6,7,8,9,16,19]: #set型のほうがベター
        dic[num] = word[0]
    else:
        dic[num] = word[:2]
print('\n 04. 元素記号:')
pprint.pprint(dic)

########### 追記 ###############
#one = {1,5,6,...}
#if num+1 in one: 


# 05. n-gram


def n_gram(text:str, num:int): 
    n_gram_list = []
#    text = text.replace(' ',"")
    for i in range(len(text) -num +1):
        n_gram_list.append(text[i:i+num])
    return n_gram_list

print('\n 05. n-gram:')
print(n_gram('I am an NLPer', 2))

text = 'I am an NLPer'
words = text.split(' ') #私も実質は一緒。関数分けていることになる。
print(n_gram(words, 2))


# 06. 集合

print('\n 06. 集合:')

# 文字bi-gramをとってそれを集合にする
X = set(n_gram('paraparaparadise', 2))
Y = set(n_gram('paragraph', 2))

union = X.union(Y)
intersect = X.intersection(Y)
diff = X.difference(Y)

print(f'和集合: {union}')
print(f'積集合: {intersect}')
print(f'差集合: {diff}')

def check_elm(s, target):
    for elm in target:
        if elm == s:
            return f'この中には文字列{s}が含まれます'
            break
    else:
        return f"この集合の中に文字列{s}は含まれていません"

print('Xについて:' , check_elm('se', X))
print('Yについて:' , check_elm('se', Y))

# 07. テンプレートによる文生成

print('\n 07. テンプレートによる文生成:')
def generate_sen(x,y,z):
    return f'{x}時の{y}は{z}'

print(generate_sen(12, '気温', 22.4))

# 08. 暗号文
print('\n 08. 暗号文:')

def cipher(text):
    character_list = n_gram(text, 1)
    character_list_encode = [chr(219 - ord(s)) if s.islower() else s for s in character_list] # encode    
    character_list_rev = [chr(219 - ord(s)) if s.islower() else s for s in character_list_encode] # decode
    
    return "".join(character_list_encode) , "".join(character_list_rev)

#            for s_encode in text_encode:
#               if s_encode.islower() == True:
#                   s_rev = chr(219 + ord(s_encode))
#                   text_rev = text_encode.translate(s_encode.maketrans({s_encode: s_rev}))            
#                   return text_rev
#           return text_encode

print(cipher('I am an NLPerz'))


###### 追記: 本田さんコード 
def cipher_honda(strings):
  message = "" #空文字に足していく形なら，aがもう一度zからaにされてしまう問題が起こらない
  for i in strings:
    if 97 <= ord(i) <= 122:
      message += chr(219-ord(i))
    else:
      message += i
  return message

print(cipher_honda('I am an NLPerz'))


print('\n 09. Typoglycemia:')

def random_character(text):
    words = text.split(" ")
    for index, word in enumerate(words):
        if len(word) > 4:
            word_ext = word[1:-1]
            characters = list(n_gram(word_ext, 1))
            random.shuffle(characters)
            random_characters = ''.join(characters)
            words[index] = word[0] + random_characters + word[-1]
            print(words)
    return " ".join(words)

### 本田さんコード
def sorting(sequence):
  sequence = sequence.split(" ")
  answer = []
  for word in sequence:
    if len(word) <= 4:
      answer.append(word)
    else:
      random.seed(0) # 乱数シードを固定
      middle = random.sample(word[1:len(word)-1], len(word[1:len(word)-1])) #len(word)は何回も出ているので、何か変数名をつけてしまったほうがいい
      answer.append(word[0] + "".join(middle) + word[len(word)-1])  
  return " ".join(answer)


## 藤井さんコード
def typoglycemia(str9):
    list9 = []
    for s9 in str9.split():
        if len(s9) > 4:
            s9 = s9[0] + ''.join(random.sample(s9[1:-1], len(s9[1:-1]))) + s9[-1]
        list9.append(s9) #ここでappendすれば、elseを書かなくていい
    return ' '.join(list9)

print(random_character('I couldn’t believe that I could actually understand what I was reading: the phenomenal power of the human mind.'))
