"""
In addition to problem 40, add three member variables head (a reference to the object of its syntactic governor), 
dep (dependency type to its governor), and children (a list of references to the syntactic dependents in the parse tree) to the class Word. 
Show the pairs of governors (parents) and their dependents (children) of the first sentence of the body of the article. 
Use the class Word in the rest of the problems in this chapter.
https://nlp100.github.io/en/ch05.html#41-read-the-parse-result-dependency

In addition to problem 40, design a class `Chunk` that represents a clause.
This class has 3 member variables, `morphs`(the list of `Morph`), `dst`(the index of clause that it depend on), `srcs`(the indexes that depend on it).
Implement a program to load the parse result, and show the dependency of the first sentence clauses of the body of the article.
Use the class Word in the rest of the problems in this chapter.
https://nlp100.github.io/ja/ch05.html#42-%E4%BF%82%E3%82%8A%E5%85%83%E3%81%A8%E4%BF%82%E3%82%8A%E5%85%88%E3%81%AE%E6%96%87%E7%AF%80%E3%81%AE%E8%A1%A8%E7%A4%BA
"""

from chunk_sentence import Sentece
import load_data

root = load_data.load()

first_sentence = root[2]

sentence = Sentece(first_sentence)

print("print dependency as normal text")
print(sentence.dependency_as_text())

print("""
----------
""")

print("print dependency as graphcal tree")
print(sentence.tree_as_text(indent_str="----", indent_last="-|--"))

# or we can check cabocha format by following command
# `cat tree.txt | head -n 41 | tail -n 38`
