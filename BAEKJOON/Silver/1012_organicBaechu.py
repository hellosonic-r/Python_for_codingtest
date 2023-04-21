from collections import deque

def bfs(x,y):
    global count 
    queue = deque()
    queue.append((x,y))
    
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            else:
                if visited[ny][nx] == 0 and board[ny][nx] == 1:
                    queue.append((nx,ny))
                    board[ny][nx] = 0
                    visited[ny][nx] = count

t = int(input())
for test_case in range(1,t+1):
    m,n,k = map(int, input().split()) #m:가로 n:세로 k:배추 심어진 위치 개수
    board = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int,input().split())
        board[y][x] = 1
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited = [[0]*m for _ in range(n)]

    count = 1
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                bfs(j,i)
                count+=1     

    print(count-1)


##한번 더 풀어보기
from collections import deque

def bfs(sx,sy):
    queue = deque()
    queue.append((sx,sy))

    while queue:
        x,y = queue.popleft()
        board[y][x] = 0    #큐에서 뺀 다음 방문체크를 하면 시간초과 에러 발생(중복방문)
        visited[y][x] = 1  
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            else:
                if board[ny][nx] == 1 and visited[ny][nx] == 0:
                    queue.append((nx,ny))

t = int(input())
for test_case in range(1, t+1):
    m, n, k = map(int, input().split()) #m:가로 / n:세로 / k:배추 심겨진 위치 개수
    board = [[0]*m for _ in range(n)]

    for _ in range(k):
        x,y = map(int, input().split())
        board[y][x] = 1

    visited = [[0]*m for _ in range(n)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    ans = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1: 
                bfs(j,i) #이어진 배추가 심어진 좌표를 모두 0으로 바꾸게 된다.
                ans += 1 
    
    print(ans)

    

