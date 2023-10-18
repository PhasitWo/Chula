from graph import Graph, Vertex, Color

def readInput(filePath:str) -> list[list[int]]:
    testCases = []
    with open(filePath, "r") as file:
        g = None
        for line in file:
            inputs = list(map(int, line.strip().split()))
            if len(inputs) == 2:
                # save city
                if g != None:
                    testCases.append(g)
                # stop
                if inputs[0] == 0 and inputs[1] == 0:
                    break
                # new city
                g = Graph(inputs[0], inputs[1])
            else:
                g.addRelation(inputs[0] - 1, inputs[1] - 1, inputs[2])
    return testCases

def solve_scc(g:Graph) -> int:
    scc_cnt = []
    def DFS(g:Graph):
        for x in g.vertices:
            x.color = Color.WHITE
            x.predecessor = None
        time = 0
        # sort by f time
        vertices_sort_by_f = g.vertices.copy()
        vertices_sort_by_f.sort(key=lambda x: x.f, reverse=True)
        for u in vertices_sort_by_f:
            if u.color == Color.WHITE:
                scc_cnt.append(None)
                time = DFS_visit(g, u, time)
    def DFS_visit(g:Graph, u:Vertex, time):
        time += 1
        u.d = time
        u.color = Color.GRAY
        for v in u.adj:
            if v.color == Color.WHITE:
                v.predecessor = u
                time = DFS_visit(g, v, time)
        u.color = Color.BLACK
        time += 1
        u.f = time
        return time
    # SCC
    DFS(g)
    g_t = g.transpose()
    scc_cnt = []
    DFS(g_t)
    if len(scc_cnt) > 1:
        return 0
    return 1

testcases = readInput("Algo/lab6/example.txt")
for case in testcases:
    print(solve_scc(case))



#    vertices_sort_by_f = g.vertices.copy()
#    vertices_sort_by_f.sort(key=lambda x: x.f, reverse=True)
