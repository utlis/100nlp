from typing import List, Tuple


def ex00(string: str, fast=False) -> str:
    """
    return a reversed string of the input string
    `fast` option provides a faster output in terms of algorithm
    """
    if fast:
        """
        faster and pythonic? vesion

            s[i:j:k]
            slice of s from i to j with step k

        note that this produces unexpected sequence when it comes to byte sequence.

        >>> w = '日本語'
        >>> w[::-1]
        '語本日'
        >>> w.encode('utf-8')[::-1].decode('utf-8')
        => error!
        """
        return string[::-1]
    else:
        # readable version
        return ''.join(reversed(string))


def ex01(string: str) -> str:
    """
    return a character sequence of odd indices ones of given a string
    """
    return string[::2]


def ex02(*texts) -> str:
    return ''.join(map(lambda x: ''.join(x), zip(texts)))


def ex03(sentence: str) -> List[str]:
    """
    return a list of character counts for given an English sentence
    """

    words = sentence.split()
    words_sign_cleaned = map(lambda word: word.replace('.,:;!?', ''), words)

    return map(len, words_sign_cleaned)


def n_gramizer(text: str, n: int =2, unit: str ="word") -> List[Tuple[str, str]]:
    """
    Input: text (str), n (Int), unit (str, "word" or "char")
    Output: list of tuples
    """
    if unit == "word":
        words = text.split()
        return [tuple(words[i:i+n]) for i in range(len(words)-n+1)]
    elif unit == "char":
        return [tuple(text[i:i+n]) for i in range(len(text)-n+1)]
    else:
        raise ValueError("'unit' option should be 'word' or 'char'")


def ex05(text, mode: str) -> List[Tuple[str, str]]:
    return n_gramizer(text, unit=mode)


def ex06(x_text: str, y_text: str) -> set, set:
    X = set(n_gramizer(x_text, unit="char"))
    Y = set(n_gramizer(y_text, unit="char"))

    return X, Y


# Test Suite
def test_ex00():
    """
    00. 文字列の逆順
    文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
    """
    assert ex00("stressed") == "desserts"


def test_ex01():
    """
    01. 「パタトクカシーー」
    「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
    """
    assert ex01("パタトクカシーー") == "タクシー"


def test_ex02():
    assert ex02("パトカー", "タクシー") == "パタトクカシーー"


def test_ex03():
    """
    03. 円周率
    "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
    """
    text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    assert ex03(text) == [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]


def test_ex04():
    """
    04. 元素記号
    "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
    """
    sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    index = [1, 5, 6, 7, 8, 9, 15, 16, 19]

    assert ex04(sentence, index) == dict(
        H=1,
        He=2,
        Li=3,
        Be=4,
        B=5,
        C=6,
        N=7,
        O=8,
        F=9,
        Ne=10,
        Na=11,
        Mi=12,  # why not Mg??
        Al=13,
        Si=14,
        P=15,
        S=16,
        Cl=17,
        Ar=18,
        K=19,
        Ca=20
    )


def test_ex05():
    """
    05. n-gram
    与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
    """
    sentence = "I am an NLPer"
    assert ex05(sentence, mode='char') == [
        ('I', ' '),
        (' ', 'a'),
        ('a', 'm'),
        ('m', ' '),
        (' ', 'a'),
        ('a', 'n'),
        ('n', ' '),
        (' ', 'N'),
        ('N', 'L'),
        ('L', 'P'),
        ('P', 'e'),
        ('e', 'r')
    ]
    assert ex05(sentence, mode='word') == [
        ('I', 'am'),
        ('am', 'an'),
        ('an', 'NLPer')
    ]


def test_ex06():
    """
    06. 集合
    "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
    """
    X, Y = ex06("paraparaparadise", "paragraph")

    assert X | Y
    assert X & Y
    assert X - Y

    print("check containment of 'se'")
    assert ('s', 'e') in X
    assert ('s', 'e') in Y


def test_ex07():
    assert ex07()


def test_ex08():
    assert ex08()


def test_ex09():
    assert ex09()
