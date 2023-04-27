import sys
sys.setrecursionlimit(10**6)

def dfs(x,y,z, count):
    global ans
    if x == 16:
        x = 1
    if y == 29:
        y = 1
    if z == 20:
        z = 1 
    if x == e and y == s and m == z:
        ans = count
        return
    dfs(x+1, y+1, z+1, count+1)

e,s,m = map(int, input().split())
ans = 0
dfs(1,1,1,1)
print(ans)