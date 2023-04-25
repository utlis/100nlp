The file enwiki-country.json.gz stores Wikipedia articles in the format:

- Each line stores a Wikipedia article in JSON format
- Each JSON document has key-value pairs:
    - Title of the article as the value for the title key
    - Body of the article as the value for the text key
- The entire file is compressed by gzip

Write codes that perform the following jobs