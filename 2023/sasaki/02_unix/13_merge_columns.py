"""
Join the contents of col1.txt and col2.txt, 
and create a text file whose each line contains 
the values of the first and second columns (separated by tab character) of the original file. 
Confirm the result by using paste command.
https://nlp100.github.io/en/ch02.html#13-merging-col1txt-and-col2txt
"""

# command: paste col1.txt col2.txt > col1-2.txt

import sys
from io import TextIOBase
from typing import List 

if len(sys.argv) != 3:
    print(f"2 file path required, but got {len(sys.argv) - 1}")
    sys.exit(1)

file1_path, file2_path = sys.argv[1], sys.argv[2] 

r1 = open(file1_path)
r2 = open(file2_path)

merged_file_path = "./col1-2.txt"
w = open(merged_file_path, "w")

class MultiReader(object):
    """
    Iterator class for composition of multi-text reader
    Iterator is a concept in programming. cf https://en.wikipedia.org/wiki/Iterator
    The way of implementation in python is https://docs.python.org/3/tutorial/classes.html#iterators
    """
    def __init__(self, readers: List[TextIOBase]) -> None:
        self.rs = readers

    def __iter__(self):
        return self
    
    def __next__(self):
        els = []
        # get line one by one for better memory perfomance
        for r in self.rs:
            els.append(r.readline().rstrip())

        # stop if one of files end
        if "" in els:
            raise StopIteration()

        return tuple(els)
        

for (el1, el2) in MultiReader([r1, r2]):
    w.write(f"{el1}\t{el2}\n")

r1.close()
r2.close()
w.close()