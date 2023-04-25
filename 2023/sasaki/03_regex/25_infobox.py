"""
Extract field names and their values in the Infobox “country”, and store them in a dictionary object.
https://nlp100.github.io/en/ch03.html#25-infobox
"""

# format is https://en.wikipedia.org/wiki/Help:Template

from typing import Dict
from wiki_data import TARGET_TITLE, load_data_by_title
# https://github.com/earwig/mwparserfromhell/
import mwparserfromhell as mw_parser

text = load_data_by_title(TARGET_TITLE)['text']
code = mw_parser.parse(text)


info_params: Dict[str, str] = {}
for template in code.filter(forcetype=mw_parser.nodes.template.Template, recursive=False):
    if "Infobox country" not in template.name:
        continue

    for param in template.params:
        info_params[str(param.name)] = str(param.value)


for name in info_params:
    print(name)
    print(info_params[name])


        


