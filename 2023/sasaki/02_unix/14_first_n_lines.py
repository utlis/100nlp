"""
Receive a natural number $N$ from a command-line argument, 
and output the first $N$ lines of the file. 
Confirm the result by using head command.
https://nlp100.github.io/en/ch02.html#14-first-n-lines
"""

# command: head -n $N$ < ./popular-names.txt

from sys import argv, exit

if 2 > len(argv) or len(argv) > 3:
    print(f"line number and file path required, but got {len(argv) - 1} args")
    exit(1)

n = int(argv[1])
file_path = argv[2]

r = open(file_path)

c = 0
for line in r:
    if c >= n:
        break

    print(line.rstrip())
    c += 1

r.close()