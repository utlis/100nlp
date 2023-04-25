from typing import TypedDict
from constants import POS_FILE


class Token(TypedDict):
    text: str
    lemma: str
    pos: str
    pos1: str


def load_data():
    rf = open(POS_FILE)

    data: list[Token] = []
    for line in rf:
        parsed = line.split("\t")
        if len(parsed) < 5:
            continue

        pos = parsed[4].split("-")

        if (len(pos) < 2):
            # error handling when 品詞細分類1 does not exists
            pos.append("")

        data.append({
            "text": parsed[0],
            "lemma": parsed[3],
            "pos": pos[0],
            "pos1": pos[1]
        })

    rf.close()

    return data
