def recur(arr:list[int], p, r):
    if r-p > 2:
        q = split(arr, p, r)
        recur(arr, p, q) # left = items that index are even
        recur(arr, q+1, r) # right = items that index are odd
    return arr

def split(arr:list[int], p, r):
    q = int((r+p-1)/2)
    even_index = r
    if r % 2 != 0:
        even_index -= 1
    for odd_index in range(1, q+1, 2):
        # swap
        temp = arr[odd_index]
        arr[odd_index] = arr[even_index]
        arr[even_index] = temp
        even_index -= 2
    return q

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


# 0 1 2 3 4 5 6 7| 8 9 10 11 12 13 14
# 0 1 2 3 4 5 6| 7 8 9 10 11 12 13
# 0 1 2 3 4 5 6| 7 8 9 10 11 12
# 0 1 2 3 4 5| 6 7 8 9 10 11
arr = [i for i in range(10)]
print(arr)
recur(arr, 0, len(arr)-1)
print(arr)
check(arr)
