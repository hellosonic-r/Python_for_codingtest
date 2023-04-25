from collections import deque

def bfs(sx,sy):
    queue = deque()
    queue.append((sx,sy))
    visited[sy][sx] = 1 #시작 좌표 방문처리
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            else:
                #다음 좌표가 방문처리 안되었거나 temp_board가 1이상인 곳(안 잠긴 곳)일 때
                if visited[ny][nx] == 0 and temp_board[ny][nx] >= 1:
                    #방문해서 방문처리 해주고
                    visited[ny][nx] = 1
                    #다음 좌표의 temp_board 값을 0으로 갱신(잠긴 곳으로 표시)
                    #잠긴 곳으로 표시해줌으로써 다음 bfs수행 시 안 잠긴 곳에 대해서 bfs수행할 수 있도록 함 
                    temp_board[ny][nx] = 0
                    #큐에 추가해줌으로써 그 다음 좌표가 잠겼는지 안잠겼는지 계속해서 확인한다 
                    queue.append((nx,ny))

n = int(input())
board = [] #지역의 높이 정보 리스트
for _ in range(n):
    board.append(list(map(int, input().split())))

#지역의 높이 정보 중 최대 높이 찾기
max_height = 0
for i in range(n):
    if max_height < max(board[i]):
        max_height = max(board[i])

dx = [0,1,0,-1]
dy = [-1,0,1,0]

max_count = 0
#0~(최대높이-1) 잠기는 모든 경우의 수 계산
for height in range(max_height):
    #임시 지역 높이 정보 리스트 초기화
    temp_board = [[0]*n for _ in range(n)]

    #height만큼 잠겼을 때, 높이 정보를 temp_board에 저장
    for i in range(n):
        for j in range(n):
            temp_board[i][j] = board[i][j] - height

    count = 0 #잠기지 않는 안전한 영역 초기화
    for k in range(n):
        for z in range(n):
            if temp_board[k][z] >= 1: #좌표 값이 1 이상인 곳은 아직 안잠긴 곳
                visited = [[0]*n for _ in range(n)] #bfs돌기 전 방문처리 위한 리스트 생성
                bfs(z,k) #bfs를 수행하여 temp_board의 안 잠긴 곳을 잠긴 곳으로 표시
                count+=1 #bfs수행했으니 count+1
    
    #height만큼 잠겼을 때 count값이 최대 값인지 확인 
    if max_count < count:
        max_count = count

print(max_count)