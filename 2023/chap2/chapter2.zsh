## #!usr/bin/zsh

# 10. Line countPermalink
# Count the number of lines of the file. Confirm the result by using wc command.

wc -l "popular-names.txt"

## option "-m" counts characters, option "-c" counts words



#11. Replace tabs into spacesPermalink
# Replace every occurrence of a tab character into a space. Confirm the result by using sed, tr, or expand command.

sed -e "s/\t/ /g" ./popular-names.txt > ./popular-names_notab_sed.txt
## option -e expresses "epression".
## /g enable us to replace all expressions in the target file.
## or 
cat ./'popular-names.txt' | tr '\t' ' ' > ./popular-names_notab_tr.txt

## tr replace a character to a character one by one.
## The number of characters which you would like to replace should be same as that to be replaced.
# 標準入力からの文字を削除または置換して、その結果を標準出力に書き出します >> 標準入力 vs 引数
## or 

cat './popular-names.txt' | expand -t 1 > ./popular-names_ex.txt

## expand command is the command which replace tab to space.
## unexpand: space to tab
#

# 12. col1.txt from the first column, col2.txt from the second column
# Extract the value of the first column of each line, and store the output into
# col1.txt. Extract the value of the second column of each line, and store the
# output into col2.txt. Confirm the result by using cut command.

cut -f 1 './popular-names.txt' > ./col1_zsh.txt
cut -f 2 './popular-names.txt' > ./col2_zsh.txt
### cut command: devides text by row
### -d: how you separate the text (default = \t)
### -f: the column you would like to extract

# 13. Merging col1.txt and col2.txtPermalink
# Join the contents of col1.txt and col2.txt, and create a text file whose each
# line contains the values of the first and second columns (separated by tab
# character) of the original file. Confirm the result by using paste command.

paste col1_zsh.txt col2_zsh.txt > cols_zsh.txt

# 14. First N linesPermalink
# Receive a natural number $N$ from a command-line argument, and output the first
# $N$ lines of the file. Confirm the result by using head command.

head -n 5 './popular-names.txt' 

# 15. Last N linesPermalink
# Receive a natural number $N$ from a command-line argument, and output the
# last $N$ lines of the file. Confirm the result by using tail command.

tail -n 3 './popular-names.txt'
### -n: lines
### default is 10 lines

# 16. Split a file into N piecesPermalink
# Receive a natural number $N$ from a command-line argument, and split the input
# file into $N$ pieces at line boundaries. Confirm the result by using split
# command.
#
N=3; cnt=`cat popular-names.txt | wc -l` ; a=$((cnt/N+1)); split -l $a popular-names.txt output
### `: expresses a command 
### ; : connect command 
### 
### : https://shinji-blog.com/nlp100/nlp100-2020-10-19/
# n=5 | split -l $n './popular-names.txt'
#
# 17. Distinct strings in the first columnPermalink
# Find distinct strings (a set of strings) of the first column of the file.
# Confirm the result by using cut, sort, and uniq commands.

cut -f 1 './popular-names.txt' | sort | uniq

# 18. Sort lines in descending order of the third columnPermalink
# Sort the lines in descending numeric order of the third column (sort lines
# without changing the content of each line). Confirm the result by using sort
# command

sort -k 3n -t \t -r './popular-names.txt'
### -k : set the key
### -n : numeric-sort
### -t : set the separator
### -r : -reverse

# 19. Frequency of a string in the first column in descending orderPermalink
# Find the frequency of a string in the first column, and sort the strings by
# descending order of their frequencies. Confirm the result by using cut, uniq,
# and sort commands.

cut -f 1 './popular-names.txt' | sort | uniq -c | sort -nr
