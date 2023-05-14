from collections import deque

def bfs(sx,sy):
    queue = deque()
    queue.append((sx,sy))
    i = 0
    board[sy][sx] = 1
    while queue:
        x,y = queue.popleft()
        if board[y][x] == n*n:
            return
        nx = x + dx[i%4]
        ny = y + dy[i%4]
        if 0<=nx<n and 0<=ny<n and board[ny][nx] == 0:
            nx,ny = nx,ny
        else:
            nx = x + dx[(i+1)%4]
            ny = y + dy[(i+1)%4]
            i+=1
        board[ny][nx] = board[y][x] + 1
        queue.append((nx,ny))


t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    board = [[0] * n for _ in range(n)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    bfs(0,0)

    print("#{}".format(test_case))
    for i in board:
        print(" ".join(map(str, i)))

    
