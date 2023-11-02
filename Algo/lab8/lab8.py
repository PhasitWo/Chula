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
def check(arr:list[int]):
    for num_index, num in enumerate(arr):
        l_num = num-1
        r_num = num+1
        flag = True
        while(l_num>-1 and r_num<len(arr)):
            left_index = arr.index(l_num)
            right_index = arr.index(r_num)
            if left_index < num_index and num_index < right_index:
                flag = False
                break
            if right_index < num_index and num_index < left_index:
                flag = False
                break
            l_num -= 1
            r_num += 1
        if not flag:
            print("INCORRECT", num)
            return
    print("CORRECT!!!")

N = 8
question = [i for i in range(N+1)]
new = recur(question, [])
print(f"n={N}\n",new, sep="")
check(new)

