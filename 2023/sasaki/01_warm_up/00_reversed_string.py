"""
Obtain the string that arranges letters of the string “stressed” in reverse order (tail to head).
https://nlp100.github.io/en/ch01.html#00-reversed-string
"""

word = "stressed"
"""
Indices may also be negative numbers, to start counting from the right
Slice indices have useful defaults; an omitted first index defaults to zero, 
an omitted second index defaults to the size of the string being sliced.
ref https://docs.python.org/3/tutorial/introduction.html#strings

Some sequences also support “extended slicing” with a third “step” parameter: 
a[i:j:k] selects all items of a with index x where x = i + n*k, n >= 0 and i <= x < j.
ref https://docs.python.org/3/reference/datamodel.html#index-15
"""
ans = word[::-1]
print(ans)
