ans = []
def dfs(index):
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return
    if index == n:
        return
    for i in range(1, n+1):
        if len(ans)!= 0:
            if ans[-1] > i:
                continue
        ans.append(i)
        dfs(index+1)
        ans.pop()


n, m = map(int, input().split())

dfs(0)