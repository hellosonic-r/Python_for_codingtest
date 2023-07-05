def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
    return

n, m = map(int, input().split()) #n:세로 m:가로
y,x,direction = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)] #0:육지

dx = [0,1,0,-1] #북 동 남 서
dy = [-1,0,1,0] 

v = [[0] * m for _ in range(n)]
v[y][x] = 1

cnt = 1
while True:
    turn_time = 0
    for i in range(4):
        turn_left()
        turn_time += 1
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0<=nx<m and 0<=ny<n:
            if board[ny][nx] == 0 and v[ny][nx] == 0:
                v[ny][nx] = 1
                x,y = nx,ny
                turn_time = 0
                cnt += 1
                break
    if turn_time == 4:
        nx = x + dx[(direction+2)%4]
        ny = y + dy[(direction+2)%4]
        if nx<0 or nx>=m or ny<0 or ny>=n:
            break
        else:
            if board[ny][nx] == 1:
                break
            else:
                v[ny][nx] = 1
                x,y = nx,ny
                turn_time = 0


print(cnt)
