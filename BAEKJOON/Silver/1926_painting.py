###dfs 런타임에러 
# import sys
# sys.setrecursionlimit(10**6)

# def dfs(y,x):
#     global count
#     count += 1
#     board[y][x] = 0
#     visited[y][x] = 1

#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if nx<0 or ny<0 or ny>=n or nx>=m:
#             continue
#         else:
#             if board[ny][nx] == 1 and visited[ny][nx] == 0:
#                 dfs(ny, nx)

# n,m = map(int, input().split()) #sero #garo
# board = []
# for _ in range(n):
#     board.append(list(map(int, input().split())))
# visited = [[0] * m for _ in range(n)]
# dx = [0,1,0,-1]
# dy = [1,0,-1,0]

# count = 0
# max_count = 0
# ans = 0


# for i in range(n):
#     for j in range(m):
#         if board[i][j] == 1:         
#             dfs(i,j)
#             ans += 1 
#             if max_count < count:
#                 max_count = count
#             count = 0

# print(ans, max_count,sep="\n")


###bfs로 풀어보자
# from collections import deque

# def bfs(sy,sx):
#     global count
#     queue = deque()
#     queue.append((sy,sx))
#     count = 1

#     while queue:
#         y,x = queue.popleft()

#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if nx < 0 or ny < 0 or nx >= m or ny >= n:
#                 continue
#             else:
#                 if visited[ny][nx] == 0 and board[ny][nx] == 1:
#                     count += 1
#                     visited[ny][nx] = 1
#                     queue.append((ny,nx))
#     return count

# n,m = map(int,input().split())
# board = []
# for _ in range(n):
#     board.append(list(map(int, input().split())))
# dx = [0,1,0,-1]
# dy = [1,0,-1,0]
# visited = [[0]*m for _ in range(n)]
# count = 0
# ans = 0 
# max_count = 0
# result = []
# for i in range(n):
#     for j in range(m):
#         if board[i][j] == 1 and visited[i][j] == 0:
#             visited[i][j] = 1
#             pic = bfs(i,j) 
#             if max_count < count:
#                 max_count = count
#             ans += 1
#             count = 0

# print(ans,max_count,sep="\n")


###다시 풀어보자
from collections import deque

def bfs(x,y):
    global size
    queue = deque()
    queue.append((x,y))
    size = 1
    visited[y][x] = 1
    board[y][x] = 0

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            else:
                if board[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    board[ny][nx] = 0
                    size += 1
                    queue.append((nx,ny))
                    

n, m = map(int, input().split()) #세로n 가로m

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [0,1,0,-1]
dy = [1,0,-1,0]
visited = [[0] * m for _ in range(n)]
size = 0
max_size = 0
count = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visited[i][j] == 0:
            bfs(j, i)
            if max_size < size:
                max_size = size
            
            size = 0
            count += 1

print(count,max_size,sep="\n")
