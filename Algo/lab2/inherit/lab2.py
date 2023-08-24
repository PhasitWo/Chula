# -*- coding: utf-8 -*-

class Graph:
    def __init__(self,graph):
        self.AllPath = []
        self.graph = graph
        self.Paths =[]

    def findPath(self,u, v, isVisit, path):
        isVisit[u] = True
        path.append(u)
        h=0
        if u == v:
            self.addAllPath(path)
        else:
            for i in range(len(g[u])):
                x = self.graph[u][i]
                if x != 0 and isVisit[i]==False:
                    while x > 0:
                        self.findPath(i, v, isVisit, path)
                        x-=1
        path.pop()
        isVisit[u]=False

    def Path(self,u,v):
        self.AllPath = []
        visit = [False]*len(self.graph)
        path = []   
        self.findPath(u,v,visit,path)
        # for i in self.AllPath:
        #     print(i)
        return self.AllPath

    def printGraph(self):
        for i in self.graph:
            print(i)

    def printAllPath(self):
        if self.AllPath:
            print("All path from %d to %d"%(self.AllPath[0][0],self.AllPath[0][-1]))
            for i in self.AllPath:
                print(i)

    def addAllPath(self,path):
        p_copy = path[:]
        self.AllPath.append(p_copy)
    
    def givenHamilCheck(self,u,v):
        self.Path(u,v)
        c=0
        for i in self.AllPath:
            if(len(i)==len(self.graph)):
                if(self.graph[v][u]!=0):
                    print("Have Hamiltonian cycle : ",i)
                else:
                    print("Have Hamiltonian path : ",i)
                    c=1
        if(c==0):
            print("Not have Hamiltonian path/cycle")

    def HamilCheck(self):
        c=0
        for u in range(len(self.graph)):
            for v in range(len(self.graph)):
                self.Path(u,v)
                if self.AllPath:
                    for i in self.AllPath:
                        self.Paths.append(i[:])
                for i in self.AllPath:
                    if(len(i)==len(self.graph)):
                        if(self.graph[v][u]!=0):
                            print("Have Hamiltonian cycle : ",i)

                        else:
                            print("Have Hamiltonian path : ",i)
                        c+=1
        # if(c==0):
        #     print("Not have Hamiltonian path/cycle")
        #     self.Connect()
        # return c
    
    def Connect(self):
        maxl = 0
        big = []
        path = []
        for i in self.Paths:
            if maxl < len(i) :
                big = i
                maxl = len(i)
        path.append(big)
        for i in self.Paths:
            a = big + i
            if self.Perfect(a,len(self.graph)):
                path.append(i)
                break
        print(path)
        print("Have to connect :")
        for i in range(len(path)-1):
             print(path[i][-1],path[i+1][0])
        print(path[0][0],path[-1][-1])
        print("to have Hamiltonian cycle: ",a)

    
    def Perfect(self,array,v):
        a = array[:]
        for i in range(v):
            if i in a:
                a.remove(i)
            else:
                return False
        if a:
            return False
        return True
            
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
        
# g =[[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,0,0,1,0]]
# g = [[0,1,1,0,0],[1,0,0,0,1],[1,0,0,1,0],[0,0,1,0,1],[0,1,0,1,1]]
# g = [[0,1,0,0,0,1],[1,0,1,0,0,0],[0,1,0,1,0,0],[0,0,1,0,1,0],[0,0,0,1,0,1],[1,0,0,0,1,0]]
# g = [[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]]
# g =  [[0,1,1,1,0],[1,0,0,1,1], [1,0,0,1,0], [1,1,1,0,1], [0,1,0,1,0]]
# g = [[0,1,0,0,0,0,0,1,0,1,0],[1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,0,1,1,1,0,0],[0,0,0,0,0,1,0,0,1,1,1],[0,0,1,0,0,0,1,0,0,0,1],[0,0,0,1,0,0,0,0,0,1,0],[0,0,1,0,1,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,1,0],[0,0,1,1,0,0,0,0,0,0,0],[1,0,0,1,0,1,0,1,0,0,0],[0,0,0,1,1,0,0,0,0,0,0]]

path = "/Users/phasit/Downloads/lab/lab2/Lab 2 test case/1.Regular/2.1.3.txt"
# path = "/3rd/ALGOR/lab2/2Extra/2.2.6.txt"


g = matrix_from_file(path)

h = Graph(g)

# h.Path(0,2)
# h.printAllPath()
# h.givenHamilCheck(0,2)
# # print(h.Path(1,3))
h.HamilCheck()
# print(h.Paths)
# h.Connect()
