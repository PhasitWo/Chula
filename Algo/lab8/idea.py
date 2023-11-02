import math

def notDAC(arr:list[int]):
    new = arr.copy()
    m = len(arr)
    for i in range(0, m):
        rearrange(arr, new, i)
        print(new)
    return new

def rearrange(old:list, new:list, i):
    candidate = []
    x1 = new[i]
    x3_index = i + 2
    while (x3_index < len(old)):
        x3 = new[x3_index]
        if (x1 + x3) % 2 == 0:
            candidate.append(x3)
        x3_index += 2
    for num in candidate:
        print(num)
        can_index = new.index(num)
        new.pop(can_index)
        new.insert(i+1, num)


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

N = 7
q = [i for i in range(N+1)]
print(q)
new = notDAC(q)
print(new)
check(new)
