from collections import deque

#외부의 치즈와 맞닿아 있으면 외부의 공기이다. 

def bfs(sx,sy):
    queue = deque()
    queue.append((sx,sy))
    v[sy][sx] = 1
    board[sy][sx] = -1

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            elif 0<=nx<m and 0<=ny<n:
                if board[ny][nx] == 1 or v[ny][nx] == 1:
                    continue
                else:   
                    v[ny][nx] = 1
                    board[ny][nx] = -1 
                    queue.append((nx,ny))
    return

def melt():
    for y in range(n):
        for x in range(m):
            if board[y][x] == 1:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<m and 0<=ny<n:
                        if board[ny][nx] == -1:
                            cnt += 1
                if cnt >= 2:
                    r.append((x,y))

n, m = map(int, input().split()) #n:세로, m:가로

board = [list(map(int, input().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]


r = []
time = 0
while True:
    r = []
    v = [[0]*m for _ in range(n)]
    bfs(0,0) #외부공기 -1로 표시
    melt()
    if len(r) == 0:
        break
    while r:
        x,y = r.pop()
        board[y][x] = 0
    time += 1

print(time)