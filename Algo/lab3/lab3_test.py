from lab3 import solve_BF, solve_greedy

def read_file(path:str) -> tuple:
    with open(path, "r") as openfile:
        array = [s for s in openfile.readline().strip()]
        k = int(openfile.readline().strip())
    return (array, k)

def test(choice:int, skip_brute_force=False):
    normal_list = ["3.1.1", "3.1.2","3.1.3","3.2.1","3.2.2","3.2.3","3.3.1","3.3.2", "3.3.3"]
    extra_list = ["3.4.1", "3.5.1", "3.5.2", "3.5.3",]
    big_list = ["3.4.2", "3.4.3",  "3.4.4", "3.4.5"]
    if choice == 0:
        lst = normal_list
        path = "normal"
    elif choice == 1:
        lst = extra_list
        path = "Extra"
    elif choice == 2:
        lst = big_list
        path = "Extra"
    else:
        return -1
    for case in lst:
        inp = read_file(f"Algo/lab3/Lab 3 test case/{path}/{case}.txt")
        print(case)
        if not skip_brute_force:
            print("Bforce:",len(solve_BF(inp[0], inp[1])[0]))
        print("greedy:",len(solve_greedy(inp[0], inp[1])))

NORMAL = 0;EXTRA = 1;BIG = 2
test(BIG, skip_brute_force=True)