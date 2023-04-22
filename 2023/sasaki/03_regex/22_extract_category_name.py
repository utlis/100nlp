"""
Extract the category names of the article.
https://nlp100.github.io/en/ch03.html#22-category-names
"""

import re
from wiki_data import TARGET_TITLE, load_data_by_title


text = load_data_by_title(TARGET_TITLE)['text']

# format is [[Category:Category name]]
category_line_reg = re.compile("\[\[Category:(.+)\]\]")


for line in text.splitlines():
    result = category_line_reg.search(line)
    if result:
        category = result.groups()[0]
        # format unexpected character, e.g. "United Kingdom|"
        formatted = category.replace("|", "")
        print(formatted)