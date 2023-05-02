from collections import deque

def bfs(sx,sy):
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
                    queue.append((nx,ny))

t = int(input())
for test_case in range(1, t+1):
    m,n,k = map(int, input().split()) #m:가로 / n:세로 / K:배추위치
    board = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int,input().split())
        board[y][x] = 1
    
    v = [[0] * m for _ in range(n)]

    dx = [0,1,0,-1]
    dy = [-1,0,1,0]

    count = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                bfs(j,i)
                count += 1

    print(count)

