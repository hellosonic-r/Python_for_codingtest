# ##시간초과
#공기가 치즈 내부에 있는 공기인지 체크
def check_hole(arr):
    for y in range(n):
        for x in range(m):
            cnt = 0
            #공기(0)인 좌표
            if arr[y][x] == 0:
                for i in range(4): #상하좌우
                    for k in range(1,max(n,m)): #가로,세로의 끝까지 탐색
                        nx = x + k*dx[i]
                        ny = y + k*dy[i]
                        if 0<=nx<m and 0<=ny<n:
                            if arr[ny][nx] == 1: #치즈(1)를 만난다면,
                                cnt += 1 #cnt값을 카운트 해준다.
                                break
            if cnt == 4: #cnt가 4라면, 공기가 치즈로 둘러쌓인 것, 즉 내부공기이다.
                v.append((x,y)) #리스트 v에 내부공기 좌표 저장
    return

def melt(arr):
    for y in range(n):
        for x in range(m):
            check = 0
            if arr[y][x] == 1:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<m and 0<=ny<n:
                        if (nx,ny) in v: #내부공기라면, 다음 방향 탐색
                            continue
                        elif arr[ny][nx] == 0:
                            check += 1 #외부 공기 카운트+1
                    if check == 2:
                        break 
            if check == 2: #밀접한 외부 공기가 2라면, 
                r.append((x,y)) #해당 치즈는 녹을 것이므로 리스트 r에 좌표 저장
    return


n, m = map(int, input().split()) #n:세로, m:가로

board = [list(map(int, input().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]


time = 0
while True:
    v = [] #내부에 있는 공기의 좌표 저장
    r = [] #녹아내릴 치즈의 좌표 저장
    check_hole(board)
    melt(board)
    if len(r) == 0:
        break
    while r:
        x, y = r.pop()
        board[y][x] = 0
    time += 1

print(time)




##다시
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
