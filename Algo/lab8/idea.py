def notDAC(arr:list[int]):
    new = arr.copy()
    for i in range(len(arr)):
        type_ = 0 if i % 2 == 0 else 1
        rearrange(arr, new, i, type_)
    return new
def rearrange(old:list, new:list, i, type_):
    x2 = i
    x1 = x2-1
    x3 = x2+1
    l_candidate = None
    r_candidate = None
    while(x1>-1 and x3<len(old)):
        x1_index = new.index(x1)
        x3_index = new.index(x3)
        if x1_index < i and i < x3_index:
            l_candidate = x1_index
            r_candidate = x3_index
        if x3_index < i and i < x1_index:
            l_candidate = x3_index
            r_candidate = x1_index
        x1 -= 1
        x3 += 1
    if l_candidate != None and r_candidate != None:
        x2_index = new.index(x2)
        if type_ == 0:
            temp = new[l_candidate]
            new[l_candidate] = x2
            new[x2_index] = temp
        else:
            temp = new[r_candidate]
            new[r_candidate] = x2
            new[x2_index] = temp


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

q = [i for i in range(6)]
new = notDAC(q)
print(new)
check(new)