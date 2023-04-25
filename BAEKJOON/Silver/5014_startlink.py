##dfs 풀다가 못품
# def dfs(count, now):
#     global ans
#     if now == g:
#         ans = count-1
#         return    
#     if now > f:
#         return
#     if now > 1000000:
#         return
#     for i in (now+u, now-d):
#         if visited[i] == 0:
#             visited[i] = 1
#             dfs(count+1, i)


# f,s,g,u,d = map(int,input().split())
# ans = -1
# visited = [0]*1000001
# dfs(0, s)
# print(ans)


##bfs로 풀이
from collections import deque

def bfs(start, end):
    queue = deque()
    queue.append(start) #현재 좌표 값 큐에 추가
    visited[start] = 1 #현재 좌표 방문처리
    while queue:
        now = queue.popleft()
        if now == end: #목표 층에 도달하면
            return visited[now]-1 #룩업테이블의 현재 좌표 값 -1 
        for i in (now+u, now-d): #위로 가거나 아래로 가는 두 가지
            if 1<=i<=f and visited[i] == 0: #1층부터 옥상까지의 범위 & 아직 방문 안한 좌표
                visited[i] = visited[now] + 1 #다음 좌표 값 = 현재 좌표 값 + 1
                queue.append(i) #다음 좌표 값 큐에 추가
    return -1 #여기까지 온다면 목표 층에 도달 못한 것

f,s,g,u,d = map(int,input().split())
visited = [0] * 1000001

ans = bfs(s,g)
if ans == -1:
    print("use the stairs")
else:
    print(ans)
