from typing import Literal
import mwparserfromhell as mw_parser

MODE = Literal["TAG_OPEN_OPENED", "NORMAL", "TAG_CLOSE_OPENED"]
class Mode():
    """
    manage current TOKEN filtering mode
    """
    def __init__(self):
        self.current: MODE = "NORMAL"
        self.prev: MODE = "NORMAL"
    
    def change(self, new: MODE):
        self.prev = self.current
        self.current = new



def make_filter(target_wiki_markup, target_tag_name):
    """
    return function for filtering style tags.
    target_wiki_markup and target_tag_name must match.

    ---
    Example: 
    ```py
    omit_bold_token = make_filter("'''", "b") # make filter function
    parser = mw_parser.parser.Parser() # initialize mwparserfromhell parser

    # [TagOpenOpen(wiki_markup="''"), Text(text='i'), TagCloseOpen(), TagOpenOpen(wiki_markup="'''"), Text(text='b'), TagCloseOpen(), Text(text='aaa'), TagOpenClose(), Text(text='b'), TagCloseClose(), TagOpenClose(), Text(text='i'), TagCloseClose()]
    tokens = parser._tokenizer.tokenize(info_params[name])

    # [TagOpenOpen(wiki_markup="''"), Text(text='i'), TagCloseOpen(), Text(text='aaa'), TagOpenClose(), Text(text='i'), TagCloseClose()]
    filtered_tokens = omit_bold_token(tokens)
    ```
    """
    mode = Mode()

    def func(tokens: list) -> list:
        filtered_tokens = []
        buffered_tokens = []

        for t in tokens:

            match mode.current:
                case "NORMAL":
                    if isinstance(t, mw_parser.parser.tokens.TagOpenOpen) and t.wiki_markup == target_wiki_markup:
                        mode.change("TAG_OPEN_OPENED")
                    elif isinstance(t, mw_parser.parser.tokens.TagOpenClose):
                        buffered_tokens.append(t)
                        mode.change("TAG_CLOSE_OPENED")
                    else:
                        filtered_tokens.append(t)
                case "TAG_OPEN_OPENED":
                    if isinstance(t, mw_parser.parser.tokens.TagCloseOpen):
                        mode.change("NORMAL")
                case "TAG_CLOSE_OPENED":
                    if isinstance(t, mw_parser.parser.tokens.Text):
                        if t.text == target_tag_name:
                            pass
                        else:
                            # not about closing target tag
                            buffered_tokens.append(t)
                            filtered_tokens += buffered_tokens
                            buffered_tokens = []
                            mode.change(mode.prev)
                    elif isinstance(t, mw_parser.parser.tokens.TagCloseClose):
                        mode.change("NORMAL")
                        buffered_tokens = []
                    else:
                        buffered_tokens.append(t)


        return filtered_tokens
    
    return func
