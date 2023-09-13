# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10000)

def readfile(path): 
    inp = []
    vector=[]
    file = open(path,"r")
    v=int(file.readline())
    for line in file:
        inp.append(line.strip().split())
    for i in inp:
        vector.append([int(i[0]),int(i[1])])
    return vector,v

def distanceCal(inp):
    ret=((((inp[0][0]-inp[1][0])**2)+((inp[0][1]-inp[1][1])**2))**0.5)+((((inp[1][0]-inp[2][0])**2)+((inp[1][1]-inp[2][1])**2))**0.5)+((((inp[2][0]-inp[0][0])**2)+((inp[2][1]-inp[0][1])**2))**0.5)
    return ret
        
    

def startTriangular(inp,cut):
   cnt=0
   for i in inp:
       if i[0]!=-2:
           cnt+=1
   if(cnt==3):
       dis=distanceCal(inp)
       return dis
   else:
       temp=[]
       minDis=0
       minIn=0
       for i in range(len(inp)):
           if inp[i][0] != -2:  
               if i==0:
                   temp.append((inp[-1])[:])
                   temp.append((inp[i])[:])
                   temp.append((inp[i+1])[:])
                   minDis=distanceCal(temp)
               elif i==len(inp)-1:
                   temp.append((inp[-2])[:])
                   temp.append((inp[-1])[:])
                   temp.append((inp[0])[:])
               else:
                   temp.append((inp[i-1])[:])
                   temp.append((inp[i])[:])
                   temp.append((inp[i+1])[:])
               distance=distanceCal(temp)
               if distance<minDis:
                   minDis=distance
                   minIn=i
       ret=inp[:]
       cut.append(minIn)
       ret[minIn]=[-2,-2]
       return startTriangular(ret, cut)
       
        
                
inp=[[0,0],[1,0],[2,1],[1,2],[0,2]]
cut=[]
test=startTriangular(inp,cut)
print("test : ",test)
print("cut : ",cut)