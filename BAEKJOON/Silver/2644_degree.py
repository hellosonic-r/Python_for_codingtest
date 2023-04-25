##DFS로 풀이
def dfs(s, count, temp_list): #방문한 노드를 temp_list에 담는다
    global ans
    if end in temp_list:
        ans = count
        return #리턴필수! 그래야 더 이상 다음 노드 안 담음!
    for i in graph[s]:
        if i not in temp_list: #temp_list에 i가 안 담겨 있다면
            dfs(i, count+1, temp_list+[i])

n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

ans = -1

dfs(start, 0, [start]) #초기 temp_list에는 시작 노드가 담겨있어야 한다
print(ans)


##BFS로 풀이
from collections import deque

def bfs(s,e):
    queue = deque()
    queue.append(s)
    visited[s] = 1
    while queue:
        node = queue.popleft()
        if node == e:
            return visited[node]-1
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = visited[node] + 1
                queue.append(i)
    return -1 #이게 실행된다면 촌수를 계산할 수 없는 거임

n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [0]*(n+1)

print(bfs(start,end))