
def numWays(amount, denoms:list) -> int:
    denoms.sort(reverse=True)
    result = 0
    memmo = {}

    def recur(amount, denoms:list):
        if len(denoms) == 1:
            # if amount is divisible by this only denom
            if amount % denoms[0] == 0:
                return 1
            else:
                return 0
        cnt = 0
        focus_denom = denoms[0]
        n = 0
        remain = amount - n*focus_denom
        while(remain >= 0):
            next_denoms = denoms.copy()
            next_denoms.pop(0)
            # avoid re-computation
            cache = memmo.get((remain, len(next_denoms)))
            if cache != None:
                print("OVERLAP")
                cnt += cache
            else:
                cnt += recur(remain, next_denoms)
            n += 1
            remain = amount - n*focus_denom
        memmo.update({(amount,len(denoms)):cnt})
        return cnt
    
    result += recur(amount, denoms)
    return result


print(numWays(50, [1, 5, 10, 20]))