###dfs로 풀어버림... 최단거리 구하는데 dfs로 풀으니까 당연히 틀리지..
# def dfs(x, y):
#     global ans
#     if x == m-1 and y == n-1:
#         result.append(ans)
#         return
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx < 0 or ny < 0 or nx >= m or ny >= n:
#             continue 
#         else:
#             if board[ny][nx] == 1 and v[ny][nx] == 0:
#                 v[ny][nx] = 1
#                 ans += 1
#                 dfs(nx, ny)
        

# n, m = map(int, input().split())
# board = []
# for _ in range(n):
#     board.append(list(map(int, str(input()))))
# dx = [0,1,0,-1]
# dy = [1,0,-1,0]
# v = [[0]*m for _ in range(n)]
# ans = 1
# result = []
# dfs(0,0)

# print(result)


### bfs로 다시 풀어보자

from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, str(input()))))
v = [[0] * m for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(sx,sy, ex,ey):
    queue = deque()
    queue.append((sx,sy))
    v[sy][sx] = 1
    while queue:
        x,y = queue.popleft()
        if (x,y) == (ex, ey):
            return v[ey][ex]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            else:
                if board[ny][nx] == 1 and v[ny][nx] == 0:
                    queue.append((nx, ny))
                    v[ny][nx] = v[y][x] + 1

ans = (bfs(0,0, m-1, n-1))

print(ans)

