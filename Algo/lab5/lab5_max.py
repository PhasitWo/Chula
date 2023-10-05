from math import sqrt
import math
import os, sys
MAX = sys.maxsize

def mysort(vertexs):
    x = sum([x[0] for x in vertexs]) / len(vertexs)
    y = sum([y[0] for y in vertexs]) / len(vertexs)
    centroid = (x, y)
    key = lambda point: (math.atan2(point[1] - centroid[1], point[0] - centroid[0]) + 2 * math.pi) % (2 * math.pi)
    sorted_index = []
    for p in vertexs:
        sorted_index.append((key(p), p))
    sorted_index.sort(key=lambda x : x[0])
    sorted_vertexs = [v[1] for v in sorted_index]
    return sorted_vertexs

def dist(p1, p2):
    return sqrt((p1[0] - p2[0])*(p1[0] - p2[0]) +
                (p1[1] - p2[1])*(p1[1] - p2[1]))
 
def cost(points, indices):
    if indices == None:
        return MAX
    sum_ = 0
    # compute sum of all perimeter of each triangles
    for i in range(0, len(indices), 3):
        p1, p2, p3 = points[indices[i]], points[indices[i+1]], points[indices[i+2]]
        sum_ += dist(p1, p2) + dist(p2, p3) + dist(p3, p1)
    return sum_
 
memmo = {}
def mTC(points, i, j):
     
    # There must be at least three points between i and j
    # in order to do triangulation
    if (j < i + 2):
        return ()
    
    # Cache
    if (i, j) in memmo:
        return memmo.get((i,j))

    # Initialize result as infinite
    res = ()
    # ** let cost(None) = MAX **
    # Find minimum triangulation by considering all
    for k in range(i + 1, j):
        res = max(res, (mTC(points, i, k) + (i, k, j) + mTC(points, k, j)), key=lambda x : cost(points, x))

    memmo.update({(i, j):res})
    return res
 
 # util
def read_file(path:str) -> tuple:
    with open(path, "r") as openfile:
        lines = openfile.readlines()
        vertex_cnt = int(lines.pop(0).strip())
        vertexs = []
        for item in lines:
            x, y = map(float, item.strip().split())
            vertexs.append([x, y])
    return vertex_cnt, vertexs
# util
def extract_diagonals(vertexs, triangles):
    diagonals = []
    def check(x, y):
        if x == len(vertexs) - 1 and y == 0:
            return
        elif abs(x - y) == 1:
            return
        elif (vertexs[y], vertexs[x]) in diagonals: # duplicate
            return
        diagonals.append((vertexs[x], vertexs[y]))
        
    for i in range(0, len(triangles), 3):
        i1, i2, i3 = triangles[i], triangles[i+1], triangles[i+2]
        check(i1, i2)
        check(i2, i3)
        check(i3, i1)
    return diagonals

def sort_vertex(vertexs:list):
    vertexs.sort(key=lambda x : [x[1],x[0]])
    print(vertexs)
# driver
BASE_PATH = "Algo/lab5/testcase/"
# test all
# test_case = os.listdir(BASE_PATH)
# test_case.remove(".DS_Store")
# test_case.sort(key=lambda x : float(x.strip(".txt").replace("Extra", "")))
# for case in test_case:
#     cnt, vertexs = read_file(BASE_PATH + case)
#     vertexs = mysort(vertexs)
#     print(case)
#     triangles = mTC(vertexs, 0, len(vertexs) - 1)
#     print("cost:",round(cost(vertexs, triangles), 4))
#     print("triangles:", triangles)
#     print("diagonals:", extract_diagonals(vertexs, triangles))
#     memmo = {} # clear cache
#     print("_"*10)




# # single test
from playground import draw_polygon
cnt, vertexs = read_file(BASE_PATH + "0.txt")
vertexs = mysort(vertexs)
triangles = mTC(vertexs, 0, len(vertexs) - 1)
print("cost:",round(cost(vertexs, triangles), 4))
print("triangles:", triangles)
print("diagonals:", extract_diagonals(vertexs, triangles))
draw_polygon(vertexs, triangles, extract_diagonals(vertexs, triangles))





