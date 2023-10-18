from enum import Enum

INF = 99999

class Color(Enum):
    WHITE = "#FFFFFF"
    GRAY = "#808080"
    BLACK = "#000000"
    RED = "#FF0000"

class Vertex:
    def __init__(self, _id):
        self.id = _id
        self.color = None
        self.d = INF
        self.f = INF
        self.predecessor = None
        self.adj = []

    def connectTo(self, vertex):
        self.adj.append(vertex)

    def __str__(self) -> str:
        return str(self.id)

class Graph:
    def __init__(self, vertex_cnt, road_cnt):
        self.vertex_cnt = vertex_cnt
        self.road_cnt = road_cnt
        self.vertices = []
        for i in range(vertex_cnt):
            self.addVertex(Vertex(i+1))

    def getVertexById(self, _id):
        for v in self.vertices:
            if v.id == _id:
                return v

    def addVertex(self, vertex:Vertex):
        self.vertices.append(vertex)

    def addRelation(self, vertex1_id, vertex2_id, type=1):
        vertex1:Vertex = self.getVertexById(vertex1_id)
        vertex2:Vertex = self.getVertexById(vertex2_id)
        vertex1.adj.append(vertex2)
        if type == 2:
            vertex2.adj.append(vertex1)

    def transpose(self):
        new_g = Graph(self.vertex_cnt, self.road_cnt)
        for v in self.vertices:
            for u in self.vertices:
                if v in u.adj:
                    new_g.addRelation(v.id, u.id)
        # copy attribute
        for x in self.vertices:
            new_v = new_g.getVertexById(x.id)
            new_v.d = x.d
            new_v.f = x.f
        return new_g
    
    def __str__(self) -> str:
        s = "________________\n"
        s += f"vertex_cnt:{self.vertex_cnt}\nroad_cnt:{self.road_cnt}\n"
        for v in self.vertices:
            s += f"{v.id} d:{v.d} f:{v.f}-> "
            for u in v.adj:
                s += str(self.vertices.index(u)+1) + " "
            s += "\n"
        s += "________________"
        return s