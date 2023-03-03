n = int(input())

graph = [[0]*1001 for _ in range(1001)]

for k in range(n):
    p,q,w,h = map(int, input().split())
    for i in range(p,p+w):
        for j in range(q,q+h):
            graph[i][j] = k + 1

for i in range(n):
    count = 0
    for m in graph:
        count += m.count(i+1)
    print(count)

