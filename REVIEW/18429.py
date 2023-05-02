def dfs(count, weight):
    global ans
    if weight < 500:
        return
    if count == n:
        ans += 1
        return
    for i in range(n):
        if v[i] == 0:
            v[i] = 1
            dfs(count+1, weight - k + num_list[i])
            v[i] = 0 

n, k = map(int, input().split())
num_list = list(map(int, input().split()))
ans = 0
v = [0]*n
dfs(0,500)
print(ans)