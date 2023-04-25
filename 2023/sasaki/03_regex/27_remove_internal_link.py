"""
In addition to the process of the problem 26, remove internal links from the values. See Help:Cheatsheet.
https://nlp100.github.io/en/ch03.html#27-remove-internal-links
"""

from typing import Dict
from wiki_data import TARGET_TITLE, load_data_by_title
# https://github.com/earwig/mwparserfromhell/
import mwparserfromhell as mw_parser

from token_filter import make_filter

text = load_data_by_title(TARGET_TITLE)['text']
code = mw_parser.parse(text)


info_params: Dict[str, str] = {}
for template in code.filter(forcetype=mw_parser.nodes.template.Template, recursive=False):
    if "Infobox country" not in template.name:
        continue

    for param in template.params:
        info_params[str(param.name)] = str(param.value)



def is_wiki_link_token(t):
    return isinstance(t, mw_parser.parser.tokens.WikilinkOpen) \
        or isinstance(t, mw_parser.parser.tokens.WikilinkSeparator) \
        or isinstance(t, mw_parser.parser.tokens.WikilinkClose)


omit_bold_token = make_filter("'''", "b")
omit_italic_token = make_filter("''", "i")

for name in info_params:

    parser = mw_parser.parser.Parser()
    
    # e.g. [[aa |aaa##sss]] -> [WikilinkOpen(), Text(text='aa '), WikilinkSeparator(), Text(text='aaa##sss'), WikilinkClose()]
    tokens = parser._tokenizer.tokenize(info_params[name])
    
    tokens = omit_italic_token(tokens)
    tokens = omit_bold_token(tokens)

    # e.g. [WikilinkOpen(), Text(text='aa '), WikilinkSeparator(), Text(text='aaa##sss'), WikilinkClose()] -> [Text(text='aa '), Text(text='aaa##sss')]
    tokens = list(filter(lambda t: not is_wiki_link_token(t), tokens))

    wiki_code = parser._builder.build(tokens)
    print(wiki_code)

