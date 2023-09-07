

def numWays(amount, denoms:list) -> int:
    memmo = {}

    def recur(amount, denoms:list, focus_denom):
        # avoid re-computation
        cache = memmo.get((amount, focus_denom))
        if cache != None:
            return cache
        # base case
        sub_sols = []
        if amount == 0: # cannot include any coin anymore
            return [[]]
        if amount < 0 or focus_denom >= len(denoms): # amount is negative or no more coin left to consider
            return None
        # include denoms[focus_denom] coin
        out1 = recur(amount - denoms[focus_denom], denoms, focus_denom)
        if out1 != None:
            for sol in out1:
                sub_sols.append(sol + [denoms[focus_denom]])
        # exclude denoms[focus_denom] coin
        out2 = recur(amount, denoms, focus_denom + 1)
        if out2 != None:
            sub_sols += out2
        # save in memmo
        memmo.update({(amount, focus_denom):sub_sols})
        return sub_sols
    
    # initial call
    res = recur(amount, denoms, 0)
    print(f"amount = {amount}\ncoins [] = {denoms}\nWays to make change = {len(res)}")
    print("_"*40)
    return res

# modify above method, return the solution that has minimum coin.
# choose best solution between INCLUDE and EXCLUDE case (minimum coin)
def minCoin(amount, denoms:list) -> int:
    memmo = {}
    def recur(amount, denoms:list, focus_denom):
        # avoid re-computation
        cache = memmo.get((amount, focus_denom))
        if cache != None:
            return cache
        # base case
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
    res = recur(amount, denoms, 0)
    print(f"amount = {amount}\ncoins [] = {denoms}\nMinimum of Coin is = {len(res)}")
    print("_"*40)
    return res

# numWays(5, [1,2,3])
# minCoin(5, [1,2,3])