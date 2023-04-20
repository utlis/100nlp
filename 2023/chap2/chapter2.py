import pandas as pd
import numpy as np
import pprint
import sys

#from more_itertools import chunked

def read_f(file_name):
    with open(file_name, 'r') as f:
        return f.read()

def read_as_df(file_name):
    with open(file_name, 'r') as f:
        df = pd.read_csv(f, sep = '\t', header = None) 
        return df

def save_f(file_name, text):
    with open(file_name, 'x') as f:
        f.write(text)


# 10. Line countPermalink
# Count the number of lines of the file. Confirm the result by using wc command.
with open('popular-names.txt', 'r') as f:
    data = f.readlines() # read 'popular-names.txt' as a list
print(len(data))

# 11. Replace tabs into spaces
# Replace every occurrence of a tab character into a space. Confirm the result
# by using sed, tr, or expand command.

data = read_f('popular-names.txt')
data_notab = data.replace('\t', ' ') 
# save_f('popular-names_notab', data_notab)

# re.sub: redular expression substitution
### unlike replace(), sub() requires patterns which should be replaced. Regular Expressions are available.


# 12. col1.txt from the first column, col2.txt from the second columnPermalink
# Extract the value of the first column of each line, and store the output into
# col1.txt. Extract the value of the second column of each line, and store the
# output into col2.txt. Confirm the result by using cut command.

df = read_as_df('./popular-names.txt') 
    ###  read files as a table. By default, it will take the first line of the text file as a header.
    ### if you add names = ['', '', ..], you can set the header.
df[0].to_csv('./col1_py.txt', index=False, header=None)
df[1].to_csv('./col2_py.txt', index=False, header=None)
    ## data type of df[n] is Series. The function .write() canot recieve Series type.

# 13. Merging col1.txt and col2.txtPermalink
# Join the contents of col1.txt and col2.txt, and create a text file whose each
# line contains the values of the first and second columns (separated by tab
# character) of the original file. Confirm the result by using paste command.

col1  = read_as_df('./col1_py.txt')
col2 = read_as_df('./col2_py.txt')
cols = pd.concat([col1, col2], axis=1) # combine dfs
cols.to_csv('./cols.txt', sep=('\t'), index=False, header=None)

### concat: combine dfs which are same structures
### merge: combine dfs by using specific columns
### join: combine dfs by using index

# 14. First N linesPermalink
# Receive a natural number $N$ from a command-line argument, and output the first
# $N$ lines of the file. Confirm the result by using head command.

print(df.head(3))

# 15. Last N linesPermalink
# Receive a natural number $N$ from a command-line argument, and output the
# last $N$ lines of the file. Confirm the result by using tail command.

print(df.tail(5))

# 16. Split a file into N piecesPermalink
# Receive a natural number $N$ from a command-line argument, and split the
# input file into $N$ pieces at line boundaries. Confirm the result by using
# split command.

with open('popular-names.txt', 'r') as f:
    data = f.readlines() # read 'popular-names.txt' as a list

n = int(sys.argv[1])
lines_len = len(data)
q = lines_len // n # quotient
r = lines_len % n ## remainder

lines = []

for i in range(0,2):
    lines = []
    lines = data[i*q:(i+1)*q]
    print(len(lines))

#for i in range(n):
#    print(df.iloc[i*q: (i+1)*q])

#for l in data, range(0,927):
#    lines = 
#print(len(lines))    
#
#for i in range(0,r):
#    lines = []
#    for l in data, range(x):
#        lines.append(l)
#    print(len(lines))
#
#
#def df_split(data_frame, n):
#    lines = len(df)
#    if lines % n == 0:


n = 3
lines = len(df)
q = lines // n # quotient
r = lines % n ## remainder

#print(lines)
#
#for i in range(n):
#    print(df.iloc[i*q: (i+1)*q])
#
#for i in range(1,n+1):
#    if r ==0:
#        if i == 1:
#            print(df.iloc[0: q +1])
#        else:
#            print(df.iloc[i*q+1: (i+1)*q +1])
#    elif i <= r:
#        if i == 1:
#            print(df.iloc[0: q +1])
#        else:
#            print(df.iloc[(i-1)*q+1: i*q +2])
#    elif i > r:
#        print(df.iloc[(i-1)*q+r::q])

# 17. Distinct strings in the first columnPermalink
# Find distinct strings (a set of strings) of the first column of the file.
# Confirm the result by using cut, sort, and uniq commands.

print(df[0].unique())

# 18. Sort lines in descending order of the third columnPermalink
# Sort the lines in descending numeric order of the third column (sort lines
# without changing the content of each line). Confirm the result by using sort
# command.

df.columns = ['name', 'gender', 'num_birth','birth_year']
df = df.sort_values(by='num_birth', ascending=False)
print(df)


## 19. Frequency of a string in the first column in descending orderPermalink
# Find the frequency of a string in the first column, and sort the strings by
# descending order of their frequencies. Confirm the result by using cut, uniq,
# and sort commands.

dic = {}
for i , value in df['name'].value_counts().iteritems():
    dic[i] = value

dic_sorted = sorted(dic.items(), key = lambda x:x[1], reverse=True)    


# ここ pprint.pprint(dic_sorted)
