# -*-coding: utf-8 -*-
moji=list("stressed")
#string="stressed"
moji.reverse()
print("".join(moji))
#パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ
#coding=utf_8
str = u"パタトクカシーー"
#str[::2]
print(str[::2])
#02:「パトカー」＋「タクシー」＝「パタトクカシーー」
    #「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
str2=u"パトカー"
str3=u"タクシー"
str4 = "".join(a+b for a, b in zip (str2, str3))
print(str4)
#03:円周率
#str5="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.".split(" ")
#print(str5)
#print len(str5)
#str6=str5.trim(",.")
#print(str6)
str5= "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str6= [len(str7.strip(",.")) for str7 in str5.split()]
print(str6)
