from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue: #큐에 아무것도 남지 않을 때까지 반복한다
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            