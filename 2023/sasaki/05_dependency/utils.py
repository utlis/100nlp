from xml.etree.ElementTree import Element

from morph import Morph


def parse_token_to_morph(token: Element) -> Morph:
    features = token.attrib["feature"].split(",")
    return Morph({
        "surface": token.text,
        "base": features[4],
        "pos": features[0],
        "pos1": features[1]
    })
