n, m = map(int, input().split()) #n:세로 m:가로
y,x, d = map(int, input().split()) #0:북 1:동 2:남 3:서(시계방향)
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [0,1,0,-1]
dy = [-1,0,1,0]

v = [[0] * m for _ in range(n)]
v[y][x] = 1
ans = 1
cnt = 0

#0:북 1:동 2:남 3:서(시계방향)

def turn_left():
    global d
    d = d - 1
    if d == -1:
        d = 3
    return d

while True:
    d = turn_left()
    nx = x+dx[d]
    ny = y+dy[d]
    if 0<=nx<m and 0<=ny<n and board[ny][nx] == 0 and v[ny][nx] == 0:
        v[ny][nx] = 1
        x, y = nx, ny
        cnt = 0
        ans+=1
    else:
        cnt+=1
    
    if cnt == 4:
        nx = x+dx[(d+2)%4]
        ny = y+dy[(d+2)%4]
        if 0<=nx<m and 0<=ny<n and board[ny][nx] == 0:
            x, y = nx, ny
            cnt = 0
        else:
            break

print(ans)