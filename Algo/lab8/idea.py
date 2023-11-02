def notDAC(arr:list[int]):
    new = arr.copy()
    for i in range(len(arr)):
        t = i % 4
        rearrange(arr, new, i, t)
    return new

def rearrange(old:list, new:list, i, t):
    x1 = i
    x3 = i + 2
    while (x3 < len(old)):
        x1_index = new.index(x1)
        x3_index = new.index(x3)
        if t == 0 or t == 1:
            new.pop(x3_index)
            x1_index = new.index(x1)
            new.insert(x1_index+1, x3)
        else:
            new.pop(x3_index)
            x1_index = new.index(x1)
            new.insert(x1_index-1, x3)
        x3 += 2


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

N = 9
q = [i for i in range(N+1)]
print(q)
new = notDAC(q)
print(new)
check(new)
