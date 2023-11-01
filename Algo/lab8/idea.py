def notDAC(arr:list[int]):
    new = arr.copy()
    for i in range(len(arr)):
        if check(new, i) == False:
            new = rearrange(new) 
    return new

def rearrange(arr):
    new = []
    new += arr[0::2]
    new += arr[1::2]
    return new

def check(arr, num_index:int) -> bool:
    num = arr[num_index]
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
        return False
    return True

q = [i for i in range(6)]
print(q)
print(notDAC(q))