def dfs(count,temp_list):
    if count == m:
        ans.append(temp_list)
        return
    for i in range(len(num_list)):
        if v[i] == 0:
            v[i] = 1
            dfs(count+1,temp_list + [num_list[i]])
            v[i] = 0

n,m = map(int, input().split())
num_list = list(range(1,n+1))
ans = []
v = [0] * n
dfs(0,[])

for i in ans:
    print(*i)