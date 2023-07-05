#n n 공간에 물고기 m마리 아기상어 1마리
#가장 처음 아기 상어의 크기는 2 
#1초에 상하좌우에 한 칸씩 이동
#자신의 크기보다 큰 물고기 칸은 지나갈 수 없음
#자신의 크기보다 작은 물고기는 먹을 수 있음. 같다면 지나갈 수 있음
#먹을 수 있는 물고기가 1마리라면 그 물고기 먹으러감
#1마리보다 많다면, 거리가 가장 가까운 물고기 먹으러감

#크기가 2인 아기 상어는 2마리 먹으면 크기 3 됨

import sys
from collections import deque

def bfs(sx,sy):
    queue = deque()
    queue.append((sx,sy))
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                v[ny][nx] = v[y][x] + 1
                queue.append((nx,ny))



n = int(sys.stdin.readline()) 
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
shark = [[0]*n for _ in range(n)]

location = []
for y in range(n):
    for x in range(n):
        if board[y][x] == 9:
            location.append(x)
            location.append(y)
            break

print(location)
shark[location[1]][location[0]] = 2



check = []
size = 2
feed_cnt = 0


dx = [0,1,0,-1]
dy = [-1,0,1,0]

time = 0

while True:
    cnt = 0 
    feeds = []
    v = [[0]*n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if board[y][x] != 0 and board[y][x] < size:
                cnt += 1
                feeds.append((x,y))
    if cnt == 0: #먹을 수 있는 물고기가 한 마리도 없다면 탈출
        break
    else:
        bfs(location[0], location[1])
        distance = 40
        x, y = 0, 0
        for feed in feeds:
            if distance > v[feed[1]][feed[0]]:
                distance = v[feed[1]][feed[0]]
                x,y = feed[0],feed[1]
        board[location[1]][location[0]] = 0
        board[y][x] = 9
        location.clear()
        location.append(x)
        location.append(y)
        feed_cnt += 1

        if feed_cnt == size:
            size += 1
            feed_cnt = 0

    time += 1

print(time)

        