"""
Find distinct strings (a set of strings) of the first column of the file. 
Confirm the result by using cut, sort, and uniq commands.
https://nlp100.github.io/en/ch02.html#17-distinct-strings-in-the-first-column
"""

# command: cut -f 1 < ./popular-names.txt | sort | uniq
# another solution: cut -f 1 < ./popular-names.txt | sort -u

import csv
import sys

set_of_strings = set()

for line in sys.stdin:
    for row in csv.reader([line], delimiter="\t"):
        set_of_strings.add(row[0])

# the output order is not consistent
# > Being an unordered collection, sets do not record element position or order of insertion.
# https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
for s in set_of_strings:
    print(s)