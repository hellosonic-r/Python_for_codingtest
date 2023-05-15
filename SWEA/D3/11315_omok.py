##TC 94/100
t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    board = [list(input()) for _ in range(n)]
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [-1,0,1,0,-1,1,1,-1]
    max_cnt = 1
    for i in range(n):
        for j in range(n):
            if board[i][j] == "o":
                for k in range(8):
                    r = [(j,i)]
                    cnt = 1
            
                    for z in range(1,n):
                        nx = j + z*dx[k]
                        ny = i + z*dy[k]
                        if nx<0 or ny<0 or nx>=n or ny>=n:
                            break #다음방향
                        else: #범위 안에 있다면
                            if board[ny][nx] == "o":
                                if (nx,ny) not in r:
                                    r.append((nx,ny))
                                    cnt += 1
                                    if max_cnt < cnt:
                                        max_cnt = cnt
                            else:
                                if max_cnt < cnt:
                                    max_cnt = cnt
                                cnt = 1
    if max_cnt >= 5:
        print("#{} {}".format(test_case, "YES"))
    else:
        print("#{} {}".format(test_case, "NO"))
        

##TC 94/100
def dfs(n,x,y,cnt):
    global count
    if cnt == 5:
        count = cnt
        return
    if n == N:
        return
    nx = x + dx[k]
    ny = y + dy[k]
    if 0<=nx<N and 0<=ny<N:
        if board[ny][nx] == "o" and (nx,ny) not in v:
            v.append((nx,ny))
            dfs(n+1, nx,ny, cnt+1)
        else:
            dfs(n+1, nx,ny, 1)

t = int(input())
for test_case in range(1,t+1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [-1,0,1,0,-1,1,1,-1]
    v = [[0]*N for _ in range(N)]
    ans = "NO"
    for i in range(N):
        for j in range(N):
            if board[i][j] == "o":
                v = [(j,i)]
                count = 1
                for k in range(8):
                    dfs(1,j,i,1)
                    if count >= 5:
                        ans = "YES"
                        break
            if ans == "YES":
                break
        if ans == "YES":
            break
    print(count)

    print("#{} {}".format(test_case, ans))


##이렇게 체크해야 맞네
t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    board = [list(input()) for _ in range(n)]
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [-1,0,1,0,-1,1,1,-1]
    ans = "NO"
    for y in range(n):
        for x in range(n):

            for k in range(8):
                for z in range(5):
                    nx = x + z*dx[k]
                    ny = y + z*dy[k] 
                    if 0<=nx<n and 0 <=ny<n and board[ny][nx] == "o":
                        pass
                    else:
                        break
                else:
                    ans = "YES"

    print("#{} {}".format(test_case, ans))


##다시 풀어보자 -> 맞았다!
t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    board = [list(input()) for _ in range(n)]
    
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [-1,0,1,0,-1,1,1,-1]
    ans = 0
    for y in range(n):
        for x in range(n):
            for i in range(8):
                cnt = 0
                for j in range(n):
                    nx = x + j*dx[i]
                    ny = y + j*dy[i]
                    if 0<=nx<n and 0<=ny<n:
                        if board[ny][nx] == "o":
                            cnt += 1
                            if cnt >= 5:
                                ans = 1
                                break
                        else: 
                            cnt = 0
    if ans == 1:
        print("#{} {}".format(test_case, "YES"))
    else:
        print("#{} {}".format(test_case, "NO"))



##이렇게 풀었더니 맞음
t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    board = [list(input()) for _ in range(n)]
    dx = [1,1,0,1]
    dy = [0,1,1,-1]
    cnt = 0
    ans = 0
    for y in range(n):
        for x in range(n):
            if board[y][x] == "o":
                for i in range(4):
                    cnt = 1
                    for j in range(1,n):
                        nx = x + j*dx[i]
                        ny = y + j*dy[i]
                        if 0<=nx<n and 0<=ny<n:
                            if board[ny][nx] == "o":
                                cnt += 1
                            else:
                                break
                    if cnt >= 5:
                        ans = 1
                        break
                if ans == 1:
                    break
            if ans == 1:
                break
        if ans == 1:
            break

    if ans == 1:
        print("#{} {}".format(test_case, "YES"))
    else:
        print("#{} {}".format(test_case, "NO"))


