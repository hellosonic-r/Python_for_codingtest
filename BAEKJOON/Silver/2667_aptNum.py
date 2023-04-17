# ## dfs 내 풀이.. 왜 틀린지 모르겠음

# def dfs(x,y):
#     global count
#     if x == n-1 and y == n-1:
#         return
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < n:
#             if board[ny][nx] == 1 and v[ny][nx] == 0:
#                 board[ny][nx] = 0
#                 v[ny][nx] = 1
#                 count += 1
#                 dfs(nx, ny)

# n = int(input())
# board = []
# for _ in range(n):
#     board.append(list(map(int, str(input()))))
# dx = [0,1,0,-1]
# dy = [1,0,-1,0]
# v = [[0] * n for _ in range(n)]
# count = 0
# ans = []

# for j in range(n):
#     for i in range(n):
#         if board[j][i] == 1 and v[j][i] == 0:
#             dfs(i,j)
#             ans.append(count)
#             count = 0

# ans.sort()
# print(len(ans))
# for i in ans:
#     print(i)


# ## 이렇게 하니까 맞음 ..;;
# def dfs(x,y):
#     global count
#     v[y][x] = 1
#     if board[y][x] == 1:
#         count += 1

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < n:
#             if board[ny][nx] == 1 and v[ny][nx] == 0:
#                 dfs(nx, ny)

# n = int(input())
# board = []
# for _ in range(n):
#     board.append(list(map(int, str(input()))))
# dx = [0,1,0,-1]
# dy = [1,0,-1,0]
# v = [[0] * n for _ in range(n)]
# count = 0
# ans = []

# for j in range(n):
#     for i in range(n):
#         if board[j][i] == 1 and v[j][i] == 0:
#             dfs(i,j)
#             ans.append(count)
#             count = 0

# ans.sort()
# print(len(ans))
# for i in ans:
#     print(i)



# ## 그래.. 그럼 내 코드 뜯어고쳐보자 >> 맞았음. 
# ## for문 안에서 count를 해주었던게 에러였던듯
# ## dfs 호출 되었을 초기에 count 해주니까 맞음

# def dfs(x,y):
#     global count
#     v[y][x] = 1
#     if board[y][x] == 1:
#         count += 1

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx<0 or ny<0 or nx>=n or ny>=n:
#             continue
#         else:
#             if board[ny][nx] == 1 and v[ny][nx] == 0:
#                 dfs(nx, ny)

# n = int(input())
# board = []
# for _ in range(n):
#     board.append(list(map(int, str(input()))))
# dx = [0,1,0,-1]
# dy = [1,0,-1,0]
# v = [[0] * n for _ in range(n)]
# count = 0
# ans = []

# for j in range(n):
#     for i in range(n):
#         if board[j][i] == 1 and v[j][i] == 0:
#             dfs(i,j)
#             ans.append(count)
#             count = 0

# ans.sort()
# print(len(ans))
# for i in ans:
#     print(i)   


##다시풀어보기
def dfs(x,y):
    global count
    board[y][x] = 0
    count += 1 

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=n:
            continue
        else:
            if board[ny][nx] == 1 and visited[ny][nx] == 0:
                dfs(nx, ny)


n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, str(input()))))
visited = [[0]*n for _ in range(n)]
count = 0
ans = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for j in range(n):
    for i in range(n):
        if board[j][i] == 1:
            dfs(i,j)
            ans.append(count)
            count = 0

ans.sort()

print(len(ans))
for i in ans:
    print(i)



