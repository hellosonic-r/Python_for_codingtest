from collections import deque

cnt = 0
result = 0
l_location = []

def solution(maps):
    answer = 0
    
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    v = [[0]*len(maps[0]) for _ in range(len(maps))]
    r = [[0]*len(maps[0]) for _ in range(len(maps))]
    
    flag = False
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "L":
                flag = True
                l_location.append(j)
                l_location.append(i)
                break
        if flag:
            break
            
    print(l_location)
    
    
    def first_bfs(sx,sy):
        global cnt
        queue = deque()
        queue.append((sx,sy))
        v[sy][sx] = 1
        while queue:
            x,y = queue.popleft()
            if maps[y][x] == "L":
                cnt = v[y][x] - 1
                return
                
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<len(maps[0]) and 0<=ny<len(maps):
                    if v[ny][nx] == 0 and maps[ny][nx] != "X":
                        v[ny][nx] = v[y][x] + 1
                        queue.append((nx,ny))

    def second_bfs(x,y):
        global result
        q = deque()
        q.append((x,y))
        r[y][x] = 1
        while q:
            x,y = q.popleft()
            if maps[y][x] == "E":
                result = r[y][x] - 1
                return
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<len(maps[0]) and 0<=ny<len(maps):
                    if r[ny][nx] == 0 and maps[ny][nx] != "X":
                        r[ny][nx] = r[y][x] + 1
                        q.append((nx,ny))
                        
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                first_bfs(j,i)
                break
    
    if cnt != 0:
        second_bfs(l_location[0], l_location[1])
        if result == 0:
            answer = -1
        else:
            answer = cnt + result
    else:
        answer = -1
    

    return answer