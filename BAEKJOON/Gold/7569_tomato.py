import sys
from collections import deque

def bfs():
    global days
    while queue:
        x,y,z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx<0 or ny<0 or nz<0 or nx>=m or ny>=n or nz>=h:
                continue
            else:
                #다음 좌표가 아직 익지 않은 토마토(0)이고, 방문하지 않았다면,
                if board[nz][ny][nx] == 0 and visited[nz][ny][nx] == 0:
                    #토마토가 익는다.
                    board[nz][ny][nx] = 1
                    #다음 좌표의 방문 테이블 값은 현재 좌표 값 + 1
                    visited[nz][ny][nx] = visited[z][y][x] + 1
                    #날짜 변수에 저장
                    days = visited[nz][ny][nx]
                    #다음 좌표를 큐에 넣는다
                    queue.append((nx, ny, nz))

m,n,h = map(int, input().split()) #m:가로 / n:세로 / h:높이

#입력값 3차원 리스트에 저장
board = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]

dx = [1,0,-1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,-1,1]

#3차원 방문 리스트 초기화 
visited = [[[0]*m for _ in range(n)] for _ in range(h)]

days = 0

queue = deque()

#먼저, 익은 토마토가 있는 좌표를 찾아낸다.
for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 1:
                queue.append((k,j,i)) #가로,세로,높이

bfs() #bfs 함수 실행
ans = days

for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 0:
                ans = -1
                break
        if ans == -1:
            break
    if ans == -1:
        break

print(ans)
