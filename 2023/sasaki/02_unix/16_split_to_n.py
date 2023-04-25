"""
Receive a natural number $N$ from a command-line argument, 
and split the input file into $N$ pieces at line boundaries. 
Confirm the result by using split command.
https://nlp100.github.io/en/ch02.html#16-split-a-file-into-n-pieces
"""

# command: split --additional-suffix ".txt" -d -n l/$N$ - "splitted-" < ./popular-names.txt
# command does not split file by line numbers but bytes AFA I can see in man manual

from fileinput import filename
from sys import argv

PREFIX = "splitted-"
SUFFIX = ".txt"

if 2 > len(argv) or len(argv) > 3:
    print(f"file number and file path required, but got {len(argv) - 1} args")
    exit(1)

n = int(argv[1])
file_path = argv[2]

r = open(file_path)

# count number of lines
c = 0
for line in r:
    c += 1

# reuse the file object
r.seek(0)

threshold_line_number = c // n
plus_one_line_file_count = c % n

for file_number in range(0, n):
    out_file_name = f"{PREFIX}{file_number:02}{SUFFIX}"
    w = open(out_file_name, "w")

    # ajust threshold for the case that line count is indivisible by file number
    _threshold_line_number = threshold_line_number + 1 if file_number < plus_one_line_file_count else threshold_line_number

    for _ in range(0, _threshold_line_number):
        # format because the last line is not followed by newline.
        w.write(f"{r.readline().rstrip()}\n")

    w.close()

r.close()