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
        # pick node that has the most degree
        deg = list(q.degree)
        deg.sort(key= lambda x : x[1], reverse=True)
        i = deg[0][0]
        result.append(i)
        adjNode = list(q[i].keys())
        for j in adjNode:
            q.remove_edge(i, j)
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

g = readInput("Algo/lab10/testcase/2.3.txt")
approx_VC(g)