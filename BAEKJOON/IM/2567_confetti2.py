num = int(input())

total_paper = [[0] * 101 for _ in range(101)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            total_paper[i][j] = 1

result = 0 

for i in range(1,101):
    for j in range(1,101):
        if tot