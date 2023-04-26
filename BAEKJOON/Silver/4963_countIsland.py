# ##DFS-런타임 에러(recursionError였지만 setrecursionlimit로 해결)
import sys
sys.setrecursionlimit(10**6)

def dfs(sx,sy):
    board[sy][sx] = 0
    visited[sy][sx] = 1
    if sx >= 50 or sy >= 50:
        return
    for i in range(8):
        nx = sx + dx[i]
        ny = sy + dy[i]
        if nx<0 or ny<0 or nx>=w or ny>=h:
            continue
        else:
            if visited[ny][nx] == 0 and board[ny][nx] == 1:
                dfs(nx,ny)

while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    board = []
    for _ in range(h):
        board.append(list(map(int, input().split())))
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [-1,0,1,0,-1,1,1,-1]
    visited = [[0]*w for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                dfs(j,i)
                count += 1
    print(count)

##BFS
from collections import deque

def bfs(sx, sy):
    queue = deque()
    queue.append((sx,sy))
    board[sy][sx] = 0
    visited[sy][sx] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=w or ny>=h:
                continue
            else:
                if board[ny][nx] == 1 and visited[ny][nx] == 0:
                    board[ny][nx] = 0 
                    visited[ny][nx] = 1
                    queue.append((nx,ny))

while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    board = []
    for _ in range(h):
        board.append(list(map(int, input().split())))
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [-1,0,1,0,-1,1,1,-1]
    visited = [[0]*w for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                bfs(j,i)
                count += 1
    print(count)