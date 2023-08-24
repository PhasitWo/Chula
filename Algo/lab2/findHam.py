def findHam(adjacencyMatrix):
    adj = adjacencyMatrix
    # Mark all the vertices as not visited
    visited = [False] * len(adj)
    result = {"path": [], "cycle": []}
    path = []
    
    def dfs(start):
        visited[start] = True
        path.append(start)
        if len(path) == len(adj):
            # check if this last vertex has an edge to the source vertex
            if adj[start][path[0]] == 1:
                path.append(path[0])
                result["cycle"].append(path.copy())
                path.pop() # pop source vertex
            # if not, then we get a hamiltonian path
            else:
                result["path"].append(path.copy())
            path.pop()
            visited[start] = False
            return
        for vertex, value in enumerate(adj[start]):
            if value == 0:  # no edge between start and vertex
                continue
            # if that vertex is not visited, tranverse to that path
            if not visited[vertex]:
                dfs(vertex)
        # go back 1 step and find another route
        path.pop()
        visited[start] = False

    for i in range(len(adj)):
        dfs(i)
    return result


testcase = [
    [0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0],
]
testcase2 = [
    [0, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0],
]

testcase3 = [
    [ 0, 1, 1, 0, 0, 1 ],
    [ 1, 0, 1, 0, 1, 1 ],
    [ 1, 1, 0, 1, 0, 0 ],
    [ 0, 0, 1, 0, 1, 0 ],
    [ 0, 1, 0, 1, 0, 1 ],
    [ 1, 1, 0, 0, 1, 0 ],
]
""" Input Graph Testcase3:
   (0)--------(2)
    |   \   /  |
    |    (1)   |
    |   /  |   |
    | /    |   |
   (5)----(4)--(3)"""

testcase4 = [
[0, 1, 0, 1, 0, 1, 0, 0], 
[1, 0, 1, 0, 0, 0, 1, 0], 
[0, 1, 0, 1, 0, 0, 0, 1], 
[1, 0, 1, 0, 1, 0, 0, 0], 
[0, 0, 0, 1, 0, 1, 0, 1], 
[1, 0, 0, 0, 1, 0, 1, 0], 
[0, 1, 0, 0, 0, 1, 0, 1], 
[0, 0, 1, 0, 1, 0, 1, 0], 
]
"""
   (0)----------------(1)
    |   \           /  |
    |    (5)-----(6)   |
    |     |       |    |
    |    (4)-----(7)   |
    |   /          \   |
   (3)----------------(2)
"""

extra = [
[0, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 0],
[0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 1, 0]
]
def matrix_from_file(file_path):
    result = []
    file = open(file_path,"r")
    index = 0
    for line in file:
        result.append([])
        for node in line.split():
            result[index].append(int(node))
        index += 1
    return result   
# test
for k, v in findHam(matrix_from_file("/Users/phasit/Downloads/lab/lab2/Lab 2 test case/1.Regular/2.1.7.txt")).items():
    print(k,":")
    print('\n'.join(str(p) for p in v))
