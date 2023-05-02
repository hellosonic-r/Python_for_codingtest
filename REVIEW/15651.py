def dfs(count, temp_list):
    if count == m:
        ans.append(temp_list)
        return
    for i in range(len(num_list)):
        dfs(count+1, temp_list + [num_list[i]])


n, m = map(int, input().split())
num_list = list(range(1, n+1))
ans = []
dfs(0, [])

for i in ans:
    print(*i)
    