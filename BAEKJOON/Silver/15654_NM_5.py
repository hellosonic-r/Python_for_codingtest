def dfs(count):
    if count == m:
        print(" ".join(map(str, ans)))
        return
    if count == n:
        return
    
    for i in range(len(num_list)):
        if visited[i] == 0:
            visited[i] = 1
            ans.append(num_list[i])
            dfs(count+1)
            ans.pop()
            visited[i] = 0

n, m = map(int ,input().split())
num_list = list(map(int, input().split()))
num_list.sort()
visited = [0] * n
ans = []

dfs(0)
