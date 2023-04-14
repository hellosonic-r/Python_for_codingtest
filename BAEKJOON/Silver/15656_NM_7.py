def dfs(count):
    if count == m:
        print(" ".join(map(str, ans)))
        return
    if count == n:
        return
    for i in range(n):
        ans.append(num_list[i])
        dfs(count+1)
        ans.pop()

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
ans = []

dfs(0)