def dfs(count, start, temp_list):
    if count == m:
        ans.append(temp_list)
        return
    for i in range(start, len(num_list)):
        dfs(count+1, i, temp_list + [num_list[i]])
n, m = map(int, input().split())

num_list = list(range(1,n+1))
ans = []

dfs(0,0,[])

for i in ans:
    print(*i)