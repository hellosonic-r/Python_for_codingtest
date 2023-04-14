def dfs(count, start_idx):
    if count == m:
        print(" ".join(map(str, ans)))
        return
    if count == n:
        return
    for i in range(start_idx,n):
        ans.append(num_list[i])
        dfs(count+1, i)
        ans.pop()

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
ans = []

dfs(0,0)