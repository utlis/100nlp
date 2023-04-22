"""
Replace every occurrence of a tab character into a space. Confirm the result by using sed, tr, or expand command.
https://nlp100.github.io/en/ch02.html#11-replace-tabs-into-spaces
"""

# command: sed -e "s/\t/ /g < popular-names.txt"

import sys

for line in sys.stdin:
    line = line.rstrip().replace("\t", " ")
    print(line)