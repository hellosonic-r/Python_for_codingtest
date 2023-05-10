board = [[0] * 101 for _ in range(101)]

n = int(input())

dx = [0,1,0,-1]
dy = [-1,0,1,0]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            board[i][j] = 1
ans = 0
for i in range(101):
    for j in range(101):
        cnt = 0
        if board[i][j] == 1:
            for k in range(4):
                nx = j + dx[k]
                ny = i + dy[k]
                if nx<0 or ny<0 or nx>=101 or ny>=101:
                    continue
                else:
                    if board[ny][nx] == 0:
                        cnt += 1
        if cnt == 1:
            ans += 1
        elif cnt == 2:
            ans += 2
print(ans)
