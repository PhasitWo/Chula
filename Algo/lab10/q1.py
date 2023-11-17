import itertools, networkx, matplotlib.pyplot as plt

def readInput(file_path:str) -> (list, int):
    with open(file_path, "r") as openfile:
        k = int(openfile.readline().strip())
        matrix = []
        for line in openfile:
            row = list(map(int, line.strip().split()))
            matrix.append(row)
        return matrix, k

def check_vertex_cover(matrix: list[list[int]], k:int) -> list:
    vertex_cnt = len(matrix)
    combinations = itertools.combinations(range(1, vertex_cnt+1), k)
    ans = []
    for c in combinations:
        is_vc = True
        for i in range(vertex_cnt):
            for j in range(i+1, vertex_cnt):
                if matrix[i][j] == 1:
                    # plus 1 to match vertex-indexing style of combinations
                    if (i+1 not in c) and (j+1 not in c): 
                        is_vc = False
                        break
            if not is_vc:
                break
        if is_vc:
            ans.append(c)
    return ans

def display(matrix: list[list[int]], result) -> None:
    g = networkx.Graph()
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            if matrix[i][j] == 1:
                g.add_edge(i+1, j+1)
    color = []
    for node in g:
        if node in result[0]:
            color.append("red")
        else:
            color.append("green")
    networkx.draw(g, with_labels = True, node_color = color)
    plt.show()


# driver code
if __name__ == '__main__' :
    matrix, k = readInput("Algo/lab10/testcase/1.5.txt")
    ans = check_vertex_cover(matrix, k)
    display(matrix, ans)
    if len(ans) != 0:
        print("Yes")
        [print(a) for a in ans]
    else:
        print("No")