
def solve_greedy2(array, k):
    solution = []
    paired = [False] * len(array)
    clamp = lambda n, minn, maxn: max(min(maxn, n), minn)
    for i1 in range(len(array)):
        if paired[i1]:
            continue
        v1 = array[i1]
        # p or g look for the other one on the right in k range
        for i2 in range(clamp(i1+k, 0, len(array)-1), i1, -1):  
            v2 = array[i2]
            if v1 != v2 and not paired[i2]:
                solution.append((i1, i2))
                paired[i1], paired[i2] = True, True
                break
    return solution

# inp = read_file(f"Algo/lab3/Lab 3 test case/normal/3.1.2.txt")
# print("test",len(solve_greedy2(inp[0], inp[1])))