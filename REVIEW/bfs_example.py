#bfs : 너비 우선 탐색 / 가까운 노드부터 탐색 / 큐

from collections import deque

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# visited = [False] * 9

# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         print(v, end = " ")
#         for i in graph[v]:
#             if not visited[i] == True:
#                 queue.append(i)
#                 visited[i] = True

# bfs(graph, 1, visited)


#try1
# visited = [False] * 9

# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         print(v, end= " ")
#         for i in graph[v]:
#             if not visited == True:
#                 queue.append(i)
#                 visited[i] = True
# bfs(graph, 1, visited)

# #try2
# visited = [False] * 9

# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True

#     while queue:
#         v = queue.popleft()
#         print(v, end = " ")
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# bfs(graph, 1, visited)


# #try3
# visited = [False] * 9

# def bfs(graph, start, visited):
#     queue = deque([start])
#     #현재 노드를 방문 처리
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         print(v, end = " ")
#         for i in graph[v]:
#             if not visited[i] == True:
#                 queue.append(i)
#                 visited[i] = True

# #try4
# visited = [False] * 9

# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         print(v, end = " ")
#         for i in graph[v]:
#             if not visited[i] == True:
#                 queue.append(i)
#                 visited[i] = True

#try5
# visited = [False] * 9

# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         print(v, end = " ")
#         for i in graph[v]:
#             if not visited[i] == True:
#                 queue.append(i)
#                 visited[i] = True

#try6
# visited = [False] * 9

# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         print(v, end = " ")
#         for i in graph[v]:
#             if not visited[i] == True:
#                 queue.append(i)
#                 visited[i] = True

#try7
visited = [False] * 9

def dfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if not visited[i] == True:
                queue.append(i)
                visited[i] = True