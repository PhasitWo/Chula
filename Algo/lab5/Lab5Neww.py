import numpy as np

#input = [[0,0],[1,0],[2,1],[1,2],[0,2]]
#input = [[0,0],[2,-1],[1,0],[2,1]]
#input = [[0,0],[2,0],[1,1.5],[2,2],[0,2]]
#input = [[1,0],[2,1],[1,2]] # print cost only
#input = [[1,0],[2,1]]
#input = [[1,0]]
#input = [[0,0],[2,2],[1,3.5],[2,4],[0,4],[0,2]]

def readfile(path): 
    inp = []
    vector=[]
    file = open(path,"r")
    v=int(file.readline())
    for line in file:
        inp.append(line.strip().split())
    for i in inp:
        vector.append([float(i[0]),float(i[1])])
    return vector,v

def cost(a,b) :
    return np.sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)

def findShortDiagonal(input,check) :
    if len(input) <= 3 and check == False:
        return 0
    else:
        check = True
        allInput = []
        allMinVal= []
        allListPath = []
        for i in range(len(input)) :
            #print("i :",i)
            inputt = []
            for j in range(i+1,len(input)) :
                inputt.append(input[j])
            if i == 0:
                inputt.append(input[0])
            else:
                for k in range(i+1) :
                    inputt.append(input[k])
            #print("inputt",inputt)
            allInput.append(inputt)
            listCost = []
            for l in range (2,len(inputt)-1) :
                listCost.append(cost(inputt[0],inputt[l]))
            #print("listCost",listCost)
            listPath = []
            min_val = listCost[0]
            index = 0
            for m in range(len(listCost)):
                if listCost[m] < min_val:
                    min_val = listCost[m]
                    index = m
            listPath.append(inputt[0])
            listPath.append(inputt[index+2])
            #print("min_val:",min_val)
            #print("listPath:",listPath)
            allMinVal.append(min_val)
            allListPath.append(listPath) 
        #print("allMinVal",allMinVal)
        minCost = allMinVal[0]
        indexP = 0
        for c in range(len(allMinVal)):
            if allMinVal[c] < minCost:
                minCost = allMinVal[c]
                indexP = c
        
        print("Diagonal :",allListPath[indexP])
        #print("indexP",indexP)   
        a = allInput[indexP]
        ind = 0
        for x in range(len(a)):
            if a[x] == allListPath[indexP][1]:
                ind = x
        if ind == 2 :
            input.remove(a[1])
        else :
            ind = len(a)-2 
            input.remove(a[len(a)-1])
        #print("input",input)
        minn = 2*minCost
        if len(input) > 3 :
            minn += findShortDiagonal(input,check)    
        return minn
    
# input,numOfPoint=readfile("1.1.txt")
# print("input:",input)
# input2 = []
# for e in input:
#     input2.append(e)
    

# sumCost = findShortDiagonal(input,False)
# if sumCost!= 0 or sumCost == 0 and len(input)==3:            
#     cost2=0
#     for i in range(len(input2)-1) :
#         cost2 += cost(input2[i],input2[i+1])
#     sumCost +=  cost2 + cost(input2[len(input2)-1],input2[0]) 
#     print(sumCost)
# else :
#     print("don't have triangle")
    
