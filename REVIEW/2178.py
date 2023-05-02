##dfs로 풀어버림... 최단거리 구하는데 dfs로 풀으니까 당연히 틀리지..
def dfs(x, y):
    global ans
    if x == m-1 and y == n-1:
        result.append(ans)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue 
        else:
            if board[ny][nx] == 1 and v[ny][nx] == 0:
                v[ny][nx] = 1
                ans += 1
                dfs(nx, ny)     

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, str(input()))))
dx = [0,1,0,-1]
dy = [1,0,-1,0]
v = [[0]*m for _ in range(n)]
ans = 1
result = []
dfs(0,0)

print(result)


## bfs로 다시 풀어보자

from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, str(input()))))
v = [[0] * m for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(sx,sy, ex,ey):
    queue = deque()
    queue.append((sx,sy))
    v[sy][sx] = 1
    while queue:
        x,y = queue.popleft()
        if (x,y) == (ex, ey):
            return v[ey][ex]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            else:
                if board[ny][nx] == 1 and v[ny][nx] == 0:
                    queue.append((nx, ny))
                    v[ny][nx] = v[y][x] + 1

ans = (bfs(0,0, m-1, n-1))

print(ans)



##bfs 다시
from collections import deque

def bfs(sx,sy,ex,ey):
    queue = deque()
    queue.append((sx,sy))
    visited[sy][sx] = 1

    while queue:
        x,y = queue.popleft()
        if (x,y) == (ex,ey):
            return visited[ey][ex]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            else:
                if board[ny][nx] == 1 and visited[ny][nx] == 0:
                    queue.append((nx,ny))
                    board[ny][nx] = 0
                    visited[ny][nx] = visited[y][x] + 1

n,m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, str(input()))))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

visited = [[0] * m for _ in range(n)]
print(bfs(0,0,m-1,n-1))



##bfs 다시
from collections import deque

def bfs(sx,sy,ex,ey): #시작(x,y)좌표, 종료(x,y)좌표
    queue = deque()
    queue.append((sx,sy)) #먼저 시작좌표를 큐에 삽입
    visited[sy][sx] = 1 #시작좌표 방문처리
    while queue: #큐가 빌때까지
        x,y = queue.popleft() #첫 번째 케이스: 처음에 넣은 시작 좌표를 꺼낸다. / 나머지 케이스: ->반복
        if (x,y) == (ex,ey): #큐가 빌때까지 돌았는데 시작좌표가 종료좌표와 일치할 때
            return visited[ey][ex] #종료좌표에 해당되는 방문리스트에 저장된 값 리턴
        for i in range(4): #동서남북 네 방향 돈다.
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=m or ny>=n: #미로 밖으로 벗어날 경우 다음 방향 실행
                continue
            else:
                if board[ny][nx] == 1 and visited[ny][nx] == 0: #갈 수 있고, 방문 안되어 있다면
                    queue.append((nx,ny)) #일단 큐에 다음좌표 넣고
                    board[ny][nx] = 0 #다음좌표 못간다 표시하고
                    visited[ny][nx] = visited[y][x] + 1 #다음좌표 방문리스트에 현재좌표+1을 저장한다.
        ##pop한 하나의 좌표에 대한 길에대한 모든 정보를 큐에 집어넣었으므로
        ##이제 다시 돌아가서 큐에 좌표를 하나씩 pop하면서 갈 수 있는지 없는지 살펴보면 된다.

n,m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, str(input()))))
dx = [0,1,0,-1]
dy = [1,0,-1,0]

visited = [[0]*m for _ in range(n)]
print(bfs(0,0,m-1,n-1))


##다시 풀어보기
from collections import deque

def bfs(sx,sy):
    global ans
    queue = deque()
    queue.append((sx,sy))
    v[sy][sx] = 1
    while queue:
        x,y = queue.popleft()
        if x == m-1 and y == n-1:
            ans = v[y][x] 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            else:
                if board[ny][nx] == 1 and v[ny][nx] == 0:
                    v[ny][nx] = v[y][x] + 1
                    queue.append((nx,ny))

n, m = map(int, input().split()) #n:세로 m:가로
board = [list(map(int, input())) for _ in range(n)]
v = [[0] * m for _ in range(n)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

ans = 0

bfs(0,0)

print(ans)


