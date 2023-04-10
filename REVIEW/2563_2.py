n = int(input())
grid = [[0]*101 for _ in range(101)]

for i in range(n):
    x, y = map(int, input().split())
    for j in range(y,y+10):
        for k in range(x,x+10):
            grid[j][k] = 1

count = 0
for i in range(101):
    count += grid[i].count(1)

print(count)
