from graph import Graph, Vertex

v1 = Vertex()
v2 = Vertex()
v3 = Vertex()
g = Graph(3, 4)
g.addVertex(v1)
g.addVertex(v2)
g.addVertex(v3)
g.addRelation(1, 2, 1)
g.addRelation(1, 3, 2)
g.addRelation(2, 3, 1)


print(g)