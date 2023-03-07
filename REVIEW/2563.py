num = int(input())

graph = [[0]*100 for _ in range(100)]

for _ in range(num):
    x, y = map(int, input().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            if graph[i][j] == 0:
                graph[i][j] = 1
fin = 0
for k in range(100):
    fin += graph[k].count(1)

print(fin)