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

def DFS(g:Graph):
    trees = []
    for x in g.vertices:
        x.color = Color.WHITE
        x.predecessor = None
    time = 0
    # sort by f time
    g.vertices.sort(key=lambda x: x.f, reverse=True)
    for u in g.vertices:
        if u.color == Color.WHITE:
            time = DFS_visit(g, u, time)
            trees.append(extract_scc(g))
    return trees

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
    
def extract_scc(g:Graph):
    lst = []
    for v in g.vertices:
        if v.color == Color.BLACK:
            lst.append(v.id)
            v.color = Color.RED
    return lst

def solve_scc(g:Graph) -> int:
    DFS(g)
    g_t = g.transpose()
    scc_lst = DFS(g_t)
    return scc_lst

def find_edge_between_scc(g:Graph, scc_1:list[int], scc_2:list[int]) -> int:
    # let  1 means scc_1 ---> scc_2
    # let  0 means scc_2 ---> scc_1
    # let -1 means no edges
    flag = -1
    for i in scc_1:
        u = g.getVertexById(i)
        for j in scc_2:
            v = g.getVertexById(j)
            if v in u.adj:
                flag = 1
                break
            if u in v.adj:
                flag = 0
                break
        if flag != -1:
            break
    return flag

def connect_two_scc(g:Graph, scc_1:list[int], scc_2:list[int]):
    # choose any vertex from scc_1 and scc_2
    flag = 0
    found = False
    for i in scc_1:
        u = g.getVertexById(i)
        for j in scc_2:
            v = g.getVertexById(j)
            # u --> v
            if v in u.adj:
                flag = 1
                found = True
                break
            if u in v.adj:
                flag = 2
                found = True
                break
        if found:
            break
    if flag == 1:
        g.addRelation(v.id, u.id)
        print(v.id, u.id)
    elif flag == 2:
        g.addRelation(u.id, v.id)
        print(u.id, v.id)
    else:
        u = scc_1[0]
        v = scc_2[0]
        g.addRelation(u, v)
        print(u,v)

def unify(g:Graph) -> int:
    SCCs = solve_scc(g)
    cnt = 0
    print(SCCs)
    while(len(SCCs) > 1):
        # interpret each ssc as a vertex and build a graph (each vertex has id as scc.index + 1)
        k = Graph(len(SCCs), 0)
        # find relations (edges) between all scc
        for i in range(len(SCCs) - 1):
            for j in range(i+1, len(SCCs)):
                scc_1 = SCCs[i]
                scc_2 = SCCs[j]
                flag = find_edge_between_scc(g, scc_1, scc_2)
                if flag == 1:
                    k.addRelation(i+1, j+1)
                elif flag == 0:
                    k.addRelation(j+1, i+1)
        # do topoligical sorting
        DFS(k)
        k.vertices.sort(key=lambda x: x.f, reverse=True)
        # connect least f to max f
        # vertex.id = scc.index + 1 --> scc.index = vertex.id - 1
        least_f_scc = SCCs[k.vertices[-1].id - 1]
        max_f_scc = SCCs[k.vertices[0].id - 1]
        connect_two_scc(g, least_f_scc, max_f_scc)
        cnt += 1
        # reevaluate
        SCCs = solve_scc(g)
    print(SCCs)
    return cnt

def unify2(g):
    SCCs = solve_scc(g)
    cnt = 0
    while(len(SCCs) > 1):
        # print(SCCs)
        # interpret each ssc as a vertex and build a graph (each vertex has id as scc.index + 1)
        k = Graph(len(SCCs), 0)
        # find relations (edges) between all scc
        for i in range(len(SCCs) - 1):
            for j in range(i+1, len(SCCs)):
                scc_1 = SCCs[i]
                scc_2 = SCCs[j]
                flag = find_edge_between_scc(g, scc_1, scc_2)
                if flag == 1:
                    k.addRelation(i+1, j+1)
                elif flag == 0:
                    k.addRelation(j+1, i+1)
        # do topoligical sorting
        DFS(k)
        k.vertices.sort(key=lambda x: x.f)
        # connect least f to max f
        # vertex.id = scc.index + 1 --> scc.index = vertex.id - 1
        x = SCCs[k.vertices[0].id - 1]
        y = SCCs[k.vertices[1].id - 1]
        connect_two_scc(g, x, y)
        cnt += 1
        # reevaluate
        SCCs = solve_scc(g)
    print(SCCs)
    return cnt

# Driver Code
BASE = "Algo/lab6/"
testFile = ["6.1.txt", "6.2.txt", "6.3.txt", "6.4.txt", "Extra6.5.txt", "Extra6.6.txt"]
# for file in testFile:
#     print(file)
#     testcases = readInput(BASE + file)
#     for g in testcases:
#         SCCs = solve_scc(g)
#         res = "result: "
#         if len(SCCs) > 1:
#             res += "0"
#         else:
#             res += "1"
#         print("SCCs:")
#         print([s for s in SCCs])
#         print(res)
    
testcase = readInput(BASE + testFile[5])
for g in testcase:
    print("_"*20)
    cnt = unify(g)
    print(cnt)
    print("_"*20)
