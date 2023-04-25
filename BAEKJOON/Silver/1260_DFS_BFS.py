from collections import deque

def dfs(c):
    visited[c] = 1 #현재 정점 방문 처리
    ans_dfs.append(c) #정답 리스트에 현재 정점 추가
    for n in graph[c]: #현재 정점과 연결된 다른 정점들 살펴보기
        if visited[n] == 0: #만약 다른 정점이 아직 방문하지 않았다면
            dfs(n) #다음 정점 방문

def bfs(s):
    queue = deque() #큐 생성
    queue.append(s) #큐에 현재(시작) 정점 추가
    visited[s] = 1 #현재 정점 방문처리
    ans_bfs.append(s) #정답 리스트에 현재 정점 추가

    while queue: #정점이 하나도 없을때까지 
        c = queue.popleft() #큐에 먼저 들어간 순으로 꺼낸다
        for n in graph[c]: #꺼낸 정점과 연결된 다른 정점들 살펴보기
            if visited[n] == 0: #만약 다른 정점이 아직 방문하지 않았다면
                queue.append(n) #큐에 다른 정점들 삽입
                ans_bfs.append(n) #정답 리스트에 다른 정점들 삽입
                visited[n] = 1 #다른 정점들 방문처리

n,m,v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

#오름차순 정렬
for i in range(1, n+1):
    graph[i].sort()


visited = [0] * (n+1)
ans_dfs = []
dfs(v)

visited = [0] * (n+1)
ans_bfs = []
bfs(v)

print(" ".join(map(str, ans_dfs)))
print(" ".join(map(str, ans_bfs)))


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


##다시 풀어보기
from collections import deque

def dfs(s):
    visited[s] = 1
    ans_dfs.append(s)
    
    for i in num_list[s]:
        if visited[i] == 0: 
            dfs(i)

def bfs(s):
    queue = deque()
    queue.append(s)
    visited[s] = 1
    ans_bfs.append(s)
    while queue:
        num = queue.popleft()
        for i in num_list[num]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                ans_bfs.append(i)

n,m,k = map(int, input().split())
num_list = [[] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int, input().split())
    num_list[s].append(e)
    num_list[e].append(s)

for i in num_list:
    i.sort()

ans_dfs = []
visited = [0] * (n+1)
dfs(k)
print(" ".join(map(str, ans_dfs)))

ans_bfs = []
visited = [0] * (n+1)
bfs(k)
print(" ".join(map(str, ans_bfs)))