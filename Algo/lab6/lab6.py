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
                g.addRelation(inputs[0], inputs[1], inputs[2])
    return testCases

def solve_scc(g:Graph) -> int:
    scc_lst = []
    def DFS(g:Graph):
        for x in g.vertices:
            x.color = Color.WHITE
            x.predecessor = None
        time = 0
        # sort by f time
        g.vertices.sort(key=lambda x: x.f, reverse=True)
        for u in g.vertices:
            if u.color == Color.WHITE:
                time = DFS_visit(g, u, time)
                scc_lst.append(extract_scc(g))
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
    
    # Solve
    DFS(g)
    g_t = g.transpose()
    scc_lst = []
    DFS(g_t)
    return scc_lst

def extract_scc(g:Graph):
    lst = []
    for v in g.vertices:
        if v.color == Color.BLACK:
            lst.append(v.id)
            v.color = Color.RED
    return lst




# Driver Code
testcases = readInput("Algo/lab6/example.txt")
for graph in testcases:
    SCCs = solve_scc(graph)
    res = "result: "
    if len(SCCs) > 1:
        res += "0"
    else:
        res += "1"
    print(res)
    print("SCCs:")
    for s in SCCs:
        print(s)
 

