"""
Split the sentence 
“Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can”.
into words, and extract the first letter from the 1st, 5th, 6th, 7th, 8th, 9th, 15th, 16th, 19th words 
and the first two letters from the other words.
Create an associative array (dictionary object or mapping object) 
that maps from the extracted string to the position (offset in the sentence) of the corresponding word.
https://nlp100.github.io/en/ch01.html#04-atomic-symbols
"""

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

normalized = sentence.replace(",", "").replace(".", "")
splitted = normalized.split(" ")

only_first_letter_indexes = [1, 5, 6, 7, 8, 9, 15, 16, 19]

ans = {}
for i in range(0, len(splitted)):
    word = splitted[i]
    s = word[1] if i + 1 in only_first_letter_indexes else word[:2]
    ans[i] = s
print(ans)
