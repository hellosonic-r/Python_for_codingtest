from collections import deque

def x_turn_right(x):
    return x+dx[(count+1)%4]
def y_turn_right(y):
    return y+dy[(count+1)%4]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[y][x] = 1
    global count, num, n
    count = 0
    while queue:
        if num > n*n:
            return
        x,y = queue.popleft()
        visited[y][x] = num
        nx = x + dx[count%4]
        ny = y  + dy[count%4]
        if (0<=nx<n and 0<=ny<n) and visited[ny][nx] == 0:
                nx = nx
                ny = ny
        else:
            nx = x_turn_right(x)
            ny = y_turn_right(y)
            count += 1
 
        queue.append((nx,ny))
        num += 1
    
t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    visited = [[0]*n for _ in range(n)]
    count = 0
    num = 1
    bfs(0,0)
    print("#{}".format(test_case))
    for i in visited:
        print(" ".join(map(str, i)))
    