def dfs(count, start, temp_list):
    if count == m:
        ans.append(temp_list)
        return
    for i in range(start, len(num_list)):
        if v[i] == 0:
            v[i] = 1
            dfs(count+1, i+1, temp_list + [num_list[i]])
            v[i] = 0

n, m = map(int, input().split())
num_list = list(range(1, n+1))
v = [0] * n

ans = []
dfs(0,0,[])

for i in ans:
    print(*i)