# computer = int(input())
# connect = int(input())

# graph = [[] for _ in range(computer + 1)]

# #각 노드가 연결된 정보를 2차원 리스트로 표현
# for _ in range(connect):
#     a,b = map(int, input().split())
#     graph[a].append(b)
#     if a not in graph[b]:
#         graph[b].append(a)

# #바이러스 방문 정보 리스트
# visited = [0] * (computer + 1)

# def dfs(x):
#     #현재 노드를 방문처리한다.
#     visited[x] = 1
#     #노드와 연결된 다른 노드를 방문처리하기 위해 for문을 수행한다.
#     for c in graph[x]:
#         if visited[c] == 0:
#             dfs(c)
#     #재귀 함수가 끝나면 visited 리스트의 요소가 1인(방문처리) 개수를 리턴한다. 
#     return visited.count(1)-1

# print(dfs(1))


computer = int(input())
connect = int(input())

graph = [[] for _ in range(computer + 1)]

#각 노드가 연결된 정보를 2차원 리스트로 표현
for _ in range(connect):
    a,b = map(int, input().split())
    graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)

#바이러스 방문 정보 리스트
visited = [0] * (computer + 1)

# def dfs(x):
#     #현재 노드를 방문처리한다.
#     visited[x] = 1
#     #노드와 연결된 다른 노드를 방문처리하기 위해 for문을 수행한다.
#     for c in graph[x]:
#         if visited[c] == 0:
#             dfs(c)
     
# print(visited) # >> [0, 0, 0, 0, 0, 0, 0, 0]
# dfs(1)
# print(visited) # >> [0, 1, 1, 1, 0, 1, 1, 0]
# print(visited.count(1)-1)
cnt = 0
def dfs(x):
    global cnt
    visited[x] = 1
    for c in graph[x]:
        if visited[c] == 0:
            dfs(c)
            cnt += 1
dfs(1)
print(cnt)