# #도시의 칸 r,c 위에서부터 r번째 왼쪽으로부터 c번째 -> (c,r)
# from collections import deque

# def bfs(sx,sy,r):
#     queue = deque()
#     queue.append((sx,sy))
#     r[sy][sx] = 1
#     while queue:
#         x,y = queue.popleft()
#         if board[y][x] == 2:
#             return abs(sx-x) + abs(sy-y)
        
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<n and 0<=ny<n:
#                 if r[ny][nx] == 0:
#                     r[ny][nx] = 1
#                     queue.append((nx,ny))

# def check():
#     global distance
#     distance = 0
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] == 1:
#                 r = [[0] * n for _ in range(n)]
#                 distance += bfs(j,i,r)
                
# def dfs(count):
#     global distance, ans
#     if count == m:
#         check()
#         if ans > distance:
#             ans = distance
#         return
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] == 2 and (j,i) not in v:
#                 board[i][j] = 0
#                 v.append((j,i))
#                 dfs(count+1)
#                 v.pop()
#                 board[i][j] = 2


# n, m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
# r = [[0] * n for _ in range(n)]
# v = []
# dx = [0,1,0,-1]
# dy = [-1,0,1,0]
# distance = 0
# ans = 100000

# dfs(0)

# print(ans)


#백트래킹으로 폐업시키지 않을 치킨집 구하기
def dfs(count, start, temp_list):
    if len(temp_list) == m: #m개가 되면,
        result.append(temp_list) #result에 저장된 리스트 저장 후 리턴
        return
    
    for i in range(start, len(chicken)):
        if i not in v:
            v.append(i)
            dfs(count+1, i+1, temp_list+[chicken[i]])
            v.pop()


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

chicken = [] #전체 치킨집의 좌표를 담는다.
result = [] #폐업하지 않은 치킨집 케이스들

#전체 치킨집 저장
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            chicken.append((j,i)) 

v = []
dfs(0,0,[]) #m개의 치킨집 좌표를 고르는 백트래킹 함수 실행

ans = [] #폐업하지 않은 치킨집 좌표를 탐색하며 각 케이스별 최단 치킨거리를 저장한다.

for k in result: #치킨집 좌표를 하나씩 꺼내면서 살펴본다.
    total = 0
    for y in range(n):
        for x in range(n):
            if board[y][x] == 1: #집인 곳의 좌표를 찾으면
                distance = 1000
                for c in k: #폐업하지 않은 치킨집 좌표 중 가까운 치킨 거리를 찾는다.
                    if distance > abs(x-c[0]) + abs(y-c[1]):
                        distance = abs(x-c[0]) + abs(y-c[1])
                total += distance #치킨 거리의 총 합을 구한다.
    
    ans.append(total)
                
print(min(ans))

