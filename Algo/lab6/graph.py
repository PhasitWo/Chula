from enum import Enum

INF = 99999

class Color(Enum):
    WHITE = "#FFFFFF"
    GRAY = "#808080"
    BLACK = "#000000"

class Vertex:
    def __init__(self):
        self.color = None
        self.d = INF
        self.f = INF
        self.predecessor = None
        self.adj = []

    def connectTo(self, vertex):
        self.adj.append(vertex)

class Graph:
    def __init__(self, vertex_cnt, road_cnt):
        self.vertex_cnt = 0
        self.road_cnt = road_cnt
        self.vertices = []
        for _ in range(vertex_cnt):
            self.addVertex(Vertex())

    def addVertex(self, vertex:Vertex):
        self.vertices.append(vertex)
        self.vertex_cnt += 1

    def addRelation(self, vertex1_index, vertex2_index, type=1):
        vertex1:Vertex = self.vertices[vertex1_index]
        vertex2:Vertex = self.vertices[vertex2_index]
        vertex1.adj.append(vertex2)
        if type == 2:
            vertex2.adj.append(vertex1)

    def transpose(self):
        new_g = Graph(self.vertex_cnt, self.road_cnt)
        for i, v in enumerate(new_g.vertices):
            for k, u in enumerate(self.vertices):
                if self.vertices[i] in u.adj:
                    new_g.addRelation(i, k)
        # copy attribute
        for x in range(self.vertex_cnt):
            new_g.vertices[x].d = self.vertices[x].d
            new_g.vertices[x].f = self.vertices[x].f

        return new_g
    
    def __str__(self) -> str:
        s = f"vertex_cnt:{self.vertex_cnt}\nroad_cnt:{self.road_cnt}\n"
        for i, v in enumerate(self.vertices):
            s += f"{i+1} -> "
            for u in v.adj:
                s += str(self.vertices.index(u)+1) + " "
            s += "\n"
        return s