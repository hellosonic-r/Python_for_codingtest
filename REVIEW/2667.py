def dfs(x,y):
    global count
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=n:
            continue
        else:
            if board[ny][nx] == 1 and v[ny][nx] == 0:
                board[ny][nx] = 0
                v[ny][nx] = 1
                count += 1
                dfs(nx,ny)

n = int(input())
board = [list(map(int, input())) for _ in range(n)]

v = [[0]*n for _ in range(n)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]
ans = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j] = 0
            v[i][j] = 1
            count = 1
            dfs(j,i)
            ans.append(count)
print(len(ans))
ans.sort()
for i in ans:
    print(i)
