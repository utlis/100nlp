"""
Extract the value of the first column of each line, and store the output into col1.txt. 
Extract the value of the second column of each line, and store the output into col2.txt. 
Confirm the result by using cut command.
https://nlp100.github.io/en/ch02.html#12-col1txt-from-the-first-column-col2txt-from-the-second-column
"""

# command: 
# cut -f 1 < popular-names.txt > ./col1.txt && \
# cut -f 2 < popular-names.txt > ./col2.txt
# default delimiter of cut command is TAB

import sys
import csv

col1_file_path = "./col1.txt"
col2_file_path = "./col2.txt"

w1 = open(col1_file_path, "w")
w2 = open(col2_file_path, "w")

for line in sys.stdin:
    # use csv module for parsing the line.
    # it is becasuse parsing tsv is troublesome task (e.g. how we process consecutive tabs)
    for row in csv.reader([line], delimiter="\t"):
        # Depending on the actual implementation, these bytes may be readily written to the underlying stream,
        # or held in a buffer for performance and latency reasons. 
        # https://docs.python.org/3/library/io.html#io.TextIOBase.buffer
        # https://docs.python.org/3/library/io.html#io.BufferedIOBase.write
        w1.write(f"{row[0]}\n")
        w2.write(f"{row[1]}\n")


# close() flushs and close the stream
# https://docs.python.org/3/library/io.html#io.IOBase.close
# but flush executed at process normally exit
# https://docs.python.org/3/library/atexit.html#module-atexit
w1.close()
w2.close()
