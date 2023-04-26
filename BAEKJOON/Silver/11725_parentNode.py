import sys
sys.setrecursionlimit(10**6)

def dfs(sn):
    for i in board[sn]:
        if visited[i] == 0:
            visited[i] = sn
            dfs(i)

n = int(input())
board = [[] for _ in range(n+1)]
for _ in range(n-1):
    s,e = map(int, input().split())
    board[s].append(e)
    board[e].append(s)

visited = [0]*(n+1)
dfs(1)
for start_node in range(2,n+1):
    print(visited[start_node])

