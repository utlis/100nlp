import re

# re.match は行頭からマッチ
# re.search はどこでもマッチ
# matchオブジェクトにgroup(), groups()で取り出し可能
# すべてのバックスラッシュをバックスラッシュでエスケープしないといけないらしい
# でも r"~" とすれば普通どおり
# とかいうけど r なくても挙動は変わらない…？

p11 = re.compile("拡散希望")
t11 = "【拡散希望】うんたらかんたら"
print(p11.search(t11))

p12 = re.compile("なう$")
t12 = '赤門前なう'
print(p12.search(t12))

p13 = re.compile("(.*)RT") # 非公式RT（文頭コメント型/無言型）
t13 = 'まぁじウケるwww RT @user_name うんたらかんたら' 
print(p13.search(t13))

p14 = re.compile("@\w+") # @の前に文字列がある場合も考慮してsearch
t14 = "@Gascar_ShunT"
print(p14.search(t14))

p15 = re.compile("@(\w+)")
t15 = "@reply りぷらいだよ〜〜ん"
user = p15.search(t15).group(1)
print("<a href=\"https://twitter.com/#!/" + user + "\">@" + user + "</a>")

p16 = re.compile('([\u4e00-\u9fff\uf900-\ufaff]+)\(([A-Z]+)\)') # Unicode CJKエリア 4E00-9FFF
t16 = '環太平洋連携協定(TPP)' #全角丸括弧も？
p16.search(t16).groups() 
# Unicode 漢字エリアについては http://tama-san.com/?p=196

p17 = re.compile('.+[ちゃん|さん|君|くん|様|さま|っち|ぽん|にゃん|丸|まる]')
t17 = 'テキストちゃん'
p17.search(t17)

p18 = re.compile("仙台市(.+)")
t18 = '仙台市びっくり市'
p18.search(t18)

p19 = re.compile("(?P<num>\d{3}-\d{4})(?P<pref>.+[都道府県])(?P<more>.+[郡区市町村])")
t19 = '113-0001 東京都文京区白山'
p19.search(t19)

p20 = re.compile('[]') # やらねば
t20 = '＼(^o^)／ｵﾜﾀ'
# http://mitukiii.hatenablog.com/entry/2013/05/31/023156
