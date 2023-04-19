from collections import deque

def bfs(sx,sy, ex,ey):
    queue = deque()
    queue.append((sx,sy))

    while queue:
        x,y = queue.popleft()
        if (x,y) == (ex,ey):
            return visited[y][x]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=length or ny>=length:
                continue
            else:
                if visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((nx,ny))


t = int(input())

for test_case in range(1, t+1):
    length = int(input())
    board = [[0] * length for _ in range(length)]
    visited = [[0] * length for _ in range(length)]
    sx,sy = map(int ,input().split())
    # board[sy][sx] = 1
    ex,ey = map(int, input().split())
    dx = [1,2,2,1,-1,-2,-2,-1]
    dy = [2,1,-1,-2,-2,-1,1,2]
    print(bfs(sx,sy,ex,ey))
    