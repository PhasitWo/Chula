# Recursive implementation for minimum
# cost convex polygon triangulation
from math import sqrt
import os, sys
from Lab5Neww import findShortDiagonal
from Lab5Neww import cost as pcost
MAX = sys.maxsize
 
def dist(p1, p2):
    return sqrt((p1[0] - p2[0])*(p1[0] - p2[0]) + \
                (p1[1] - p2[1])*(p1[1] - p2[1]))
 
def cost(points, i, j, k):
    p1 = points[i]
    p2 = points[j]
    p3 = points[k]
    return dist(p1, p2) + dist(p2, p3) + dist(p3, p1)
 
memmo = {}
def mTC(points, i, j):
     
    # There must be at least three points between i and j
    # in order to do triangulation
    if (j < i + 2):
        return 0
    
    # Cache
    cache = memmo.get((i, j))
    if cache != None:
        return cache

    # Initialize result as infinite
    res = MAX
    best_k = -1
    # Find minimum triangulation by considering all
    for k in range(i + 1, j):
        out = min(res, (mTC(points, i, k) + mTC(points, k, j) + cost(points, i, k, j)))
        if out != res:
            best_k = k
        res = out
    res = round(res, 4)
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

# driver
BASE_PATH = "Algo/lab5/testcase/"
# test_case = os.listdir(BASE_PATH)
# test_case.sort(key=lambda x : float(x.strip(".txt").replace(".", "").replace("Extra", "")))
# for case in test_case:
#     vertex_cnt, vertexs = read_file(BASE_PATH + case)
#     print(case)
#     print(mTC(vertexs, 0, len(vertexs) - 1))
#     print("_"*10)
cnt, vertexs = read_file(BASE_PATH + "0.txt")
print(mTC(vertexs, 0, len(vertexs) - 1))

# numOfPoint,input=read_file(BASE_PATH + "0.txt")
# print("input:",input)
# input2 = []
# for e in input:
#     input2.append(e)
# sumCost = findShortDiagonal(input2,False)
# if sumCost!= 0 or sumCost == 0 and len(input)==3:            
#     cost2=0
#     for i in range(len(input2)-1) :
#         cost2 += pcost(input2[i],input2[i+1])
#     sumCost +=  cost2 + pcost(input2[len(input2)-1],input2[0]) 
#     print(sumCost)
# else :
#     print("don't have triangle")