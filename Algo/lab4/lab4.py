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

# modify above method, return the number of coin in the solution.
# choose minimum amount of coin in the solution between include and exclude case
import sys
INT_MAX = sys.maxsize
class const:
    min = INT_MAX
    best = None

def minCoin(amount, denoms:list) -> int:
    denoms.sort(reverse=True)
    solution = []
    memmo = {}

    def recur(amount, denoms:list, focus_denom):
        # # avoid re-computation
        # cache = memmo.get((amount, focus_denom))
        # if cache != None:
        #     print("OVERLAP", f"({amount},{denoms[focus_denom:]}) --> {cache}")
        #     return cache
        # base case
        if amount == 0: # cannot include any coin anymore
            if len(solution) < const.min:
                print("FOUND MIN!!!!!!!!!!!", solution)
                const.min = len(solution)
                const.best = solution.copy()
            return len(solution)
        if amount < 0 or focus_denom >= len(denoms): # amount is negative or no more coin left to consider
            return INT_MAX
        # include denoms[focus_denom] coin
        solution.append(denoms[focus_denom])
        out1 = recur(amount - denoms[focus_denom], denoms, focus_denom)
        solution.pop()
        # exclude denoms[focus_denom] coin
        out2 = recur(amount, denoms, focus_denom + 1)
        memmo.update({(amount, focus_denom):min(out1, out2)})
        return min(out1, out2)
    
    # initial call
    solution.append(denoms[0])
    out1 = recur(amount - denoms[0], denoms, 0)
    solution.pop()
    out2 = recur(amount, denoms, 1)
    print(const.best)
    return min(out1, out2)

print(minCoin(100, [1,3,4,6]))