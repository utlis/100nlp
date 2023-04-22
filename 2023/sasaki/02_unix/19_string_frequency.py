"""
Find the frequency of a string in the first column, 
and sort the strings by descending order of their frequencies. 
Confirm the result by using cut, uniq, and sort commands.
https://nlp100.github.io/en/ch02.html#19-frequency-of-a-string-in-the-first-column-in-descending-order
"""

# command: cut -f 1 < ./popular-names.txt | sort | uniq -c | sort -r -n -k 1

import sys
import csv

string_frequency = {}

for line in sys.stdin:
    for row in csv.reader([line], delimiter="\t"):
        s = row[0]
        if s not in string_frequency:
            string_frequency[s] = 0
        
        string_frequency[s] += 1

sf_list = list(string_frequency.items())
sf_list.sort(key=lambda x: x[1], reverse=True)

for (s, freq) in sf_list:
    print(f"{freq} {s}")