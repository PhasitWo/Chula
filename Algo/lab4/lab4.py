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


import sys
class const:
    best = []
# m is size of coins array (number of different coins)
def minCoins(coins, m, V):
    const.best = []
    sol = []
    def recur(coins, m, V):
        # base case
        if (V == 0):
            const.best.append(sol.copy())
            return 0

        # Initialize result
        res = sys.maxsize

        # Try every coin that has smaller value than V
        for i in range(0, m):
            if (coins[i] <= V):
                sol.append(coins[i])
                sub_res = recur(coins, m, V-coins[i])
                sol.pop()
                # Check for INT_MAX to avoid overflow and see if
                # result can minimized
                if (sub_res != sys.maxsize and sub_res + 1 < res):
                    res = sub_res + 1
                    # const.best = sol.copy()

        return res
    
    res = recur(coins, m, V)
    print(len(const.best))
    return res



# Driver
# 25, [1,3,4]
coins = [1,5,10,20]
m = len(coins)
V = 50
print("Minimum coins required is",minCoins(coins, m, V))
# print(numWays(11, [5, 6, 9, 1]))