from collections import deque

def bfs(sx,sy):
    global size
    queue = deque()
    queue.append((sx,sy))
    board[sy][sx] = 0
    v[sy][sx] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            else:
                if board[ny][nx] == 1 and v[ny][nx] == 0:
                    board[ny][nx] = 0
                    v[ny][nx] = 1
                    size +=1 
                    queue.append((nx,ny))

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

v = [[0] * m for _ in range(n)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

max_size = 0
count = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            size = 1 
            bfs(j,i)
            if max_size < size:
                max_size = size
            count += 1

print(count,max_size,sep="\n")