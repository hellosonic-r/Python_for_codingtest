computer = int(input())
connect = int(input())

graph = [[] for _ in range(computer + 1)]

for _ in range(connect):
    a,b = map(int, input().split())
    graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)

visited = [0] * (computer + 1)

def dfs(graph, x, visited):
    visited[x] = 1
    for c in graph[x]:
        if visited[c] == 0:
            dfs(graph, c, visited)
    return visited.count(1)-1

print(dfs(graph, 1, visited))