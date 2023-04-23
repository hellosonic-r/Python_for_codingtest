# from collections import deque

# def bfs(v):
#     queue = deque()
#     queue.append(v)
#     while queue:
#         x = queue.popleft()
#         if x == k:
#             return visited[x]
#         for i in (x-1, x+1, 2*x):
#             if 0 <= i <= 100000 and not visited[i]:
#                 visited[i] = visited[x] + 1
#                 queue.append(i)

# n,k = map(int, input().split())
# visited = [0 for i in range(100001)]
# print(bfs(n))

##다시 풀어보기
from collections import deque

def bfs(subin): #x는 수빈이의 현재 위치
    queue = deque()
    queue.append(subin)
    visited[subin] = 1
    while queue:
        x = queue.popleft()
        if x == k:
            return visited[x]-1
        for i in (x-1, x+1, 2*x):
            if 0<=i<=100000 and visited[i] == 0:
                visited[i] = visited[x] + 1
                queue.append(i) 

n, k = map(int, input().split())
visited = [0 for _ in range(100001)]
print(bfs(n))

##다시 풀어보기
from collections import deque

def bfs(sx, ex):
    global count
    queue = deque()
    queue.append(sx)
    #수빈이 위치 방문처리 
    visited[sx] = 1

    while queue:
        x = queue.popleft()
        if x == ex: #수빈이가 동생과 만난다면 
            return visited[x] - 1 #룩업테이블에 저장된 값-1 리턴
        for i in (x-1, x+1, 2*x): #수빈이가 갈 수 있는 위치
            #문제의 조건 범위를 벗어나지 않고, 방문하지 않은 곳이라면
            if 0<=i<=100000 and visited[i] == 0:
                #우선 방문처리
                visited[i] = visited[x] + 1
                #큐에 다음 좌표 삽입
                queue.append(i)
                
n, k = map(int, input().split())
visited = [0] * 100001 #룩업테이블(문제의 조건 범위)
count = 0

print(bfs(n,k))