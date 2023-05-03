##DFS 백트래킹.. 깊이우선탐색으로 하나밖에 못찾음
def dfs(n,x,y,temp_list,check_list,cnt):
    global ans
    if len(temp_list)==7:
        check_list.sort()
        if cnt >= 4 and check_list not in checking:
            checking.append(check_list)
            ans += 1
            print(temp_list)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=5 or ny>=5:
            continue
        else:
            if v[ny][nx] == 0:
                v[ny][nx] = 1
                if board[ny][nx] == "S":
                    check = ny*10 + nx
                    dfs(n+1, nx,ny,temp_list+[board[ny][nx]],check_list+[check],cnt+1)
                elif board[ny][nx] == "Y":
                    check = ny*10 + nx
                    dfs(n+1, nx,ny,temp_list+[board[ny][nx]],check_list+[check],cnt)
                v[ny][nx] = 0

board = [list(input()) for _ in range(5)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

v = [[0]*5 for _ in range(5)]

ans = 0
checking = []
for i in range(5):
    for j in range(5):
        if board[i][j] == "S":
            v[i][j] = 1
            dfs(0,j,i,[board[i][j]],[i*10+j],1)
            v[i][j] = 0

print(ans)
print(checking)



from collections import deque

def bfs(x_list, y_list):
    bfs_v = [[1]*5 for _ in range(5)] #뽑은 7개가 연결되어있는지 확인하기 위한 방문 테이블
    for i in y_list:
        for j in x_list:
            bfs_v[i][j] = 0
    queue = deque()
    queue.append((x_list[0],y_list[0]))
    bfs_v[y_list[0]][x_list[0]] = 1
    check = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=5 or ny>=5:
                continue
            else:
                if bfs_v[ny][nx] == 0:
                    bfs_v[ny][nx] = 1
                    check+=1 
                    queue.append((nx,ny))
    if check == 7:
        return True
    else:
        return False


def dfs(count, Y_cnt , x_list,y_list):
    global ans
    if Y_cnt >= 4:
        return
    if count == 7:
        if bfs(x_list,y_list):
            ans+=1 
        return 
    for i in range(5):
        for j in range(5):
            if v[i][j] == 0:
                v[i][j] = 1
                if board[i][j] == "Y":
                    dfs(count+1, Y_cnt+1, x_list+[j], y_list+[i])
                    v[i][j] = 0
                elif board[i][j] == "S":
                    dfs(count+1, Y_cnt, x_list+[j], y_list+[i])
                    v[i][j] = 0
                

board = [list(input()) for _ in range(5)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

v = [[0]*5 for _ in range(5)] #무작위로 7개 뽑는 방문 테이블
arr = []
ans = 0

dfs(0,0,[],[])

print(ans)


##DFS 백트래킹.. 깊이우선탐색으로 하나밖에 못찾음
def dfs(n,x,y,temp_list,check_list,cnt):
    global ans
    if len(temp_list)==7:
        check_list.sort()
        if cnt >= 4 and check_list not in checking:
            checking.append(check_list)
            ans += 1
            print(temp_list)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=5 or ny>=5:
            continue
        else:
            if v[ny][nx] == 0:
                v[ny][nx] = 1
                if board[ny][nx] == "S":
                    check = ny*10 + nx
                    dfs(n+1, nx,ny,temp_list+[board[ny][nx]],check_list+[check],cnt+1)
                elif board[ny][nx] == "Y":
                    check = ny*10 + nx
                    dfs(n+1, nx,ny,temp_list+[board[ny][nx]],check_list+[check],cnt)
                v[ny][nx] = 0

board = [list(input()) for _ in range(5)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

v = [[0]*5 for _ in range(5)]

ans = 0
checking = []
for i in range(5):
    for j in range(5):
        if board[i][j] == "S":
            v[i][j] = 1
            dfs(0,j,i,[board[i][j]],[i*10+j],1)
            v[i][j] = 0

print(ans)
print(checking)




#왜 4가 나오지 - y,x 바꿔서 썼음
from collections import deque

def bfs(arr):
    bfs_v = [[1]*5 for _ in range(5)] #뽑은 7개가 연결되어있는지 확인하기 위한 방문 테이블
    for i in arr:
        bfs_v[i[0]][i[1]] = 0
    queue = deque()
    queue.append(arr[0])
    bfs_v[arr[0][0]][arr[0][1]] = 1
    check = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=5 or ny>=5:
                continue
            else:
                if bfs_v[ny][nx] == 0:
                    bfs_v[ny][nx] = 1
                    check+=1 
                    queue.append((nx,ny))
    if check == 7:
        return True
    else:
        return False


def dfs(count, start, Y_cnt):
    global ans
    if Y_cnt >= 4:
        return
    if count == 7:
        if bfs(arr):
            ans+=1 
        return 
    for i in range(start, 25):
        x = i % 5
        y = i // 5
        if v[y][x] == 0:
            v[y][x] = 1
            arr.append((x,y))
            if board[y][x] == "S":
                nY_cnt = Y_cnt
            else:
                nY_cnt = Y_cnt + 1
            dfs(count+1, i+1, nY_cnt)
            arr.pop()
            v[y][x] = 0
                

board = [list(input()) for _ in range(5)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

v = [[0]*5 for _ in range(5)] #무작위로 7개 뽑는 방문 테이블
arr = []
ans = 0

dfs(0,0,0)

print(ans//2)






##다른 코드 참고(해결)
from collections import deque

def bfs(arr):
    bfs_v = [[1]*5 for _ in range(5)] #뽑은 7개가 연결되어있는지 확인하기 위한 방문 테이블
    for i in arr:
        bfs_v[i[1]][i[0]] = 0
    queue = deque()
    queue.append(arr[0])
    bfs_v[arr[0][1]][arr[0][0]] = 1
    check = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=5 or ny>=5:
                continue
            else:
                if bfs_v[ny][nx] == 0:
                    bfs_v[ny][nx] = 1
                    check+=1 
                    queue.append((nx,ny))
    if check != 7:
        return False
    else:
        return True


def dfs(count, start, Y_cnt):
    global ans
    if Y_cnt >= 4:
        return
    if count == 7:
        if bfs(arr):
            ans+=1 
        return 
    for i in range(start, 25):
        x = i % 5
        y = i // 5

        arr.append((x,y))
        dfs(count+1, i+1, Y_cnt + (board[y][x] == "Y"))
        arr.pop()

                

board = [list(input()) for _ in range(5)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

v = [[0]*5 for _ in range(5)] #무작위로 7개 뽑는 방문 테이블
arr = []
ans = 0

dfs(0,0,0)

print(ans)


##다시 풀어보기
from collections import deque

def bfs(arr):
    bfs_v = [[1]*5 for _ in range(5)] #뽑은 7개가 연결되어있는지 확인하기 위한 방문 테이블
    for i in arr:
        bfs_v[i[1]][i[0]] = 0
    queue = deque()
    queue.append(arr[0])
    bfs_v[arr[0][1]][arr[0][0]] = 1
    check = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=5 or ny>=5:
                continue
            else:
                if bfs_v[ny][nx] == 0:
                    bfs_v[ny][nx] = 1
                    check+=1 
                    queue.append((nx,ny))
    if check == 7:
        return True
    else:
        return False


def dfs(count, start, Y_cnt):
    global ans
    if Y_cnt >= 4:
        return
    if count == 7:
        if bfs(arr):
            ans+=1 
        return 
    for i in range(start, 25):
        x = i % 5
        y = i // 5
        if v[y][x] == 0:
            v[y][x] = 1
            arr.append((x,y))
            if board[y][x] == "S":
                nY_cnt = Y_cnt
            else:
                nY_cnt = Y_cnt + 1
            dfs(count+1, i+1, nY_cnt)
            arr.pop()
            v[y][x] = 0
                
board = [list(input()) for _ in range(5)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

v = [[0]*5 for _ in range(5)] #무작위로 7개 뽑는 방문 테이블
arr = []
ans = 0

dfs(0,0,0)

print(ans)

#--------------------블로그 작성--------------------

##다시풀어보기 - 메인함수에 별도의 학생 리스트 두기
from collections import deque

def bfs(seven_list):
    bfs_v = [[1]*5 for _ in range(5)] #방문 테이블 초기화. 기본값 = 1
    for i in seven_list: #리스트에 저장된 좌표 하나하나 방문하여 방문테이블 값을 0으로 바꿔준다.
        bfs_v[i[1]][i[0]] = 0
    queue = deque()
    queue.append(seven_list[0])
    bfs_v[seven_list[0][1]][seven_list[0][0]] = 1 #제일 처음 좌표는 방문 처리
    cnt = 1 #카운트도 기본 1
    while queue:
        x,y = queue.popleft()
        #네 방향을 돌아가면서 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=5 or ny>=5:
                continue
            else:
                #만약 다음 좌표가 0이라면 리스트에 저장된 좌표라는 뜻
                if bfs_v[ny][nx] == 0:
                    bfs_v[ny][nx] = 1
                    cnt += 1 #카운트 해준다
                    queue.append((nx,ny))
    #다 돌고나서 7번 다 카운트되었다면 그리드상 이어져 있는 것임
    if cnt == 7:
        return True
    else:
        return False

def dfs(count, start, Y_cnt):
    global ans
    if Y_cnt >= 4: #Y가 4가 되면 리턴(S가 4개 이상 담겨야 하므로)
        return
    
    if count == 7: #7명을 다 고르면
        if bfs(seven_list): #그 7명이 그리드 상 이어져있는지 확인
            ans+=1 #이어져있다면 ans += 1
        return
    
    for i in range(start, 25): #2차원 리스트를 1차원 리스트로. / 시작점을 start로 줌으로써 다음 선택 시 중복되지 않게
        x = i%5 
        y = i//5

        seven_list.append((x,y)) #메인 함수의 리스트 사용하니까 append, pop 메서드 사용해줘야 함
        dfs(count+1, i+1, Y_cnt+int(board[y][x] == "Y")) #넣어주는 현재 좌표 값이 Y라면 1이 추가될 것임
        seven_list.pop()


board = [list(input()) for _ in range(5)]
# v = [[0] * 5 for _ in range(5)] #dfs내에 방문 테이블 필요 없음 
#      -> 왜? 하위함수 호출 시 함수 start 파라미터 값으로 i+1 주기 때문에 

dx = [0,1,0,-1]
dy = [-1,0,1,0]

seven_list = [] #메인함수에 7명 학생 담을 리스트 만듬(백트래킹 시 append,pop메서드 필수)
ans = 0

dfs(0,0,0)
print(ans)



##다시 풀어보기 - 함수 파라미터에 학생 리스트 두기
from collections import deque

def bfs(arr):
    v_bfs = [[1]*5 for _ in range(5)]
    queue = deque()
    for i in arr:
        v_bfs[i[1]][i[0]] = 0
    v_bfs[arr[0][1]][arr[0][0]] = 1
    queue.append(arr[0])
    check = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=5 or ny>=5:
                continue
            else:
                if v_bfs[ny][nx] == 0:
                    v_bfs[ny][nx] = 1
                    check+=1 
                    queue.append((nx,ny))
    if check == 7:
        return True
    else:
        return False

def dfs(count, start, S_cnt, temp_list):
    global ans
    if count == 7:
        if S_cnt >= 4:
            if bfs(temp_list): #(함수 파라미터의 리스트도 사용이 가능함)
                ans+=1
        return
    for i in range(start, 25):
        x = i%5
        y = i//5
        
        dfs(count+1, i+1, S_cnt+int(board[y][x] == "S"), temp_list+[(y,x)])


board = [list(input()) for _ in range(5)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

ans = 0

dfs(0,0,0,[])

print(ans)
