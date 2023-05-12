from collections import deque

def bfs(sx,sy):
    queue = deque()
    queue.append((sx,sy))
    board[sy][sx] = 1
    i = 0 #turn횟수
    while queue:
        x,y = queue.popleft()
        if board[y][x] == k:
            return x+1,y+1
        nx = x + dx[i%4]
        ny = y + dy[i%4]
        if 0<=nx<c and 0<=ny<r and board[ny][nx] == 0:
            nx = nx
            ny = ny
        else:
            i += 1
            nx = x + dx[i%4]
            ny = y + dy[i%4]
        board[ny][nx] = board[y][x] + 1
        queue.append((nx,ny))
                    

c,r = map(int, input().split()) #c:가로 r:세로
k = int(input())

board = [[0] * c for _ in range(r)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

if k > c*r:
    print(0)
else:
    print(" ".join(map(str, bfs(0,0))))
