##시간초과 - 메인함수에서 모든 좌표를 들르면서 다리를 놓음
from collections import deque

def build_bridge(sx,sy):
    global ans
    q = deque()
    q.append((sx,sy))
    while q:
        x,y = q.popleft()
        if v[y][x] != 0 and v[y][x] != v[sy][sx]:
            ans = min(ans, visited[y][x]-1)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            else:
                if (v[ny][nx] == 0 or v[ny][nx] != v[sy][sx]) and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((nx,ny))

def bfs(sx,sy):
    global islandNum
    queue = deque()
    queue.append((sx,sy))
    v[sy][sx] = islandNum
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            else:
                if board[ny][nx] != 0 and v[ny][nx] == 0:
                    v[ny][nx] = islandNum
                    queue.append((nx,ny))
            
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
v = [[0] * n for _ in range(n)]
dx = [0,1,0,-1]
dy = [-1,0,1,0]
islandNum = 1
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and v[i][j] == 0:
            bfs(j,i)
            islandNum += 1

ans = n*2
for i in range(n):
    for j in range(n):
        visited = [[0] * n for _ in range(n)]
        if v[i][j] != 0 and visited[i][j] == 0:
            build_bridge(j,i)

print(ans)



##성공코드
from collections import deque

#섬 구분하기
def bfs(sx,sy):
    global islandNum #섬 번호 변수
    queue = deque()
    queue.append((sx,sy))
    v[sy][sx] = islandNum #리스트 v에 섬 번호를 저장한다. 현재 좌표의 섬 번호는 islandNum.
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            else:
                #다음 좌표가 육지(1)이고, 아직 방문안했다면
                if board[ny][nx] != 0 and v[ny][nx] == 0:
                    #다음 좌표에 섬 번호 표시한다.
                    v[ny][nx] = islandNum
                    queue.append((nx,ny))

#다리 놓기
def build_bridge(num):
    global ans
    #거리를 저장할 리스트를 생성한다. 초기 좌표값은 -1
    distance = [[-1]*n for _ in range(n)]
    q = deque()
    #섬 번호를 표시한 그리드를 돌면서 섬 번호에 해당하는 좌표를 큐에 넣는다.
    for i in range(n):
        for j in range(n):
            if v[i][j] == num:
                q.append((j,i))
                #거리는 0부터 시작하므로 섬에 해당하는 좌표 값0으로 갱신한다.
                distance[i][j] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #범위를 벗어나면 다음으로
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            #다음 좌표의 섬 번호가 0 초과(육지)이고, 현재 섬 번호가 아니라면 
            if v[ny][nx] > 0 and v[ny][nx] != num:
                #현재 좌표의 거리 정보와 ans 중 최소값을 ans에 넣는다.
                ans = min(ans, distance[y][x])
                return #리턴해준다.
            #만약 바다이고, 아직 방문 안했다면, 거리 값을 갱신한다.
            if v[ny][nx] == 0 and distance[ny][nx] == -1:
                distance[ny][nx] = distance[y][x] + 1
                q.append((nx, ny))
            
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
v = [[0] * n for _ in range(n)]
dx = [0,1,0,-1]
dy = [-1,0,1,0]

#가로세로 i,j에 해당하는 좌표에 섬 번호를 바꾼다.
islandNum = 1
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and v[i][j] == 0:
            bfs(j,i)
            islandNum += 1 #bfs한번 실행되고 나면 섬 번호를 1씩 올려준다.

ans = n*2

for i in range(1, islandNum):
    build_bridge(i)

print(ans)