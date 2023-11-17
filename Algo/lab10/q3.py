import networkx, matplotlib.pyplot as plt
from q1 import check_vertex_cover, display

def readInput(file_path:str) -> (int, list):
    with open(file_path, "r") as openfile:
        clause_cnt = int(openfile.readline().strip())
        clause_lst = []
        for line in openfile:
            row = list(map(int, line.strip().split()))
            clause_lst.append(row)
        return clause_cnt, clause_lst
    
def reduce_3SAT_to_VC(clause_lst:list[int]):
    g = networkx.Graph()
    # find variables
    variables = set()
    for clause in clause_lst:
        x = {abs(i) for i in clause.copy()}
        variables.update(x)
    # create variable pair
    for var in variables:
        g.add_edge("vp/"+str(var), "vp/"+str(-var))
    for index, clause in enumerate(clause_lst):
        # create clause triangle
        prefix = f"ct{index}/"
        g.add_edge(prefix+str(clause[0]), prefix+str(clause[1]))
        g.add_edge(prefix+str(clause[1]), prefix+str(clause[2]))
        g.add_edge(prefix+str(clause[2]), prefix+str(clause[0]))
        # connect CT and VP
        g.add_edge(prefix+str(clause[0]), "vp/"+str(clause[0]))
        g.add_edge(prefix+str(clause[1]), "vp/"+str(clause[1]))
        g.add_edge(prefix+str(clause[2]), "vp/"+str(clause[2]))
    matrix = networkx.to_numpy_array(g)
    k = len(variables) + 2*len(clause_lst)
    # can use this func in q1 to find solution
    # ans = check_vertex_cover(matrix, k)
    # display(matrix, ans)
    print(g.number_of_nodes())
    print(k)
    print(matrix)
    # networkx.draw(g, with_labels = True)
    # plt.show()

clause_cnt, clause_lst = readInput("Algo/lab10/testcase/3.2.txt")
reduce_3SAT_to_VC(clause_lst)