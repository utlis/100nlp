"""
Visualize a dependency tree of a sentence as a directed graph. 
Consider converting a dependency tree into DOT language and use Graphviz for drawing a directed graph. 
In addition, you can use pydot for drawing a dependency tree.
https://nlp100.github.io/en/ch05.html#44-visualize-dependency-trees
"""

import load_data
from chunk_sentence import Sentece

# you have to install graphiz
# see instalation manual
# https://graphviz.org/download/
import pydot

root = load_data.load()
first_sentence = root[2]
sentece = Sentece(first_sentence)

graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="white")

for chunk in sentece.chunks:
    graph.add_node(pydot.Node(chunk.id, label=chunk.to_text()))

for chunk in sentece.chunks:
    if chunk.dst == -1:
        continue
    graph.add_edge(pydot.Edge(chunk.id, chunk.dst, color="black"))

graph.write("result_44_draw_graph.svg", format="svg")
