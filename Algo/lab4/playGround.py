import sys
INT_MAX = sys.maxsize
class const:
    min = INT_MAX
    best = None

def numWays(amount, denoms:list) -> int:
    denoms.sort(reverse=False)
    solution = []
    memmo = {}

    def recur(amount, denoms:list, focus_denom):
        # avoid re-computation
        cache = memmo.get((amount, focus_denom))
        if cache != None:
            print("OVERLAP", f"({amount},{denoms[focus_denom:]}) --> {cache}")
            return cache
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
    print(const.min)
    print(const.best)
    return min(out1, out2)

print(numWays(6, [1,3,4]))