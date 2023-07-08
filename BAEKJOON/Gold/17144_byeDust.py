from collections import deque

#미세먼지가 존재하는 위치를 찾는다.
def find_dust():
    cnt = 0
    dust_list = []
    for y in range(n):
        for x in range(m):
            if board[y][x]>0:
                cnt = 0 
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<m and 0<=ny<n:
                        if board[ny][nx] >= 0:
                            cnt += 1
                dust_list.append((x,y,cnt))
    return dust_list

#1. 먼저 미세먼지 있는 좌표에서 확산된다. 다른테이블(a)에 표시, 몇방향으로 확산되었는지 표시
#2. 확산이 완료된 원본 미세먼지 수치 줄인다.
#3. 1번의 테이블과 합친다.


#미세먼지가 1초당 확산되면 결과 그리드 업데이트
def bfs(arr): # arr = x,y,cnt
    v = [[0] * m for _ in range(n)]
    for j in range(len(arr)):
        x,y = arr[j][0], arr[j][1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n:
                if board[ny][nx] >= 0:
                    v[ny][nx] += (board[y][x]//5)

    for i in range(len(arr)):
        x,y = arr[i][0],arr[i][1]
        cnt = arr[i][2]
        board[y][x] = board[y][x] - ((board[y][x]//5) * cnt)

    for y in range(n):
        for x in range(m):
            board[y][x] += v[y][x]


def top_move(a,b):
    global top_x,top_y
    q = deque()
    q.append((a,b))
    tx = [0,1,0,-1]
    ty = [-1,0,1,0]
    count = 0 
    while q:
        x,y = q.popleft()
        if x == top_x+1 and y == top_y:
            return
        nx = x + tx[count%4]
        ny = y + ty[count%4]
        if 0<=nx<m and 0<=ny<=top_y:
            board[y][x] = board[ny][nx]
        else:
            count += 1
            nx = x + tx[count%4]
            ny = y + ty[count%4]
            
            board[y][x] = board[ny][nx]
        q.append((nx,ny))


def down_move(a,b):
    global down_x,down_y
    q = deque()
    q.append((a,b))
    lx = [0,1,0,-1]
    ly = [1,0,-1,0]
    count = 0 
    while q:
        x,y = q.popleft()
        if x == down_x+1 and y == down_y:
            return
        nx = x + lx[count%4]
        ny = y + ly[count%4]
        if 0<=nx<m and down_y<=ny<n:
            board[y][x] = board[ny][nx]
        else:
            count += 1
            nx = x + lx[count%4]
            ny = y + ly[count%4]
            
            board[y][x] = board[ny][nx]
        q.append((nx,ny))



n,m,t = map(int, input().split()) #r:세로 c:가로

board = [list(map(int, input().split())) for _ in range(n)]

#공기청정기 위치 찾기
top_x,top_y,down_x,down_y = 0,0,0,0
machine_location_check = 0
for y in range(n):
    for x in range(m):
        if board[y][x] == -1:
            if machine_location_check == 0:
                top_x,top_y = x,y
                machine_location_check += 1
            elif machine_location_check == 1:
                down_x,down_y = x,y
                machine_location_check += 1
        if machine_location_check == 2:
            break
    if machine_location_check == 2:
        break

dx = [0,1,0,-1]
dy = [-1,0,1,0]


while t != 0:
    bfs(find_dust())
    top_move(top_x,top_y)
    down_move(down_x,down_y)
    board[top_y][top_x] = -1
    board[down_y][down_x] = -1
    board[top_y][top_x+1] = 0
    board[down_y][down_x+1] = 0
    t -= 1

ans = 0
for y in range(n):
    for x in range(m):
        if board[y][x] == -1:
            continue
        ans += board[y][x]
print(ans)