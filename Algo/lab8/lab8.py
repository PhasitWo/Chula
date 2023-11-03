def recur(arr:list[int], ans):
    if len(arr) < 3:
        # option 1
        # for num in arr:
        #     print(num, end=" ")
        
        # option 2
        ans += arr
        return ans
    recur(arr[0::2], ans) # left = items that index are even
    recur(arr[1::2], ans) # right = items that index are odd
    return ans
# T(n) = 2T(n/2) + n ????
def check_all(arr:list[int]):
    flag = True
    for num_index, num in enumerate(arr):
        x1_index = num_index - 1
        x3_index = num_index + 1
        while(x1_index>-1 and x3_index<len(arr)):
            x1 = arr[x1_index]
            x3 = arr[x3_index]
            if (x1+x3)/2 == num:
                flag = False
                break
            x1_index -= 1
            x3_index += num_index + 1
        if not flag:
            print(num)
            return False
    return True

N = 8
question = [i for i in range(1, N+1)]
new = recur(question, [])
print(f"n={N}\n",new, sep="")
print(check_all(new))

