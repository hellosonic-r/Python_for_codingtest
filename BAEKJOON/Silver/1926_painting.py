# ###dfs 런타임에러 
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


# ###bfs로 풀어보자
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


# ###다시 풀어보자
# from collections import deque

# def bfs(x,y):
#     global size
#     queue = deque()
#     queue.append((x,y))
#     size = 1 #사이즈는 1부터 시작
#     visited[y][x] = 1 #현재 좌표 방문처리
#     board[y][x] = 0 #방문한 현재 좌표에 0 저장

#     while queue:
#         x,y = queue.popleft() #큐에 저장된 좌표를 꺼낸다
#         for i in range(4): #동서남북 4개 방향에 대하여 갈 수 있는지(1인지) 판단
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx<0 or ny<0 or nx>=m or ny>=n: #범위 벗어나면 continue
#                 continue
#             else:
#                 #갈 수 있다면(다음 좌표가 1이거나, 방문하지 않았다면)
#                 if board[ny][nx] == 1 and visited[ny][nx] == 0: 
#                     visited[ny][nx] = 1 #일단 방문처리
#                     board[ny][nx] = 0 #다음 좌표도 0으로 표시
#                     size += 1 #사이즈를 1 증가
#                     queue.append((nx,ny)) #다음 좌표를 큐에 넣는다
                    

# n, m = map(int, input().split()) #세로n 가로m

# board = []
# for _ in range(n):
#     board.append(list(map(int, input().split())))

# dx = [0,1,0,-1]
# dy = [1,0,-1,0]
# visited = [[0] * m for _ in range(n)]
# size = 0
# max_size = 0
# count = 0

# #전체 보드에 대하여
# for i in range(n):
#     for j in range(m):
#         if board[i][j] == 1: #좌표가 1인 곳이 있다면 bfs 함수 실행
#             bfs(j, i) #bfs 함수 실행. 실행이 완료되면 size값이 변화되고, 들른 모든 좌표값이 0이 됨
#             if max_size < size:
#                 max_size = size
#             size = 0 #다음 bfs 함수를 위해 사이즈 초기화
#             count += 1

# print(count,max_size,sep="\n")


##다시 풀어보기
from collections import deque

def bfs(sx,sy):
    global count
    queue = deque()
    queue.append((sx,sy))
    board[sy][sx] = 0
    visited[sy][sx] = 1
    count = 1
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
                    queue.append((nx,ny))
                    count += 1

n,m = map(int, input().split()) #n:세로 / m:가로
board = []
for _ in range(n):
    board.append(list(map(int ,input().split())))

visited = [[0] * m for _ in range(n)]

count = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
result = []
ans = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            bfs(j,i)
            result.append(count)
            count = 0
            ans += 1

print(ans)
if len(result) == 0:
    print(0)
else:
    print(max(result))


