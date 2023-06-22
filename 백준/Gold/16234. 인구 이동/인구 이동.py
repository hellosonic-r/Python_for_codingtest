from collections import deque

def bfs(sx,sy):
    global cnt,l,r,temp_total,temp_cnt,check
    queue = deque()
    queue.append((sx,sy))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            else:
                if l <= abs(board[ny][nx] - board[y][x]) <= r and v[ny][nx] == 0:
                    v[ny][nx] = cnt
                    queue.append((nx,ny))
                    temp_list.append((nx,ny))
                    temp_total += board[ny][nx]
                    temp_cnt += 1
                    check += 1
 

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]


answer = 0

while True:
    v = [[0] * n for _ in range(n)]
    cnt = 0
    d = {}
    check = 0
    move_list = []
    for y in range(n):
        for x in range(n):
            if v[y][x] == 0:
                temp_list = []
                cnt += 1
                temp_list.append((x,y))
                v[y][x] = cnt
                temp_total = board[y][x]
                temp_cnt = 1
                bfs(x,y)
                move_list.append(temp_list)
                d[cnt] = temp_total // temp_cnt


    if len(d) == n*n:
        break
    time = 0
    for k in move_list: #0,1,2
        time += 1
        for i,j in k:
            if v[j][i] == time:
                board[j][i] = d[time]

    if check == 0:
        break

    answer += 1
                
print(answer)