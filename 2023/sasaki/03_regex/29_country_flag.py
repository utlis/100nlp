"""
Obtain the URL of the country flag by using the analysis result of Infobox.
(Hint: convert a file reference to a URL by calling imageinfo in MediaWiki API)
https://nlp100.github.io/en/ch03.html#29-country-flag
"""


import json
from typing import Dict
from wiki_data import TARGET_TITLE, load_data_by_title
import requests

# https://github.com/earwig/mwparserfromhell/
import mwparserfromhell as mw_parser

text = load_data_by_title(TARGET_TITLE)["text"]
code = mw_parser.parse(text)

info_params: Dict[str, str] = {}
for template in code.filter(forcetype=mw_parser.nodes.template.Template, recursive=False):
    if "Infobox country" not in template.name:
        continue

    for param in template.params:
        info_params[str(param.name).replace(" ", "")] = str(param.value)

image_name = info_params["image_flag"]

# cf. https://www.mediawiki.org/wiki/API:Imageinfo
request_url = 'https://commons.wikimedia.org/w/api.php?action=query&titles=File:' + image_name + '&prop=imageinfo&iiprop=url&format=json'
response = requests.get(request_url).text

# response data is json, since json format is specified above
response_data = json.loads(response)

for name in response_data["query"]["pages"]:
    page_data = response_data["query"]["pages"][name]

    # page_data["imageinfo"] is expected [{'url': 'https://upload.wikimedia.org/wikipedia/commons/8/83/Flag_of_the_United_Kingdom_%283-5%29.svg', 'descriptionurl': 'https://commons.wikimedia.org/wiki/File:Flag_of_the_United_Kingdom_(3-5).svg', 'descriptionshorturl': 'https://commons.wikimedia.org/w/index.php?curid=895166'}]
    for image_data in page_data["imageinfo"]:
        print(image_data["url"])

