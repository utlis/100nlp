# https://github.com/SamuraiT/mecab-python3
from constants import TXT_FILE, POS_FILE
import MeCab

tagger = MeCab.Tagger()


rf = open(TXT_FILE, "r")
wf = open(POS_FILE, "w")

# read line by line from file for better memory performance
for line in rf:
    # omit unneeded characters
    line = line.rstrip().replace(" ", "").replace("　", "")

    if len(line) == 0:
        print(line)
        continue

    tag = tagger.parse(line)
    wf.writelines([tag])

wf.close()
rf.close()
