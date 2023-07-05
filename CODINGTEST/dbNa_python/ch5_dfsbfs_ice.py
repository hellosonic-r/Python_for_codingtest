##내풀이
def dfs(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n:
            if board[ny][nx] == 0:
                board[ny][nx] = 1
                dfs(nx,ny)

n, m = map(int, input().split()) #세로:n 가로:m

board = [list(map(int, input().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

ans = 0

for y in range(n):
    for x in range(m):
        if board[y][x] == 0:
            board[y][x] = 1
            ans += 1
            dfs(x,y)

print(ans)



##교재 풀이
def dfs(x,y):
    if x<0 or y<0 or x>=m or y>=n:
        return False
    if board[y][x] == 0:
        board[y][x] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for y in range(n):
    for x in range(m):
        if dfs(x,y):
            ans += 1

print(ans)



