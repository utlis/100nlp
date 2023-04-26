import re
import json
from urllib import request, parse
import requests

## 20. Read JSON documentsPermalinki ##########

with open('jawiki-country.json', 'r') as f:
    res = [json.loads(line) for line in f.readlines()] # リスト内包表記: 前半部分＝何をリストに入れるのか, 後半部分＝for文を回す対象
#    for line in f.readlines():
#        res.append(json.loads(line)) # loads = load string, 今回は1行ずつが1jsonだったのでloadが使えない

uk_text = [d['text'] for d in res if d['title']=="イギリス"][0] # [0]をつけないとuk_textはリストになっている


## 21. Lines with category namesPermalink #######

for m in re.findall(r'\[\[Category:.+', uk_text): # =は前の文字が一文字以上続くことを表す
    print(m)
    # 正規表現にはr、matchは色々な表現を許したときに完全にその対象と一致するか否か
    # 前後に .* をつけたらmatchで行けるが。

## 22. Category names 
for m in re.finditer(r'\[\[Category:(.*)\]\]', uk_text): # finditerを使い、()で正規表現部分を囲むと、gourpメソッドで該当の文字列が取れる
    print(m.group(0))
    print(m.group(1))

## 23. Section structure
for m in re.finditer(r'(={2,10})([^ =]+)(={2,10})', uk_text): # ^は先頭、$は末尾、また、^を使うと否定（拾わないでほしい文字）になる
    sec_name = m.group(2)
    sec_level = len(m.group(1))-1
    print(sec_name, sec_level)

## 24. Media references
for m in re.finditer(r'(File|ファイル)\:([^|\}\]]+)', uk_text):
#    print(m.group(0))
     print(m.group(2))


## 25. Infobox
## 26. Remove emphasis 
pattern = re.compile(r'^\{\{基礎情報.*?$(.*?)^\}\}$', re.MULTILINE + re.S)
base_info = pattern.findall(uk_text)[0]
#print(base_info)

pattern = re.compile(r'^\|([^=\|].+?)=(.+?[^ ])$', re.MULTILINE + re.S)
emphasis = re.compile(r'\'{2,5}', re.MULTILINE + re.S) ## 26. Remove emphasis
links_1 = re.compile(r'\[{2}(.+?)\]{2}', re.MULTILINE + re.S) ## 27. remove internal links
links_2 = re.compile(r'\[\[.+\|(.+)\]\]', re.MULTILINE + re.S) ## 27. remove internal links

base_info_dic = {}
for m in re.finditer(pattern, base_info):
    key = m.group(1).strip()

    value = m.group(2).strip()
    value = re.sub(emphasis, '', value)
    value = re.sub(links_2, r'\1', value) 
    value = re.sub(links_1, r'\1', value) 


    base_info_dic[key] = value

for k, v in base_info_dic.items():
    print(k, ':', v)

## 28. Remove MediaWiki mark

remove_1 = re.compile(r'(\{{2}|\[{2})(.+?)(\}{2}|\]{2})', re.MULTILINE)
remove_2 = re.compile(r'en\||仮リンク\||lang\||fr\||ファイル:', re.MULTILINE)
remove_3 = re.compile(r'<\w{1,4}(.+)/>', re.MULTILINE)
remove_4 = re.compile(r'<ref.*?>(.+?)</ref>', re.MULTILINE)

for key, value in base_info_dic.items():
    value = re.sub(remove_1, r'\2', value)
    value = re.sub(remove_2, '', value)
    value = re.sub(remove_3, '', value)
    value = re.sub(remove_4, r' \1', value)

    base_info_dic[key] = value

for key, value in base_info_dic.items():
    if key == '標語':
        value = re.sub(r'\{\{(.+)）', r'\1', value)
        base_info_dic[key] = value
    if key == '確立形態1':
        value = re.sub(r'）', '', value)
        base_info_dic[key] = value
    if key == '確立形態3':
        value = re.sub(r'）', '', value)
        base_info_dic[key] = value

for k, v in base_info_dic.items():
    print(k, ':', v)


## 29. Country flag
## リクエスト生成
url = 'https://www.mediawiki.org/w/api.php?' \
    + 'action=query' \
    + '&titles=File:' + parse.quote(base_info_dic['国旗画像']) \
    + '&format=json' \
    + '&prop=imageinfo' \
    + '&iiprop=url'

## json形式でダウンロード
resp = requests.get(url)
d = resp.json()

## urlを表示
print(d['query']['pages']['-1']['imageinfo'][0]['url'])
