"""
Extract references to media files linked from the article.
https://nlp100.github.io/en/ch03.html#24-media-references
"""

import re
from wiki_data import TARGET_TITLE, load_data_by_title


text = load_data_by_title(TARGET_TITLE)['text']

# in this script, a media file is linked with following format
# [[File:Wiki.png|thumb|Caption]] or [[:File:File name]]
file_phrase_reg = re.compile("\[\[:?File:([^|]+).*\]\]")


for line in text.splitlines():
    result = file_phrase_reg.search(line)
    if result:
        file_name = result.groups()[0]

        print(file_name)
