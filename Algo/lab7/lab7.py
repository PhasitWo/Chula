from graph import Graph, Vertex

INF = 999999
def readInput(filePath:str) -> (Graph, list[tuple]):
    questions = []
    with open(filePath, "r") as file:
        cnt = 0
        for line in file:
            inputs = list(map(int, line.strip().split()))
            if cnt == 0: # first line
                g = Graph(inputs[0], inputs[1])
            elif len(inputs) == 3:
                g.addRelation(inputs[0], inputs[1], inputs[2])
            else:
                questions.append((inputs[0], inputs[1]))
            cnt += 1
    return (g, questions)

def solve_FW(g:Graph, questions:list[tuple]):
    n = g.vertex_cnt
    g.init_D0()
    g.init_Pi0()
    d = g.D
    pi = g.Pi
    # compute D(u) and Pi(u) from u=1 to n
    for k in range(1, n+1):
        new_d = [[INF for y in range(n)] for x in range(n)]
        d.append(new_d)
        new_pi = [[None for y in range(n)] for x in range(n)]
        pi.append(new_pi)
        for i in range(n):
            for j in range(n):  
                x = k-1 # x is intermediate vertex index
                d[k][i][j] = min(d[k-1][i][j],  d[k-1][i][x]+d[k-1][x][j])
                if d[k-1][i][j] <= d[k-1][i][x]+d[k-1][x][j]:
                    pi[k][i][j] = pi[k-1][i][j]
                else:
                    pi[k][i][j] = pi[k-1][x][j]
    # find path for each question
    for u, v in questions:
        s = f"({u},{v}) -> "
        s += str(find_path(pi[n], u, v)) + "\n"
        print(s)
    return (d[n], pi[n])

def find_path(pi:list[list], vertex_id1, vertex_id2):
    lst = []
    def recur(pi, i, j):
        if i == j:
            lst.append(i+1)
        elif pi[i][j] == None:
            print("No Path")
        else:
            recur(pi, i, pi[i][j])
            lst.append(j+1)
    recur(pi, vertex_id1-1, vertex_id2-1) # convert id to array index
    return lst


# Driver Code
g, q = readInput("Algo/lab7/7.1.txt")
solve_FW(g, q)
