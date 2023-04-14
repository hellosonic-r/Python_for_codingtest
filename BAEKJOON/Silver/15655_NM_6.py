# 내 풀이.. 방문처리가 빠졌다.
def dfs(count, start = 0):
    if count == m:
        print(" ".join(map(str, ans)))
        return
    if count == n:
        return
    for i in range(start, n):
        ans.append(num_list[i])
        dfs(count+1, i+1)
        ans.pop()

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()    
ans = []  

dfs(0)

## 강의보고 다시 풀어본다.
def dfs(count, start):
    if count == m:
        print(" ".join(map(str, ans)))
        return
    if count == n:
        return
    for i in range(start, n):
        if visited[i] == 0:
            visited[i] = 1
            ans.append(num_list[i])
            dfs(count+1, i+1)
            ans.pop()
            visited[i] = 0

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
ans = []
visited = [0] * n
dfs(0,0)