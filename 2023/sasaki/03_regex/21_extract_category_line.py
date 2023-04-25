"""
Extract lines that define the categories of the article.
https://nlp100.github.io/en/ch03.html#21-lines-with-category-names
"""

import re
from wiki_data import TARGET_TITLE, load_data_by_title


text = load_data_by_title(TARGET_TITLE)['text']

category_line_reg = re.compile("\[\[Category:.+]\]")


for line in text.splitlines():
    if category_line_reg.search(line):
        print(line)