##dfs로 풀이
import sys
sys.setrecursionlimit(10**6)

def dfs(x,y,i,num):
    if num == 0:
        return
    
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<n and 0<=ny<n and board[ny][nx] == 0:
        board[ny][nx] = num
        dfs(nx,ny,i,num-1)
    else:
        nx = x + dx[(i+1)%4]
        ny = y + dy[(i+1)%4]
        board[ny][nx] = num
        dfs(nx,ny,(i+1)%4,num-1)
                
n = int(input())
k = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

board = [[0] * n for _ in range(n)]

board[0][0] = n*n
dfs(0,0,0,n*n-1)

for i in range(n):
    print(" ".join(map(str, board[i])))

flag = False
for i in range(n):
    for j in range(n):
        if board[i][j] == k:
            flag = True
            print(i+1, j+1)
            break
    if flag:
        break




##bfs로 풀이
from collections import deque

def bfs(sx,sy):
    queue = deque()
    queue.append((sx,sy))
    v[sy][sx] = n*n
    i = 0
    cnt = 0
    while queue:
        x,y = queue.popleft()
        if cnt == n*n-1:
            return
        
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n and v[ny][nx] == 0:
            v[ny][nx] = v[y][x] - 1
        else:
            nx = x + dx[(i+1)%4]
            ny = y + dy[(i+1)%4]
            i = (i+1)%4
            v[ny][nx] = v[y][x] - 1
        queue.append((nx,ny))
        cnt+=1

n = int(input())
k = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

board = [[0] * n for _ in range(n)]
v = [[0] * n for _ in range(n)]

bfs(0,0)

for i in range(n):
    print(" ".join(map(str, v[i])))

flag = False
for i in range(n):
    for j in range(n):
        if v[i][j] == k:
            flag = True
            print(i+1,j+1)
            break
    if flag:
        break


