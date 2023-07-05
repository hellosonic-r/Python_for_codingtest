n = int(input())
command = list(input().split())
dx = [0,1,0,-1]
dy = [-1,0,1,0]

d = {"U":0, "R":1, "D":2, "L":3}

x,y = 0,0

for c in command:
    nx = x + dx[d[c]]
    ny = y + dy[d[c]]
    if 0<=nx<n and 0<=ny<n:
        x,y = nx,ny
    else:
        continue

print(y+1,x+1)
