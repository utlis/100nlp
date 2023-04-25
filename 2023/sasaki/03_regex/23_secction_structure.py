"""
Extract section names in the article with their levels. 
For example, the level of the section is 1 for the MediaWiki markup "== Section name ==".
https://nlp100.github.io/en/ch03.html#23-section-structure
"""

import re
from wiki_data import TARGET_TITLE, load_data_by_title


text = load_data_by_title(TARGET_TITLE)['text']

# format is "==Level 2==" (do not use  =Level 1=  as it is for page titles)
# using (.+) instead of (.+?), matched title will be followed by "="
category_line_reg = re.compile("^(={2,6})\s*(.+?)\s*(={2,6})$")


for line in text.splitlines():
    result = category_line_reg.search(line)
    if result:
        prefix, title, suffix = result.groups()[0:3]

        # the length of prefix and suffix must be the same
        if len(prefix) != len(suffix):
            continue
        print(f"heading {len(prefix)}: '{title}'")