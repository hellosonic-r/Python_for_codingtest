# from collections import deque

# def bfs(x,y):
#     global count
#     queue = deque()
#     queue.append((x,y))
#     visited[y][x] = 1
#     board[y][x] = 0
#     count = 1
#     while queue:
#         x,y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx<0 or ny<0 or nx>=n or ny>=m:
#                 continue
#             else:
#                 if visited[ny][nx] == 0 and board[ny][nx] == 1:
#                     visited[ny][nx] = 1
#                     board[ny][nx] = 0
#                     count += 1
#                     queue.append((nx,ny))

# m,n,k = map(int, input().split()) #m:세로 n:가로
# board = [[1]*n for _ in range(m)]
# for _ in range(k):
#     x1,y1,x2,y2 = map(int,input().split())
#     for i in range(y1, y2):
#         for j in range(x1, x2):
#             board[i][j] = 0

# visited = [[0]*n for _ in range(m)]
# count = 0

# dx = [0,1,0,-1]
# dy = [1,0,-1,0]
# ans = 0
# result = []
# for i in range(m):
#     for j in range(n):
#         if board[i][j] == 1:
#             bfs(j,i)
#             result.append(count)
#             count = 0
#             ans += 1

# result.sort()
# print(ans)
# print(" ".join(map(str,result)))

##다시 풀어보기
from collections import deque

def bfs(sx,sy):
    global num
    queue = deque()
    queue.append((sx,sy))
    visited[sy][sx] = 1
    board[sy][sx] = 0
    num = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            else:
                if board[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    board[ny][nx] = 0
                    queue.append((nx,ny))
                    num += 1


m,n,k = map(int, input().split()) #m:세로 n:가로 k:직사각형 개수

board = [[1]*n for _ in range(m)]

#직사각형 그린 부분은 0으로 표시
for _ in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            board[i][j] = 0


dx = [0,1,0,-1]
dy = [-1,0,1,0]

ans = 0
num = 0
area_list = []
for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            visited = [[0]*n for _ in range(m)]
            bfs(j,i)
            area_list.append(num)
            ans += 1

area_list.sort()

print(ans)
print(" ".join(map(str, area_list)))
