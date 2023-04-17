# from collections import deque

# def dfs(c):
#     visited[c] = 1
#     ans_dfs.append(c)
#     for n in graph[c]:
#         if visited[n] == 0:
#             dfs(n)

# def bfs(s):
#     queue = deque()
#     queue.append(s)
#     visited[s] = 1
#     ans_bfs.append(s)

#     while queue:
#         c = queue.popleft()
#         for n in graph[c]:
#             if visited[n] == 0: #가보지 않았다면 큐에 삽입
#                 queue.append(n)
#                 ans_bfs.append(n)
#                 visited[n] = 1                

# n,m,v = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     start, end = map(int, input().split())
#     graph[start].append(end)
#     graph[end].append(start)

# #오름차순 정렬
# for i in range(1, n+1):
#     graph[i].sort()


# visited = [0] * (n+1)
# ans_dfs = []
# dfs(v)

# visited = [0] * (n+1)
# ans_bfs = []
# bfs(v)

# print(" ".join(map(str, ans_dfs)))
# print(" ".join(map(str, ans_bfs)))


## 다시풀어보기 
from collections import deque

def dfs(c):
    visited[c] = 1
    ans_dfs.append(c)
    for n in graph[c]:
        if visited[n] == 0:
            dfs(n)

def bfs(s):
    queue = deque()
    queue.append(s)
    visited[s] = 1
    ans_bfs.append(s)

    while queue:
        c = queue.popleft()
        for n in graph[c]:
            if visited[n] == 0:
                queue.append(n)
                visited[n] = 1
                ans_bfs.append(n)

n,m,v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, n+1):
    graph[i].sort()

visited = [0] * (n+1)
ans_dfs = []
dfs(v)

visited = [0] * (n+1)
ans_bfs = []
bfs(v)

print(ans_dfs)
print(ans_bfs)