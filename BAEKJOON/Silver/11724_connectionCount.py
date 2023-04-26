import sys
sys.setrecursionlimit(10**4)

def dfs(sn):
    for i in board[sn]:
        if visited[i] == 0:
            visited[i] = sn
            dfs(i)

n,m = map(int, input().split())
board = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    start, end = map(int ,input().split())
    board[start].append(end)
    board[end].append(start)

count = 0

#1번노드부터 마지막 노드까지 방문
for i in range(1,n+1):
    #만약 해당 노드가 방문 전이라면
    if visited[i] == 0:
        #방문해서 dfs수행
        #노드가 연결되어 있다면 연결된 노드의 방문 테이블은 갱신될 것
        dfs(i)
        count += 1

print(count)

