# brute force
# def solve_BF(array:[], k):
#     paired = [False] * len(array)
#     solution = []
#     all_solution = []

#     def recur(start):
#         jump = False
#         if start == (len(array) - 1):
#             all_solution.append(solution.copy())
#             return
#         for index in range(start+1, len(array)):
#             value = array[index]
#             if paired[start] and not paired[index]:
#                 jump = True
#                 recur(index)
#             elif (array[start] != value and (index - start) <= k
#                 and not paired[index]):
#                 solution.append((start, index))
#                 paired[start] = True
#                 paired[index] = True
#                 paired_with = index
#         if not paired[start] or not jump:
#             recur(start+1)
#         if paired[start]:
#             paired[start] = False
#             paired[paired_with] = False
#             solution.pop()

#     recur(0)

#     # maximum = len(max(all_solution))
#     # cnt = 0
#     # for sol in all_solution:
#     #     if len(sol) == maximum:
#     #         cnt += 1
#     return all_solution

def solve_BF(array:[], k):
    paired = [False] * len(array)
    solution = []
    all_solution = []

    def recur(start):
        found_sol = False
        for index in range(len(array)):
            value = array[index]
            if index == start or array[start] != "G": # skip itself and skip if it's not "G"
                continue
            if value == "P" and abs(index - start) <= k and not paired[index]:
                solution.append((start, index))
                paired[start] = True
                paired[index] = True
                found_sol = True
                # find next "G" to pass to recur
                found_g = False
                for g in range(start+1, len(array)):
                    if array[g] == "G" and not paired[g]:
                        found_g = True
                        recur(g)
                        break
                if not found_g:
                    all_solution.append(solution.copy())
                    paired[start] = False
                    paired[index] = False
                    solution.pop()
                    continue
                paired[start] = False
                paired[index] = False
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
        
    recur(0)

    # maximum = len(max(all_solution))
    # cnt = 0
    # for sol in all_solution:
    #     if len(sol) == maximum:
    #         cnt += 1
    return all_solution

            # 0    1    2    3    4
testcase1 = ["G", "P", "P", "G", "P"]
testcase2 = ["P", "P", "G", "G", "P", "G"]
testcase3 = ["G", "P", "G", "P", "P", "G"]
[print(i) for i in solve_BF(testcase1, 2)]
