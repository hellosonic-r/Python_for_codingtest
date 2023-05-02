import sys
sys.setrecursionlimit(10**6)

def dfs(count, e,s,m):
    global ans
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1
    if e == E and s == S and m == M:
        ans = count
        return
    dfs(count+1, e+1,s+1,m+1)
    
E,S,M = map(int, input().split())
ans = 0
dfs(1,1,1,1)
print(ans)