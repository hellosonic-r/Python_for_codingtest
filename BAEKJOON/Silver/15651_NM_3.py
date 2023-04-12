ans = []

def dfs(first):
    if len(ans) == m:

        print(" ".join(map(str, ans)))
        return
    if first == n:
        return
    for i in range(1, n+1):
        ans.append(i)
        dfs(first+1)
        ans.pop()

n, m = map(int, input().split())
num_list = list(range(1,n+1))

dfs(0)