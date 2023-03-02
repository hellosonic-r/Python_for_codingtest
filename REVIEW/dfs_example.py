#dfs : 깊이 우선 탐색 / 스택 / 재귀함수 사용


graph = [
    [],
    [2,3,8], #노드 1과 연결된 노드 2, 3, 8
    [1,7],  #노드 2와 연결된 노드 1, 7
    [1,4,5],    #노드 3과 연결된 노드 1, 4, 5
    [3,5],  #노드 4와 연결된 노드 3, 5
    [3,4],  #노드 5와 연결된 노드 3, 4  
    [7],    #노드 6과 연결된 노드 7
    [2,6,8],    #노드 7과 연결된 노드 2,6,8
    [1,7]   #노드 8과 연결된 노드 1,7
]
#try1
# visited = [False] * 9 #각 노드가 방문한 정보를 리스트 자료형으로 표현

# def dfs(graph, v, visited):
#     #현재 노드를 방문 처리
#     visited[v] = True
#     print(v, end = " ")
#     #현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v]:
#         if not visited[i] == True:
#             dfs(graph, i , visited)

# dfs(graph, 1, visited)
#try2
# visited = [False] * 9

# def dfs(graph,v,visited):
#     visited[v] = True
#     print(v, end = " ")
#     for i in graph[v]:
#         if not visited[i] == True:
#             dfs(graph,i,visited)
# dfs(graph,1,visited)

#try3
# visited = [False] * 9

# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end = " ")
#     for i in graph[v]:
#         if not visited[i] == True:
#             dfs(graph, i, visited)
# dfs(graph,1,visited)

#try4
# visited = [False] * 9
# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end = " ")
#     for i in graph[v]:
#         if not visited[i] == True:
#             dfs(graph, i, visited)
# dfs(graph,1,visited)

#try5
visited = [False] * 9
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = " ")
    for i in graph[v]:
        if not visited[i] == True:
            dfs(graph, i, visited)
dfs(graph,1,visited)
