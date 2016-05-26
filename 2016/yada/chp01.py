"""
00. 文字列の逆順
文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
"""


def ex00(string: str, fast=False) -> str:
    if fast:
        """
        faster and pythonic? vesion

            s[i:j:k]
            slice of s from i to j with step k

        note that this produces unexpected sequence when it comes to byte sequence.

        >>> w = '日本語'
        >>> w[::-1]
        '語本日'
        >>> w.encode('utf-8')[::-1].decode('utf-8')  # => error!
        """
        return string[::-1]
    else:
        # readable version
        return ''.join(reversed(string))


def test_ex00():
    assert ex00("stressed") == "desserts"
