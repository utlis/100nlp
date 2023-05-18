# README
This repository use [cabocha](https://taku910.github.io/cabocha/) with [mecab](https://taku910.github.io/mecab/) morphological analyzer which use Juman dictionary.

## If you want to change a source...
If you want change source text, 
1. change `source.txt`
2. execute `python init.py`
3. do `docker compose up`.

This generate a new `parsed.xml`. You can configure process by editting `docker-compose.yml`.

This operation requires [docker](https://docs.docker.com/engine/install/) and [docker compose](https://docs.docker.com/compose/install/).

# Note
There are differences between English version and Japanese version.
I write comments in English, but questions I tackle are Japanese version.