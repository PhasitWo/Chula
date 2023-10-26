from enum import Enum
INF = 999999
MINF = -999999

class Vertex:
    def __init__(self, _id):
        self.id = _id
        self.color = None
        self.d = INF
        self.f = INF
        self.predecessor = None
        self.adj = []

    def __str__(self) -> str:
        return str(self.id)

class Graph:
    def __init__(self, vertex_cnt, edge_cnt):
        self.vertex_cnt = vertex_cnt
        self.edge_cnt = edge_cnt
        self.D = [] # list of matrix
        self.Pi = [] # list of matrix
        self.vertices = []
        self.edges = dict()
        for i in range(vertex_cnt):
            self.addVertex(Vertex(i+1))

    def init_D0(self):
        d0 = [[INF for y in range(self.vertex_cnt)] for x in range(self.vertex_cnt)]
        for i in range(0, self.vertex_cnt):
            u = self.getVertexById(i+1)
            for j in range(0, self.vertex_cnt):
                if i == j:
                    d0[i][j] = 0
                    continue
                v = self.getVertexById(j+1)
                if v in u.adj:
                    d0[i][j] = self.getWeightById(i+1, j+1)
        self.D.append(d0)

    def init_Pi0(self):
        pi0 = [[None for y in range(self.vertex_cnt)] for x in range(self.vertex_cnt)]
        for i in range(0, self.vertex_cnt):
            for j in range(0, self.vertex_cnt):
                if i == j or self.D[0][i][j] == INF:
                    continue
                elif i != j and self.D[0][i][j] < INF:
                    pi0[i][j] = i
        self.Pi.append(pi0)

    def init_D0_extra(self):
        d0 = [[MINF for y in range(self.vertex_cnt)] for x in range(self.vertex_cnt)]
        for i in range(0, self.vertex_cnt):
            u = self.getVertexById(i+1)
            for j in range(0, self.vertex_cnt):
                if i == j:
                    d0[i][j] = 0
                    continue
                v = self.getVertexById(j+1)
                if v in u.adj:
                    d0[i][j] = self.getWeightById(i+1, j+1)
        self.D.append(d0)

    def getVertexById(self, _id):
        for v in self.vertices:
            if v.id == _id:
                return v
            
    def getWeightById(self, vertex1_id, vertex2_id):
        e = (vertex1_id, vertex2_id) if vertex1_id < vertex2_id else (vertex2_id, vertex1_id)
        return self.edges[e]

    def addVertex(self, vertex:Vertex):
        self.vertices.append(vertex)

    def addRelation(self, vertex1_id, vertex2_id, weight):
        vertex1:Vertex = self.getVertexById(vertex1_id)
        vertex2:Vertex = self.getVertexById(vertex2_id)
        vertex1.adj.append(vertex2)
        vertex2.adj.append(vertex1)
        e = (vertex1_id, vertex2_id) if vertex1_id < vertex2_id else (vertex2_id, vertex1_id)
        self.edges.update({e:weight})
        self.edge_cnt += 1          
    
    def __str__(self) -> str:
        s = "________________\n"
        s += f"vertex_cnt:{self.vertex_cnt}\nedge_cnt:{self.edge_cnt}\n"
        for k, v in self.edges.items():
            s += f"{k} -> {v}"
            s += "\n"
        s += "________________"
        return s