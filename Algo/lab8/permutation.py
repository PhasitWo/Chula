import itertools

def check(arr:list[int]):
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
            return False
    return True

q = [i for i in range(100)]
left = q[0::2]
permute_left = list(itertools.permutations(left))
right = q[1::2]
permute_right = list(itertools.permutations(right))
ans = []
for p in permute_left:
    if check(p):
        ans += p
        break
for m in permute_right:
    if check(m):
        ans += m
        break
print(ans)
print(check(ans))