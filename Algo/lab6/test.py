# from graph import Graph, Vertex, Color
SCCs = [1, 2, 3, 4, 5]
for i in range(len(SCCs) - 1):
        for j in range(i+1, len(SCCs)):
                print(SCCs[i], SCCs[j])