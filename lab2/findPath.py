# def findPathBFS(adjacencyMatrix, start: int, end: int):
#     # mark all vertices as not visited
#     adj = adjacencyMatrix
#     visited = [False] * len(adj)
#     queue = []
#     queue.append(start)
#     visited[start] = True
#     # while queue is not empty
#     while queue:
#         n = queue.pop(0)
#         if n == end:
#             return True

#         for i in range(len(adj[n])):
#             # adj[n][i] == 0 means no edge between them
#             if adj[n][i] == 1 and visited[i] == False:
#                 queue.append(i)
#                 visited[i] = True
    # return False

# depth-first search -> Time Complexity : O(2^vertice)
def path(adjacencyMatrix, start, end):
    adj = adjacencyMatrix
    # Mark all the vertices as not visited
    visited = [False] * len(adj)
    all_path = []
    path = []
    def dfs(start, end):
        visited[start] = True
        path.append(start)
        if start == end:
            all_path.append(path.copy())
            path.pop()
            visited[start] = False
            return
        for vertex, value in enumerate(adj[start]):
            if value == 0: # no edge between start and vertex
                continue
            # if that vertex is not visited, tranverse to that path
            if not visited[vertex]:
                dfs(vertex, end)

        path.pop()
        visited[start] = False
    dfs(start, end)
    return all_path
    
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

[print(p) for p in path(testcase2, 0, 5)]