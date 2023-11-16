import networkx, matplotlib.pyplot as plt

def readInput(file_path:str) -> networkx.Graph:
    with open(file_path, "r") as openfile:
        matrix = []
        for line in openfile:
            row = list(map(int, line.strip().split()))
            matrix.append(row)
    g = networkx.Graph()
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            if matrix[i][j] == 1:
                g.add_edge(i, j)
    return g

# www.geeksforgeeks.org/introduction-and-approximate-solution-for-vertex-cover-problem/
def approx_VC(g: networkx.Graph):
    q = g.copy()
    result = []
    while(q.number_of_edges() != 0):
        # pick any edge
        i, j = list(q.edges)[0]
        # i, j = q.edges[0]
        result.append(i)
        result.append(j)
        for e in q.edges:
            if e[0] == i or e[0] == j:
                q.remove_edge(e[0], e[1])
            elif e[1] == i or e[1] == j:
                q.remove_edge(e[0], e[1])
    # coloring
    color = []
    for node in g:
        if node in result:
            color.append("red")
        else:
            color.append("green")
    networkx.draw(g, with_labels = True, node_color = color)
    plt.show()
    print(result)
    print(len(result))
    return result

g = readInput("Algo/lab10/sample2.txt")
approx_VC(g)