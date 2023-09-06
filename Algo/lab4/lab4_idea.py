# numways(amount, denoms, focus_denom) = numways(amount-0*denoms[focus_denom], focus_denom + 1) + ... + numways(amount-k*denoms[focus_denom], focus_denom + 1)
# Ex. numways to find change --> amount = 50, denoms = {20, 10, 5, 1}
#  = (numways of using 0 of 20) + (numways of using 1 of 20)  + ... + (numways of using 2 of 20)   **next layer will not include 20 anymore**
# hard to track the all the solution
def numWays2(amount, denoms:list) -> int:
    denoms.sort(reverse=True)
    result = 0
    memmo = {}

    def recur(amount, denoms:list, focus_denom):
        if len(denoms) - focus_denom == 1:
            # if amount is divisible by this only denom
            if amount % denoms[focus_denom] == 0:
                return 1
            else:
                return 0
        cnt = 0
        n = 0
        remain = amount - n*denoms[focus_denom]
        while(remain >= 0):
            # avoid re-computation
            cache = memmo.get((remain, focus_denom + 1))
            if cache != None:
                print("OVERLAP")
                cnt += cache
            else:
                cnt += recur(remain, denoms, focus_denom + 1)
            n += 1
            remain = amount - n*denoms[focus_denom]
        memmo.update({(amount,focus_denom):cnt})
        return cnt
    
    result += recur(amount, denoms, 0)
    return result

# รุ่นพี่ minCoin idea, so slowwwwwww
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
print(numWays2(50, [1, 5, 10, 20]))