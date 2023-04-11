def dfs(num):
    if num == m:
        print(" ".join(map(str, s)))
        return
    
    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs(num+1)
            s.pop()

n, m = map(int, input().split())
s = []

dfs(0)

