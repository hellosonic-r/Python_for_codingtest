from collections import deque

def bfs(sx,sy,ex,ey):
    global cnt
    queue = deque()
    queue.append((sx,sy))
    v[sy][sx] = 1

    while queue:
        x,y = queue.popleft()
        if x == ex and y == ey:
            return v[y][x]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n:
                if board[ny][nx] == 1 and v[ny][nx] == 0:
                    queue.append((nx,ny))
                    v[ny][nx] = v[y][x] + 1




n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

v = [[0]*m for _ in range(n)]
cnt = 0


ans = bfs(0,0,m-1,n-1)

print(ans)