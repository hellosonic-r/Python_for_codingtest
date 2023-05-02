def dfs(y):
    global ans
    if y == n:
        ans += 1
        return
    for x in range(n):
        if v1[x] == 0 and v2[x+y] == 0 and v3[x-y] == 0:
            v1[x],v2[x+y],v3[x-y] = 1,1,1
            dfs(y+1)
            v1[x],v2[x+y],v3[x-y] = 0,0,0

n = int(input())
v1 = [0] * n
v2 = [0] * (2*n)
v3 = [0] * (2*n)
ans = 0

dfs(0)
print(ans)