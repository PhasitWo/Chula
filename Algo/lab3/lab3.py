# brute force : Time Complexity could be O(min(G's, P's)^max(G's, P's)) ???
def solve_BF(array:[], k):
    paired = [False] * len(array)
    solution = []
    all_solution = []
    # fuction to find lower bound and upper bound to search for P
    clamp = lambda n, minn, maxn: max(min(maxn, n), minn) 

    def recur(start):
        found_sol = False
        lower = clamp(start-k, 0 , len(array))
        upper = clamp(start+k+1, 0 , len(array))
        for index in range(lower, upper):
            value = array[index]
            if index == start: # skip itself
                continue
            if value == "P" and not paired[index]:
                found_sol = True
                solution.append((start, index))
                paired[start], paired[index] = True, True
                # find next "G" to pass to recur
                found_g = False
                for g in range(start+1, len(array)):
                    if array[g] == "G" and not paired[g]:
                        found_g = True
                        recur(g)
                        break
                if not found_g:
                    all_solution.append(solution.copy()) # save this solution
                # roll back 1 step and continue finding other Passenger for this Grab
                paired[start], paired[index] = False, False
                solution.pop()
        
        if not found_sol:
        # find next "G" to pass to recur
            found_g = False
            for g in range(start+1, len(array)):
                if array[g] == "G" and not paired[g]:
                    found_g = True
                    recur(g)
                    break
            if not found_g:
                all_solution.append(solution.copy())
                return
    # Driver Code: find first g to pass to recur
    for index, value in enumerate(array):
        if value == "G":
            recur(index)
            break
    all_solution.sort(key=lambda x:len(x), reverse=True)
    return all_solution

# greedy : Time Complexity could be O(n^2)???
def solve_greedy(array, k):
    solution = []
    paired = [False] * len(array)
    for i1 in range(len(array)):
        if paired[i1]:
            continue
        v1 = array[i1]
        # p or g look for the other one on the right in k range
        for i2 in range(i1+1, i1+1+k):  
            if i2 >= len(array): # index out of range
                break
            v2 = array[i2]
            if v1 != v2 and not paired[i2]:
                solution.append((i1, i2))
                paired[i1], paired[i2] = True, True
                break

    return solution

# wrong greedy --> not suitable with this problem
# g_pos and p_pos with the same index doesn't mean both are closest to each other
    # grab_pos = []
    # passenger_pos = []
    # solution = []
    # for index, value in enumerate(array): 
    #     if value == "G":
    #         grab_pos.append(index)
    #     else:
    #         passenger_pos.append(index)
    # # sort
    # grab_pos.sort()
    # passenger_pos.sort()
    # print("G pos:",grab_pos)
    # print("P pos:",passenger_pos)  

    # maximum = min(len(grab_pos), len(passenger_pos))
    # for i in range(maximum):
    #     if abs(grab_pos[i] - passenger_pos[i]) <= k:
    #         solution.append((grab_pos[i], passenger_pos[i]))