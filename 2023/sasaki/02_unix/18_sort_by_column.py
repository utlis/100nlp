"""
Sort the lines in descending numeric order of the third column 
(sort lines without changing the content of each line). 
Confirm the result by using sort command.
https://nlp100.github.io/en/ch02.html#18-sort-lines-in-descending-order-of-the-third-column
"""

# command: sort -n -r -k 3 < popular-names.txt
# interesting experiment of merge-sort by sort command
# https://zenn.dev/saka1/articles/0498f7c8dbdba8

import csv
import sys

# bad code for memory perfomance
# however, reading all data is required for sort
# e.g. csv-sort library implements merge-sort, which is memory-efficient
# https://pypi.org/project/csvsort/
r = csv.reader(sys.stdin, delimiter="\t")
rows = []
for row in r:
    rows.append(row)

# another solution: use sorted() function
# https://docs.python.org/3/howto/sorting.html#sorting-basics
# list.sort() is better for memory perfomance because it does not make copied list.
rows.sort(key=lambda r: int(r[2]), reverse=True)
for row in rows:
    print("\t".join(row))
