# numWays to find coin change = numWays to find coin change by INCLUDING current coin + numWays to find coin change by EXCLUDING current coin 
# numWays(amount, denoms, focus_denom) = numWays(amount-denoms[focus_denom], denoms, focus_denom) + numWays(amount, denoms, focus_denom+1)
# When avoiding repeated recursive call, we can only get the number of all solution right, but not able to track the solution of repeated call.
# a workaround is to save solutions along with cnt in memmo ,but in exchange for a huge cost of space.
def numWays(amount, denoms:list) -> int:
    result = 0
    all_solution = []
    solution = []
    memmo = {}

    def recur(amount, denoms:list, focus_denom):
        # # avoid re-computation
        # cache = memmo.get((amount, focus_denom))
        # if cache != None:
        #     print("OVERLAP")
        #     return cache
        cnt = 0
        if amount == 0: # cannot include any coin anymore
            all_solution.append(solution.copy())
            return 1
        if amount < 0 or focus_denom >= len(denoms): # amount is negative or no more coin left to consider
            return 0
        # include denoms[focus_denom] coin
        solution.append(denoms[focus_denom])
        cnt += recur(amount - denoms[focus_denom], denoms, focus_denom)
        solution.pop()
        # exclude denoms[focus_denom] coin
        cnt += recur(amount, denoms, focus_denom + 1)
        memmo.update({(amount, focus_denom):cnt})
        return cnt
    
    # initial call
    solution.append(denoms[0])
    result += recur(amount - denoms[0], denoms, 0)
    solution.pop()
    result += recur(amount, denoms, 1)
    print(all_solution)
    return result


# modify above method, return the solution that has minimum coin.
# choose best solution between INCLUDE and EXCLUDE case (minimum coin)
def minCoin(amount, denoms:list) -> int:
    memmo = {}
    def recur(amount, denoms:list, focus_denom):
        # avoid re-computation
        cache = memmo.get((amount, focus_denom))
        if cache != None:
            print("OVERLAP", (amount, focus_denom))
            return cache
        if amount == 0: # cannot include any coin anymore
            return []
        if amount < 0 or focus_denom >= len(denoms): # amount is negative or no more coin left to consider
            return None
        # include denoms[focus_denom] coin
        out1 = recur(amount - denoms[focus_denom], denoms, focus_denom)
        if out1 != None:
            out1 += [denoms[focus_denom]]
        # exclude denoms[focus_denom] coin
        out2 = recur(amount, denoms, focus_denom + 1)
        # compare both case
        res = None
        if out1 == None and out2 == None:
            res = None
        elif out1 != None and out2 != None:
            res = min(out1, out2, key=lambda x : len(x))
        else:
            res = out1 if out1 != None else out2
        # save in memmo
        saved_value = res.copy() if res != None else None
        memmo.update({(amount, focus_denom):saved_value})
        return res
    
    # initial call
    denoms.sort(reverse=True)
    res = recur(amount, denoms, 0)
    return res
print(minCoin(100, [1,3,4,6]))