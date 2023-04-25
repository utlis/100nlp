"""
Count the number of lines of the file. Confirm the result by using wc command.
https://nlp100.github.io/en/ch02.html#10-line-count
"""

# command: wc -l < popular-names.txt
# wc command with 'lines' option counts new line, so it does not match real line count.
# solution is use grep command: "grep -c '^' < popular-names.txt"

import sys

c = 0
for line in sys.stdin:
    c += 1
    print(f"{c}: {line.rstrip()}")

print(f"line count is {c}")