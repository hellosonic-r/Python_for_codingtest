##이왜틀
from collections import deque
def check_no_tomato(x,y):
    global count
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=m or ny>=n or board[ny][nx]==-1:
            count += 1
    if count == 4:
        return False

def bfs():
    global days
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            if board[ny][nx] == 0 and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                days = visited[ny][nx]
                queue.append((nx,ny))

m, n = map(int, input().split()) #m:가로 칸의 수 / n:세로 칸의 수
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
dx = [0,1,0,-1]
dy = [1,0,-1,0]
visited = [[0]*m for _ in range(n)]
days = 0
ans = 0
queue = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            count = 0
            if check_no_tomato(j,i) == False:
                ans = -1
                break
        if board[i][j] == 1:
            queue.append((j,i))
    if ans == -1:
        break

if ans != -1:
    bfs()
    ans = days

print(ans)


##다시풀어보자
from collections import deque

def bfs():
    global days
    while queue: #큐가 빌때까지 반복 수행
        x,y = queue.popleft()
        #동서남북 네 방향으로 토마토가 익을 수 있는지 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #전체 박스를 벗어난다면, 지나간다.
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            #다음 좌표가 아직 안익은 토마토이고, 방문하지 않았다면
            if board[ny][nx] == 0 and visited[ny][nx] == 0:
                #다음 좌표의 토마토를 익었다고 처리하고
                board[ny][nx] = 1
                #방문 테이블 값을 1 증가시킨다.
                visited[ny][nx] = visited[y][x] + 1
                #날짜 변수에 다음 방문 테이블 값 저장
                days = visited[ny][nx]
                queue.append((nx,ny))

m, n = map(int, input().split()) #m:가로 칸의 수 / n:세로 칸의 수
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

visited = [[0]*m for _ in range(n)]
days = 0
ans = 0
queue = deque()

#먼저, 익은 토마토(1) 좌표를 queue에 추가한다.
#queue에 넣어주는 작업을 먼저 해야 모든 익은 토마토의 좌표부터 탐색을 시작한다.
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            queue.append((j,i))

bfs() #모든 익은 토마토의 좌표를 큐에 저장한 후, bfs 수행
ans = days #정답은 날짜 변수에 저장된 값

#board 좌표 값을 하나씩 확인하며, 아직도 0이 있다면, 토마토는 익을 수 없는 것이므로,
#정답은 -1 
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            ans = -1
            break
    if ans == -1:
        break

print(ans)
