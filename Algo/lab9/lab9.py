def compute_prefix(P:str) -> list[int]:
    m = len(P)
    pi = [None] * m
    pi[0] = -1
    k = -1
    for q in range(1, m): # 1 to m-1
        while k > -1 and P[k+1] != P[q]:
            k = pi[k-1]
        if P[k+1] == P[q]:
            k = k+1
        pi[q] = k
    return pi

# display prefix that is matched the actual KMP algo
def display_prefix(prefix:list[int]):
    print([i+1 for i in prefix])

def KMP_matcher(t, p):
    n = len(t)
    m = len(p)
    pi = compute_prefix(p)
    display_prefix(pi)
    ans = []
    q = -1
    for i in range(0, n): # 0 to n-1
        while q > -1 and p[q+1] != t[i]:
            q = pi[q]
        if p[q+1] == t[i]:
            q = q + 1
        if q == m-1: # match last index of pattern
            # +1 to match indexing in KMP algo
            ans.append(f"{(i-m+1)+1} LR")
            q = pi[q] # find next match
    q = -1
    for i in range(n-1, -1, -1): # n-1 to 0
        while q > -1 and p[q+1] != t[i]:
            q = pi[q]
        if p[q+1] == t[i]:
            q = q + 1
        if q == m-1: # match last index of pattern
            # +1 to match indexing in KMP algo
            ans.append(f"{i+m} RL")
            q = pi[q] # find next match
    return ans

def KMP_matcher_extra(t, p):
    n = len(t)
    m = len(p)
    pi = compute_prefix(p)
    display_prefix(pi)
    ans = []
    cnt = 0
    q = -1
    i = 0
    while cnt != n+m-1:
        while q > -1 and p[q+1] != t[i]:
            q = pi[q]
        if p[q+1] == t[i]:
            q = q + 1
        if q == m-1: # match last index of pattern
            # +1 to match indexing in KMP algo
            ans.append(f"{(cnt-m+1)+1} LR")
            q = pi[q] # find next match
        i = (i + 1) % n
        cnt += 1
    cnt = 0
    q = -1
    i = 0
    while cnt != n+m-1:
        while q > -1 and p[q+1] != t[n-1-i]:
            q = pi[q]
        if p[q+1] == t[n-1-i]:
            q = q + 1
        if q == m-1: # match last index of pattern
            # +1 to match indexing in KMP algo
            ans.append(f"{n-cnt+m-1} RL")
            q = pi[q] # find next match
        i = (i + 1) % n
        cnt += 1
 
    return ans

def naive(t, p):
    n = len(t)
    m = len(p)
    ans = []
    for s in range(0, n-m+1): # O to n-m
        found = True
        for i in range(0, m):
            if p[i] != t[s+i]:
                found = False
                break
        if found:
            ans.append(f"{(s+1)} LR")
    for s in range(0, n-m+1): # O to n-m
        found = True
        for i in range(0, m):
            if p[i] != t[n-1-s-i]:
                found = False
                break
        if found:
            ans.append(f"{(n-s)} RL")
    return ans

def naive_extra(t, p):
    n = len(t)
    m = len(p)
    ans = []
    for s in range(0, n): # O to n-1
        found = True
        for i in range(0, m):
            if p[i] != t[(s+i)%n]:
                found = False
                break
        if found:
            ans.append(f"{(s+1)} LR")
    for s in range(0, n): # O to n-1
        found = True
        for i in range(0, m):
            if p[i] != t[n-1-(s+i)%n]:
                found = False
                break
        if found:
            ans.append(f"{(n-s)} RL")
    return ans
# ถ้า extra คือท้าย text ต่อกับต้น text แบบ circular ให้เปลี่ยน for loop
# เป็น while loop โดยจะทำแค่จำนวนรอบ cnt = text.length + pattern.length - 1
# ถ้าทำเกินกว่านั้นจะเริ่มรอบใหม่เหมือนเดิม
text = "YXYXYYXYXYYX"
pattern = "XYXY"
# ans = naive(text, pattern)
ans = naive_extra(text, pattern)
print(len(ans))
for a in ans:
    print(a)