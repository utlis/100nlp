"""
Implement a function cipher that converts a given string with the specification:

- Every alphabetical lowercase letter c is converted to a letter whose ASCII code is (219 - [the ASCII code of c])
- Keep other letters unchanged

Every alphabetical lowercase letter c is converted to a letter whose ASCII code is (219 - [the ASCII code of c])
Keep other letters unchanged
Use this function to cipher and decipher an English message.
https://nlp100.github.io/en/ch01.html#08-cipher-text
"""


def cipher(src: str) -> str:
    out = ""
    for c in src:
        code = ord(c)
        is_lower = code >= 97 and code <= 122
        if is_lower:
            out += chr(219 - code)
        else:
            out += c
    return out


src = "Every alphabetical lowercase letter c is converted to a letter whose ASCII code is (219 - [the ASCII code of c])"
encoded = cipher(src)
decoded = cipher(encoded)

result = f"""src: {src}
encoded: {encoded}
decoded: {decoded}
"""
print(result)
