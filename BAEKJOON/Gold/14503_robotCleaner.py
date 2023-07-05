# ##틀림. 방향벡터 조심. 
# n, m = map(int, input().split()) #n:세로 m:가로
# y,x, d = map(int, input().split()) #0:북 1:동 2:남 3:서(시계방향)
# board = []

# for _ in range(n):
#     board.append(list(map(int, input().split())))

# dx = [0,1,0,-1]
# dy = [-1,0,1,0]

# v = [[0] * m for _ in range(n)]
# v[y][x] = 1
# ans = 1

# #0:북 1:동 2:남 3:서(시계방향)

# def turn_left():
#     global d
#     d = d - 1
#     if d == -1:
#         d = 3
#     return d

# while True:
#     cnt = 0
#     for _ in range(4):
#         d = turn_left()
#         nx = x+dx[d]
#         ny = y+dy[d]
#         if 0<=nx<m and 0<=ny<m and v[ny][nx] == 0 and board[ny][nx] == 0:
#             v[ny][nx] = 1
#             x, y = nx, ny
#             ans+=1
#             break
#         else:
#             cnt += 1

#     if cnt == 4:
#         nx = x+dx[(d+2)%4]
#         ny = y+dy[(d+2)%4]
#         if 0<=nx<m and 0<=ny<m and board[ny][nx] == 0:
#             x, y = nx, ny
#         else:
#             break

# print(ans)



##다시 풀어보기
n, m = map(int, input().split()) #n:세로 m:가로
y,x, d = map(int, input().split()) #0:북 1:동 2:남 3:서
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [0,1,0,-1]
dy = [-1,0,1,0]

v = [[0] * m for _ in range(n)]
v[y][x] = 1 #로봇 청소기가 있는 칸은 방문처리
ans = 1
cnt = 0

#0:북 1:동 2:남 3:서(

def turn_left(): #반시계 방향으로 회전
    global d
    d = d - 1
    if d == -1:
        d = 3
    return d

while True:
    d = turn_left() #반시계 방향으로 회전해서 다음 좌표를 탐색한다.
    nx = x+dx[d]
    ny = y+dy[d]
    #만약 다음 좌표가 범위에 있고, 벽이 아니고, 아직 방문하지 않은(청소하지 않은) 좌표라면
    if 0<=nx<m and 0<=ny<n and board[ny][nx] == 0 and v[ny][nx] == 0:
        v[ny][nx] = 1 #방문한다.
        x, y = nx, ny #좌표 갱신
        cnt = 0 
        ans+=1 #청소하는 칸 + 1
    else: #만약 다음 좌표에 방문하지 못한다면
        cnt+=1 #회전 카운트
    
    if cnt == 4: #만약 회전 카운트가 4가 된다면
        #현재 바라보고 있는 방향에서 후진한 좌표를 구한다.
        nx = x+dx[(d+2)%4] 
        ny = y+dy[(d+2)%4]
        if 0<=nx<m and 0<=ny<n and board[ny][nx] == 0: #후진이 가능하다면,
            x, y = nx, ny #좌표 갱신
            cnt = 0 #회전 카운트 초기화
        else: #만약 후진이 불가하다면 
            break #반복문 탈출

print(ans)