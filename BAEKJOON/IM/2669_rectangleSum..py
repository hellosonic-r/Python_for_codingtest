graph = [[0] * 100 for _ in range(100)]

for _ in range(4):
    x,y,p,q = map(int, input().split())
    for i in range(x,p):
        for j in range(y,q):
            graph[i][j] = 1

sum = 0
for i in range(100):
    sum += graph[i].count(1)
print(sum)
    