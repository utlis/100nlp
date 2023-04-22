"""
Receive a natural number $N$ from a command-line argument, 
and output the last $N$ lines of the file. 
Confirm the result by using tail command.
https://nlp100.github.io/en/ch02.html#15-last-n-lines
"""

# command: tail -n $N$ < ./popular-names.txt

from sys import argv, exit
from collections import deque

if 2 > len(argv) or len(argv) > 3:
    print(f"line number and file path required, but got {len(argv) - 1} args")
    exit(1)

n = int(argv[1])
file_path = argv[2]

r = open(file_path)

# Deques support thread-safe, memory efficient appends 
# and pops from either side of the deque 
# with approximately the same O(1) performance in either direction.
# https://docs.python.org/3/library/collections.html#collections.deque
lines = deque()

for line in r:
    lines.append(line.rstrip())

    if (len(lines) > n):
        lines.popleft()


for line in lines:
    print(line)