grid = [[0] * 100 for _ in range(100)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            grid[i][j] = 1

ans = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] == 1:
            count = 0
            for k in range(4):
                nx = j + dx[k]
                ny = i + dy[k]
                if nx < 0 or ny < 0 or nx > 99 or ny > 99:
                    continue 
                else:
                    if grid[ny][nx] == 1:
                        count += 1
            if count == 2:
                ans += 2
            elif count == 3:
                ans += 1
print(ans)
        


