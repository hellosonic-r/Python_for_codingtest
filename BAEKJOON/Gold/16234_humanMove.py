##시간초과
from collections import deque

#bfs로 연합 가능한 좌표 방문하여 탐색
def bfs(sx,sy):
    global cnt,l,r,temp_total,temp_cnt,check
    queue = deque()
    queue.append((sx,sy))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            else:
                #현재 좌표의 나라와 다음 좌표의 나라의 인구 차이가 조건에 부합하고,
                if l <= abs(board[ny][nx] - board[y][x]) <= r \
                    and v[ny][nx] == 0: #아직 방문처리 되지 않았다면
                    v[ny][nx] = cnt #방문처리 해준다(cnt로 방문처리하는 이유는 연합하는 나라 구분하기 위해서)
                    queue.append((nx,ny))
                    #나중에 연합을 이루는 각 칸의 인구수를 계산해야 하므로, 방문한 나라의 인구수의 합을 저장한다.
                    temp_total += board[ny][nx]  
                    temp_cnt += 1 #연합을 이루는 나라의 숫자를 카운트한다.
                    check += 1
 

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]


answer = 0

while True: #연합이 더이상 불가능할 때까지 반복한다
    v = [[0] * n for _ in range(n)]
    cnt = 0
    d = {}
    check = 0
    #나라들을 방문하면서 연합인지 아닌지 체크
    for y in range(n): 
        for x in range(n):
            if v[y][x] == 0: #아직 방문체크 되지않은 나라라면
                cnt += 1 #연합 1, 연합 2, 연합 3,,, 연합한 나라를 구분하기 위한 변수
                v[y][x] = cnt #첫 방문하는 나라의 연합 번호를 방문 테이블에 표시
                temp_total = board[y][x] #첫 방문한 나라의 인구 수를 방문한 나라의 총 인구수 변수에 저장
                temp_cnt = 1 #연합한 나라의 개수 카운트(현재 방문한 나라부터 1부터 카운트)
                bfs(x,y) #bfs돌면서 어떤 나라들이 서로 연합되었는지 확인한다
                d[cnt] = temp_total // temp_cnt #연합 1, 연합 2,,, 연합별로 연합번호에 해당하는 인구수 딕셔너리에 저장

    if len(d) == n*n: #만약 딕셔너리가 입력받은 나라의 개수와 같다면, 연합에 실패한 것이므로
        break #반복문 탈출
    
    ##이 부분에서 시간초과 원인 발생한듯.
    for i in range(1,cnt+1): #연합 번호를 1부터 cnt(마지막으로 저장된 연합번호)까지 돌면서
        #모든 좌표를 탐색
        for y in range(n): 
            for x in range(n):
                #방문테이블에 해당 연합번호가 저장되어있다면
                if v[y][x] == i: 
                    #딕셔너리 d에서 해당 연합번호를 키로 갖는 값으로 갱신
                    board[y][x] = d[i]

    if check == 0: #bfs를 돌았음에도 check가 0이라면 연합할 나라가 없는 것
        break

    answer += 1
                
print(answer)







            
##시간초과
from collections import deque

def bfs(sx,sy):
    global cnt,l,r,temp_total,temp_cnt,check
    queue = deque()
    queue.append((sx,sy))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            else:
                if l <= abs(board[ny][nx] - board[y][x]) <= r and v[ny][nx] == 0:
                    v[ny][nx] = cnt
                    queue.append((nx,ny))
                    temp_list.append((nx,ny)) #연합한 나라의 좌표 저장
                    temp_total += board[ny][nx] 
                    temp_cnt += 1
                    check += 1
 

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]


answer = 0

while True:
    v = [[0] * n for _ in range(n)]
    cnt = 0
    d = {}
    check = 0
    move_list = []
    for y in range(n):
        for x in range(n):
            if v[y][x] == 0:
                temp_list = []
                cnt += 1
                temp_list.append((x,y)) #연합한 나라의 좌표 저장(현재좌표)
                v[y][x] = cnt
                temp_total = board[y][x]
                temp_cnt = 1
                bfs(x,y)
                move_list.append(temp_list) #bfs 수행 후 move_list에 연합한 나라의 좌표 저장
                d[cnt] = temp_total // temp_cnt


    
    if len(d) == n*n:
        break

    ##이 부분 고쳐서 시간초과 해결
    time = 0
    for k in move_list: #연합한 나라의 좌표들이 저장된 move_list를 하나씩 꺼내서 살펴본다.
        #k : 각 연합번호에 해당하는 연합한 나라들의 좌표들
        time += 1 #연합 1 부터 시작해서 연합 2, 연합 3,,,
        for i,j in k: 
            if v[j][i] == time:
                board[j][i] = d[time] 


    if check == 0:
        break

    answer += 1
                
print(answer)


            
