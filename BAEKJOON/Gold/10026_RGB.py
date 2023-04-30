from collections import deque

def bfs(sx,sy,color,v):
    queue = deque()
    queue.append((sx,sy))
    v[sy][sx] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            else:
                if board[ny][nx] == color and v[ny][nx] == 0:
                    v[ny][nx] = 1
                    queue.append((nx,ny))

n = int(input())

board = []

#R,G,B를 각각 0,1,2로 바꿔준다.
for _ in range(n):
    string = list(input())
    temp_list = []
    for i in string:
        if i == "R":
            temp_list.append(0)
        elif i == "G":
            temp_list.append(1)
        elif i == "B":
            temp_list.append(2)
    board.append(temp_list)

dx = [0,1,0,-1]
dy = [-1,0,1,0]

visited = [[0] * n for _ in range(n)] #적록색약 아닌사람 방문 테이블
rg_visited = [[0] * n for _ in range(n)] #적록색약인 사람 방문 테이블

cnt = 0 #적록색약 아닌사람
rg_cnt = 0 #적록색약인 사람

#적록색약 아닌사람 먼저 카운트
for rgb in range(3): #R,G,B 돌아가며 확인
    for i in range(n):
        for j in range(n):
            if board[i][j] == rgb and visited[i][j] == 0: #아직 방문 안했다면
                bfs(j,i,rgb,visited) #bfs수행 (이때, rgb정보와 방문테이블을 변수로 하여 호출한다.)
                cnt += 1

#적록색약 아닌사람 카운트 끝났으니 이제 적록색약인 사람 카운트 할 차례
#R,G 값을 같게 만든다.
for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            board[i][j] = 1

#적록색약인 사람 카운트
for rgb in range(1,3):
    for i in range(n):
        for j in range(n):
            if board[i][j] == rgb and rg_visited[i][j] == 0:
                bfs(j,i,rgb,rg_visited)
                rg_cnt += 1

print(cnt, rg_cnt)
