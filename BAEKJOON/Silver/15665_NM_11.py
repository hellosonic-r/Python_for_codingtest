def dfs(count, temp_list):
    if count == m:
        ans.append(temp_list)
        return
    if count == n:
        return
    
    prev = 0
    for i in range(n):
        if prev != num_list[i]:
            prev = num_list[i]
            dfs(count+1, temp_list + [num_list[i]])

n,m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
ans = []

dfs(0, [])

for i in ans:
    print(" ".join(map(str, i)))