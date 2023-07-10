import copy
from collections import deque

def bfs(sx,sy):
    queue = deque()
    queue.append((sx,sy))
    v[sy][sx] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n:
                if v[ny][nx] == 0 and temp[ny][nx] == 0:
                    v[ny][nx] = 1
                    temp[ny][nx] = 2
                    queue.append((nx,ny))


n, m = map(int, input().split()) #세로:n 가로:m
board = [list(map(int, input().split())) for _ in range(n)]

#0:빈칸 1:벽 2:바이러스
total_new_wall = []

for y in range(n):
    for x in range(m):
        if board[y][x] == 0:
            total_new_wall.append((x,y))


walls = []

for i in range(len(total_new_wall)-2):
    for j in range(i+1, len(total_new_wall)-1):
        for k in range(j+1, len(total_new_wall)):
            x = [total_new_wall[i], total_new_wall[j], total_new_wall[k]]
            walls.append(x)


dx = [0,1,0,-1]
dy = [-1,0,1,0]

result = 0

while walls:
    cnt = 0
    temp = copy.deepcopy(board)
    wall_list = walls.pop()
    for x,y in wall_list:
        temp[y][x] = 1
    v = [[0 for _ in range(m)] for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if v[y][x] == 0 and board[y][x] == 2:
                bfs(x,y)
    
    for y in range(n):
        for x in range(m):
            if temp[y][x] == 0:
                cnt += 1
    
    result = max(result, cnt)
    # print()
    # for i in range(n):
    #     print(" ".join(map(str, temp[i])))

print(result)

