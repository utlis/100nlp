import xml.etree.ElementTree as ET


def load():
    xml_data = ""
    with open("parsed.xml") as rf:
        xml_data = "\n".join(rf.readlines())

    xml_data_with_root = f"<document>{xml_data}</document>"

    root = ET.fromstring(xml_data_with_root)

    return root
