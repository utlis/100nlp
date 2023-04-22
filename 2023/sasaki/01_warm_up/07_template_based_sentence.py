"""
Implement a function that receives arguments, x, y, and z and returns a string “{y} is {z} at {x}”, 
where “{x}”, “{y}”, and “{z}” denote the values of x, y, and z, respectively. 
In addition, confirm the return string by giving the arguments x=12, y="temperature", and z=22.4.
https://nlp100.github.io/en/ch01.html#07-template-based-sentence-generation
"""


def generate_sentence(x, y, z) -> str:
    return f"{y} is {z} at {x}"


print(generate_sentence(12, "temperature", 22.4))
