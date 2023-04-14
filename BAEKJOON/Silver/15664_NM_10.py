def dfs(count, start, temp_list):
    if count == m:
        ans.append(temp_list)
        return
    if count == n:
        return
    
    prev = 0
    for i in range(start, n):
        if prev != num_list[i]:
            prev = num_list[i]
            dfs(count+1, i+1, temp_list+[num_list[i]])

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
ans = []

dfs(0,0,[])
for i in ans:
    print(" ".join(map(str, i)))
