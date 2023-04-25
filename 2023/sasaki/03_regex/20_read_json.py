"""
Read the JSON documents and output the body of the article about the United Kingdom. 
Reuse the output in problems 21-29.
https://nlp100.github.io/en/ch03.html#20-read-json-documents
"""

from wiki_data import TARGET_TITLE, load_data_by_title

data = load_data_by_title(TARGET_TITLE)
print(data["text"])