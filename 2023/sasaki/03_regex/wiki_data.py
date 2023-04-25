import gzip
import json
import os
import pickle
from typing import List, TypedDict

DATA_FILE_PATH = "./enwiki-country.json.gz"
PICKLE_FOLDER_PATH = "./dist"

# title specified by question 20
TARGET_TITLE = "United Kingdom"

class WikiArticle(TypedDict):
    title: str
    text: str

def load_data_by_title(title: str) -> WikiArticle:
    """
    load wiki data from pickle if the file exists.
    load wiki data and store it as pickle if the file does not exist.
    if source data is updated, then you should exec "rm ./dist/*" command.
    """

    pickle_file_path = f"{PICKLE_FOLDER_PATH}/{title.replace(' ', '')}.pickle"

    # https://docs.python.org/3/library/pickle.html
    try:
        pf = open(pickle_file_path, "rb")
        data = pickle.load(pf)
        return data
    except FileNotFoundError:
        print(f"pickle file not found at {pickle_file_path}")
        pass
    except TypeError:
        print(f"invalid pickle file")
        pass

    result: WikiArticle = {}

    # find data from gzip
    r = gzip.open(DATA_FILE_PATH, "r")
    matched = False
    for line in r:
        data: WikiArticle = json.loads(line)
        if data["title"] == title:
            result = data
            matched = True
            break
    r.close()

    if matched == False:
        raise KeyError(title)

    # save found data as a pickle file
    try:
        os.makedirs(PICKLE_FOLDER_PATH)
    except FileExistsError:
        pass
    
    with open(pickle_file_path, "wb") as wf:
        pickle.dump(result, wf, pickle.HIGHEST_PROTOCOL)

    return result

