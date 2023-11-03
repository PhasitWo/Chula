def wun(arr, i):
    x1_index = i
    x3_index = i + 1
    x1 = arr[x1_index]
    swap = False
    while(x3_index<len(arr)):
        x3 = arr[x3_index]
        if (x1+x3) % 2 == 0:
            x2 = int(x1+x3)/2
            x2_index = None
            for j in range(x1_index, x3_index):
                if arr[j] == x2:
                    x2_index = j
                    break
            if x2_index != None:
                if x1 < x3:
                    # swap x2 x3
                    temp = arr[x2_index]
                    arr[x2_index] = arr[x3_index]
                    arr[x3_index] = temp
                    swap = True
                    x3_index = i + 1
                    continue
                else:
                    temp = arr[x2_index]
                    arr[x2_index] = arr[x1_index]
                    arr[x1_index] = temp
                    swap = True
                    x3_index = i + 1
                    continue
        x3_index += 1
    return swap
    
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

# driver code

arr = [x for x in range(1, 100+1)]
wun(arr, 0)
print(arr)
print(check_all(arr))
