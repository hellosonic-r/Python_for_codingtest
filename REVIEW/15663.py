def dfs(count, temp_list):
    if len(temp_list) == m:
        ans.append(temp_list)

    if count == n:
        return
    
    prev = 0
    for i in range(len(num_list)):
        if visited[i] == 0 and prev != num_list[i]:
            prev = num_list[i]
            visited[i] = 1
            dfs(count+1, temp_list+[num_list[i]])
            visited[i] = 0

n, m = map(int, input().split())
num_list = list(map(int,input().split()))
num_list.sort() ##1 7 9 9
visited = [0] * n
ans = []
dfs(0,[])
for i in ans:
    print(" ".join(map(str, i)))