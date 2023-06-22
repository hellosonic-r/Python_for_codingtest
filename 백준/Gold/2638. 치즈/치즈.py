from collections import deque

#외부의 공기와 2개 이상 맞닿아있다면 녹을 치즈이다.

#외부 공기 좌표값을 -1로 바꿔주는 코드
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
            ##방문처리 안할 좌표 먼저 생각하면 쉽다.
            # 범위를 벗어나거나, 치즈(1)이거나, 이미 방문 했다면 continue한다. 
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            else:
                if board[ny][nx] == 1 or v[ny][nx] == 1:
                    continue
                else:   
                    v[ny][nx] = 1 #방문처리
                    board[ny][nx] = -1 #외부 공기 좌표값 -1로 표시
                    queue.append((nx,ny))
    return

#녹아내릴 치즈의 좌표 구하는 코드
def melt():
    for y in range(n):
        for x in range(m):
            if board[y][x] == 1:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<m and 0<=ny<n:
                        if board[ny][nx] == -1: #외부 공기와 맞닿아있다면
                            cnt += 1 #cnt 값 +1
                if cnt >= 2: #cnt 값이 2 이상이라면, 즉 2개 이상의 외부 공기와 맞닿아 있다면
                    r.append((x,y)) #녹아내릴 치즈이므로 r에 해당 좌표 추가

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
    melt() #녹아내릴 치즈의 좌표 구하기
    if len(r) == 0: #녹아내릴 치즈가 없다면 
        break #반복문 탈출
    while r:
        x,y = r.pop()
        board[y][x] = 0
    time += 1

print(time)
